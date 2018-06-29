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
        a = date.year
        if (((a % 400) == 0) or (((a % 4) == 0) and ((a % 100) != 0))):
            return True
        else:
            return False

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
        num = 0
        with open(filename) as u:
            for line in u:
                text_words = list(re.findall(r'\w+', line.casefold()))    #ищем слова
                num += text_words.count(word.casefold())
        return num

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
        pass

    assert text_stat("homework/textstat1.txt") == (6, 69, 445)
    assert text_stat("homework/textstat2.txt") == (6, 73, 459)
    assert text_stat("homework/textstat3.txt") == (10, 73, 467)
