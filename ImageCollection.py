# COMP90055 Computing Project
# Supervisor: Prof. Richard Sinnott
# 874204 Liangmu ZHU
# @ Master of Information Technology
# Contact: liangmuz@student.unimelb.edu.au

import os
import sys
from datetime import date
from icrawler.builtin import GoogleImageCrawler
from icrawler.builtin import FlickrImageCrawler

image_path = '/Users/picca/COMP90055'
API_KEY = '8fd6694fc4d635b4a0ab63c887323bba'


BuildingList = open('landmarks.txt','rt')

for nameList in BuildingList:
    name = nameList.strip('\n')
    imageDirG = image_path + '/' + name + ' Google'
    imageDirF = image_path + '/' + name + ' Flickr'
    searchName = 'Melbourne ' + name
    google_crawler = GoogleImageCrawler(storage = {'root_dir': imageDirG})
    google_crawler.crawl(keyword = searchName, max_num = 500)
    flickr_crawler = FlickrImageCrawler(API_KEY, storage={'root_dir': imageDirF})
    flickr_crawler.crawl(max_num = 500, tags = searchName)
#, text = searchName
print("Collection is done")
