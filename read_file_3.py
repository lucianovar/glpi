#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 23:05:33 2021

@author: eu
"""
#from bs4 import BeautifulSoup
from clear_html2 import clearhtml

f1 = "/home/eu/Documents/glpi/glpi_tickets_2020.csv"
f2 = "/home/eu/Documents/glpi/tickets.csv"

fescreve = open("/home/eu/Documents/glpi/glpi_limpo.txt", "w+")
fescreve.write("afdsadfafafd" + "\n")

#with open("/home/eu/Documents/glpi/glpi_tickets_2020.csv" , 'r') as reader:
    #print( reader.readlines() )
   # s = clean_html( str(reader.readlines()))
    #print(s)
    #fescreve.write( "sd" + "\n")

f = open("/home/eu/Documents/glpi/glpi_tickets_2020.csv", "r")
for x in f:
  #print(x)
  s = clearhtml(x) 
  fescreve.write( s )
  

fescreve.close()

print("feito")