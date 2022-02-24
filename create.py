#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 15:55:21 2022

@author: Michel
"""

# coding=utf-8

# imports

from pythonMVC.core.DB import engine

from sqlalchemy import Table, Column, Integer, String, MetaData

from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

otherEngine = create_engine("mysql://root:password@127.0.0.1/myPythonApp")
if not database_exists(engine.url):
    create_database(otherEngine.url)

print(database_exists(otherEngine.url))

meta = MetaData()

user = Table(
   'user_table', meta, 
   Column('user_id', Integer, primary_key = True), 
   Column('username', String(50)), 
   Column('password_hash', String(72)), 
)

# generate database schema
meta.create_all(engine)

