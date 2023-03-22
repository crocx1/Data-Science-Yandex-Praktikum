#!/usr/bin/env python
# coding: utf-8

# <div style="border:solid green 2px; padding: 20px">
#     
# <b>Павел, привет!</b> Мы рады тебя видеть на территории код-ревьюеров. Ты проделал большую работу над проектом, но давай познакомимся и сделаем его еще лучше! У нас тут своя атмосфера и несколько правил:
# 
# 
# 1. Меня зовут Александр Матвеевский. Я работаю код-ревьюером, моя основная цель — не указать на совершенные тобою ошибки, а поделиться своим опытом и помочь тебе стать аналитиком данных.
# 2. Общаемся на ты.
# 3. Если хочешь написать, спросить - не нужно стесняться. Только выбери свой цвет для комментария.  
# 4. Это учебный проект, тут можно не бояться сделать ошибку.  
# 5. У тебя неограниченное количество попыток для сдачи проекта.  
# 6. Let's Go!
# 
# ---
# 
# Я буду красить комментарии цветом, пожалуйста, не удаляй их:
# 
# <div class="alert alert-block alert-danger">✍
#     
# 
# __Комментарий от ревьюера №1__
# 
# Такой комментарий нужно исправить обязательно, он критически влияет на удачное выполнение проекта.
# </div>
#     
# ---
# 
# <div class="alert alert-block alert-warning">📝
#     
# 
# __Комментарий от ревьюера №1__
# 
# 
# Такой комментарий является рекомендацией или советом. Можешь использовать их на своё усмотрение.
# </div>
# 
# ---
# 
# <div class="alert alert-block alert-success">✔️
#     
# 
# __Комментарий от ревьюера №1__
# 
# Такой комментарий  говорит о том, что было сделано что-то качественное и правильное =)
# </div>
#     
# ---
#     
# Предлагаю работать над проектом в диалоге: если ты что-то меняешь в проекте или отвечаешь на мои комментарии — пиши об этом. Мне будет легче отследить изменения, если ты выделишь свои комментарии:   
#     
# <div class="alert alert-info"> <b>Комментарии студента:</b> Например, вот так.</div>
#     
# Всё это поможет выполнить повторную проверку твоего проекта оперативнее. Если будут какие-нибудь вопросы по моим комментариям, пиши, будем разбираться вместе :)    
#     
# ---

# # Исследование объявлений о продаже квартир
# 
# В вашем распоряжении данные сервиса Яндекс.Недвижимость — архив объявлений о продаже квартир в Санкт-Петербурге и соседних населённых пунктов за несколько лет. Нужно научиться определять рыночную стоимость объектов недвижимости. Ваша задача — установить параметры. Это позволит построить автоматизированную систему: она отследит аномалии и мошенническую деятельность. 
# 
# По каждой квартире на продажу доступны два вида данных. Первые вписаны пользователем, вторые — получены автоматически на основе картографических данных. Например, расстояние до центра, аэропорта, ближайшего парка и водоёма. 

# <div class="alert alert-block alert-warning">📝
#     
# 
# __Комментарий от ревьюера №1__
# 
# 
# Отличная практика - расписывать цель и основные этапы своими словами (этот навык очень поможет на фильнальном проекте). Хорошо было бы добавить ход и цель исследования. Пример можно посмотреть в самом первом проекте (Музыка городов)
# </div>

# Данный проект направлен на изучение рынка недвижимости в Питере и его окрестностях. В нем предоставлены данные по различным особенностям зданий, их  локаций, и тех характеристик. 
# Цель работы - обработать масив данных по недвижимости и найти основные закономерности, аномалии, зависимости.

# ### Откройте файл с данными и изучите общую информацию. 

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display

data = pd.read_csv('/datasets/real_estate_data.csv', sep ='\t')
print(data.head())
print(data.info())
data.hist(figsize=(15, 20))

plt.show()


# <div class="alert alert-block alert-success">✔️
#     
# 
# __Комментарий от ревьюера №1__
# Такие предупеждения можно убрать 2 способами:
#     
# 1. В конец кода добавить `plt.show()`, но для этого нужно вызвать библиотеку matplotlib
# 2. В конец кода добавить `;`
#     
# ![image.png](attachment:image.png)
# </div>

# ### Предобработка данных

