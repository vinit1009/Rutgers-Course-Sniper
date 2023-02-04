from __future__ import unicode_literals
from __future__ import print_function
from os.path import abspath, join, dirname
import random
import webbrowser
import asyncio
import re
from selenium import webdriver
import string
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.action_chains import ActionChains
import requests #dependency
from discord_webhook import DiscordWebhook


async def main():
    print('Hello ...')
    await asyncio.sleep(2)
    print('... World!')
    
async def main2():
    print('Hello ...')
    await asyncio.sleep(15)
    print('... World!')
    
    
index_file = open('index.txt', 'r')
index_read = index_file.readlines()

    

web = webdriver.Chrome()
url = "https://sims.rutgers.edu/webreg/"

web.get(url)

asyncio.run(main())

web.find_element_by_xpath("/html/body/div[1]/div[3]/p[1]/a").click()

asyncio.run(main())

net = "vjs72"
netId = web.find_element_by_xpath("/html/body/main/div/div[2]/div[1]/div[2]/form/section/div[1]/input")
netId.send_keys(net)

pw = "#password"
paw = web.find_element_by_xpath("/html/body/main/div/div[2]/div[1]/div[2]/form/section/section[1]/div/input")
paw.send_keys(pw)

web.find_element_by_xpath("/html/body/main/div/div[2]/div[1]/div[2]/form/section/input[4]").click()

asyncio.run(main())



n = 0
while True:
    print("1")
    try:
        web.find_element_by_xpath("/html/body/div[1]/div[1]/form/div/input").click()
    
        asyncio.run(main())
        print("2")
    except:
        pass


    try:
        ind = index_read[n]
        print("3")
        asyncio.run(main())
    except:
        n = 0
        ind = index_read[n]
        print("4")
        asyncio.run(main())
    print("5")
    print(index_read[n])
    asyncio.run(main())
    index = web.find_element_by_xpath("/html/body/div[2]/div[1]/form/ol/li[1]/input")
    print("6")
    index.send_keys(ind)
    print("7")
    asyncio.run(main())
    print("8")
    #web.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[2]/input").click()
    print("9")
    asyncio.run(main2())
    x = web.find_element_by_xpath("/html/body/div[1]/p/span[1]").text
    if(x != "14.0"):
        webhook = DiscordWebhook(url='#', content='Registered - ')
        response = webhook.execute()
       
        print("Payload delivered successfully, code {}.")

#result: https://i.imgur.com/DRqXQzA.png
    
    print(x)
    print("10")
    n = n+1
    print("11")
    web.refresh()
    print("12")
    asyncio.run(main2())
    print("13")
    asyncio.run(main2())

