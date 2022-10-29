import spacy
import pandas as pd
nlp = spacy.load('ru_core_news_sm')
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq


# принимает в качестве аргумента файл, который нужно открыть
# функция открывает документ  возвращает его
def open_lem_cut_file(file):
    file2 = ""
    with open(file, 'r', encoding= "utf8")  as t:
        nums = t.read()
    file2 += nums
    lem_file = lem(file2)
    return (cut_dict(lem_file))


# принимает в качестве аргумента троку
# возвращает отсортированный словарь с лемматизацией
def lem(doc):
    doc = nlp(doc.lower())
    list1 =[token.lemma_ for token in doc]
    dic = {}
    for word in list1:
        if word.isalpha():
            if dic.get(word):
                dic[word] = dic[word] + 1
            else:
                dic[word] = 1
    dic = dict(sorted(dic.items(), key=lambda x: x[1]) )
    return(dic)

# принимает словарь
# возвращает урезанный словарь без 10% самых редко употребляемых слов
# и без 10% самых часто употребляемых слов
def cut_dict(dict_name):
    l = int(len(dict_name) * 0.1)
    len_hhk = len(dict_name)
    new_dict_name = {}
    i = 0
    for x in dict_name:
        i+=1
        if (i > l) and (i < (len_hhk-l)):
            new_dict_name[x] = dict_name[x]
    return new_dict_name

# принимает словарь по области и словарь по тексту
# возвращает коэфицент соответствия
def baes (dict_obl, dict_txt):
    count = 0
    for word in dict_txt:
        if word in dict_obl:
            count+=1
    return count/len(dict_txt)




##################################
# загрузка текста о компании с сайта
d = pq(url='https://www.localguides.ru')
soup = BeautifulSoup(str(d))
text = soup.get_text()
content = lem(text)
print (text)

##################################
# получение частотных словарей по областям искусство и жкх
art = open_lem_cut_file('opk_art.txt')
hhk = open_lem_cut_file('opk_hhk.txt')


##################################
# получение коэфицента совпадений
print ('искусство')
print (baes(art, content))
print ('жкх')
print (baes(hhk, content))

    
        










