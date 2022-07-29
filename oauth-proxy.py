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
spec = importlib.util.spec_from_file_location("emailoauth2proxy", "email-oauth2-proxy/emailproxy.py")
emailproxy = importlib.util.module_from_spec(spec)
sys.modules["emailoauth2proxy"] = emailproxy
spec.loader.exec_module(emailproxy)

emailproxy.App()
