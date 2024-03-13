import re
from utils import timer


file_v = 'text'
file = '2023/Day25/input/' + file_v + '.txt'

queue = []
bfs_explored = []
dfs_explored = set()


@timer
def main():
    with open(file) as raw:
        text = raw.readlines()
        print(text)

    my_list = []
    for line in text:
        split_line = line.split(': ')
        # print(split_line)
        # print(split_line[1])
        split_list = split_line[1].replace(' ', ', ').strip('\n')
        # print(split_list)
        qwe = re.findall(r'([a-z]{3})', split_list)
        # print(qwe)
        qwe.insert(0, split_line[0])
        index = 1
        len_qwe = len(qwe)
        while index < len_qwe:
            my_list.append(qwe[0] + ' -- ' + qwe[index])
            index += 1
    print(my_list)
    path = '2023/Day25/input/' + file_v + '_test.txt'
    with open(path, mode='w') as that_file:
        for line in my_list:
            that_file.write(str(line) + '\n')

    second_list = []
    path = '2023/Day25/input/my_list-with_3_removed.txt'
    with open(path, mode='r') as r_file:
        for line in r_file:
            asd = line.strip('\n')
            line_split = asd.split(' -- ')
            second_list.append(line_split)

    print(second_list)

    graph_list = []
    for stuff in second_list:
        rep = [stuff[1]]
        stuff.pop(1)
        stuff.append(rep)
        graph_list.append(stuff)

    bfs_search = []
    for line in graph_list:
        root = line[0]
        graph = line[1]
        my_search = BFS(bfs_explored, graph, root)
        if bfs_search.count(my_search) == 0:
            bfs_search.append(my_search)
    len_bfs = len(bfs_search)
    print(len_bfs)

    dfs_search = []
    for line in graph_list:
        root = line[0]
        graph = line[1]
        mine_search = DFS(dfs_explored, graph, root)
        if dfs_search.count(mine_search) == 0:
            dfs_search.append(mine_search)
    len_bfs = len(dfs_search)
    print(len_bfs)


def BFS(bfs_explored, graph, root):
    bfs_explored.append(root)
    queue.append(root)
    while queue:
        v = queue.pop(0)
        if bfs_explored.count(v) > 0:
            return v
        for edge in graph(v):
            if bfs_explored.count(edge) == 0:
                bfs_explored.append(edge)
                queue.append(edge)


def DFS(dfs_explored, graph, root):
    if root not in dfs_explored:
        dfs_explored.add(root)
        for neighbor in graph:
            DFS(dfs_explored, graph, root)


main()
