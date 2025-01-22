from collections import Counter

# with open("books/test.txt") as f:
with open("books/frankenstein.txt") as f:
    file_contents = f.read()

print("--- Begin report of books/frankenstein.txt ---")
def word_counter(text):
    return(len(text.split()))

print(f"{word_counter(file_contents)} words found in the document\n")

def count_character(text):
    text = text.lower()
    # count = {i: text.count(i) for i in text if i.isalpha()}
    count = Counter(char for char in text if char.isalpha())
    return count
sorted_counts = sorted(count_character(file_contents).items(), key=lambda x: x[1], reverse=True)

for k, v in sorted_counts:
    print(f"The '{k}' character was found {v} times")

print("--- End report ---")

def main():
    word_counter(file_contents)
    count_character(file_contents)

if __name__ == "__main__":
    main()