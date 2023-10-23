import telebot
from telebot import types

token = '6841221425:AAHNBoAb5dOi4ujLYCltjIqEcxDkvY3wso4'
bot = telebot.TeleBot(token)
@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("привет")
    btn2 = types.KeyboardButton("кд чд")
    btn3 = types.KeyboardButton("хсе мемы")
    btn4 = types.KeyboardButton("бабуле")
    btn5 = types.KeyboardButton("сэд муд")
    btn6 = types.KeyboardButton("твоему крашу")
    btn7 = types.KeyboardButton("ругань")
    btn8 = types.KeyboardButton("споки")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
    bot.send_message(m.chat.id, 'приветик, {0.first_name}! здесь ты можешь найти картинки на любой случай жизни.\nвыбери, картинка какой категории тебе нужна'.format(m.from_user), reply_markup=markup)
@bot.message_handler(content_types=["text","stiker"])
def handle_text(m):
    if m.text == "ругань":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("к категориям")
        markup.add(back) 
        bot.send_media_group(m.chat.id,[telebot.types.InputMediaPhoto("https://sun9-1.userapi.com/impg/pQmVaCyelXqz83oaLyDG--sOAjKUzQN0qYU_dA/UQSfhHmx2oc.jpg?size=1472x1472&quality=95&sign=c1ed1f536cb30f64c9b02aadef9de56b&type=album"), telebot.types.InputMediaPhoto("https://sun9-56.userapi.com/impg/9O_Di8hb9K8YrFrC1Ua6IiRgJaVxVbHYAbQRIg/TmJ3Frc3zfg.jpg?size=782x782&quality=95&sign=ab989ee508c2e63372ec519b62923495&type=album"), telebot.types.InputMediaPhoto("https://sun9-63.userapi.com/impg/Umx3HMt3sbjO8myOBykmWbayaDWoFJ9yJmr87Q/PVZm6Du7yvw.jpg?size=720x658&quality=95&sign=24b93e17e84eb6aa484eb03500c8066e&type=album"),telebot.types.InputMediaPhoto("https://sun9-32.userapi.com/impg/frkFRcbmzDMSjZmxj4hIlLpQgt7wCVftducQMQ/FZiH9yQVqpg.jpg?size=749x755&quality=95&sign=4f622875e5faaf1e9830848fd0688f73&type=album"),telebot.types.InputMediaPhoto("https://sun9-71.userapi.com/impg/MgD_jKst-3SFViZG6JBVMa-ja8aCS1JXJWKdCw/DMd0xwl02SU.jpg?size=451x438&quality=95&sign=a1a8d4d454869c36e4dde063e9bc7f86&type=album"),telebot.types.InputMediaPhoto("https://sun9-64.userapi.com/impg/UryNt57r5ZlZ7j2YyMVeuVDM0tnf6TNqAihxsQ/ZyLqR7eX19M.jpg?size=600x600&quality=95&sign=b1fba58e551dd091740bbc36e5f9c040&type=album"),telebot.types.InputMediaPhoto("https://sun9-32.userapi.com/impg/iBLZmJLRWg1ko5Ui5VO3yQCdSgu_1zqzF7EYKQ/SqIfGJXvaJE.jpg?size=720x720&quality=95&sign=36ac3570c2f444f93b1d42877e2f147e&type=album"), telebot.types.InputMediaPhoto("https://sun9-35.userapi.com/impg/lXbB7NAg9s1G8bcTkxGrfBDQhD0WHgCbiPSHAw/3hUROijzRng.jpg?size=736x736&quality=95&sign=ebe821cd768c059728fc000ce925216c&type=album"), telebot.types.InputMediaPhoto("https://sun9-50.userapi.com/impg/wLWojs8IfvePhKpV0MvhESntAKdK6VnJ_JAFAg/GY5HvJyDIkc.jpg?size=453x604&quality=95&sign=4930dfe328d4e494e7b9d25fe057d8ae&type=album"), telebot.types.InputMediaPhoto("https://sun9-23.userapi.com/impg/g3lDXfbotmMVDaVwizuKgl1ga4xfFjjzThNz-w/QGtTzbpZYcQ.jpg?size=584x585&quality=95&sign=f72d5ac5823d3a71a2bed8daeb5caeac&type=album")])
        bot.send_message(m.chat.id, text="можешь посмотреть другие категории картинок", reply_markup=markup)
    elif m.text == "твоему крашу":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("к категориям")
        markup.add(back) 
        bot.send_media_group(m.chat.id,[telebot.types.InputMediaPhoto("https://sun9-3.userapi.com/impg/JcrkRVBczdNMSnTb6CccnFpfpHdTJ-cNf7qV4Q/hwtfi7o1Cfw.jpg?size=736x736&quality=95&sign=049cb427400ca1f3cec1895e65e37b45&type=album"), telebot.types.InputMediaPhoto("https://sun9-69.userapi.com/impg/OdyIdHPCwjXHg_XOK56-eyiNAt2rM1CUO8_Kjw/jIQBBjven1Q.jpg?size=736x736&quality=95&sign=7135486f1cb68abd48ff960bbb3080db&type=album"),telebot.types.InputMediaPhoto("https://sun9-70.userapi.com/impg/XCD-ntzxsgQfXuF_-xz8wBzcNw_Zuq7w37i9dw/75JA18tPEDU.jpg?size=730x728&quality=95&sign=21562c880961423e0ba865f7d9e46dc9&type=album"),telebot.types.InputMediaPhoto("https://sun9-77.userapi.com/impg/iG4qVK2Fs4MbhYE5TXRHEiHt8w3GdLtvyeUSwA/VQgIwr7gTDw.jpg?size=748x465&quality=95&sign=b9f583a969c06a2086359fd7cb80d2a0&type=album"),telebot.types.InputMediaPhoto("https://sun9-44.userapi.com/impg/zH-8bzxPlAdfyeEA22YJSKS_Dp7IyBfVhNV2qg/FuAQVTdlhh8.jpg?size=720x475&quality=95&sign=7be4375f3b310a3d841707af2458ff4c&type=album"),telebot.types.InputMediaPhoto("https://sun9-72.userapi.com/impg/BAn0bdLBCFmJJnzogC76P_r59tDUZPifVnATYA/U5L3CVx-Ibw.jpg?size=474x480&quality=95&sign=f34df9476a8213ddf2f01b524470e9eb&type=album"),telebot.types.InputMediaPhoto("https://sun9-57.userapi.com/impg/p0zKtaKzBE1llLv84R06T2OSD-mCC_soXB42tA/Zx33jBhbsug.jpg?size=582x577&quality=95&sign=f301fff0b7a662f233da31d04b4a1e9f&type=album"),telebot.types.InputMediaPhoto("https://sun9-57.userapi.com/impg/M_jxajwr0i8eJrrbbJjIEwWth48ekRXtJSIaOQ/F5UFOaYW9Jk.jpg?size=440x649&quality=95&sign=94aff1614dc1d9d026d6169c8f73574b&type=album"),telebot.types.InputMediaPhoto("https://sun9-62.userapi.com/impg/RR5hVpquTbIpspOBE5T-DpzYtVenkxYKc2v0xw/TyI9Yl7KyMc.jpg?size=736x719&quality=95&sign=ee7448b0e2accb4a20cac84da54a457c&type=album"),telebot.types.InputMediaPhoto("https://sun9-65.userapi.com/impg/53DDs3tn7Z6mVSAEXopxepHiM27LWxz6yaWALQ/vpCBT1ipg9I.jpg?size=593x593&quality=95&sign=d9ab83714fbf9fa7df1fa194d5ed1f6d&type=album")])
        bot.send_message(m.chat.id, text="можешь посмотреть другие категории картинок", reply_markup=markup)
    elif (m.text == "к категориям"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton("привет")
        btn2 = types.KeyboardButton("кд чд")
        btn3 = types.KeyboardButton("хсе мемы")
        btn4 = types.KeyboardButton("бабуле")
        btn5 = types.KeyboardButton("сэд муд")
        btn6 = types.KeyboardButton("твоему крашу")
        btn7 = types.KeyboardButton("ругань")
        btn8 = types.KeyboardButton("споки")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8) 
        bot.send_message(m.chat.id, text="менюшка", reply_markup=markup)    
        bot.polling(none_stop=True, interval=0)
