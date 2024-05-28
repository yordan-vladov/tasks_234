text = input()

text = text.replace("e","i")
text = text.split()

print(text)

i_counter = 0
for word in text:
    if "i" in word:
        i_counter += 1

print(i_counter)