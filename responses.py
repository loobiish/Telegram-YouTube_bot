from datetime import datetime
from yt_dlp import YoutubeDL
from telegram import Chat
import asyncio
import nest_asyncio
nest_asyncio.apply()



def sampleResposnse(chat_id, user_message):

    user_message = str(user_message).lower()

    if user_message in ("hello", "hi", "hey", "whatsup", "namaste"):
        return "Hello, I'm a bot that download YouTube videos from a given link! Try to send me a link!"
    
    if user_message in ("how are you?", "how are you", "how's everything?", "how's everything", "how are you doing?"):
        return "I'm fine as long as I'm not banned by YouTube :D"
    
    if user_message in ("thanks", "thank you", "thx", "thank", "thank you!"):
        return "I'm glad that I was helpful for you :D"
    
    if user_message in ("time", "time?", "what is the time?", "what's the time", "time now"):
        now = datetime.now()
        time_now = now.strftime("%d/%m/%y, %H:%M:%S")
        return "The time is now: " + str(time_now)
    
    
    else:
        return "Sorry my usability is limited so I did not understand what you are trying to say. :("


    