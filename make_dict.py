import spacy
import pandas as pd
nlp = spacy.load('ru_core_news_sm')
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq
from openpyxl import load_workbook
import pickle

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

def load_dictionary(doc):   
    # загрузка словаря из файла
    with open(doc, 'rb') as file:
        myvar = pickle.load(file) 
    return myvar



art = open_lem_cut_file('opk_art.txt')
with open('art.pkl', 'wb') as file:
    pickle.dump(art, file) 
    
hhk = open_lem_cut_file('opk_hhk.txt')
with open('hhk.pkl', 'wb') as file:
    pickle.dump(hhk, file)
    
safety = open_lem_cut_file('opk_safety.txt')
with open('safety.pkl', 'wb') as file:
    pickle.dump(safety, file)
    
main = open_lem_cut_file('opk_main.txt')
with open('main.pkl', 'wb') as file:
    pickle.dump(main, file)
    
helth = open_lem_cut_file('opk_helth.txt')
with open('helth.pkl', 'wb') as file:
    pickle.dump(helth, file)
    
engineer = open_lem_cut_file('opk_engineer.txt')
with open('engineer.pkl', 'wb') as file:
    pickle.dump(engineer, file)
    
news = open_lem_cut_file('opk_news.txt')
with open('news.pkl', 'wb') as file:
    pickle.dump(news, file)
    
study = open_lem_cut_file('opk_study.txt')
with open('study.pkl', 'wb') as file:
    pickle.dump(study, file)
    
other = open_lem_cut_file('opk_other.txt')
with open('other.pkl', 'wb') as file:
    pickle.dump(other, file)
    
agricultural = open_lem_cut_file('opk_agricultural.txt')
with open('agricultural.pkl', 'wb') as file:
    pickle.dump(agricultural, file)
    
sport = open_lem_cut_file('opk_sport.txt')
with open('sport.pkl', 'wb') as file:
    pickle.dump(sport, file) 


















