import telebot
import config

bot = telebot.TeleBot(config.BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_game(message):
    welcome_text = (
        "🔥 *КРЕСТОНОСЕЦ: ПУТЬ МЕСТИ* 🔥\n\n"
        "_Вы шли через древний лес, когда открылся портал тьмы..._\n\n"
        "⚔️ Ваш отряд погиб. Чудовища растерзали всех. Выжили только вы. "
        "Теперь в вашем сердце лишь ярость и жажда возмездия.\n\n"
        "🌑 Вы *поклялись* найти этих тварей и уничтожить их, даже если это будет последнее, что вы сделаете.\n\n"
        "➖➖➖\n"
        "🚩 *Ваше путешествие начинается здесь...*"
    )
    
    bot.send_message(
        message.chat.id,
        welcome_text,
        parse_mode='Markdown'
    )

if name == "main":
    bot.polling(none_stop=True)
