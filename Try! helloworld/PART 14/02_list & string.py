str = '오늘은 날씨가 흐림'

words = str.split(" ")
position = words.index("흐림")
words[position] = "맑음"
new_str = " ".join(words)

print(new_str)