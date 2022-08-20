# oauth2-proxy

## How to use:

1. Create working directory and download oauth2-proxy_windows.exe
2. Download example config to same directory from: https://raw.githubusercontent.com/simonrob/email-oauth2-proxy/main/emailproxy.config
3. Modify config
4. Run for testing (and manually stop it afterwards):

```
D:\oauth2-proxy\oauth2-proxy_windows.exe --config-file D:\oauth2-proxy\emailproxy.config
```

5. Copy service-utilities/start.bat to working directory
6. Download nssm.exe and copy it to working directory: https://nssm.cc/download
7. Start Service

```
net start OAuth2-Proxy
```

8. Start Authentication f.E. Using Thunderbird (IMAP Port 1993, SMTP Port 1587) and check Logs in working directory
> or at: C:\Windows\Temp\_MEIXXXXX\email_oauth2_proxy\emailproxy.log to get Authentification-URL


## Build

Build using pyinstaller:

```
pyinstaller --add-data 'email_oauth2_proxy/*:email_oauth2_proxy' -F -c -n oauth2-proxy_linux oauth-proxy.py
```

> Note: Maybe you need some more file permissions:
> sudo chmod +r /usr/share/icons/Vibrancy-Colors-Full-Dark/actions/scalable/document-open-recent.svg
> sudo chmod +r /usr/share/icons/Vibrancy-Colors-Full-Dark/actions/scalable/go-home.svg