# <div class="alert alert-block alert-success">✔️
#     
# 
# __Комментарий от ревьюера №1__
# 
# Проверить колличество пропусков в % можно вот так: 
#     
#     
#     pd.DataFrame(round(df.isna().mean()*100,)).style.background_gradient('coolwarm')

# In[2]:


print('Не понял, как запустить, выдает только ошибки')


# In[ ]:





# In[3]:


print('Ищем явные дубликаты')
print()
print(data.duplicated().sum())
print('Дубликатов нет, но сделаем дроп')
print()
print('Удаляем явные дубликаты')
print()
data = data.drop_duplicates().reset_index(drop=True) 
print()
print('Проверяем')
print()
print(data.duplicated().sum())


# <div class="alert alert-block alert-success">✔️
#     
# 
# __Комментарий от ревьюера №2__
# 
# Проверка на дубликаты - основа предобработки данных
# </div>

# In[4]:


print('Ищем пропуски')
print()
print(data.isnull().sum())
print()


# In[5]:


print('Просматриваем столбцы с пропусками')
print()
print(data['is_apartment'].unique())
print(data.groupby('is_apartment')['is_apartment'].count())
print()
print(data['balcony'].unique())
print(data.groupby('balcony')['balcony'].count())
data['balcony'] = data['balcony'].fillna(0.)
print(data.groupby('balcony')['balcony'].count())
print()
print('ceiling_height', data['ceiling_height'].unique())
print('living_area',data['living_area'].unique())
print('is_apartment',data['is_apartment'].unique())
print('kitchen_area',data['kitchen_area'].unique())
print('locality_name',data['locality_name'].unique())
print('airports_nearest',data['airports_nearest'].unique())
print('cityCenters_nearest',data['cityCenters_nearest'].unique())
print('parks_around3000',data['parks_around3000'].unique())
print('parks_nearest',data['parks_nearest'].unique())
print('ponds_around3000',data['ponds_around3000'].unique())
print('ponds_nearest',data['ponds_nearest'].unique())
print('days_exposition',data['days_exposition'].unique())
print()
data['parks_around3000'] = data['parks_around3000'].fillna(0.)
print(data.groupby('parks_around3000')['parks_around3000'].count())
print()
data['ponds_around3000'] = data['ponds_around3000'].fillna(0.)
print(data.groupby('ponds_around3000')['ponds_around3000'].count())
print()
print(data.info())
print(data.head())
data['balcony']  = data['balcony'].astype('int64', errors='ignore')
data['ponds_around3000'] = data['ponds_around3000'].astype('int64', errors='ignore')
data['parks_around3000']  = data['parks_around3000'].astype('int64', errors='ignore')
data['last_price']  = data['last_price'].astype('int64', errors='ignore')
data['total_area']  = data['total_area'].astype('int64', errors='ignore')
print()
print(data.info())
print(data.head())
print()


# In[6]:


print('Поиск дубликатов')
print()
display(data['locality_name'].unique())
data['shrt_name'] = data['locality_name']
duplicates = ['деревня ', 'садовое товарищество ', 'село ', 'поселок городского типа ', 'посёлок городского типа ',  'городской посёлок ', 'городской поселок ', 'посёлок при железнодорожной станции ', 'посёлок станции ', 'садоводческое некоммерческое товарищество ', 'коттеджный поселок ', 'коттеджный посёлок ', 'посёлок ', 'поселок ']
for i in duplicates:
    data['shrt_name'] = data['shrt_name'].str.replace(i, '')
display(data['shrt_name'].unique())
print()


# <div class="alert alert-block alert-success">✔️
#     
# 
# __Комментарий от ревьюера №2__
# 
# Отличный код)
# </div>

# In[7]:


print('Работа с некоректными данными')
display(data['ceiling_height'].unique())
duplicates = [27., 24., 26., 14., 20.0,  22.6, 27.5, 100.]
name = [2.7, 2.4, 2.6, 1.4, 2.0,  2.26, 2.75, 10.0]
for i in range(len(duplicates)):
    data['ceiling_height'] = data['ceiling_height'].replace(duplicates[i], name[i])
display(data['ceiling_height'].unique())


# In[8]:


print(data['last_price'].dtype)


# In[9]:


