import emoji

def is_contain_emojis(s):
    if isinstance(s, str):
        if emoji.emoji_count(s) > 0:
            return True
        return False
    return False

def extract_emojis(text):
    if not isinstance(text, str):
        return text
    return ''.join(c for c in text if c in emoji.EMOJI_DATA)

def remove_emojis(text):
    return emoji.replace_emoji(text)

    