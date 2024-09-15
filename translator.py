from translate import Translator
while True:
    lang_to_translate = input("Enter the language to translate(en): ")
    if lang_to_translate.lower() == "exit":
        print("Exiting translator...")
        break
    translator = Translator(to_lang=lang_to_translate)
    from_user = input("Input your sentence: ")
    with open("words.txt", mode="w") as file:
        file.write(from_user)

    try:
        with open("words.txt", "r") as eng_sentence:
            sentence = eng_sentence.readline()
            translation = translator.translate(sentence)
            print(translation)

        with open("translated.txt", mode="w") as translated_sentence:
            translated_sentence.write(translation)
    except FileNotFoundError:
        print("File not found")

