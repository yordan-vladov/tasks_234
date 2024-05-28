text = input()
n_count = text.lower().count('n')

all_capital = True
text = text.split()

for word in text:
    if word[0] != word[0].upper():
        all_capital = False
        break

print(f"n = {n_count}, {text}, {all_capital}")