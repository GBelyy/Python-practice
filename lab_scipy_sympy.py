#Задание 1
""""
from sympy import *
x = Symbol('ro')  # as ro
y = Symbol('lambda')  # as lambda
z = Symbol('mu')  # as mu
matrix = Matrix([[0, 0, 0, -1/x, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, -1/x, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, -1/x, 0, 0, 0],
                 [-(y+2*z), 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, -z, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, -z, 0, 0, 0, 0, 0, 0],
                 [-y, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [-y, 0, 0, 0, 0, 0, 0, 0, 0]])
w = matrix.eigenvals()
for key, value in w.items():
  print("{0}: {1}".format(key,value))  #Собств.значение: кратность корня
"""""
#Задание 2
"""""
import numpy as np
import matplotlib.pyplot as plt

filename = input("Введите название файла:")
f = open(filename)
N = int(f.readline())
arr = np.loadtxt(f)
b = arr[-1]
A = arr[0:-1].reshape(N,N)
y = np.linalg.solve(A,b)
x = np.arange(0,len(y))

fig, ax = plt.subplots()
plt.grid()
ax.bar(x, y,color='darkgreen')
ax.set(xlabel="Номер решения",
       ylabel='X(i)')

fig.set_figwidth(12)
fig.set_figheight(6)

plt.show()
"""""
#Задание 3
"""""
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

t = np.arange(0, 10, 0.01)
y0 = [0, np.sqrt(2)]

#Решение scipy
def func(y, t):
    return -2 * y
y_sci = odeint(func, y0, t)[:, 1]

#Решение sympy
x = sp.symbols('x')
y = sp.Function('y')
eq = sp.Eq(sp.Derivative(y(x), x), -2 * y(x))
f = sp.dsolve(eq, ics={y(0): sp.sqrt(2)})
y_sym = np.zeros(t.size)
for i in range(t.size):
    y_sym[i] = (f.rhs).subs({x: t[i]}).n()

fig, (graph, dif) = plt.subplots(1, 2,figsize=(15,15))

fig.subplots_adjust(hspace=0.2)
graph.plot(t, y_sci, label='sympy')
graph.plot(t, y_sym, label='scipy')
graph.set(title='Решения дифференциального уравнения')
graph.legend()
graph.grid()

dif.plot(t, y_sym - y_sci)
dif.set_title('Разность решений sympy и scipy')
dif.grid()
plt.show()
"""""