#---- By JYDNX

from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse
import telegram
import sys
import os
from datetime import datetime 
import pytz 

print('Telebot by - JYDNX\n')

#Configure This first
#----------#
TOKEN = "Add your BotFather Access key"

url = "Enter the URL of your sitemap.xml"

CHAT_ID = "@channel_name"
#----------#



no_of_videos = int(input("Enter the number of latest posts or link you wanna post - "))

def get_sitemap(url):
    get_url = requests.get(url)

    if get_url.status_code == 200:
        return get_url.text
    else:
        print('Unable to fetch sitemap: %s.' % url)

def process_sitemap(s):
    soup = BeautifulSoup(s, 'lxml')
    result = []

    for loc in soup.findAll('loc'):
        result.append(loc.text)

    return result

def is_sub_sitemap(url):
    parts = urlparse(url)
    if parts.path.endswith('.xml') and 'sitemap' in parts.path:
        return True
    else:
        return False


def parse_sitemap(s):
    sitemap = process_sitemap(s)
    result = []

    while sitemap:
        candidate = sitemap.pop()

        if is_sub_sitemap(candidate):
            sub_sitemap = get_sitemap(candidate)
            for i in process_sitemap(sub_sitemap):
                sitemap.append(i)
        else:
            result.append(candidate)

    return result

#------- Main function
def main():
    sitemap = get_sitemap(url)
    final = {}
    url_count = 0
    
    a = parse_sitemap(sitemap)    
    return a

if __name__ == '__main__':
    final = main()
    for i in range(no_of_videos):
        key = list(final)[i]
        
        #Can edit the text to send to your channel
        post = "Link - "+key+"\n👆👆👆👆"
        
        bot = telegram.Bot(token=TOKEN)
        bot.sendMessage(chat_id = CHAT_ID, text = post)
        print("\n"+key +" posted to Telegram")
    
    sys.exit()
    


        
