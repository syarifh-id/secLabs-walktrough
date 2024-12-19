┌──(altair㉿Sysbraykr)-[~]
└─$ nmap 157.173.116.25
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-12-15 17:13 WIB
Stats: 0:00:14 elapsed; 0 hosts completed (1 up), 1 undergoing Connect Scan
Connect Scan Timing: About 53.22% done; ETC: 17:14 (0:00:11 remaining)
Nmap scan report for vmi2148870.contaboserver.net (157.173.116.25)
Host is up (0.26s latency).
Not shown: 996 closed tcp ports (conn-refused)
PORT     STATE    SERVICE
22/tcp   open     ssh
25/tcp   filtered smtp
631/tcp  open     ipp
8080/tcp open     http-proxy

Nmap done: 1 IP address (1 host up) scanned in 38.59 seconds

┌──(altair㉿Sysbraykr)-[~]
└─$ nmap 157.173.116.25 -sV
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-12-15 17:14 WIB
Stats: 0:00:35 elapsed; 0 hosts completed (1 up), 1 undergoing Connect Scan
Connect Scan Timing: About 89.83% done; ETC: 17:15 (0:00:04 remaining)
Nmap scan report for vmi2148870.contaboserver.net (157.173.116.25)
Host is up (0.26s latency).
Not shown: 992 closed tcp ports (conn-refused)
PORT     STATE    SERVICE       VERSION
22/tcp   open     ssh           OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
25/tcp   filtered smtp
631/tcp  open     ipp           CUPS 2.4
1073/tcp filtered bridgecontrol
2288/tcp filtered netml
3889/tcp filtered dandv-tester
6156/tcp filtered unknown
8080/tcp open     http          Node.js Express framework
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 54.46 seconds

┌──(altair㉿Sysbraykr)-[~]
└─$ curl -v http://157.173.116.25:8080/
*   Trying 157.173.116.25:8080...
* Connected to 157.173.116.25 (157.173.116.25) port 8080
> GET / HTTP/1.1
> Host: 157.173.116.25:8080
> User-Agent: curl/8.8.0
> Accept: */*
>
* Request completely sent off
< HTTP/1.1 404 Not Found
< X-Powered-By: Express
< Content-Security-Policy: default-src 'self'
< X-Content-Type-Options: nosniff
< Content-Type: text/html; charset=utf-8
< Content-Length: 139
< Date: Sun, 15 Dec 2024 10:16:10 GMT
< Connection: keep-alive
<
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Error</title>
</head>
<body>
<pre>Cannot GET /</pre>
</body>
</html>
* Connection #0 to host 157.173.116.25 left intact

┌──(altair㉿Sysbraykr)-[~]
└─$