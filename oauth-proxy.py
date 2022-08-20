#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#####################################################################
# title:  OAuth-Proxy
# author: Josias Bruderer
# date:   29.07.2022
# desc:   A simple IMAP/POP/SMTP proxy with OAuth 2.0 authentication.
#         Based on Simon Robinsons Email OAuth 2.0 Proxy:
#         https://github.com/simonrob/email-oauth2-proxy
#####################################################################


import importlib.util
import sys
import os
from email_oauth2_proxy import emailproxy

if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
    os.chdir(application_path)

print('Temporary runtime directory:' + __file__)
print('Working directory: ' + os.getcwd())

__file__ = os.getcwd() # overwrite runtime directory with working directory

emailproxy.App()
