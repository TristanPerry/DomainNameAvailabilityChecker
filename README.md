# Domain Name Availability Checker

A very simple domain name availability checker that goes directly to the registry to see if a domain is available or not.

I've currently hardcoded it for .com (whois.verisign-grs.com registry) since this is all I tend to check myself.

Usage is command line:

```
$ python domainchecker.py testing123.com
Domain taken. Expires on 2020-05-17T18:23:34Z
```

```
$ python domainchecker.py testing123534563.com
Domain is free
```
