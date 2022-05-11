#Задание 1
"""""
import matplotlib.pyplot as plt
filename = input("Введите название файла:")
x = []
y = []
f = open(filename)
number = int(f.readline().split()[0])
for line in f:
    q = [float(n) for n in line.split()]
    x.append(q[0])
    y.append(q[1])
    # обработка случая,когда начинает обрабатываться следующий блок данных в том же файле
    number -=1
    if number == 0:
        break

plt.plot(x, y,marker ='o',linestyle=' ',color='black')
kx = (max(x)- min(x))/10
ky = (max(y)- min(y))/10
plt.axis([min(x) - kx, max(x) + kx, min(y)-ky, max(y)+ky])
plt.title("Number of points" + ": " + str(len(x)))
plt.show()
"""""


#Задание 2
"""""
def get_ax_limits(q):#Находим общие пределы для осей
    Mx_x = []
    Mn_x = []
    Mx_y = []
    Mn_y = []
    for i in range(len(q)):
        if i % 2 == 0:
            Mx_x.append(max(q[i]))
            Mn_x.append(min(q[i]))
        else:
            Mx_y.append(max(q[i]))
            Mn_y.append(min(q[i]))
    return [min(Mn_x),max(Mx_x),min(Mn_y)-1,max(Mx_y)+1]

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.animation as animation

filename = input("Введите название файла:")
f = open(filename)
q = []
for line in f:
    q.append([float(n) for n in line.split()])
    
#Визуализация в виде большого графика
fig = plt.figure(figsize=[6,30])
for i in range(1,int(len(q)/2)+1):
    graph = fig.add_subplot(3, 2, i)
    graph.plot(q[i*2-2],q[i*2-1])
    graph.set(
        title = "Frame"+" "+str(i),
        xlim = [get_ax_limits(q)[0],get_ax_limits(q)[1]],
        ylim = [get_ax_limits(q)[2],get_ax_limits(q)[3]] )
    graph.grid(axis='both')
    graph.xaxis.set_major_locator(ticker.MultipleLocator(3))#деления сетки по х
    graph.yaxis.set_major_locator(ticker.MultipleLocator(3))#деления сетки по у

plt.subplots_adjust(hspace=0.35,wspace = 0.2)
plt.show()

#Визуализация в виде gif-файла(lab.gif)
fig, ax = plt.subplots()
def animate(i):
    ax.clear()
    ax.axis(get_ax_limits(q))
    line = ax.plot(q[i*2-2], q[i*2-1])
    return line
lab_animation = animation.FuncAnimation(fig,
                                      animate, 
                                      frames=6,
                                      interval = 10,
                                      repeat = True)
lab_animation.save('lab.gif',fps=10)
"""""


#Задание 3
""""
import matplotlib.pyplot as plt
import numpy as np

def sum_lists(q1,q2):
    q3 = []
    for i in range(len(q1)):
        q3.append(q1[i]+q2[i])
    return q3

filename = input("Введите название файла:")
f = open(filename)
q = []
width = 0.35
ind1 = np.arange(7)
ind2 = np.arange(6)
preps = [[],[],[],[],[],[],[]]#массив всех оценок ,поставленных преподавателем
groups = [[],[],[],[],[],[]]#массив всех оценок,полученных группой
grad_pr = [[],[],[],[],[],[],[],[]]#массив распредления преподавателей по оценкам
grad_gr = [[],[],[],[],[],[],[],[]]#массив распредления групп по оценкам
for line in f:
    q.append([n for n in line.split(';')])

for el in q:#распределяем оценки по преподавателям
    if el[0] == "prep1":
        preps[0].append(int(el[2]))
    if el[0] == "prep2":
        preps[1].append(int(el[2]))
    if el[0] == "prep3":
        preps[2].append(int(el[2]))
    if el[0] == "prep4":
        preps[3].append(int(el[2]))
    if el[0] == "prep5":
        preps[4].append(int(el[2]))
    if el[0] == "prep6":
        preps[5].append(int(el[2]))
    if el[0] == "prep7":
        preps[6].append(int(el[2]))
for el in q:#распределяем оценки по группам
    if el[1] == "751":
        groups[0].append(int(el[2]))
    if el[1] == "752":
        groups[1].append(int(el[2]))
    if el[1] == "753":
        groups[2].append(int(el[2]))
    if el[1] == "754":
        groups[3].append(int(el[2]))
    if el[1] == "755":
        groups[4].append(int(el[2]))
    if el[1] == "756":
        groups[5].append(int(el[2]))
for i in range(7):
    grad_pr[0].append(preps[i].count(3))
    grad_pr[1].append(preps[i].count(4))
    grad_pr[2].append(preps[i].count(5))
    grad_pr[3].append(preps[i].count(6))
    grad_pr[4].append(preps[i].count(7))
    grad_pr[5].append(preps[i].count(8))
    grad_pr[6].append(preps[i].count(9))
    grad_pr[7].append(preps[i].count(10))
for i in range(6):
    grad_gr[0].append(groups[i].count(3))
    grad_gr[1].append(groups[i].count(4))
    grad_gr[2].append(groups[i].count(5))
    grad_gr[3].append(groups[i].count(6))
    grad_gr[4].append(groups[i].count(7))
    grad_gr[5].append(groups[i].count(8))
    grad_gr[6].append(groups[i].count(9))
    grad_gr[7].append(groups[i].count(10))

plots_pr = []  # диаграммы преп-ов
plots_gr = []  # диаграммы оценок
fig, (graph1, graph2) = plt.subplots(nrows=2, ncols=1)

bottom1 = [0 for x in range(8)]
bottom2 = [0 for x in range(8)]
for i in range(8):
    if i == 0:
        plots_pr.append(graph1.bar(ind1, grad_pr[i], width,label=str(i+3)))
        plots_gr.append(graph2.bar(ind2, grad_gr[i], width,label=str(i+3)))
    else:
        plots_pr.append(graph1.bar(ind1, grad_pr[i], width, bottom=bottom1,label=str(i+3)))
        plots_gr.append(graph2.bar(ind2, grad_gr[i], width, bottom=bottom2,label=str(i+3)))
    bottom1 = sum_lists(grad_pr[i], bottom1)
    bottom2 = sum_lists(grad_gr[i], bottom2)


graph1.set_ylabel('Number of students')
graph1.set_title('Marks per prep')
graph1.set_xticks(ind1)
graph1.set_xticklabels(['prep1', 'prep2', 'prep3', 'prep4', 'prep5', 'prep6', 'prep7'])
graph1.set_yticks(np.arange(0, 25, 5))
graph1.legend()

graph2.set_ylabel('Number of students')
graph2.set_title('Marks per group')
graph2.set_xticks(ind2)
graph2.set_xticklabels(['751', '752', '753', '754', '755', '756'])
graph2.set_yticks(np.arange(0, 25, 5))
graph2.legend()

plt.subplots_adjust(hspace=0.5)
plt.show()
"""
