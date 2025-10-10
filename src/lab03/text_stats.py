import sys
import text 

stdin = sys.stdin.read()
#все слова списком
allwords= text.tokenize(stdin)
#уник слова списком
uniquewords=text.count_freq(allwords)
#слово и частота списком
top= text.top_n(uniquewords,5)
print(f'Всего слов: {len(allwords)}')
print(f'Уникальных слов: {len(uniquewords)}')
print("Топ-5:")
for i in top:
    print(i[0]+':'+str(i[1])) 
