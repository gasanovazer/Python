def load_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        words = [line.strip() for line in file]
    return words

def find_words_by_length(words, length):
    return [word for word in words if len(word) == length]

def find_words_by_pattern(words, pattern):
    return [word for word in words if all(c1 == c2 or c2 == '*' for c1, c2 in zip(word, pattern))]

def filter_words_by_characters(words, characters_to_exclude):
    return [word for word in words if not any(char in word for char in characters_to_exclude)]

def filter_words_containing_characters(words, characters_to_include):
    return [word for word in words if any(char in word for char in characters_to_include)]

def main():
    file_path = input("Введите имя файла: ")
    words = load_words(file_path)

    length = int(input("Введите длину слова для поиска: "))
    filtered_by_length = find_words_by_length(words, length)
    print(f"Найдено {len(filtered_by_length)} слов(а) длины {length}.")

    print("Найденные слова:")
    for word in filtered_by_length:
        print(word)

    pattern = input("Введите шаблон для поиска (используйте '*' для обозначения любой буквы): ")
    filtered_by_pattern = find_words_by_pattern(filtered_by_length, pattern)
    
    print(f"Найдено {len(filtered_by_pattern)} слов(а) по заданному шаблону.")
    print("Найденные слова:")
    for word in filtered_by_pattern:
        print(word)

    characters_to_exclude = input("Введите буквы, которые следует исключить из результатов: ")
    filtered_by_characters = filter_words_by_characters(filtered_by_pattern, characters_to_exclude)
    
    print(f"Найдено {len(filtered_by_characters)} слов(а) после применения фильтрации по буквам.")
    print("Найденные слова:")
    for word in filtered_by_characters:
        print(word)

    characters_to_include = input("Введите буквы, которые должны содержаться в словах: ")
    filtered_by_included_characters = filter_words_containing_characters(filtered_by_characters, characters_to_include)
    
    print(f"Найдено {len(filtered_by_included_characters)} слов(а) после применения фильтрации по включенным буквам.")
    print("Найденные слова:")
    for word in filtered_by_included_characters:
        print(word)

if __name__ == "__main__":
    main()
