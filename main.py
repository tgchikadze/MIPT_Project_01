'''
Приложение для работы с файлами.
Функционал:
1. Рекурсивный обход директории, копирование с переименованием
всех найденных файлов с расширением TSV в заданный каталог
2. Рекурсивный обход директории, копирование
всех найденных файлов с указанной датой последнего изменения в заданный каталог
3. Diff - сравнение содержимого двух текстовых файлов
...
Данный файл проекта содержит функционал, необходимый для запуска консольного приложения
'''
def command_parser(*args, **kwargs):
    '''
    Функция берет на вход командную строку и парсит ее содержимое.
    Затем запускает соответствующую функцию из custom_parser.py
    :param args:
    :param kwargs:
    :return:
    '''
    try:
        import custom_parser
    except:
        print("Библиотека не найдена")
    pass
command_parser()
print('Done')