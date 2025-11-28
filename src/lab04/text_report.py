from src.lab03.text import normalize, tokenize, count_freq, top_n
from collections import Counter
from src.lab04.io_txt_csv import write_csv, read_text


def frequencies_from_text(text: str) -> dict[str, int]:
    from src.lab03.text import normalize, tokenize

    tokens = tokenize(normalize(text))
    return Counter(tokens)  # dict-like


def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))


# превратили в строки из нормализованых слов и частот
# text=sorted_word_counts(frequencies_from_text(read_text("data/inputnotexcist.txt")))
# write_csv(text, "data/report.csv", header=("word", "count"))

text = sorted_word_counts(frequencies_from_text(read_text("data/input.txt")))
write_csv(text, "data/report.csv", header=("word", "count"))

inputt = read_text("data/input.txt")
tokens = tokenize(normalize(inputt))
dictt = Counter(tokens)
sorted_freq = sorted_word_counts(dictt)

print(f"Всего слов: {len(tokens)}")
print(f"Уникальных слов: {len(dictt)}")
print(f"Топ-5:")
for word, count in sorted_freq[:5]:
    print(f"{word}:{count}")
