from os import system
import re
import spacy
from utils.checkabbreviation import CheckAbbreviations
import utils.arguments as arguments
from utils.textsplitter import TextSplitter

text_splitter = TextSplitter()

def dot_splitter(text, out_file=None):
    words = text_splitter.split(text.replace('\n', '').strip())
    
    split_indexes = []

    for index, word in enumerate(words):

        if word:
            # check if has a dot
            if '.' in word and not has_symbols(word):

                # numbers
                try:
                    float(word)
                    if word.index('.') != len(word) - 1:
                        continue
                except:
                    pass
                    
                if not abbrev_checker.check(word):
                    if index < len(words) - 1:
                        current_word = nlp(word)
                        next_word = nlp(words[index + 1])

                        #print(current_word.text, current_word[0].pos_)
                        #print(next_word[0].text, next_word[0].pos_)
                        
                        if next_word[0].pos_ == 'PUNCT' and has_symbols(next_word.text):
                            split_indexes.append(index)

                        elif next_word[0].pos_ == 'ADP' and '.' not in next_word.text: 
                            pass
                        
                        elif next_word[0].pos_ == 'PUNCT' and \
                            re.search(r'\w+', next_word[0].text):
                                pass

                        elif next_word[0].pos_ != 'PROPN' and \
                            '.' not in next_word.text and \
                                index + 1 != len(words) - 1:
                            split_indexes.append(index)

    # print(words)
    # print(split_indexes)
    if len(split_indexes):
        if len(split_indexes) == 1 and split_indexes[0] == len(words) - 1:
            show_result(' '.join(words), out_file)
        else:
            past = 0

            for split_i in split_indexes:
                show_result(' '.join(words[past: split_i + 1]), out_file)
                past = split_i + 1
            
            if past != len(words):
                show_result(' '.join(words[past:]), out_file)

    else:
        show_result(' '.join(words), out_file)

def show_result(text, out_file=None):
    if out_file:
        out_file.write(text + '\n')
    else:
        print(text)

def has_symbols(word):
    symbols = ['"', '(', ')', '[', ']']
    has_symbol = False

    for s in symbols:
        if s in word:
            has_symbol = True
    
    return has_symbol
    

if __name__ == '__main__':

    # get arguments
    args = arguments.args()

    # check spacy module
    try:
        nlp = spacy.load(args.lang)
    except OSError:
        system(f'python -m spacy download {args.lang}')
        nlp = spacy.load(args.lang)

    # create the abbreviation checker
    abbrev_checker = CheckAbbreviations(args.abbrev_path)
    text_splitter = TextSplitter()

    try:
        while True:
            text = input()
            dot_splitter(text)
    except EOFError:
        pass
