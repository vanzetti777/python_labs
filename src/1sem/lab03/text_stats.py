import sys
from src.lab03.text import normalize, tokenize, count_freq, top_n

stdin = sys.stdin.read()
# все слова списком
allwords = tokenize(stdin)  # убрали text.
# уник слова списком
uniquewords = count_freq(allwords)  # убрали text.
# слово и частота списком
top = top_n(uniquewords, 5)  # убрали text.
print(f"Всего слов: {len(allwords)}")
print(f"Уникальных слов: {len(uniquewords)}")
print("Топ-5:")
for i in top:
    print(i[0] + ":" + str(i[1]))
