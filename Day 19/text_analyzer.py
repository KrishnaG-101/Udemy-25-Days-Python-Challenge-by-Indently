# This file contains the code for text analyzer project.

from collections import Counter
import re

def analyze(path : str) -> None:
    with open(path, "r", encoding="utf-8") as file:
        text : str = file.read()
    
    # list of words
    words : list[str] = re.findall(r"\b\w+\b", text.lower())
    
    # count of white spaces
    white_space_count : int = sum(char.isspace() for char in text)
    # count of characters
    character_count_with_space : int = len(text)
    # count of words
    word_count : int = len(words)
    
    # count of each punctuation [",", ".", ";", ":", "'", "-", "!"]
    
    # 3 most common words
    three_most_common_words : list[tuple[str, int]] = Counter(words).most_common(3)
    
    # display
    print(f"Number of characters in the text: {character_count_with_space}")
    print(f"Number of white spaces in the text: {white_space_count}")
    print(f"Number of words in the text: {word_count}")
    print(f"Three most common words in our text: {three_most_common_words}")

def main() -> None:
    analyze("Day 19/sample.txt")

if __name__ == "__main__":
    main()