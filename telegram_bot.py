from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import requests

API_URL = "https://qwen3-4gl9.onrender.com"  # غير هذا للرابط الفعلي لسيرفرك على Render
ALLOWED_USER_ID = 6837315281  # معرف تلجرام الخاص بك فقط مسموح له باستخدام البوت

def start(update: Update, context: CallbackContext):
    update.message.reply_text("مرحبًا! أرسل لي رسالة وسأرد عليك.")

def handle_message(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    if user_id != ALLOWED_USER_ID:
        update.message.reply_text("عذرًا، لا يمكنك استخدام هذا البوت.")
        return
    
    user_text = update.message.text
    try:
        response = requests.post(API_URL, json={"text": user_text}).json()
        reply = response.get("response", "عذرًا، حدث خطأ في الرد.")
    except Exception as e:
        reply = "خطأ في الاتصال بالخدمة."
    update.message.reply_text(reply)

def main():
    updater = Updater("7537714477:AAGbdxU0pvQEpBK2Ee5qDguOGcTQPsdIp8o", use_context=True)  # ضع توكن بوت تلجرام هنا
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
