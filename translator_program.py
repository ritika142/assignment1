from textblob import TextBlob

text = input("Enter text here=> ")
obj = TextBlob(text)

print("Detecting language\n", obj.detect_language())

print("Translate to")
print("1. bengali\t 2.chinese \t 3. german\t 4. gujrati\t 5. japanese:")
to = int(input("Enter your choice=> "))
if 5 < to < 1:
    print("Wrong choice")
    exit()
elif to == 1:
    to = 'bn'
elif to == 2:
    to = 'zh'
elif to == 3:
    to = 'de'
elif to == 4:
    to = 'gu'
else:
    to = 'jv'

print(obj.translate(to=to))
