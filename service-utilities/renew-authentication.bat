@echo off
net stop OAuth2-Proxy
timeout 1 > NUL
type D:\oauth2-proxy\emailproxy.config | findstr /v token_salt | findstr /v access_token_expiry | findstr /v access_token | findstr /v refresh_token | findstr /v last_activity > D:\oauth2-proxy\emailproxy.config
timeout 1 > NUL
net start OAuth2-Proxy