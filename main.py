text = "" #шифр текст
letter_count = {}

for char in text.lower():
    if char.isalpha():
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1


for letter, count in sorted(letter_count.items(), key=lambda x: x[1], reverse=True):
    print(f"'{letter}': {count}")

replace_map = {} #словарь перевода

trans_table = str.maketrans(replace_map)
decoded_text = text.translate(trans_table)


print(text)
print(decoded_text)