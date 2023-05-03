from telegram.ext import *
from telegram import Update
import responses as r
import constants as keys


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

def error(update, context):
    print(f"Update {update} cause error {context.error}")
    return None


if __name__ == '__main__':
    application = ApplicationBuilder().token(keys.API_Token).build()

    # Commands
    application.add_handler(CommandHandler('start', startCommand))
    application.add_handler(CommandHandler('help', helpCommand))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handleMessage))
    application.add_error_handler(error)

    application.run_polling()