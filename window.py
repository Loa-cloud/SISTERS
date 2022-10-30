from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
import spacy
import pandas as pd
nlp = spacy.load('ru_core_news_sm')
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq
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

# принимает словарь по области и словарь по тексту
# возвращает коэфицент соответствия
def baes (dict_obl, dict_txt):
    count = 0
    for word in dict_txt:
        if word in dict_obl:
            count+=1
    return count/len(dict_txt)



def command1():
    industry_tf.delete("1.0", "end")
    result=description_tf.get("1.0","end")
    content = lem(result)
    d = {'КУЛЬТУРА И ИСКУССТВО': baes(art, content),
         'ЖКХ': baes(hhk, content),
         'БЕЗОПАСНОСТЬ': baes(safety, content),
         'ПРОМЫШЛЕННОСТЬ': baes(main, content),
         'ЗДРАВОохРАНЕНИЕ': baes(helth, content),
         'ИССЛЕДОВАНИЯ И ИНЖЕНЕРНО-ТЕХНИЧЕСКОЕ ПРОЕКТИРОВАНИЕ': baes(engineer, content),
         'КОНТЕНТ И СМИ': baes(news, content),
         'ОБРАЗОВАНИЕ': baes(study, content),
         'ПРОФЕССИОНАЛЬНАЯ ДЕЯТЕЛЬНОСТЬ ПРОЧАЯ': baes(other, content),
         'СЕЛЬСКОЕ ХОЗЯЙСТВО (ВКЛЮЧАЯ РЫБОЛОВСТВО)': baes(agricultural, content),
         'СПОРТ, ТУРИЗМ И СФЕРА ОБСЛУЖИВАНИЯ': baes(sport, content)}
    d = dict(sorted(d.items(), key=lambda x: x[1]) )

    for x in d:
    #    industry_tf.insert("{0}.0".format(x), '\n')
        industry_tf.insert("1.0", x)
        industry_tf.insert("1.0", '\n')

def load_dictionary(doc):   
    # загрузка словаря из файла
    with open(doc, 'rb') as file:
        myvar = pickle.load(file) 
    return myvar

    
    


art = load_dictionary('art.pkl')
hhk = load_dictionary('hhk.pkl')
safety = load_dictionary('safety.pkl')
main = load_dictionary('main.pkl')
helth = load_dictionary('helth.pkl')
engineer = load_dictionary('engineer.pkl')
news = load_dictionary('news.pkl')
study = load_dictionary('study.pkl')
other = load_dictionary('other.pkl')
agricultural = load_dictionary('agricultural.pkl')
sport = load_dictionary('sport.pkl')


window = Tk()
window.title('Хакатон')
window.geometry('900x600')



frame = Frame(
   window,
   padx=10,
   pady=10
)
frame.pack(expand=True)

description_lb = Label(
   frame,
   text="Описание:  "
)
description_lb.grid(row=3, column=1)

industry_lb = Label(
   frame,
   text="Отрасль:  ",
)
industry_lb.grid(row=3, column=2)

description_tf =Text(
   frame, width=50, height=30,
)
description_tf.grid(row=4, column=1, pady=5, padx=5)

industry_tf = scrolledtext.ScrolledText(
   frame, width=50, height=30
)
industry_tf.grid(row=4, column=2, pady=5, padx=5)

cal_btn = Button(
   frame,
   text='Обработать',
   command = command1
)
cal_btn.grid(row=5, column=1)

def command2():
    description_tf.delete(1.0, END)


cal_btn2 = Button(
frame,
text='Очистить',
command = command2
)
cal_btn2.grid(row=5, column=2)


window.mainloop()


