import sqlite3
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = '8781909897:AAEYoT4ONnLH15gURUewmSh2HjO52H8EQOM'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("👤 Profil", callback_data="profile"), InlineKeyboardButton("🛍 Mağaza", callback_data="shop")],
        [InlineKeyboardButton("💰 Kazan", callback_data="earn"), InlineKeyboardButton("💸 Para İadesi", callback_data="refund")],
        [InlineKeyboardButton("ℹ️ Bilgi", callback_data="info"), InlineKeyboardButton("🎁 Ücretsiz İstek", callback_data="free")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("✨ Sasu Snos Ana Menüye Hoş Geldiniz!\n\nBir işlem seçin:", reply_markup=reply_markup)

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot baslatildi!")
    app.run_polling()
    