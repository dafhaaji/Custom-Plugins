
# Custom-Plugins USERGE 
# https://github.com/UsergeTeam/Userge

# Credit~~
# https://github.com/Ajibcdefgh/ProjectDark (ProjectDark)
# https://github.com/vckyou/Geez-UserBot (GeezProject) 
# https://github.com/apisuserbot/King-Userbot (King-Userbot)

# t.me/dafhaaji

import asyncio

from re import sub
from random import choice
from userge import userge

#>>>>>>>>>>>>>>>>

@userge.on_cmd("hand$", about={'header': "Hand Emoticon..."})
async def hand_(message):
    """hand animation"""
    animation_chars = [
        "👈",
        "👉",
        "☝️",
        "👆",
        "🖕",
        "👇",
        "✌️",
        "🤞",
        "🖖",
        "🤘",
        "🤙",
        "🖐️",
        "👌",
    ]
    animation_interval = 1
    animation_ttl = range(13)

    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 13])

#>>>>>>>>>>>>>>>>

@userge.on_cmd("semangat$", about={'header': "Semangat..."})
async def punten_(message):
    """semangat"""
    await message.edit("`Apapun Yang Terjadi`")
    await asyncio.sleep(3)
    await message.edit("`Tetaplah Bernapas`")
    await asyncio.sleep(1)
    await message.edit("`Dan Selalu Bersyukur`")
    await asyncio.sleep(1)
    await message.edit("`Hahaha`")

#>>>>>>>>>>>>>>>>

@userge.on_cmd("foff$", about={'header': "ffof..."})
async def foff_(message):
    """fuck animation"""
    await message.edit(".                       /¯ )")
    await message.edit(".                       /¯ )\n                      /¯  /")
    await message.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /"
    )
    await message.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸"
    )
    await message.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ "
    )
    await message.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')"
    )
    await message.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /"
    )
    await message.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´"
    )
    await message.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´\n            \\              ("
    )
    await message.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´\n            \\              (\n              \\  "
    )

#>>>>>>>>>>>>>>>>

@userge.on_cmd("awk$", about={'header': "Awkwokwokwok..."})
async def awk_(message):
    """awkwokwo"""
    await message.edit(
        "────██──────▀▀▀██\n"
        "──▄▀█▄▄▄─────▄▀█▄▄▄\n"
        "▄▀──█▄▄──────█─█▄▄\n"
        "─▄▄▄▀──▀▄───▄▄▄▀──▀▄\n"
        "─▀───────▀▀─▀───────▀▀\n`Awkwokwokwok..`"
    )

#>>>>>>>>>>>>>>>>

@userge.on_cmd("punten$", about={'header': "Punten..."})
async def punten_(message):
    """punten"""
    await message.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**Punten**")

#>>>>>>>>>>>>>>>>

@userge.on_cmd("hoa$", about={'header': "Hoaaa..."})
async def hoa_(message):
    """hoaa"""
    await message.edit(
            "`\n█████████`"
            "`\n█▄█████▄█`"
            "`\n█▼▼▼▼▼`"
            "`\n█       Hoaaaa....`"
            "`\n█▲▲▲▲▲`"
            "`\n█████████`"
            "`\n ██   ██`")

#>>>>>>>>>>>>>>>>

@userge.on_cmd("huh$", about={'header': "Huhhh.."})
async def huh_(message):
    """this for u"""
    await message.edit("\n(\\_/)"
                     "\n(●_●)"
                     "\n />❤️ *Ini Buat Kamu")
    await asyncio.sleep(3)
    await message.edit("\n(\\_/)"
                     "\n(●_●)"
                     "\n/>💔  *Aku Ambil Lagi")
    await asyncio.sleep(2)
    await message.edit("\n(\\_/)"
                     "\n(●_●)"
                     "\n💔<\\  *Terimakasih")

#>>>>>>>>>>>>>>>>

@userge.on_cmd("gas$", about={'header': "Ninuninu...."})
async def gas_(message):
    """ambulance"""
    await message.edit("___________________🚑")
    await message.edit("________________🚑___")
    await message.edit("______________🚑_____")
    await message.edit("___________🚑________")
    await message.edit("________🚑___________")
    await message.edit("_____🚑______________")
    await message.edit("__🚑_________________")
    await message.edit("🚑___________________")
    await message.edit("_____________________")
    await message.edit(choice(HILIH))

#>>>>>>>>>>>>>>>>

@userge.on_cmd("anjay$", about={'header': "Anjay...."})
async def anjay_(message):
    """anjay"""
    await message.edit("""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠉⠉⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡟⠀⣠⣶⣿⣿⣶⣄⠀⢹⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣇⠀⠻⣿⣿⣿⣿⠟⠀⣸⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡏⠉⠀⠀⠉⠉⠀⠀⠉⢹⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡏⠉⠉⠉⠉⠉⠉⠉⠉⢹⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠙⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡏⠉⠉⠉⠉⠉⠉⠁⣠⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣇⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⢹⡏⠉⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠉⠉⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡟⠀⣠⣶⣿⣿⣶⣄⠀⢹⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣇⠀⠻⣿⣿⣿⣿⠟⠀⣸⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡏⠉⠀⠀⠉⠉⠀⠀⠉⢹⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠋⢹⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡇⠀⠉⠛⠛⠋⠉⠀⣀⣠⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⠉⠙⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣀⠀⢹⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠋⢹⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡇⠀⠉⠛⠛⠋⠉⠀⣀⣠⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⠉⠙⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣀⠀⢹⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
""")

