import sys
from collections import Counter
from text import normalize, tokenize
def frequencies_from_text(text: str) -> dict[str, int]:
    from text import normalize, tokenize
    tokens = tokenize(normalize(text))
    return Counter(tokens)  # dict-like

def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))

import io_txt_csv
text=sorted_word_counts(frequencies_from_text(io_txt_csv.read_text("data/input.txt")))
print(text)