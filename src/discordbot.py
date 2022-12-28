import discord
from discord.ext.commands import Bot
import requests
from bs4 import BeautifulSoup
from datetime import datetime,date


TOKEN = '____'
intents = discord.Intents.default()
bot = Bot(command_prefix='!', intents=intents)
@bot.event
async def on_ready():
    print(f'logged in as {bot.user}')
    
@bot.command()
async def menu(message):
  html = requests.get('https://sj.hongik.ac.kr/site/food/food_menu.html').text # Load the site 
  html = BeautifulSoup(html,features="lxml")

  day_menu=[]

  menu_lunch_data=[html.select(".foodmenu")[i].get_text() for i in range(0,5)] # Put in menu_lunch_data in html-> 'class==foodmenu'
  menu_dinner_data=[html.select(".foodmenu")[i].get_text() for i in range(6,11)] # same dinner data
  #day_menu=[menu_lunch_data[i].strip()+"\n\n"+menu_dinner_data[i].strip() for i in range(0,5)] # Remove data's space
  menu_dinner_data.append("주말 및 종강 후 에는 B동 석식을 운영하지 않습니다.") # Add exception ->if>>  Cafeteria didn't open day

  menu_lunch_data.append("주말에는 B동 학교식당을 운영하지 않습니다.")
  menu_lunch_data.append("주말에는 B동 학교식당을 운영하지 않습니다.")

  days=["mon","tue","wed","thr","fri","sat","sun"]
  dictionary = {key:value for key,value in zip(days,day_menu)} # Using by Comprension -> create Dictionary
  
  #if not dictionary['mon']: # This If sentense that prints an error message when there is no data in the site
  #  menu_lunch_data.append("학교 공식 사이트에 메뉴 정보가 없습니다. 업로드를 기다려주세요")
    
  def cycle(date): # A function that retrieves a date and finds a dictionary value
      days=["mon","tue","wed","thr","fri","sat","sun"]
      day = date.weekday()
      return days[day] # amend part -> version upgrade   
            
  embed = discord.Embed(title="B동(세움관) 학교식당 중식 메뉴입니다.",description="",color=0x0aa40f)
  embed.set_author(name="홍익대학교 정보 알리미", url="https://sj.hongik.ac.kr/site/food/food_menu.html", icon_url="https://www.hongik.ac.kr/front/images/local/pic_ui_01_01.png")
  embed.add_field(name="오늘의 중식", value=menu_lunch_data[days.index(cycle(date.today()))] , inline=True)
  embed.add_field(name="오늘의 석식", value=menu_dinner_data[5] , inline=True)
  embed.set_thumbnail(url="https://www.hongik.ac.kr/front/images/local/header_logo.png")
  embed.set_footer(text="Developed by WellshCorgi.", icon_url="https://cdn.discordapp.com/attachments/779326874026377226/789098688315654164/Flag_of_South_Korea.png")
  
  await message.send(embed=embed)

bot.run(TOKEN)
