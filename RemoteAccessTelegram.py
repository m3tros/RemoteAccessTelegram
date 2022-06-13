import os
import signal
import telebot 
import shlex
from subprocess import PIPE, Popen

bot = telebot.TeleBot('') # Here you need to insert your token.
users = [] # Insert your telegram user id here.

# Limited number of users using the bot.
@bot.message_handler(func=lambda message: message.chat.id not in users)
def some(message):
    pass

# Receiving a message -> Executing a command -> Return the result of executing a command
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == '/start':
        bot.send_message(message.chat.id, '''RemoteAccessTelegram 1.0
Github: https://github.com/John-MetrosSoftware/RemoteAccessTelegram

Available bot commands:
    exit or quit - Shutdown of the bot on the machine.''')
        return
    try:
        with Popen(message.text, stdout=PIPE, stderr=None, shell=True) as process:
            return_result_command = process.communicate()[0].decode('utf-8')
            command_split = shlex.split(message.text)
            if str(command_split[0]).lower() == 'exit' or str(command_split[0]).lower() == 'quit':
                bot.send_message(message.chat.id, 'Completion of the work...')
                os.kill(os.getpid(), signal.SIGINT)
            elif str(command_split[0]).lower() == 'cd':
                os.chdir(str(command_split[-1]))
            else:
                bot.send_message(message.chat.id, return_result_command)
    except Exception as error:
        bot.send_message(message.chat.id, error)


if __name__ == '__main__':
    bot.infinity_polling()