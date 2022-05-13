from googletrans import Translator

translator = Translator()
# sentence = "안녕하세요 박진석입니다"
language = input("Choose language to interperrt to: ")
sentence = input("Enter a sentence: ")


result = translator.translate(sentence, language)

detected = translator.detect(sentence)

print(detected.lang, ":", sentence)
print(result.dest, ":", result.text)