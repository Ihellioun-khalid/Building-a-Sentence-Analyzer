sentence = input('Please enter a sentence : ')
words = sentence.split(' ')
char_count = {}
for word in words:
    characteres = list(word)
    for char in characteres:
        if char in char_count:
            char_count[char] = char_count[char] + 1
        else:
            char_count[char] = 1
sorted_keys = sorted(char_count.keys())
for k in sorted_keys:
    v = char_count[k]
    print("Found :", k, v, "times")
