#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 04:54:16 2020

@author: Ay
"""
# This code is written by Nuray Nasib


from urllib import request
from bs4 import BeautifulSoup as BS
import re
import pandas as pd


################################################################################
################################################################################
url='https://www.rottentomatoes.com/top/bestofrt/'   #starting url is declared
html = request.urlopen(url)
bs = BS(html, 'html.parser')
tags = bs.find_all('table')[2].find_all('a')        # all the a tags is stored in tags list

links=['https://www.rottentomatoes.com' + tag['href'] for tag in tags]   # here we join all the href part of the tags with https://www.rottentomatoes.com and make a full links list for movie pages



################################################################################
################################################################################

d = pd.DataFrame({'Title':[], 'Tatometer':[], 'Audience Score':[], 'MPAA':[], 'Genre':[], 'Director':[], 'Writer':[],'Box Office':[] })  # used pandas to store all the data later
for link in links:



#try except helps to avoid crashes or errors if xpath is not found

    try:                                            # i run bs again to request link for every page
        html = request.urlopen(link)
        bs = BS(html.read(), 'html.parser')
    except:
        print("Not Found")

    try:                                            # all the wanted data is found and stored in variables with the help of html tags
        title = bs.find('h1').text
    except:
        title = ''

    try:
        tatometer = bs.find('a', {'id':re.compile("tomato_meter_link")}).span.next_sibling.next_sibling.text
    except:
        tatometer = ''


    try:
        audience =bs.find('div', {'class':re.compile("mop-ratings-wrap__half audience-score")}).h2.a.span.next_sibling.next_sibling.text
    except:
        audience = ''

    try:
         rating = bs.find('div', string='Rating: ').next_sibling.next_sibling.text
    except:
        rating = ''



    try:
        genre = bs.find('div', string='Genre: ').next_sibling.next_sibling.text
    except:
        genre = ''


    try:
        director = bs.find('div', string='Directed By: ').next_sibling.next_sibling.text
    except:
        director = ''


    try:
        writer = bs.find('div', string='Written By: ').next_sibling.next_sibling.text
    except:
        writer = ''

    try:
        boxOffice = bs.find('div', string='Box Office: ').next_sibling.next_sibling.text
    except:
        boxOffice = ''

    rotten = {'Title': title, 'Tatometer': tatometer, 'Audience Score' : audience , 'MPAA':rating, 'Genre':genre, 'Director':director, 'Writer':writer,'Box Office':boxOffice }

    d = d.append(rotten, ignore_index = True)   # all the found data is added to d
    print(d)

#################################################################################
## This part saves data to csv.
#################################################################################
d.to_csv('rottentomatoes.csv')   # and saved to csv file
