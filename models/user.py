#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 14:21:44 2022
user model
@author: Michel
"""
import bcrypt

from sqlalchemy import Column, String, Integer
from pythonMVC.core.DB import Base

class User(Base):
    
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True)
    username = Column(String)
    password_hash = Column(String)

    def __init__(self, username, password):
        self.username = username
        salt = bcrypt.gensalt()
        password = password.encode() #encode before hashing
        self.password_hash = bcrypt.hashpw(password,salt)
