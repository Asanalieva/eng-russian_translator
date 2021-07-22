from translate import Translator
translator = Translator(to_lang='Russian')
try:
    while True:

        this_word = str(input('Write word to translate: '))
        out = translator.translate(this_word)
        print(out)
except ValueError:
    print('Enter a word!')