print('Меняем высоту потолков относительно района')
print()
for locality_name in data['shrt_name'].unique():
    median = data.loc[data['shrt_name'] == locality_name, 'ceiling_height'].median()
    data.loc[(data['ceiling_height'].isna())&(data['shrt_name'] == locality_name), 'ceiling_height'] = median
    
data.loc[data['ceiling_height'].isna(), 'ceiling_height'] = data['ceiling_height'].median()


# <div class="alert alert-block alert-danger">✍
#     
# 
# __Комментарий от ревьюера №1__
# 
# Твой проект тяжело читать, т.к. в нем нет подзаголовков, весь код написан в одной ячейке / нет промежуточных выводов Пожалуйста, воспользуйся методичкой по оформлению проектов, что бы исправить эти недостатки. Ее можно найти в блоке курса: ****Полезные инструкции для учёбы - Оформление проекта - Рекомендации по выполнению проектов****
# 
# В виде комментариев к коду стоит писать пояснения, почему ты применил те или иные методы python, зачем сгруппировал данные, для чего нужны срезы и т.д.
# Все остальное - выводы, рекомендации, принятые решения, указание на обнаруженные аномалии, анализ графиков и т.д. нужно писать в ячейках makdown. Так твой проект будет проще читать.
# </div>

# <div class="alert alert-block alert-success">✔️
#     
# 
# __Комментарий от ревьюера №1__
# 
# Согласен, если пропуск - вероятнее всего балкон отсутствует

# <div class="alert alert-block alert-success">✔️
#     
# 
# __Комментарий от ревьюера №1__
# 
# Некоторые столбцы можно поменять на значения, относительно своего района (например высота пололков). Вот так
#     
#     
# ![image.png](attachment:image.png)
#     
# Если хочешь - дарю свой код =)
# </div>

# In[ ]:





# <div class="alert alert-block alert-success">✔️
#     
# 
# __Комментарий от ревьюера №1__
# 
# Если пропусков меньше 5-10% их лучше сразу удалить, дабы сэкономить время
# </div>

# <div class="alert alert-block alert-warning">📝
#     
# 
# __Комментарий от ревьюера №1__
# 
# Давай посмотрим на столбец `last_price`, он имеет дробный тип данных. Но ведь никто не продаёт недвижку с копейками. Что думаешь?
# </div>

# <div class="alert alert-block alert-warning">📝
#     
# 
# __Комментарий от ревьюера №1__
# 
# Лучше не хардкодить, а использовать функцию: если значение больше 15, то разделить на 10
# </div>

# Подскажи пожалуйста,
# Написал такой код, но он выдает ошибку, пробовал много разных вариантов, почему-то не могу создать тот, который будет работать согласно комментарию 
# 
# print()
# print(data['ceiling_height'].unique())
# print()
# for i in data['ceiling_height']:
#     if i > 15:
#         data['ceiling_height'][i]/10
# 
# print(data['ceiling_height'].unique())

# <div class="alert alert-block alert-danger">✍
#     
# 
# __Комментарий от ревьюера №1__
# 
# Отсутствует проверка на явные дубликаты, поправишь, пожалуйста?

# Ошибки
# ceiling_height - не стандартный потолок, у которого есть пеерады в высоте. 
# living_area - корпоративное здание, не предусмотрена жилая площадь
# floors_total - одноэтажное здание
# is_apartment - скорее всего не аппартаменты
# kitchen_area - корпоративное здание, не предусмотрена кухонная площадь
# locality_name - склад, завод, который находится за территорией города
# airports_nearest - скорее всего нет аэроорта
# cityCenters_nearest - скорее всего слишком далеко до центра города
# parks_nearest - не известно сколько до ближайшего парка в км
# ponds_nearest - не известно сколько до ближайшего пруда в км
# days_exposition - еще не было снято, нет завершающей даты 
# 
# Измененный тип данных
# balcony - не может быть дробным
# ponds_around3000 - в таблице только данные 1,2,3 - так что не может быть дробным 
# parks_around3000 - в таблице только данные 1,2,3 - так что не может быть дробным 
# last_price - нет дробных значений
# total_area  - нет дробных значений
# 
# Я бы еще изменил, но не дают пустые 
# floors_total - не может быть дробным
# airports_nearest - в таблице нет дробных значений
# cityCenters_nearest - в таблице нет дробных значений
# parks_nearest - в таблице нет дробных значений
# ponds_nearest - в таблице нет дробных значений
# days_exposition -  не может быть дробным

