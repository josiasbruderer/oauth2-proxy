@echo off
net stop OAuth2-Proxy
timeout 1 > NUL
call D:\oauth2-proxy\service-utilities\logrotate.bat D:\oauth2-proxy\emailproxy.log 10 10000000
timeout 1 > NUL
call D:\oauth2-proxy\service-utilities\logrotate.bat D:\oauth2-proxy\err.log 10 10000000
timeout 1 > NUL
call D:\oauth2-proxy\service-utilities\logrotate.bat D:\oauth2-proxy\out.log 10 10000000
timeout 1 > NUL
net start OAuth2-Proxy