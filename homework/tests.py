import re


def test_text_stat_hard():
    """
    Задание: необходимо реализовать функцию, которая принимает filename - имя текстового файла 
    и возвращает кортедж: (количество строк, количество слов, количество символов) в тексте.
    Текст может содержать любые символы латинского алфавита, цифры, пробелы и знаки пунктуации.
    Словом считается число-буквенная последовательность (например elephant, el3phant или 449).
    """

    def text_stat(filename):
        num_line, num_words, num_characters = 0, 0, 0
        
        with open(filename, "r") as f:
            for line in f:
                num_line += len(re.findall(r'\n', line))     # ищем строки по символам Enter
                num_words += len(re.findall(r'\w+', line))   # ищем слова
                num_characters += len(line)                  # считаем символы
        return (num_line, num_words, num_characters)

    assert text_stat("homework/textstat1.txt") == (6, 69, 445)
    assert text_stat("homework/textstat2.txt") == (6, 73, 459)
    assert text_stat("homework/textstat3.txt") == (10, 73, 467)
