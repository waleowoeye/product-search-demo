import requests
from bs4 import BeautifulSoup
import urllib3
import csv
import json
import wget
import os
import numpy as np
import pandas as pd
from collections import OrderedDict, defaultdict


category = input('Category name: ')

dest_folder = "/Users/wale/Documents/Working/imageScrape/"+ category + '/'
os.makedirs(dest_folder, exist_ok=True)
print(dest_folder)


url = 'https://www.athome.com/'+category+'/'

http = urllib3.PoolManager()
response = http.request('GET', url)

html = BeautifulSoup(response.data, 'html.parser')

tags = html.find_all('img')
del(tags[1])
tags_data = json.dumps(str(tags))
print(type(tags_data), tags_data)

for tag in tags:
    print(tag)
    src = tag.get('src')
    image_uri = 'GCS bucket'
    image_id = 'blank'
    product_set_id = tag.get('data-pid')
    product_id = product_set_id
    product_category = category
    product_display_name = tag.get('data-productname')
    labels = src
    bounding_poly = 'means what?'
    r = requests.get(src.strip(), allow_redirects=True)
    try:
        wget.download(url=src.strip(), out=dest_folder)
        with open(dest_folder + 'metadata.csv', 'a') as csvfile:
            tagwriter = csv.writer(csvfile, delimiter=',')
            tagwriter.writerow([image_uri, image_id, product_set_id, product_id, product_category, \
                                product_display_name, labels, bounding_poly, src])
    except Exception:
        print(Exception)
        continue






















