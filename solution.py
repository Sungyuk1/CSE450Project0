import re

def make_sarcastic(text):
    text = text.rstrip()

    #use regext
    pattern = ' (\\\\s)'
    text = re.sub(pattern, '', text)
    text = text + ' \s'
    return text

text = "Life is Great!"
print(make_sarcastic(text))
