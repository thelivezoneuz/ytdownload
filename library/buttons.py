# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Name     : inline-tube-mate [ Telegram ]
# Repo     : https://github.com/m4mallu/inine-tube-mate
# Author   : Renjith Mangal [ https://t.me/space4renjith ]

from urllib.parse import quote
from presets import Presets
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_btn = [
    [
        InlineKeyboardButton('Ko`rish', callback_data='view_btn'),
        InlineKeyboardButton('O`chirish', callback_data='del_btn')

    ],
    [
        InlineKeyboardButton('Yordam', callback_data='help_btn'),
        InlineKeyboardButton('Yordam', url='t.me/i_shakhzod')
    ],
    [
        InlineKeyboardButton('Yopish', callback_data='close_btn'),
        InlineKeyboardButton('Inline Qidirish', switch_inline_query_current_chat='')
    ]
]


del_thumb = [
    [
        InlineKeyboardButton("DEL THUMB", callback_data="thumb_del_conf_btn"),
        InlineKeyboardButton("Ortga", callback_data="a_back_btn")
    ]
]

join_channel = [
    [
        InlineKeyboardButton('⚙ Yangiliklar', url='https://telegram.me/Ultrasoft_uz'),
        InlineKeyboardButton('Inline qidirish', switch_inline_query_current_chat='')
    ]
]


back_button = [
    [
        InlineKeyboardButton('⬅️ Ortga', callback_data='back_btn')
    ]
]

close_button = [
    [
        InlineKeyboardButton('❌ Yopish', callback_data='close_btn'),
        InlineKeyboardButton('Uyga', callback_data='home_btn')
    ]
]

cancel_button = [
    [
        InlineKeyboardButton('Bekor qilmoq', callback_data='cancel_btn')
    ]
]

prompt_thumb_btn = [
    [
        InlineKeyboardButton('Ha', callback_data='set_thumb_btn'),
        InlineKeyboardButton('Yo`q', callback_data='close_btn')
    ]
]

reply_markup_cancel = InlineKeyboardMarkup(cancel_button)
reply_markup_close = InlineKeyboardMarkup(close_button)
reply_markup_back = InlineKeyboardMarkup(back_button)
reply_markup_join = InlineKeyboardMarkup(join_channel)
reply_markup_del_thumb = InlineKeyboardMarkup(del_thumb)
reply_markup_start = InlineKeyboardMarkup(start_btn)
reply_markup_thumb = InlineKeyboardMarkup(prompt_thumb_btn)

def get_reply_markup(username):
    url = 't.me/share/url?url=' + quote(Presets.SHARE_BUTTON_TEXT.format(username=username))
    buttons = [[InlineKeyboardButton('Share bot', url=url),
                InlineKeyboardButton("Search Inline", switch_inline_query_current_chat='')]]
    reply_markup_share = InlineKeyboardMarkup(buttons)
    return reply_markup_share