#>>>>>>>>>>>>>>>>

@userge.on_cmd("kntl$", about={'header': "Kntl luu...."})
async def kntl_(message):
    """tydack ramah"""
    await message.edit("""
⣠⡶⠚⠛⠲⢄⡀
⣼⠁ ⠀⠀⠀ ⠳⢤⣄
⢿⠀⢧⡀⠀⠀⠀⠀⠀⢈⡇
⠈⠳⣼⡙⠒⠶⠶⠖⠚⠉⠳⣄
⠀⠀⠈⣇⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄
⠀⠀⠀⠘⣆ ⠀⠀⠀⠀ ⠀⠈⠓⢦⣀
⠀⠀⠀⠀⠈⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠲⢤
⠀⠀⠀⠀⠀⠀⠙⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧
⠀⠀⠀⠀⠀⠀⠀⡴⠋⠓⠦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠈⣇
⠀⠀⠀⠀⠀⠀⣸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡄
⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇
⠀⠀⠀⠀⠀⠀⢹⡄⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃
⠀⠀⠀⠀⠀⠀⠀⠙⢦⣀⣳⡀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⢦⣀⣀⣀⣀⣠⡴⠚⠁⠉⠉⠉
""")

#>>>>>>>>>>>>>>>>

@userge.on_cmd("koc$", about={'header': "Ngocok dulu ngab..."})
async def koc(message):
    """colay animation"""
    await message.edit("8✊===D")
    await message.edit("8=✊==D")
    await message.edit("8==✊=D")
    await message.edit("8===✊D")
    await message.edit("8==✊=D")
    await message.edit("8=✊==D")
    await message.edit("8✊===D")
    await message.edit("8=✊==D")
    await message.edit("8==✊==D")
    await message.edit("8===✊D💦")
    await message.edit("8==✊=D💦💦")
    await message.edit("8=✊==D💦💦💦")
    await message.edit("8✊===D💦💦💦💦")
    await message.edit("8===✊D💦💦💦💦💦")
    await message.edit("┐(´д｀)┌")

#>>>>>>>>>>>>>>>>

@userge.on_cmd("babi$", about={'header': "Babi luu...."})
async def babi_(message):
    """pig ngok"""
    await message.edit("┈┈┏━╮╭━┓┈╭━━━━╮\n"
                     "┈┈┃┏┗┛┓┃╭┫Ngok ┃\n"
                     "┈┈╰┓▋▋┏╯╯╰━━━━╯\n"
                     "┈╭━┻╮╲┗━━━━╮╭╮┈\n"
                     "┈┃▎▎┃╲╲╲╲╲╲┣━╯┈\n"
                     "┈╰━┳┻▅╯╲╲╲╲┃┈┈┈\n"
                     "┈┈┈╰━┳┓┏┳┓┏╯┈┈┈\n"
                     "┈┈┈┈┈┗┻┛┗┻┛┈┈┈┈\n")

#>>>>>>>>>>>>>>>>

@userge.on_cmd("y$", about={'header': "👍"})
async def y_(message):
    """thumb"""
    await message.edit("‡‡‡‡‡‡‡‡‡‡‡‡▄▄▄▄\n"
                     "‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█\n"
                     "‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█\n"
                     "‡‡‡‡‡‡‡‡‡‡█‡‡‡‡‡█\n"
                     "‡‡‡‡‡‡‡‡‡█‡‡‡‡‡‡█\n"
                     "██████▄▄█‡‡‡‡‡‡████████▄\n"
                     "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
                     "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
                     "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
                     "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
                     "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
                     "▓▓▓▓▓▓█████‡‡‡‡‡‡‡‡‡‡‡‡██\n"
                     "█████‡‡‡‡‡‡‡██████████\n")

#>>>>>>>>>>>>>>>>

@userge.on_cmd("ii", about={
    'header': "HILIH KINTIL >.<",
    'usage': "{tr}ii [input | reply to msg]"})
async def ii_(message):
    """aeiou to i"""
    input_str = message.input_or_reply_str
    if not input_str:
        await message.edit("` Hilih no text given! `")
        return
    reply_text = sub(r"([aeiou])", "i", input_str)
    reply_text = sub(r"([AEIOU])", "I", reply_text)
    reply_text += " " + choice(HILIH)
    await message.edit(reply_text)

HILIH = (

    "┐(´д｀)┌",

    "┐(´～｀)┌",

    "┐(´ー｀)┌",

    "┐(￣ヘ￣)┌",

    "╮(╯∀╰)╭",

    "╮(╯_╰)╭",

    "┐(´д`)┌",

    "┐(´∀｀)┌",

    "ʅ(́◡◝)ʃ",

    "┐(ﾟ～ﾟ)┌",

    "┐('д')┌",

    "┐(‘～`;)┌",

    "ヘ(´－｀;)ヘ",

    "┐( -“-)┌",

    "ʅ（´◔౪◔）ʃ",

    "ヽ(゜～゜o)ノ",

    "ヽ(~～~ )ノ",

    "┐(~ー~;)┌",

    "┐(-。ー;)┌",

    r"¯\_(ツ)_/¯",

    r"¯\_(⊙_ʖ⊙)_/¯",

    r"¯\_༼ ಥ ‿ ಥ ༽_/¯",

    "乁( ⁰͡  Ĺ̯ ⁰͡ ) ㄏ",

)
