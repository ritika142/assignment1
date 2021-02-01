from textblob import TextBlob

data = input("Enter the data => ")
obj = TextBlob(data)
lst = obj.noun_phrases
print("There are ", len(lst), " noun phrases in the inputed text-:", end="\n\n")
for np in lst:
    print(np, end="\t\t")

