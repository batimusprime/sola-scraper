from bs4 import BeautifulSoup
import urllib.request
import re
import csv
#filename = (raw_input("enter filename: "))
#outputname = (raw_input("enter output name: "))

with open('sitemap.html', 'r') as f:
    red = f.read()
#with open(outputname, 'w') as csvfile:

soup = BeautifulSoup(red, 'lxml')

file = open('output_file.txt', 'w')

for link in soup.findAll('a'):
    file.write(link.get('href') + '\n')
