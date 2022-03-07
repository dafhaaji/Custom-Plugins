""" hilih kintil """

# Copyright (C) 2020-2022 by UsergeTeam@Github, < https://github.com/UsergeTeam >.

#

# This file is part of < https://github.com/UsergeTeam/Userge > project,

# and is released under the "GNU v3.0 License Agreement".

# Please see < https://github.com/UsergeTeam/Userge/blob/master/LICENSE >

# from ProjectDark to Userge

# t.me/dafhaaji

# All rights reserved.

import os

import asyncio

from re import sub

from random import choice

from userge import userge, Message, pool

@userge.on_cmd("hilih", about={

    'header': "hilih kintil >.<",

    'usage': "{tr}hilih [input | reply to msg]"})

async def test_(message: Message):

    """hilih"""

    input_str = message.input_or_reply_str

    if not input_str:

        await message.err("`no text given!  `" + choice(HILIH))

        return

    reply_text = []

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
