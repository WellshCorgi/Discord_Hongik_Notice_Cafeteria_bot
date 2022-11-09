import discord
from discord.ext.commands import Bot
import requests
from bs4 import BeautifulSoup
from datetime import datetime,date


TOKEN = 'your discode bot token'
intents = discord.Intents.default()
bot = Bot(command_prefix='!', intents=intents)
@bot.event
async def on_ready():
    print(f'logged in as {bot.user}')
    
@bot.command()
async def menu(message):
  html = requests.get('https://sj.hongik.ac.kr/site/food/food_menu.html').text # Load the site 
  html = BeautifulSoup(html,features="html.parser")

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
      return day # amend part -> version upgrade
    
  def find_menu(): # A function that prints an error message when there is no data in the site
      if not dictionary['mon']:
           print("학교 공식 사이트에 메뉴 정보가 없습니다. 업로드를 기다려주세요")
      else:
          print(dictionary[cycle(date.today())])
            
  embed = discord.Embed(title="B동(세움관) 학교식당 중식 메뉴입니다.",description="",color=0xff0000)
  embed.set_author(name="홍익대학교 정보 알리미", url="https://sj.hongik.ac.kr/site/food/food_menu.html", icon_url="https://www.hongik.ac.kr/front/images/local/header_logo.png")
  embed.add_field(name="오늘의 중식", value=menu_lunch_data[cycle(date.today())] , inline=True)
  embed.add_field(name="오늘의 석식", value=menu_dinner_data[cycle(date.today())] , inline=True)
  embed.set_thumbnail(url="https://www.hongik.ac.kr/front/images/local/header_logo.png")
  embed.set_footer(text="자세한 정보는 위의 프로필 버튼의 사이트를 방문해주세요.", icon_url="https://cdn.discordapp.com/attachments/779326874026377226/789098688315654164/Flag_of_South_Korea.png")

  await message.send(embed=embed)

bot.run(TOKEN)