# <div class="alert alert-block alert-success">✔️
#     
# 
# __Комментарий от ревьюера №2__
#     
# Второй раздел сделан хорошо. Проверены основные возможные проблемы в данных.

# ### Проведите исследовательский анализ данных

# In[10]:


print('Новые столбцы')
data['m2_price'] = data['last_price']/data['total_area']
data['dow']= pd.to_datetime(data['first_day_exposition']).dt.dayofweek
data['month']= pd.to_datetime(data['first_day_exposition']).astype('datetime64[M]').astype(int) % 12 + 1
data['year']= pd.to_datetime(data['first_day_exposition']).dt.year
def floor_count(q):
    w = q['floors_total']
    y = q['floor']
    if y == 1:
        return 'первый'
    elif y == w:
        return 'последний'
    else:
        return 'другой'
data['floor_type'] = data[['floor', 'floors_total']].apply(floor_count, axis =1)
data['km']= data['cityCenters_nearest']/1000
data['km']= data['km'].round()
print(data.head())


# <div class="alert alert-block alert-warning">📝
#     
# 
# __Комментарий от ревьюера №1__
# 
# Совет: обычно в датафреймах содержатся данные за несколько лет. Важно выбрать корректный метод для вычленения месяца, иначе месяца разных годов могут стать одним месяцем. Обрати внимание на метод astype('datetime64[M]'). Для его использования не нужно обращаться к pd.DatetimeIndex. 
#     
# Вот хорошая статья на этот счёт: 
#     
#     https://pythobyte.com/how-to-work-with-dates-and-times-in-python-0a176355/
# </div>

# <div class="alert alert-block alert-success">✔️
#     
# 
# __Комментарий от ревьюера №2__
# 
# Этот метод нужен для визуализации динамики по неделям, месяцам или годам (смотря какой метод выберешь)
#     
# Код выглядит так:
#     
#         df['first_day_exposition'].dt.date #приводим к временному формату
#         df['first_day_exposition'].astype('datetime64[M]') 
#     
# Если года разные, то в новой колонке месяца у тебя отобразится первый день месяца ('2019-05-01')
# </div>

# <div class="alert alert-block alert-success">✔️
#     
# 
# __Комментарий от ревьюера №1__
# 
# Этот раздел выполнен качественно
# </div>

# ### Общий вывод

# In[11]:


print(data['total_area'].describe())
total_area = data[data['total_area'] < 120.]
total_area.hist('total_area', bins = 120)
print()



# Данный график показывает, что наибольшая площадь 900 м.кв., наименьшая 12. В среднем плозать 60 кв.м., что в целом похоже на правду
# 
# Уменьшил диапозон до 120 для лучшего распознования. на графике видно, что не бывает квартир с определенной площадью. Это может быть связано с особенностями торительства здания и правилами по объему здания, куда данные размеры не попадают. 
# 
# 

# <div class="alert alert-block alert-success">✔️
#     
# 
# __Комментарий от ревьюера №2__
# 
# Отличная визуализация
# </div>

# In[12]:


print(data['living_area'].describe())
living_area = data[data['living_area'] < 70.]
living_area.hist('living_area', bins = 70)
print()


# Для наглядности слегка урезал график по жилплощади. Если мы посмотрим график, то заметим несколько пиков, это может быть вызвано тем, что в жилых несколько комнта, которые обыно имеют разную +- стандартную площадь около 12 метров, собстевнно с этим и связаны скачки.
# 

# In[13]:


print(data['kitchen_area'].describe())
kitchen_area = data[data['kitchen_area'] < 25.]
kitchen_area.hist('kitchen_area', bins = 25)
print()


# Для наглядности слегка урезал график. 
# На графике видно, что пик по кухням приходится на 7-10 метров и падает к 25. По большому счету есть кухни с огромной площадью, но имея небольшую квартиру кухня тоже будет маленькая. А даже в большой квартире иметь кухню больше 25-30 метров не иммет особого смысла, большие кухни могут быть в ресторанах, столовых и др местах. Возможно этот процент из-за них.
# 
# 

# In[14]:


print(data['rooms'].describe())
rooms = data[data['rooms'] < 7.]
rooms.hist('rooms', bins = 7);


# Для наглядности слегка урезал график. 
# На графике видно, что в среднем в квартирах есть 2-4 комнаты
# 

