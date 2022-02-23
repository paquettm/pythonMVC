#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 14:21:44 2022
user model
@author: Michel
"""
import bcrypt

class user:
    
    def __init(self):
        pass
    
    #private
    __username = ""
    __password = ""
    __password_hash = ""
    __email = ""
    __message = ""
    
    #getters/accessors
    def getUsername(self):
        return self.__username
    def getPassword(self):
        return self.__password
    def getEmail(self):
        return self.__email
    def getMessage(self):
        return self.__message
    
    #setters
    def setUsername(self,username):
        self.__username = username
    def setPassword(self,password):
        self.__password = password
        self.__password_hash = bcrypt.hashpw(password)   
    def setEmail(self,email):
        self.__email = email    
    def setMessage(self,message):
        self.__message = message    