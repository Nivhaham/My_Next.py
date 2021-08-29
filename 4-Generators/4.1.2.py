# 4.1.2
def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    generate_english = (words[spanish_word] for spanish_word in sentence.split())
    return generate_english


# Spanish to English Translator
def main():
    spanish_sentence = "la gato esta  "
    # print(list(translate(spanish_sentence)))
    for word in translate(spanish_sentence):
        print(word)


if __name__ == '__main__':
    main()
