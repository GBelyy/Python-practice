def get_date(users, user_name):
    for i in range(len(users)):
        if users[i]["Email"] == user_name:
            date = users[i]["Created_at"]
    return date

import json
import networkx as nx

input_file = "C:/Users/Gleb/Desktop/Class task 6.11/input.csv" # файл с требуемыми путями
users_file = "C:/Users/Gleb/Desktop/Class task 6.11/users.json" # файл с инф-ей о пользователях
finish_file = "C:/Users/Gleb/Desktop/Class task 6.11/finish.json" # файл,куда будет выводиться результат

G = nx.MultiGraph()
input_data = []
finish_data = []
# список пользователей
with open(users_file, "r") as read_users:
    users = json.load(read_users)
# список требуеммых путей
with open(input_file, "r") as read_input:
    for line in read_input:
        input_data.append([n for n in line.split(',')])

# создаем граф ,добавляя вершины - пользователей и ветви - подписчиков
for i in range(len(users)):
    email = users[i]["Email"]
    for el in users[i]["Subscribers"]:
        G.add_edge(email, el["Email"])
# расчет кратчайших путей для всех пар вершин
predecessors, _ = nx.floyd_warshall_predecessor_and_distance(G)

for i in range(len(input_data)):
    pathes = []
    try:# Обработка случая отсутсвия путей
        shortest_path = nx.reconstruct_path(input_data[i][0], input_data[i][1].strip("\n"), predecessors)
        pathes = []
        for k in range(len(shortest_path)):
            if k != 0 and k != len(shortest_path)-1:
                pathes.append({"email": shortest_path[k],
                               "created_at": get_date(users, shortest_path[k])})
    except:
        pass
    el_finish = {'id': str(i), 'from': str(input_data[i][0]), 'to': str(input_data[i][1].strip("\n")),
                 "path": pathes}
    finish_data.append(el_finish)

with open(finish_file, "w") as write_file:
    json.dump(finish_data,write_file,indent = 4)
