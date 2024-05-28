text = input()
text = text.split()
text = "_".join(text)

print(f"{text}, {text.lower() == text}") 