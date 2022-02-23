#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 14:59:03 2022
user controller
@author: Michel
"""
from pythonMVC.models.dbcontext import MySQL

#controller for business logic
class user:
    __connection = None
    
    def __init__(self):
        self.__connection = MySQL.connect()
        
    def Login(self,user):
        if self.__isValidLogin(user):
            if self.__isAuthentic(user):
                self.__authorize(user)
            else:
                user.setMessage("Incorrect username and password.")
        else:
            user.setMessage("Please enter your username and password.")
    
    def __isValidLogin(self,user):
        cursor = self.__connection.cursor()
        cursor.execute("SELECT `id` FROM user WHERE `username`=")
        return user.getUsername() != "" and user.getPassword() != ""
    
    def __isAuthentic(self,user):
        return user.getUsername() == "root" and user.getPassword() == "password"
    
    def __authorize(self,user):
        user.setMessage(user.getUsername() + " is logged in.")
    
    

        
u = user
print(MySQL.message)