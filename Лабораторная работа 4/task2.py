def get_count_char(str_):
    dict={}
    str1="".join(str_.split())
    str1=str_.lower()
    for i in str1:
        if i.isalpha():
            if i not in dict:
                dict[i] = 1
            else:
                dict[i]=dict[i]+1
    return (dict)
main_str ="""
   # Данное предложение будет разбиваться на отдельные слова.
    #В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов.
    #Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
