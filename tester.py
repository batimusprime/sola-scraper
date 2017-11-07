import bs4 as bs
import urllib.request
import csv
#index for enumeration of URL list
index = 0

#should be .txt
sitemapfile = input('Enter sitemap TXT name: ')
#MUST be CSV
outfile = input('Enter output CSV name: ')

#returns the lines from the input sitemap file
with open(sitemapfile + '.txt') as f:
    content = f.readlines()

#add contents of file to list
content = [x.strip() for x in content]


with open((outfile + '.csv'), 'w+', newline='') as csvfile:

#best formatting for URL list
    csvwriter = csv.writer(csvfile, delimiter='|', escapechar=' ', quoting=csv.QUOTE_NONE)
#best formatting for headers
    headlinewriter = csv.writer(csvfile, escapechar=' ', quoting=csv.QUOTE_NONE)

    for index, items in enumerate(content):
#GET html for items in list
        sauce = urllib.request.urlopen(items).read()
#parse with beautiful soup and lxml html parser
        soup = bs.BeautifulSoup(sauce, 'lxml')
#convert header to string
        headline = str(content[index])
#insert headline to delineate between rows of imgs
        headlinewriter.writerow([headline])
#find all image tags
        for img in soup.find_all('img'):
#write those images to csv with writer
            csvwriter.writerow([img])