# In[15]:


print(data['ceiling_height'].describe())
ceiling_height = data[data['ceiling_height'] < 5.]
ceiling_height.hist('ceiling_height', bins = 5);


# Для наглядности слегка урезал график. 
# 
# В данных показано, что существуют аномально высокие потокли в 32 метра, это может быть ошибкой, или техническим зданием в виде какой-то вышки. В среднем высотка потоков 2.5-3 метра, что является нормой
# 

# In[16]:


print(data['floor'].describe())
floor = data[data['floor'] < 25.]
floor.hist('floor', bins = 25);


# Есть квартиры до 33 этажей, однако подовляющее большиство это в среднем 4-6 этажи, что похоже направду поскольку это Питер. Застройка Питера и окрестностей это не выскоие здания.
# 
# Также на графике видно,, что нет нигде 13 этажей, это явно ошибка в данных
# 
# 

# In[17]:


print(data['floor_type'].describe())
floor_type =  data.groupby("floor_type")['first_day_exposition'].count()
print(floor_type)
floor_type.plot.pie();


# Не понимаю, почему не могу построить гистограмму, также хотел через unique().count() посчитать кол-во, но тоже не дает
# 

# <div class="alert alert-block alert-success">✔️
#     
# 
# __Комментарий от ревьюера №2__
# 
# Полученные данные соответствуют реалиям
# </div>

# In[18]:


print(data['floors_total'].describe())
floors_total = data[data['floors_total'] < 25.]
floors_total.hist('floors_total', bins = 25);


# В данных существуют многоэтажные здания до 60 этажей, однако подовляющее большиство это в среднем 4-6 этажки.
# 

# In[19]:


print(data['km'].describe())
km = data[data['km'] < 25.]
km.hist('km', bins = 25);


# 14 км примерно среднее расстояния до центра города, но есть и здания, растояние от которых до центра более 60км, возможно северные дачи и коттеджи
# 
# 

# In[20]:


print(data['airports_nearest'].describe())
data.hist('airports_nearest', bins = 19);


# 20-30 км примерно среднее расстояния до аэропорта, что в целом нормально соотносится с данными до центра города, если учесть что аэропорт обычно удален от него
# 
# 

# In[21]:


print(data['parks_nearest'].describe())
parks_nearest = data[data['parks_nearest'] < 1500]
parks_nearest.hist('parks_nearest', bins = 30);


# в среднем парк находится в полукиллометре от здания.
# 
# 

# In[22]:


print(data['dow'].describe())
data.hist('dow', bins = 7);


# Как мы видим пик активности это раюочие дни, что не удивительно, потому что большинство объявлений создаются риэлторами, которые работают по будням
# 

# In[39]:


#print(data['month'].describe())
data['month'].hist();


# Пик сдачи приходится на фев-апр и сен-ноябрь

# <div class="alert alert-block alert-danger">✍
#     
# 
# __Комментарий от ревьюера №1__
# 
# Тут аналогично. Поправишь оформление по проекту, чтобы дальше не акцентировать на этом внимание
# </div>

# <div class="alert alert-block alert-warning">📝
#     
# 
# __Комментарий от ревьюера №1__
# 
# Я бы советовал сократить range и тогда мы сможем увидеть пиковые значения. 
# </div>

# <div class="alert alert-block alert-danger">✍
#     
# 
# __Комментарий от ревьюера №1__
# 
# Отсутствует гистограмма по типу этажа. Добавишь, пожалуйста?
# </div>

# <div class="alert alert-block alert-success">✔️
#     
# 
# __Комментарий от ревьюера №2__
# 
# Спасибо за правки)
# </div>

# Не могу построить гитограмму, говорит, что это не число и не дает, подскажи как лучше сделать, пока только выделил его как сумму значений.
# 

# In[24]:


print('2 часть')
print(data['days_exposition'].describe())
days_exposition = data[data['days_exposition'] < 200]
days_exposition.hist('days_exposition', bins = 200);


# Медиана - 95 дней, среднее - 180 дней., наиболее длительная продажа - 1580 дней иил 4 года. Показатель медианы в 3 месяца довольно схож с реальностью, насколько я понимаю. Минимальная продажа составила 1 день, что довольно странно, однако вполне возможно, например, если договорились заранее и просто испольщовали сервис как юр инструмент
# 
# Из особенностей графика есть несколько пиков, которые сильно выбиваются из общего масива. Это может быть какая-то акция, за счет чего произошел такой скачек или ошибка в данных
# 
# Мне кажется быстрая продажа происходит за до 3х месяцев, долгая от 1.5 лет

