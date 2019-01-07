# Domain Name Availability Checker

A very simple domain name availability checker that goes directly to the registry to see if a domain is available or not.

I've currently hardcoded it for .com (whois.verisign-grs.com registry) since this is all I tend to check myself.

Usage is command line:

```
> ~/Documents/Projects
$ python domain.py testing123.com
Domain taken. Expires on 2019-05-17T18:23:34Z
```

```
> ~/Documents/Projects
$ python domain.py testing123534563.com
Domain is free
```
