#!/usr/bin/python
# -*- coding: UTF-8 -*-
#Service.py

class Service:
    _id = 0
    _client = ""
    _product = ""
    _status = ""
    
    def __init__(self,client="",product="",status=""):
        self._client = client
        self._product = product
        self._status = status
