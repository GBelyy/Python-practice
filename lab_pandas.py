import pandas as pd
import numpy as np
#CLOUD DATA
""""
def search(lat,lon,np_cloud):
    for i in range(len(np_cloud)):
        if (900 - i)/10 == lat:
            for j in range(len(np_cloud[0])):
                if (j - 1800)/10 == lon:
                    return np_cloud[i][j]


test_file = "C:/Users/Gleb/Desktop/rem.csv"
df_cities = pd.read_csv(test_file,header=None)
nmp_cities = df_cities.values.tolist()
for n in range(1,13):
    filename = "C:/Users/Gleb/Desktop/cloud_"+str(n)+".csv"
    df_cloud = pd.read_csv(filename,delimiter=';',header=None)
    nmp_cloud = df_cloud.values.tolist()
    for k in nmp_cities:
        cloud = search(k[0],k[1],nmp_cloud)
        k.append(1-cloud)

df = pd.DataFrame(nmp_cities)
df.to_csv('cities_new.csv')
"""
file = "C:/Users/Gleb/Desktop/final_data.csv"
df = pd.read_csv(file,delimiter=';')
df_total = df.groupby("REGION")[['Total cost','AREA']].sum()
df_count = df.groupby("REGION")['Total cost'].count()

df_final = pd.merge(df_total,
               df_count,how='inner',on='REGION')
df_final.to_csv('regions.csv')
#Задание 2
""""
import matplotlib.pyplot as plt

#"C:/Users/Gleb/Desktop/flights.csv"
filename = input("Введите название файла:")
df = pd.read_csv(filename, index_col=" ")

fig, (tw, tp, nf) = plt.subplots(nrows=1, ncols=3,figsize=(10,15))

df[['CARGO','WEIGHT']].groupby('CARGO').sum().plot(ax=tw,kind='bar',title="Total weight per Cargo",legend=False)
df[['CARGO','PRICE']].groupby('CARGO').sum().plot(ax=tp,kind='bar',title="Total price per Cargo",legend=False)
df[['CARGO','PRICE']].groupby('CARGO').count().plot(ax=nf,kind='bar',title="Number of fligths per Cargo",legend=False)

plt.xlabel("")
fig.autofmt_xdate(rotation=45)
plt.subplots_adjust(wspace=0.35)
plt.show()
"""""

#Задание 3
"""""
import matplotlib.pyplot as plt
#Таблица - C:/Users/Gleb/Desktop/students_info.xlsx
#Ejudge - C:/Users/Gleb/Desktop/results_ejudge.html

filename_excel= "C:/Users/Gleb/Desktop/students_info.xlsx"
filename_html = "C:/Users/Gleb/Desktop/results_ejudge.html"
data = pd.merge(pd.read_excel(filename_excel, sheet_name='logins', engine='openpyxl')
                ,pd.read_html(filename_html)[0]
                ,how='inner',left_on='login', right_on='User').fillna(0)  # Общая таблица
del data['login']  #Удаляем ненужное поле с логинами

    #Задание 3.1

fig, (gr_fac, gr_out) = plt.subplots(nrows=1, ncols=2,figsize=(10,15))

av_fac = pd.merge(data[['group_faculty','Solved']].groupby('group_faculty').sum(),
               data[['group_faculty','User']].groupby('group_faculty').count(),how='inner',on='group_faculty')
av_fac['Average_result_fac'] = av_fac.Solved/av_fac.User
del av_fac['User']
del av_fac['Solved']
av_fac.plot(ax=gr_fac,kind='bar',title="Av result per faculty",legend=False)

av_out = pd.merge(data[['group_out','Solved']].groupby('group_out').sum(),
               data[['group_out','User']].groupby('group_out').count(),how='inner',on='group_out')
av_out['Average_result_out'] = av_out.Solved/av_out.User
del av_out['User']
del av_out['Solved']
av_out.plot(ax=gr_out,kind='bar',title="Av result per out group",legend=False)

plt.xlabel("")
fig.autofmt_xdate(rotation=0)
plt.subplots_adjust(wspace=0.35)
plt.show()

    #Задание 3.2
    
#Таблицы тех,кто прошел хотя бы один тест по последним задачам
best_fac = data.query("H > 10 or G > 10")[['group_faculty','User']].groupby('group_faculty').count()
best_out = data.query("H > 10 or G > 10")[['group_out','User']].groupby('group_out').count()

fig, (gr_fac, gr_out) = plt.subplots(nrows=1, ncols=2,figsize=(10,15))

best_fac.plot(ax=gr_fac,kind='bar',title="Good students per faculty",legend=False)
best_out.plot(ax=gr_out,kind='bar',title="Good students per out group",legend=False)

plt.xlabel("")
fig.autofmt_xdate(rotation=0)
plt.subplots_adjust(wspace=0.35)
plt.show()
"""""