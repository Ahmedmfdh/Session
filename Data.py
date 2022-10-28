from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
📟¦مرحبـاً بـك عزيـزي 📬 {}
⚡¦في بــوت استـخـراج جلـسـة
⚡¦استـخـراج تيرمـكـس تليثون
⚡¦وبــايــروجـرام للـمـيــوزك🎧
- يعمـل هـذا البـوت لمساعدتـك بطريقـة سهلـه للحصـول على كـود تيرمكـس لتشغيل تلـيثون والبايروجرام لتشغيل سـورس اغــاني تم انشـاء هـذا البـوت بواسطـة:  [❪❪͡,𝐃𝐀𝐃 𝐄𝐋𝐌𝐎𝐆𝐑𝐄𝐌 ⍣⃝🇻🇳𝐄𝐋𝐘𝐀𝐇𝐎𝐔𝐃𝐘𓏴❫❫](https://t.me/SourseZezoMusic)
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🌐¦اضـغـط لـبـدا استـخـراج كــود", callback_data="generate")],
        [InlineKeyboardButton(text="🔙رجوع", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("🌐¦اضـغـط لـبـدا استـخـراج كــود", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🌐¦اضـغـط لـبـدا استـخـراج كــود", callback_data="generate")],
        [InlineKeyboardButton(❪❪͡,𝐃𝐀𝐃 𝐄𝐋𝐌𝐎𝐆𝐑𝐄𝐌 ⍣⃝🇻🇳𝐄𝐋𝐘𝐀𝐇𝐎𝐔𝐃𝐘𓏴❫❫", url="https://t.me/SourseZezoMusic")],
        [
            InlineKeyboardButton("❓¦طـريـقـه الاسـتـخـدام", callback_data="help"),
            InlineKeyboardButton("💾¦مـعـلومـات", callback_data="about")
      ],
        [InlineKeyboardButton("⚙️¦الــســـورس", url="https://t.me/SourseZezoMusic")],
    ]


    # Help Message
    HELP = """
**📚¦الاوامــر الـمتـاحـه**
/about - معلومات البوت
/help - طريقه استخدامي
/start - حتى تشغل البوت
/generate - حتى تبدا بأستخراج كود
/cancel - لألغاء الاستخراج
/restart - اعادة تشغيل البوت
"""

    # About Message
    ABOUT = """
**💾¦مـعـلومـات** 
⚡¦بـوت استخـراج كـود تيرمكـس خـاص بســورس التليـثون وكــود بـايــروجـرام خـاص بـسـورس الـمـيـوزك🎶

🌀¦قـنـاه الـبـوت : [🔮SourseMUSIC🔮](https://t.me/SourseZezoMusic)

🌏¦اللـغــه : [بـايـثـون](www.python.org)

👨🏼‍💻¦الـمـبـرمــج : @SourseZezoMusic
    """