# <div class="alert alert-block alert-danger">✍
#     
# 
# __Комментарий от ревьюера №1__
# 
# Давай тут уменьшим range до 100-200 (ведь именно в эти дни происходят основные продажи), возможно тут есть интересные аномалии. Так же в таких моментах лучше делать колличество корзин = колличеству дней (в соответствии с range)
#     
# ---
#     
# Как думаешь сколько дней занимает быстрая продажа, а сколько дней - можно считать, что это уже долгая продажа?
# </div>

# <div class="alert alert-block alert-success">✔️
#     
# 
# __Комментарий от ревьюера №2__
#     
# Эти аномалии очень похожи на техническую особенность самой платформы: вероятнее, в эти дни платформа автоматически убирает объявления, если пользователь его не продлил
# </div>

# <div class="alert alert-block alert-success">✔️
#     
# 
# __Комментарий от ревьюера №2__
# 
# Да, от 1.5 лет можно считать долгой продажей
# </div>

# In[25]:


data_summary = data[['total_area', 'living_area', 'kitchen_area', 'rooms', 'floor_type', 'dow', 'month', 'year', 'last_price']]
print(data_summary.head())
print(data_summary.info())
pd.plotting.scatter_matrix(data_summary, figsize=(9, 9));


# In[26]:


print(' График зависимости Пирсона - total_area от last_price')
print()
data.plot(x='total_area', y='last_price', kind='scatter', alpha=0.3);


# Как видно на графике при увеличении площади цена растет, но не очень сильно, также есть несколько дорогих объектов с сравнительно небольшой ценой, но нет дешевых объектов с большой ценой. Так в целом и есть на рынке недвижимости

# In[27]:


print(' График зависимости Пирсона - living_area от last_price')
print()
data.plot(x='living_area', y='last_price', kind='scatter', alpha=0.3);


# Зависимость цены от жилой площади меньше, чем от общей площади. Скорее всего потому что в более дорогих квартирах важна не столько жилая площадь, сколько доп опции нежилых помещений - градеробы, большая кухня, несколько сан узлов, парковки и тд.

# In[28]:


print(' График зависимости Пирсона - kitchen_area от last_price')
print()
data.plot(x='kitchen_area', y='last_price', kind='scatter', alpha=0.3);


# В данном графике довольно биполярная зависимость, можно увидеть, что есть много больших кухонь, с низкой ценой квартиры - думаю это можно отнести к комерческим зданиям - офисы, столовые, рестораны и тд. А также маленькие кухни с большой ценой - думаю это могут быть пентхаусы, дорогие квартиры в небоскребах и тд, где стоимость м кв во много раз выше. 

# In[29]:


print(' График зависимости Пирсона - rooms от last_price')
print()
data.plot(x='rooms', y='last_price', kind='scatter', alpha=0.3);


# На графике видно, что примерно до 5-6 комантыных квартир цена пропорционально увеличивается относительно комнат, после в целом паадет. Думаю это возможно из-за того, что больше 6 комнта практически не продавались жилые квартиры, а больше были коммерчиские, стоимость которых ниже в средем на рынке. 
# 
# Также существует выко на 8 комнтах за огромные деньги - думаю это имогли быть люкс пентхаусы
# 

# In[30]:


print(' График зависимости Пирсона - floor_type от last_price')
print()
data.plot(x='floor_type', y='last_price', kind='scatter', alpha=0.3);


# Как видно всреднем самые дешевые на 1м этаже, самые дорогие на последнем. В целом это объяснимо, потому что люди выбирают жить выше, с красивым видом и подальше от шума города, поэтому и цена выше.

# <div class="alert alert-block alert-success">✔️
#     
# 
# __Комментарий от ревьюера №2__
# 
# Верная интерпретация значений корреляции Пирсона. Ты молодец =)
# </div>

# In[31]:


print(' График зависимости Пирсона - dow от last_price')
print()
data.plot(x='dow', y='last_price', kind='scatter', alpha=0.3);


