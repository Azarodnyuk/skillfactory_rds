import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

description = {'client_id':['идентификатор клиента'],
               'app_date':['дата обращения'],
            'education':['уровень образования'],
            'sex':['пол заёмщика'],
            'age':['возраст заёмщика'],
            'car':['флаг наличия автомобиля'],
            'car_type':['флаг автомобиля-иномарки'],
            'decline_app_cnt':['количество отказанных прошлых заявок'],
            'good_work':['флаг наличия «хорошей» работы'],
             'skore_bki':['кредитный рейтинг'],
            'bki_request_cnt':['количество запросов в БКИ'],
               'region_rating':['рейтинг региона'],
            'home_address':['категоризатор домашнего адреса'],
            'work_address':['категоризатор рабочего адреса'],
            'income':['доход заёмщика'],
               'sna':['--------------'],
               'first_time':['--------------'],
            'foreign_passport':['наличие загранпаспорта'],
            'default':['наличие дефолта']}

def DESCR():
    DESC = pd.DataFrame(data=description).T
    DESC.columns = ['описание данных']
    return DESC


def make_hist_and_box(data, column):

    fig, ax = plt.subplots(2,2,figsize=(18,8))
    
    sns.histplot(data[column],bins=50, ax=ax[0,0], kde=True)
    sns.histplot(np.log(data[column]+1),bins=50, ax=ax[0,1], kde=True)
    sns.boxplot(data[column], orient='h', width=0.2,ax=ax[1,0])
    sns.boxplot(np.log(data[column]+1),orient='h',width=0.2, ax=ax[1,1])

    plt.show()
    
def compare_dist(data, column):

    fig = plt.figure(figsize=(6,4))
    
    sns.histplot(data[data['flag']==1][column],bins=data[column].nunique(), kde=False)
    sns.histplot(data[data['flag']==0][column],bins=data[column].nunique(), kde=False, color='orange')

    plt.show()