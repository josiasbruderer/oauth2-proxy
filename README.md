# oauth2-proxy

How to use:

1. Create working directory and download oauth2-proxy_windows.exe
2. Download example config to same directory from: https://raw.githubusercontent.com/simonrob/email-oauth2-proxy/main/emailproxy.config
3. Modify config
4. Run for testing (and stop it afterwards):

```
D:\oauth2-proxy\oauth2-proxy_windows.exe --config-file D:\oauth2-proxy\emailproxy.config
```

 5. Create Windows service and start:

```
sc.exe create OAuth2-Proxy binPath="D:\oauth2-proxy\oauth2-proxy_windows.exe --config-file D:\oauth2-proxy\emailproxy.config" start=auto
net start OAuth2-Proxy
```