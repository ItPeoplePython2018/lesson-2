import datetime
import re


def test_leap_year():
    """
    Задание: необходимо реализовать функцию is_leap_year, принимающую на вход объект типа datetime.date
    и возвращающую True, если год этой даты високосным, False - в противном случае.
    Документация по типу datetime.date находится здесь:
    https://docs.python.org/3/library/datetime.html#datetime.date
    Алгоритм определения високосного года можно посмотреть в википедии:
    https://ru.wikipedia.org/wiki/Високосный_год#Григорианский_календарь
    """

    def is_leap_year(date):
        print(date)
        if date.year % 4 != 0 or (date.year % 100 == 0 and date.year % 400 != 0):
            return False
        else:
            return True

    assert is_leap_year(datetime.date(year=2000, month=5, day=13))
    assert is_leap_year(datetime.date(year=2016, month=11, day=1))
    assert is_leap_year(datetime.date(year=1600, month=8, day=9))
    assert not is_leap_year(datetime.date(year=1900, month=1, day=1))
    assert not is_leap_year(datetime.date(year=2003, month=3, day=7))
    assert not is_leap_year(datetime.date(year=2001, month=10, day=15))


def test_file_data():
    """
    Задание: необходимо реализовать функцию, которая принимает filename - имя текстового файла и переменную word,
    содержащую искомое слово. Функция должна возвращать количество вхожений искомого слова в исходный текст, без
    учета регистра. Текст не содержит знаков препинания, а слова разделены пробелами.
    Для чтения данных из файла можно воспользоваться функцией open()
    Документация по работе с файлами находится здесь:
    https://docs.python.org/3/tutorial/inputoutput.html
    """

    def count_word_in_file(filename, word):
        with open(filename) as f:
            count = f.read() \
                .lower() \
                .split() \
                .count(word.lower())
        return count

    assert count_word_in_file("homework/pony.txt", "радуга") == 0
    assert count_word_in_file("homework/pony.txt", "и") == 3
    assert count_word_in_file("homework/pony.txt", "пони") == 5

    
def test_text_stat_hard():
    """
    Задание: необходимо реализовать функцию, которая принимает filename - имя текстового файла 
    и возвращает кортедж: (количество строк, количество слов, количество символов) в тексте.
    Текст может содержать любые символы латинского алфавита, цифры, пробелы и знаки пунктуации.
    Словом считается число-буквенная последовательность (например elephant, el3phant или 449).
    """

    def text_stat(filename):
        with open(filename) as f:
            text = f.read()
            rows = sum(1 for line in text.split('\n'))
            words = len(re.findall(r'\w+', text))
            symbols = sum(1 for line in text)
            stat = (rows, words, symbols)
            return stat

    # в первых двух файлах по 7 строк, а в конце третьего файла есть пустая строка, которую мы тоже должны посчитать.
    assert text_stat("homework/textstat1.txt") == (7, 69, 445)
    assert text_stat("homework/textstat2.txt") == (7, 73, 459)
    assert text_stat("homework/textstat3.txt") == (11, 73, 467)

