#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#####################################################################
# title:  OAuth-Proxy
# author: Josias Bruderer
# date:   20.08.2022
# desc:   A simple IMAP/POP/SMTP proxy with OAuth 2.0 authentication.
#         Based on Simon Robinsons Email OAuth 2.0 Proxy:
#         https://github.com/simonrob/email-oauth2-proxy
#####################################################################


import importlib.util
import sys
import os
import shutil
from src.email_oauth2_proxy import emailproxy
from src.download_and_unzip import download_and_unzip

if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
else:
    application_path = os.path.dirname(os.path.realpath(__file__))

os.chdir(application_path)

print('Temporary runtime directory:' + os.path.dirname(os.path.realpath(__file__)))
print('Working directory: ' + os.getcwd())

if not os.path.exists(os.getcwd() + '/emailproxy.config'):
    shutil.copyfile(os.path.dirname(os.path.realpath(__file__)) + '/email_oauth2_proxy/emailproxy_example.config',
                    os.getcwd() + '/emailproxy.config')

if not os.path.exists(os.getcwd() + '/service-utilities'):
    shutil.copytree(
        os.path.dirname(os.path.realpath(__file__)) + '/service-utilities',
        os.getcwd() + '/service-utilities')
    download_and_unzip('https://nssm.cc/release/nssm-2.24.zip', os.getcwd() + '/service-utilities')

emailproxy.UpdatePath(os.getcwd())
emailproxy.App()
