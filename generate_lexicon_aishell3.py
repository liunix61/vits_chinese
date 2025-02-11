#!/usr/bin/env python3
from test_aishell3 import load_pinyin_dict, Pinyin, MyConverter, chinese_to_phonemes
from text.symbols import symbols


def generate_tokens():
    tokens = "aishell3/tokens.txt"
    with open(tokens, "w", encoding="utf-8") as f:
        for i, s in enumerate(symbols):
            f.write(f"{s} {i}\n")
    print(f"Generated {tokens}")


def generate_lexicon():
    with open("./aishell3/3500.txt", encoding="utf-8") as f:
        words = f.read().strip()
    words = list(set(list(words)))
    words.sort()

    load_pinyin_dict()
    pinyin_parser = Pinyin(MyConverter())

    lexicon = "./aishell3/lexicon.txt"
    with open(lexicon, "w", encoding="utf-8") as f:
        for w in words:
            phonemes = chinese_to_phonemes(pinyin_parser, w)
            phonemes = phonemes.split()
            # Remove the first sil, the last two sil and eos
            phonemes = phonemes[1:-2]
            phonemes = " ".join(phonemes)
            f.write(f"{w} {phonemes}\n")
    print(f"Generated {lexicon}")


def main():
    generate_tokens()
    generate_lexicon()


if __name__ == "__main__":
    main()
