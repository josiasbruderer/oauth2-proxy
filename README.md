# oauth2-proxy

Used to proxy OAuth2.0 for IMAP, POP and SMTP. 

Based on Simon Robinsons Email OAuth 2.0 Proxy: https://github.com/simonrob/email-oauth2-proxy

## How to use:

1. Create working directory and download oauth2-proxy_windows.exe
2. Run once to create .config and .log files as well as service-utilities folder

```
D:\oauth2-proxy\oauth2-proxy_windows.exe
```

3. Modify .config
4. Run for testing (and manually stop it afterwards):

```
D:\oauth2-proxy\oauth2-proxy_windows.exe --config-file D:\somewhere-else\emailproxy.config
```

> Parameter --config-file is optional an only required if .config is not in working directory

## Install Service:

1. Run service-utilities/install-service.bat
2. Start Service

```
net start OAuth2-Proxy
```

## Testing:

1. Start Authentication f.E. Using Thunderbird (IMAP Port 1993, SMTP Port 1587) 
2. Check Logs in working directory to get Authentication-URL


## Build

Build from source using pyinstaller:

```
pyinstaller --add-data 'src/email_oauth2_proxy/*:src/email_oauth2_proxy' --add-data 'service-utilities/*:service-utilities' -F -c -n oauth2-proxy_linux oauth-proxy.py
```

> Note: Maybe you need some more file permissions:
> sudo chmod +r /usr/share/icons/Vibrancy-Colors-Full-Dark/actions/scalable/document-open-recent.svg
> sudo chmod +r /usr/share/icons/Vibrancy-Colors-Full-Dark/actions/scalable/go-home.svg