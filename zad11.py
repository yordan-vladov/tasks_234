text = input()
text = text[:-4]
text = text.upper()
print(text,text.isalpha(),sep=", ")
print(f"{text}, {text.isalpha()}")
