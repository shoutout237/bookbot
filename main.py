book_path = "books/frankenstein.txt"

def get_text_book(book_path):
  with open(book_path) as f:
    file_content = f.read()
    return file_content

def count_words(text):
  text_words = text.split()
  print(f'{len(text_words)} words found in the document')

def count_letters(text):
  text_words = text.split()
  text_chars = []
  for word in text_words:
    for letter in word:
      if letter.isalpha():
        text_chars.append(letter.lower())
  count_char = dict((char,text_chars.count(char)) for char in set(text_chars))
  for x, y in count_char.items():
    print(f"the '{x}' character was found {y} times")

def main():
  print("--- Begin report of books/frankenstein.txt ---")
  count_words(get_text_book(book_path))
  count_letters(get_text_book(book_path))

main()
