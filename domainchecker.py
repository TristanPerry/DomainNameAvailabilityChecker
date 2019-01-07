#!/usr/bin/env  python

import socket, re, sys

def whois_request(domain, server, port=43):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((server, port))
    sock.send(("%s\r\n" % domain).encode("utf-8"))
    buff = b""
    while True:
        data = sock.recv(1024)
        if len(data) == 0:
            break
        buff += data
    return buff.decode("utf-8")

domain_name = sys.argv[1]

response = whois_request(domain_name, 'whois.verisign-grs.com')

if re.search("Domain Name: %s" % domain_name.upper(), response):
    try:
        expiry_date = re.search("Registry Expiry Date\: (.*)", response).group(1)
    except AttributeError:
        expiry_date = '???'
    print("Domain taken. Expires on %s" % expiry_date)
else:
    print("Domain is free")