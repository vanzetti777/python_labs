import sys
import text as text
stdin = sys.stdin.readline()
#все слова
allwords= text.tokenize(stdin)
uniquewords=text.count_freq(stdin)
ton=top_n
print(f'Всего слов: {len(allwords)}')
print(f'Уникальных слов: {len(uniquewords)}')
print("Топ-5:")
