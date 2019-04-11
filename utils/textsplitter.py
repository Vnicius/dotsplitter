import re

class TextSplitter:
    def __init__(self):
        self.split_regex = re.compile(r'(\S*\([^\)]+\)\S*)|(\S*\"[^\"]+\"\S*)|(\S*\[[^\]]+\]\S*)|([\S]+)')

    def split(self, text):

        splitted = []
        for word in self.split_regex.finditer(text):
            for g in word.groups():
                if g:
                    splitted.append(g)
        
        return splitted