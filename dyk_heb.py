'''
A script for getting random Wikipedia "Did you know" articles
from the Hebrew Wikipedia.

Written by Ronen K Jul. 2015, with some help by Ron Y.
This script is under public domain; feel free to do whatever you want with it.
'''

import urllib.request
import re
import time
import webbrowser
import os

URL = r'https://he.wikipedia.org/wiki/%D7%95%D7%99%D7%A7%D7%99%D7%A4%D7%93%D7%99%D7%94:%D7%94%D7%99%D7%93%D7%A2%D7%AA_%D7%90%D7%A7%D7%A8%D7%90%D7%99'

def get_page_data():
    data = None
    
    with urllib.request.urlopen(URL) as f:
        data = f.read()

    return data.decode('utf-8')

def get_value(pagedata):
    data = re.search(r'<div class="floatleft">.*<\/div>\s(<p>.*<\/p>)', pagedata).groups(1)[0]

    # Get rid of links
    linkg = re.findall(r'<a([^>]+)>(.+?)</a>', data)
    for res in linkg:
        data = data.replace(res[0], res[1])
    
    return data

def output_file(data):
    outpath = str(time.time()) + '.html'
    
    # Output the file
    with open(outpath, 'wt', encoding='utf-8') as f:
        f.write('<html><head><meta charset="utf-8"><title></title></head><body>')
        f.write(data)
        f.write('</body></html>')

    return outpath

def display_file(data):
    path = output_file(data)

    # Open the file using the webbrowser module
    webbrowser.open(path)

def main():
    # Get page data
    pagedata = get_value(get_page_data())
    display_file(pagedata)

    print('DONE!')

if __name__ == '__main__':
    main()