# Как видно из графика, то большинство сделок пропорционально распределны. Самые дорогие продажи были в субботу, что может быть из-за 2х причин, очень дорогую недвижимость людям удобнее выбирать и покупиать в выходной, или это был частный случай, который мог быть в люой другой день. 

# In[32]:


print(' График зависимости Пирсона - month от last_price')
print()
data.plot(x='month', y='last_price', kind='scatter', alpha=0.3);


# График месяца примерно такойже как и по дням, в среднем все +- идентично

# In[33]:


print(' График зависимости Пирсона - year от last_price')
print()
data.plot(x='year', y='last_price', kind='scatter', alpha=0.3);


# Видно, что пик дорогой недвижимости был в 2017 году, возможжно это было приурочено к отркытию Лахта Центра, где было много дорогой площади

# <div class="alert alert-block alert-danger">✍
#     
# 
# __Комментарий от ревьюера №1__
# 
# Давай каждый пункт шага рассмотрим отдельно и графики подкрепим корреляцией Пирсона. И так же сразу интерпретируем полученные результаты?
# </div>

# <div class="alert alert-block alert-success">✔️
#     
# 
# __Комментарий от ревьюера №2__
# 
# Графики верны
# </div>

# In[34]:


print('Средняя цена')
print()

data['amount'] =  1
#data_city = data.groupby(['shrt_name']).sum()
#data_city = data_city.sort_values(['amount'], ascending = False)
#print(data_city['amount'].head(10))
#cities = ['Санкт-Петербург', 'Мурино', 'Кудрово', 'Шушары', 'Всеволожск', 'Пушкин', 'Колпино', 'Парголово', 'Гатчина', 'Выборг']

avg_price = data.pivot_table(index= 'shrt_name', values = 'amount', aggfunc='sum').sort_values('amount', ascending = False).head(10)

print(avg_price)


# <div class="alert alert-block alert-warning">📝
#     
# 
# __Комментарий от ревьюера №2__
# 
# Таблица верна. Совет: на общие продажи лучше смотреть через призму медианы. Она более устойчива к выбросам
# </div>

# In[35]:


print('Питер')
print()
data_piter = data[data['shrt_name'] == 'Санкт-Петербург']
avg_km = data_piter.pivot_table(index= 'km', values = 'last_price', aggfunc='mean').sort_values('km', ascending = True).head(25).round()
print(avg_km)
print()
print(' График зависимости Пирсона - km от last_price')
print()
data_piter.plot(x='km', y='last_price', kind='scatter', alpha=0.3);


# Как видно из графика - чем дальше от центра тем ниже стоимость. Наиболее высокая цена до 8 км от центра
# 

# Вывод про проекту
# 
# В данном проекте были обработаны данные по основным харрактеристикам недвижимости.
# Основные выводы согласно данным
# Самая дорогая недвижимость в Санкт-Петербурге
# Наибольшее количество объявлений в Санкт-Петербурге
# Чем ближе к центру тем в среднем дороже стоит недвижимость
# 

# <div class="alert alert-block alert-danger">✍
#     
# 
# __Комментарий от ревьюера №1__
# 
# Для этих райнов нужно найти среднюю цену. Но лучше не хардкодить, а использовать группировку
# </div>

# 

# <div class="alert alert-block alert-success">✔️
#     
# 
# __Комментарий от ревьюера №1__
# 
# Хорошо
# </div>

# **Чек-лист готовности проекта**
# 
# Поставьте 'x' в выполненных пунктах. Далее нажмите Shift+Enter.

# <div class="alert alert-block alert-warning">📝
# Комментарий от ревьюера №1 </b> 
# 
# 
# 
# У тебя получилась очень сильная и хорошая работа. Здорово, что расчеты ты сопровождаешь иллюстрациями, а так же не забываешь про комментарии, твой проект интересно проверять. 
# 
# ---
# 
# Нужно поправить:
# 
# 1) Оформление проекта
# 
# 2) Проверка на дубликаты
# 
# 3) Отсутствуют шаг задания (тип этажа)
# 
# 4) Уменьшить range, чтобы рассмотреть пики
# 
# 5) Сколько занимает быстрая продажа, а сколько долгая?
# 
# 6 Построить графики scatter раздельно и подкрепить корреляцией
# 
# 7) ТОП-10
# 
# 8) Нет решения по последнему шагу и финальный вывод
# 
# 9) После каждого графика (или серии тестов) писать вывод по полученным данным с учетом поставленной бизнес задачи
# 
# 10) Подправить выводы, после изменений
# 
# ----
# 
# 
# Если у тебя будут какие-то вопросы по моим комментариям - обязательно пиши! Буду ждать работу на повторное ревью :)</div>

