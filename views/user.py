#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 14:32:05 2022
the user login view
@author: Michel
"""
from pythonMVC.models.user import user
from pythonMVC.controllers.user import user as userController

u = user()
uc = userController()
print('___________________________')
u.setUsername(input("Please write your username:"))
u.setPassword(input("Please write your password:"))

uc.Login(u)
print(u.getMessage())