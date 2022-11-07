import requests
from bs4 import BeautifulSoup
import schedule 
from datetime import datetime,date
import time


html = requests.get('https://sj.hongik.ac.kr/site/food/food_menu.html').text # Load the site 
html = BeautifulSoup(html,features="lxml")

day_menu=[]

menu_lunch_data=[html.select(".foodmenu")[i].get_text() for i in range(0,5)] # Put in menu_lunch_data in html-> 'class==foodmenu'
menu_dinner_data=[html.select(".foodmenu")[i].get_text() for i in range(6,11)] # same dinner data


for i in range(0,5):
    day_menu.append(menu_lunch_data[i].strip()+"\n\n"+menu_dinner_data[i].strip()) # Remove data's space

days=["mon","tue","wed","thr","fri"]
dictionary = {key:value for key,value in zip(days,day_menu)} # Using by Comprension -> create Dictionary

def cycle(date): # A function that retrieves a date and finds a dictionary value
    days=["mon","tue","wed","thr","fri"] 
    day = date.weekday()
    print(days[day] if day == "sat" or "sun" else "주말에는 B동 학식을 운영하지 않습니다")
    
def find_menu(): # A function that prints an error message when there is no data in the site
    if not dictionary['mon']:
         print("학교 공식 사이트에 메뉴 정보가 없습니다. 업로드를 기다려주세요")
    else:
        print(dictionary[cycle(date.today())])


schedule.every().day.at("10:30").do(find_menu) #Set time to start function
while True:
    schedule.run_pending()
    time.sleep(1)