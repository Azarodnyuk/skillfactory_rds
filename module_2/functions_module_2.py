#!/usr/bin/env python
# coding: utf-8

# In[1]:

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from itertools import combinations
from scipy.stats import ttest_ind



def description():
    
    description = [["school","аббревиатура школы, в которой учится ученик"],

    ["sex","пол ученика ('F' - женский, 'M' - мужской)"],

    ["age","возраст ученика (от 15 до 22)"],

    ["address","тип адреса ученика ('U' - городской, 'R' - за городом)"],

    ["famsize","размер семьи('LE3' <= 3, 'GT3' >3)"],

    ["Pstatus","статус совместного жилья родителей ('T' - живут вместе 'A' - раздельно)"],

    ["Medu","образование матери (0 - нет, 1 - 4 класса, 2 - 5-9 классы, 3 - среднее специальное или 11 классов, 4 - высшее)"],

    ["Fedu","образование отца (0 - нет, 1 - 4 класса, 2 - 5-9 классы, 3 - среднее специальное или 11 классов, 4 - высшее)"],

    ["Mjob","работа матери ('teacher' - учитель, 'health' - сфера здравоохранения, 'services' - гос служба, 'at_home' - не работает, 'other' - другое)"],

    ["Fjob","работа отца ('teacher' - учитель, 'health' - сфера здравоохранения, 'services' - гос служба, 'at_home' - не работает, 'other' - другое)"],
    ["reason","причина выбора школы ('home' - близость к дому, 'reputation' - репутация школы, 'course' - образовательная программа, 'other' - другое)"],

    ["guardian","опекун ('mother' - мать, 'father' - отец, 'other' - другое)"],

    ["traveltime","время в пути до школы (1 - <15 мин., 2 - 15-30 мин., 3 - 30-60 мин., 4 - >60 мин.)"],

    ["studytime","время на учёбу помимо школы в неделю (1 - <2 часов, 2 - 2-5 часов, 3 - 5-10 часов, 4 - >10 часов)"],

    ["failures","количество внеучебных неудач (n, если 1<=n<=3, иначе 0)"],

    ["schoolsup","дополнительная образовательная поддержка (yes или no)"],

    ["famsup","семейная образовательная поддержка (yes или no)"],

    ["paid","дополнительные платные занятия по математике (yes или no)"],

    ["activities","дополнительные внеучебные занятия (yes или no)"],

    ["nursery","посещал детский сад (yes или no)"],

    ["higher","хочет получить высшее образование (yes или no)"],

    ["internet","наличие интернета дома (yes или no)"],

    ["romantic","в романтических отношениях (yes или no)"],

    ["famrel","семейные отношения (от 1 - очень плохо до 5 - очень хорошо)"],

    ["freetime","свободное время после школы (от 1 - очень мало до 5 - очень мого)"],

    ["goout","проведение времени с друзьями (от 1 - очень мало до 5 - очень много)"],

    ["health","текущее состояние здоровья (от 1 - очень плохо до 5 - очень хорошо)"],

    ["absences","количество пропущенных занятий"],

    ["score","баллы по госэкзамену по математике"]
                  ]
    
    index = [description[i][0] for i in range(len(description))]
    data = [description[i][1] for i in range(len(description))]
    
    return pd.DataFrame(data=data, index=index, columns = ['description'])




def scatter_statistics(math):
    
    quantative_columns = math.select_dtypes(exclude='object').columns
    
    fig, axes = plt.subplots(3,4, figsize=(19,13))

    for j in range(4):
        for i in range(3):

            col = quantative_columns[4*i+j]

            group_max = math.groupby(col,sort=True,axis=0).max().score
            group_min = math.groupby(col,sort=True,axis=0).min().score
            group_median = math.groupby(col,sort=True,axis=0).median().score



            axes[i][j].scatter(data=math, x=col, y=quantative_columns[12],marker='.')

            axes[i][j].plot(list(group_max.index), 
                         group_max, '-o',label='max')

            axes[i][j].plot(list(group_min.index), 
                         group_min, '-o', label='min')

            axes[i][j].plot(list(group_median.index), 
                         group_median, '-o', label='median')

            axes[i][j].grid(True)
            axes[i][j].set_xlabel(col)
            axes[i][j].set_ylabel('score')
            axes[i][j].legend()

            
            
            
def investigate_num_col(math, col, math_description):
    
    fig, axes = plt.subplots(1,2, figsize=(15,3))
    
    if col != 'studytime, granular':
        print('\n*********************************************************************')
        print(col,'-',math_description.loc[col,'description'])
        print('\n*********************************************************************')
        
    else:        
        print('\n*********************************************************************')
        print(col,'-  no description')
        print('\n*********************************************************************')
        
    print('\nПосчитаем количество каждого из значений в столбце', col)
    data = pd.DataFrame(data=math[col].value_counts(ascending=False))
    data.columns = ['counts']
    display(data.T)

    print('\nРассмотрим статистики в столбце', col)
    display(pd.DataFrame(data=math.describe()[col]).T)

    sns.distplot(math[col], rug=True, bins=len(math[col].value_counts()), ax=axes[0])
    axes[0].set_title('\nГистограмма распределения \n значений столбца {}\n'.format(col))
    axes[0].grid(True)

    sns.boxplot(y=col,  data=math, ax=axes[1], color='orange', orient='h', saturation=1.0)
    axes[1].set_title('\n Boxplot for ' + col +'\n')
    axes[1].grid(True)
        
        
        
        
def get_boxplot(data, column):
    fig, ax = plt.subplots(figsize = (8, 3))
    sns.boxplot(x=column, 
                y='score', 
                data=data,
                ax=ax)
#     plt.xticks(rotation=45)
    ax.set_title('Boxplot for ' + column)
    plt.show()
    
    
    
    
def get_stat_dif(data, column):
    cols = data.loc[:, column].value_counts().index
    combinations_all = list(combinations(cols, 2))
    for comb in combinations_all:
        if ttest_ind(data.loc[data.loc[:, column] == comb[0], 'score'], 
                        data.loc[data.loc[:, column] == comb[1], 'score']).pvalue \
            <= 0.05/len(combinations_all): # Учли поправку Бонферони
            print('Найдены статистически значимые различия для колонки:', column)
            break
            
            
            
            
def null_count(data):
    null_count = pd.DataFrame(index=data.columns, columns=['null_count'])
    for i in list(null_count.index):
        null_count.loc[i,'null_count'] = data[i].isna().sum()
    null_count['null_count_percent'] = null_count['null_count']*100 / len(data)
    return null_count




def pairplot(data, start_x, stop_x, start_y,stop_y):
    
    """This function let us to make pairplot for choosen range of quantative columns"""
    
    quantative_columns = data.select_dtypes(exclude='object').columns
    sns.pairplot(data, 
                 x_vars=quantative_columns[start_x:stop_x],
                 y_vars=quantative_columns[start_y:stop_y], 
                 kind = 'reg', height=2, markers='.');


    
    
    
def statistics(data1,data2, col):
    alpha = ttest_ind(data1[col], data2[col], equal_var=False, nan_policy='omit').pvalue 
    if alpha < 0.05:
        print("\n Выборочные средние по столбцу",col, "не равны")
#     else:
#         print("\n Выборочные средние по столбцу",col, "возможно равны")

