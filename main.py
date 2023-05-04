from telegram.ext import *
from telegram import Update
import os
import responses as r
import constants as keys
from yt_dlp import YoutubeDL


async def startCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text= "I'm a bot, send me a YouTube link and see the magic!!"
    )

async def helpCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text= "Click on share button of the YouTube video that you want to download and copy it's link. \
                After that paste that link here and send it to me!"
    )
    
async def handleMessage(update, context):
    chat_id=update.effective_chat.id
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text= r.sampleResposnse(chat_id, update.message.text)
    )

async def youtubeMessage(update, context):
    chat_id=update.effective_chat.id
    user_message = update.message.text
    
    try:
        user_message = "https://www.youtube.com/watch?v=" + user_message[-11:]
        URLS = [user_message]
        with YoutubeDL() as yld:
            yld.download(URLS)
            video_info = yld.extract_info(URLS[0], download=False)
            video_name = video_info['title']
            file_name = video_name + " ["+ str(user_message[-11:]) +"].mp4"
        with open(file_name, "rb") as file:
            await context.bot.send_document(chat_id, document=file, filename= video_name)
    except Exception as e:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text= f"The link is not working :( \
                 {e}"
        )
    if os.path.exists(file_name):
        os.remove(file_name)
    
    await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text= "Video downloaded successfully!!"
            )
    


    

def error(update, context):
    print(f"Update {update} cause error {context.error}")
    return None


if __name__ == '__main__':
    application = ApplicationBuilder().token(keys.API_Token).build()

    # Commands
    application.add_handler(CommandHandler('start', startCommand))
    application.add_handler(CommandHandler('help', helpCommand))
    application.add_handler(MessageHandler(filters.Regex("https://youtu.be/") & (~filters.COMMAND), youtubeMessage))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handleMessage))
    application.add_error_handler(error)

    application.run_polling()