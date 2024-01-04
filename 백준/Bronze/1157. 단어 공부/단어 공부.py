word = input().upper()
unique_word = list(set(word))
cnt_word = []

for i in unique_word:
    cnt = word.count(i)
    cnt_word.append(cnt)

if cnt_word.count(max(cnt_word)) >= 2:
    print('?')
else:
    print(unique_word[cnt_word.index(max(cnt_word))])