# Convert string to camel case

import re


def to_camel_case(text):
    if text == '':
        return ''

    check = text[0].isupper()

    words = [word.capitalize() for word in re.split('-|_', text)]
    print(words)
    if not check:
        words[0] = words[0].lower()
    ss = ''
    for s in words:
        ss += s

    return ss



# after realizing I was an idiot

def sol2(text):
    return text[:1] + text.title()[1:].replace('_', '').replace('-', '')

