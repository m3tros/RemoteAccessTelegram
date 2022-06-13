 

<p align="center"> 
  <img src="https://user-images.githubusercontent.com/107058068/173295144-26031d02-65c3-4972-ac73-909a656a2c76.png" alt="RemoteAccessTelegram" width="80px" height="80px">
</p>
<h1 align="center">Remote Access Telegram</h1> 

## Description
A remote access script for transmitting machine control commands is used by telegram.<br>
This script was written in <a href="https://python.org">python3</a>. Using the <a href="https://pypi.org/project/pyTelegramBotAPI/0.3.0/">pyTelegramBotAPI</a> library.
<br><br>
__This project is purely informational in nature.__
## Installation for python3
### Libraries
- <a href="https://pypi.org/project/pyTelegramBotAPI/0.3.0/">pyTelegramBotAPI</a>
```bash
git clone https://github.com/John-MetrosSoftware/RemoteAccessTelegram
cd RemoteAccessTelegram
pip3 install -r requirements.txt
```
Now you need to edit the file RemoteAccessTelegram.py
```python
bot = telebot.TeleBot('') # Here you need to insert your token.
```
You need to insert a token here. You can get it by creating a bot in <a href="https://telegram.me/BotFather">BotFather</a>.<br>
```python
users = [] # Insert your telegram user id here.
```
In these square brackets you need to enter your telegram user id. You can get it from the <a href="https://t.me/getmyid_bot">Get My ID bot</a>.<br>
This is necessary so that only a limited number of users can use the bot. Since with the help of a bot you will control the machine.
