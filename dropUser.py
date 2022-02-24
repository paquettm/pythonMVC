#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 15:55:21 2022

@author: Michel
"""

# coding=utf-8

# imports
from pythonMVC.models.user import User

from pythonMVC.core.DB import Session, engine, Base

# generate database schema
Base.metadata.create_all(engine)

# create a new session
session = Session()

User.__table__.drop(engine)

# commit and close session
session.commit()
session.close()