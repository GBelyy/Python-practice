import numpy as np
import matplotlib.pyplot as plt
# Задание 1
""""
from PIL import Image
data = input("Введите имя файла:")
img = Image.open(data)
arr = np.asarray(img)
mx = arr.max()
mn = arr.min()
k = mn*np.ones(arr.shape)
finish = np.around((arr-k)*255/(mx-mn))
im = Image.fromarray(finish.astype('uint8'), 'L')
im.show()
#im.save("new_"+data,save_all=True)
"""""
# Задание 2
""""
filename = input("Введите имя файла:")
arr = np.loadtxt(filename)
A=[]
for i in range(arr.size):
    if i<9:
        A.append((sum(arr[:i+1]) / (i+1)))
    else:
        A.append((sum(arr[i-9:i]) / 10))
A = np.array(A)
# Визуализация
fig = plt.figure(frameon=True)
graph_1 = fig.add_subplot(1, 2, 1)
graph_2 = fig.add_subplot(1, 2, 2)
graph_1.plot(arr)
graph_2.plot(A)
graph_1.grid(axis='both')
graph_2.grid(axis='both')
graph_1.set(title="До обработки",
            ylim=[0,35],
            xlim=[0,99])
graph_2.set(title="После обработки",
            ylim=[0,35],
            xlim= 0,99])
plt.subplots_adjust(hspace=0.35, wspace = 0.2)
plt.show()
"""""

# Задание 3
""""
import matplotlib.animation as animation

filename = input("Введите имя файла:")
data = np.loadtxt(filename)
k = data.shape[0]# размер строки
number = int(input("Введите количество итераций:"))
arr = np.loadtxt(filename).reshape(k,1) # перевод строки в столбец
A = np.fromfunction(lambda x, y: x == (y+1), (k, k), dtype=int)*(-1)+np.eye(k) + np.fromfunction(lambda x,y: ((x == 0) & (y == k -1)), (k, k), dtype=int)*(-1)
q = []
for m in range(number):
    q.append(arr)
    arr = arr + (-0.5)*A.dot(arr)

# Визуализация
fig, ax = plt.subplots()
def animate(i):
    ax.clear()
    el = q[i].reshape(1, k).tolist()[0]
    ax.axis([0,k,0,max(a.max() for a in q)])
    ax.grid(axis="both")
    line = ax.plot(el)
    return line
lab_animation = animation.FuncAnimation(fig,
                                      animate,
                                      frames=number,
                                      interval = 0,
                                      repeat = True)
lab_animation.save('lab_numpy.gif',fps=20)
"""""