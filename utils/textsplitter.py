import re

def text_splitter(text):
    splitted = []
    for word in re.finditer(r'(\S*\([^\)]+\)\S*)|(\S*\"[^\"]+\"\S*)|(\S*\[[^\]]+\]\S*)|([\S]+)', text):
        for g in word.groups():
            if g:
                splitted.append(g)
    
    return splitted