# Discord Bot : Hongik_Notice_Cafeteria
## Description
1. Language : Python
2. Detailed Description : Python으로 'Beautifulsoup4'과 'Discord Bot module'을 사용한 디스코드 알림 개발 프로그램(Discord notification development program using Beautifulsoup4 and Discord bot module with Python)
---
## Project Overview
-매일 오전 10시 30분에 디스코드를 통하여 홍익대학교 식당 메뉴를 알림 받고 사용자가 원할 때, '!menu'를 입력하여 당일 메뉴의 정보를 받을 수 있다
To notice about Hongik University's cafeteria menu at every 10:30am on Discord,
When the user enters '!menu' in the chat room when user want, the information about the menu is informed through the UI

-도커 이미지를 통해 컨테이너에 적용하였고 배포하였습니다.
It works by distributing 'centos/python-38-centos7' through a docker as a base image through a container
---

## How to use?
* Default : Discord API Key를 discordbot.py의 8번 Line의 token변수에 넣어주시기 바랍니다.

* [주의] 해당 파일에서 기본적인 인터페이스 제공 및 원리를 보여드리기 위해 메소드에 키를 넣었지만 실제 서비스를 하시는 경우 보안적인 측면을 고려하기 위해 환경변수에 저장하거나 yml파일 혹은 외부 DB서버로부터 불러오는 방법들을 추천드립니다

## Result
### Working on Docker app 
Using Docker, the image 'centos/python-38-centos7' was set as the base image and distributed through a container
<img width="977" alt="도커 참조" src="https://user-images.githubusercontent.com/112881296/209771366-c895a2ae-ef14-42cb-a907-3326628fae2d.png">

----
### Working on Discord
<img width="540" alt="작동화면" src="https://user-images.githubusercontent.com/112881296/209770998-7fffc30d-5012-4578-8a44-ca4cff834a4b.png">



### Updates verion0.1
2022/11/08 -> When executing code, I can check an errors. Completeing partial of Function [cycle]

### Updates version 0.2
2022/11/10 -> pathed on Discord by Discord Bot, if you are hongik univ student you can use this code 'just type your bot token'

### Updates version 0.3
2022/11/11 -> removed some function and some function was slightly modified.

## Updates version 0.4 & Releases
2022/12/28 -> Add Dockerfile and Modifying code with structural changes in the information-provided site
 [The function to receive an alarm at a specific time will be implemented soon]


Thanks for the advice --J-hoplin / https://github.com/J-hoplin1
