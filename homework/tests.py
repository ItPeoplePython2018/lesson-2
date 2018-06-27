import datetime

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
        if date.year % 100 == 0:
            if date.year % 400 == 0:
                return True
            else:
                return False
        else:
            if date.year % 4 == 0:
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
        myFileLists = []
        myFileWords = []
        fileWord = ''
        count = 0
        with open("filename", encoding="utf-8") as myFile:
            
            "dividing the text into lines and replacing \n to ' '"
            for line in myFile:

                #line = line.lower().replace('\n', ' ')
                #line = line.replace('\n', ' ')

                myFileLists.append(line.lower().replace('\n', ' '))

                
            'dividing lines into words'
            for fileList in myFileLists:
                for fileListLetter in fileList:
                    if fileListLetter != ' ':
                        fileWord += fileListLetter
                    else:
                        myFileWords.append(fileWord)
                        fileWord = ''


            'finding the word'
            for words in myFileWords:
                if words == word:
                        count += 1

                        
        myFile.close()

        return count
 

    assert count_word_in_file("homework/pony.txt", "радуга") == 0
    assert count_word_in_file("homework/pony.txt", "и") == 3
    assert count_word_in_file("homework/pony.txt", "пони") == 5
    
