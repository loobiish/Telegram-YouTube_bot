from datetime import datetime
from yt_dlp import YoutubeDL

def sampleResposnse(chat_id, user_message):
    if "https://youtu.be/" in user_message:
        try:
            user_message = "https://www.youtube.com/watch?v=" + user_message[-11:]
            URLS = [user_message]
            with YoutubeDL() as yld:
                video_info = yld.extract_info(URLS[0], download=False)
                video_name = video_info['title']
                print("===============================")
                print(video_name)
                return yld.download(URLS)
        except Exception as e:
            return f"Sorry, it seems like the given link is broken :( \
                Here's the error that occured: {e}"

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
    
    

    return "Sorry my usability is limited so I did not understand what you are trying to say. :("


    