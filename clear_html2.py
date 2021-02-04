#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 15:26:10 2021

@author: eu
"""


from bs4 import BeautifulSoup
import re


def cleantags(txt):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', txt )
  return cleantext

def clearhtml(html):
    soup      = BeautifulSoup( html , 'html.parser')
    s         = soup.get_text()
    s2        = cleantags(s)
    return s2
    