# <div style="border:solid blue 3px; padding: 20px">
# <div class="alert alert-block alert-success">✔️
#     
# 
# __Коментарий от ревьюера №2__
# 
# 
# В остальном всё чудно😊. Твой проект так и просится на github =)   
#     
# Поздравляю с успешным завершением проекта 😊👍
# И желаю успехов в новых работах 😊
#     
# ---
#     
# От себя хочу порекомендовать тебе отличную книгу про язык Python. Она очень классная (можно купить как новую, так и на Авито попадается. Вот ссылка на pdf этой книги)
#     
# https://monster-book.com/avtomatizaciya-zadach-s-python
# </div>

# In[ ]:





# In[ ]:





# - [x]  открыт файл
# - [х]  файлы изучены (выведены первые строки, метод `info()`, гистограммы и т.д.)
# - [х]  определены пропущенные значения
# - [х]  заполнены пропущенные значения там, где это возможно
# - [х]  есть пояснение, какие пропущенные значения обнаружены
# - [х]  изменены типы данных
# - [х]  есть пояснение, в каких столбцах изменены типы и почему
# - [х]  устранены неявные дубликаты в названиях населённых пунктов
# - [х]  устранены редкие и выбивающиеся значения (аномалии) во всех столбцах
# - [х]  посчитано и добавлено в таблицу: цена одного квадратного метра
# - [х]  посчитано и добавлено в таблицу: день публикации объявления (0 - понедельник, 1 - вторник и т.д.)
# - [х]  посчитано и добавлено в таблицу: месяц публикации объявления
# - [х]  посчитано и добавлено в таблицу: год публикации объявления
# - [х]  посчитано и добавлено в таблицу: тип этажа квартиры (значения — «первый», «последний», «другой»)
# - [х]  посчитано и добавлено в таблицу: расстояние в км до центра города
# - [х]  изучены и описаны следующие параметры:
#         - общая площадь;
#         - жилая площадь;
#         - площадь кухни;
#         - цена объекта;
#         - количество комнат;
#         - высота потолков;
#         - этаж квартиры;
#         - тип этажа квартиры («первый», «последний», «другой»);
#         - общее количество этажей в доме;
#         - расстояние до центра города в метрах;
#         - расстояние до ближайшего аэропорта;
#         - расстояние до ближайшего парка;
#         - день и месяц публикации объявления
# - [х]  построены гистограммы для каждого параметра
# - [х]  выполнено задание: "Изучите, как быстро продавались квартиры (столбец days_exposition). Этот параметр показывает, сколько дней «висело» каждое объявление.
#     - Постройте гистограмму.
#     - Посчитайте среднее и медиану.
#     - В ячейке типа markdown опишите, сколько обычно занимает продажа. Какие продажи можно считать быстрыми, а какие — необычно долгими?"
# - [х]  выполнено задание: "Какие факторы больше всего влияют на общую (полную) стоимость объекта? Постройте графики, которые покажут зависимость цены от указанных ниже параметров. Для подготовки данных перед визуализацией вы можете использовать сводные таблицы."
#         - общей площади;
#         - жилой площади;
#         - площади кухни;
#         - количество комнат;
#         - типа этажа, на котором расположена квартира (первый, последний, другой);
#         - даты размещения (день недели, месяц, год);
# - [х]  выполнено задание: "Посчитайте среднюю цену одного квадратного метра в 10 населённых пунктах с наибольшим числом объявлений. Выделите населённые пункты с самой высокой и низкой стоимостью квадратного метра. Эти данные можно найти по имени в столбце `locality_name`."
# - [х]  выполнено задание: "Ранее вы посчитали расстояние до центра в километрах. Теперь выделите квартиры в Санкт-Петербурге с помощью столбца `locality_name` и вычислите среднюю цену каждого километра. Опишите, как стоимость объектов зависит от расстояния до центра города."
# - [х]  в каждом этапе есть промежуточные выводы
# - [х]  есть общий вывод

# In[ ]:



