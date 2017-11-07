from bs4 import BeautifulSoup
import urllib2
import re
import csv
filename = (raw_input("enter filename: "))
outputname = (raw_input("enter output name: "))

with open(filename, 'r') as f:
    red = f.read()
with open(outputname, 'w') as csvfile:
    
    soup = BeautifulSoup(red, 'lxml')
    images = []
    csvwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for link in soup.findAll('a'):
        images.append(link.get('href'))
#        print images
 #       print link.get('href')
 #       csvwriter.writerow(link.get('href'))