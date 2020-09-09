text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
        ["Ephemeral", "lasts", "one", "day", "only"],
        ["Accolade", "is", "an", "expression", "of", "praise"]]

n = int(input())
x = len(text)
new_text = [word for i in range(x) for word in text[i] if len(word) <= n]
print(new_text)
