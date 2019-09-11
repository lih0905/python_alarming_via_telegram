# -*- coding: utf-8 -*-

import requests
import telegram
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler

bot = telegram.Bot(token='970060618:AAFbYa2iflYVkwzmoDddsapDXTgJZ0xCKCE')
url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20190915'


def job_function():
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    gold = soup.select_one('span.gold')
    
    if (gold):
        gold = gold.find_parent('div', class_='col-times')
        title = gold.select_one('div.info-movie > a > strong').text.strip()
        bot.sendMessage(chat_id=874758964, text=title + " GOLD 예매가 열렸습니다.")
        sched.pause()

sched = BlockingScheduler()
sched.add_job(job_function, 'interval', seconds=30)
sched.start()
