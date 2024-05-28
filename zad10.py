text = input()

text = text.replace("i","e")
text = text.split()

print(text)

e_counter = 0
for word in text:
    if "e" in word:
        e_counter += 1

print(e_counter)