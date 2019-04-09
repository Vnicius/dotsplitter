from os import system
import spacy
from utils.checkabbreviation import CheckAbbreviations
import utils.arguments as arguments

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

    text = input()

    while text:
        words = text.split(' ')
        split_indexes = []

        for index, word in enumerate(words):

            if word.strip():
                # check if has a dot
                if '.' in word:
                    if not abbrev_checker.check(word):
                        if index < len(words) - 1:
                            current_word = nlp(word)
                            next_word = nlp(words[index + 1])

                            print(word)
                            print(current_word[0].pos_)

                            if current_word[0].pos_ == 'PROPN' and next_word[0].pos_ == 'PROPN' and ('.' not in words[index + 1] or ',' not in words[index + 1]):
                                split_indexes.append(index)
                            elif next_word[0].pos_ != 'PROPN' and '.' not in words[index + 1]:
                                split_indexes.append(index)
                        else:
                            split_indexes.append(index)
                elif '!' in word or '?' in word:
                    split_indexes.append(index)

        print(words)
        print(split_indexes)
        if len(split_indexes):
            if len(split_indexes) == 1 and split_indexes[0] == len(words) - 1:
                print(' '.join(words))
            else:
                past = 0

                for split_i in split_indexes:
                    print(' '.join(words[past: split_i + 1]))
                    past = split_i + 1

                print(' '.join(words[past:]))

        else:
            print(' '.join(words))

        text = input()
