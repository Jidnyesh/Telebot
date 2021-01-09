from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse
import telegram
import sys
import os
from datetime import datetime 
import pytz 


# 1591084792:AAGg3icVQx7Ah-K1uY7ZjCtIkJv46cIvRYg
TOKEN = "1591084792:AAGg3icVQx7Ah-K1uY7ZjCtIkJv46cIvRYg"

CHAT_ID = "@myonlymilf"
print('Telebot by - JYDNX\n')

no_of_videos = int(input("Enter the number of latest videos you wanna post - "))

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




def main():
    url = "https://myonlymilf.com/post-sitemap.xml"

    sitemap = get_sitemap(url)
    final = {}
    url_count = 0
    
    a = parse_sitemap(sitemap)    
    return a


if __name__ == '__main__':
    final = main()
    for i in range(no_of_videos):
        key = list(final)[i]
        post = "Link - "+key+"\n👆👆👆👆"
        bot = telegram.Bot(token=TOKEN)
        bot.sendMessage(chat_id = CHAT_ID, text = post)
        print("\n"+key +" posted to Telegram")
    
    sys.exit()
    #To select todays videos
    # timeZ_Kl = pytz.timezone('Asia/Kolkata')  
    # dt_Kl = datetime.now(timeZ_Kl)
    # dt_Kl = str(dt_Kl)[0:10]
    
    # for key in final:
    #     site = final[key][0:10]

    #     if site == dt_Kl and key != "https://myonlymilf.com/":
            
            # post = "Link - "+key+"\n👆👆👆👆"
            # bot = telegram.Bot(token=TOKEN)
            # bot.sendMessage(chat_id = CHAT_ID, text =post)
            # print(key+" posted to Telegram")

        
