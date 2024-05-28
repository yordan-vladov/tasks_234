text = input().split()

text = text[::-1]
text = "-".join(text)

print(text)
print(text.count("a"))