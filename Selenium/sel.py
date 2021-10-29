#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 02:48:52 2020

@author: Ay
"""

from selenium import webdriver
import time
import pandas as pd

gecko_path = '/usr/local/bin/chromedriver'  # location of the driver is declared

url = 'https://www.rottentomatoes.com/top/bestofrt/'  # starting url is declared

options = webdriver.chrome.options.Options()
options.headless = False

driver = webdriver.Chrome(options=options, executable_path=gecko_path)

driver.get(url)  # webpage is loaded

d = pd.DataFrame(
    {'Title': [], 'Tatometer': [], 'Audience Score': [], 'MPAA': [], 'Genre': [], 'Director': [], 'Writer': [],
     'Box Office': []})  # dataframe is made using pandas

shows = driver.find_elements_by_xpath(
    "//td/a[@class='unstyled articleLink']")  # all the <a> tags of the shows is stored as a list

links = [link.get_attribute('href') for link in shows]  # links to the movie pages is stored in a list
print(links)
for link in links:
    print(link)
    print("###################")
    driver.get(link)  # go to the every movie's page
    time.sleep(1)

    # code Written till this part by Aymir Aydinli

    # all the elemets is found by xpath and declared as variables

    # try except helps to avoid crashes or errors if xpath is not found
    try:

        title = driver.find_element_by_xpath("//h1[@class='mop-ratings-wrap__title mop-ratings-wrap__title--top']").text
        print(title)
    except:

        print("Not Found")

    try:
        tatometer = driver.find_element_by_xpath("//a[@id='tomato_meter_link']/span[2]").text
        print(tatometer)
    except:
        print("Not Found")

    try:

        audience = driver.find_element_by_xpath(
            "//div[@class='mop-ratings-wrap__half audience-score']/h2/a/span[@class='mop-ratings-wrap__percentage']").text
        print(audience)
    except:
        print("Not Found")

    try:

        rating = driver.find_element_by_xpath("//*[.='Rating: ']/following-sibling::div").text
        print(rating)
    except:
        print("Not Found")

    try:

        genre = driver.find_element_by_xpath("//*[.='Genre: ']/following-sibling::div").text
        print(genre)
    except:
        print("Not Found")

    try:

        director = driver.find_element_by_xpath("//*[.='Directed By: ']/following-sibling::div/a").text
        print(director)
    except:
        print("Not Found")

    try:

        writer = driver.find_element_by_xpath("//*[.='Written By: ']/following-sibling::div/a").text
        print(writer)
    except:
        print("Not Found")

    try:

        boxOffice = driver.find_element_by_xpath("//*[.='Box Office: ']/following-sibling::div").text
        print(boxOffice)
    except:
        print("Not Found")

        rotten = {'Title': title, 'Tatometer': tatometer, 'Audience Score': audience, 'MPAA': rating, 'Genre': genre,
                  'Director': director, 'Writer': writer, 'Box Office': boxOffice}

        d = d.append(rotten, ignore_index=True)  # all the declared variables is stored in data frame

d.to_csv('rottenSelenium.csv')  # saved as .csv file

# code Written till this part is written by Nuray Nasib
