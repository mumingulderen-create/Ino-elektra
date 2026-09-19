import os
import re

# Comprehensive list of emoji chars to strip
EMOJI_CHARS = [
    '\U0001F4DE', # 📞
    '\U0001F4AC', # 💬
    '\U0001F6A8', # 🚨
    '\U000026A1', # ⚡
    '\U0001F4CB', # 📋
    '\U0001F50C', # 🔌
    '\U0001F4B6', # 💶
    '\U0001F9ED', # 🧭
    '\U0001F4CD', # 📍
    '\U0001F6E1', # 🛡
    '\U00002B50', # ⭐
    '\U0001F4C5', # 📅
    '\U00002753', # ❓
    '\U00002709', # ✉
    '\U0001F525', # 🔥
    '\U0001F4A7', # 💧
    '\U0001F3E1', # 🏡
    '\U00002600', # ☀️
    '\U0001F4F8', # 📸
    '\U0001F697', # 🚗
    '\U0001F504', # 🔄
    '\U0001F6E0', # 🛠
    '\U00002696', # ⚖
    '\U0001F33F', # 🌿
    '\U0001F4A1', # 💡
    '\U0001F30A', # 🌊
    '\U0001F9F1', # 🧱
    '\U0001F373', # 🍳
    '\U0001F527', # 🔧
    '\U0001F91D', # 🤝
    '\U0001F9EA', # 🧪
    '\U0001F9FE', # 🧾
    '\U0001F3D8', # 🏘
    '\U0001F4F7', # 📷
    '\U0001F914', # 🤔
    '\U0001F552', # 🕒
    '\U0000FE0F', # variation selector-16
    '\U0000FE0E', # variation selector-15
]

def strip_emojis(text):
    for ch in EMOJI_CHARS:
        text = text.replace(ch, '')
    # Also clean regex emojis
    text = re.sub(r'[\U0001F300-\U0001F6FF\U0001F900-\U0001F9FF\U0001FA00-\U0001FAFF\u2600-\u26FF\u2700-\u27BF\u2B50]', '', text)
    # Clean double spaces caused by emoji removal
    text = re.sub(r'  +', ' ', text)
    text = text.replace(' >', '>')
    text = text.replace('> ', '>')
    return text

print("Emoji cleaner module ready")
