from utils.checkabbreviation import CheckAbbreviations

if __name__ == '__main__':
    abbrev_checker = CheckAbbreviations()
    text = input()

    while text:
        words = text.split(' ')
        split_indexes = []

        print(words)

        for index, word in enumerate(words):
            if word.strip():
                if '.' in word:
                    if not abbrev_checker.check(word):
                        split_indexes.append(index)
                elif '!' in word or '?' in word:
                    split_indexes.append(index)

        print(split_indexes)

        if len(split_indexes):
            past = 0

            for split_i in split_indexes:
                print(' '.join(words[past: split_i + 1]))
                past = split_i + 1

            print(' '.join(words[past:]))

        else:
            print(' '.join(words))

        text = input()
