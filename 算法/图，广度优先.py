# 李佳朗
# 开发时间：2023
class GraphAdjMat:
    # 基于邻接矩阵实现的无向图类
    def __init__(self, vertices: list[int], edges: list[list[int]]):
        # 构造方法
        # 顶点列表，元素代表“顶点值”，索引代表“顶点索引”
        self.vertices: list[int] = []
        # 邻接矩阵，行列索引对应“顶点索引”
        self.adj_mat: list[list[int]] = []
        # 添加顶点
        for val in vertices:
            self.add_vertex(val)
        # 添加边
        # 请注意，edges元素代表顶点索引，即对应vertices元素索引
        for e in edges:
            self.add_edge(e[0], e[1])


def graph_bfs(graph: GraphAjList, start_vet: Vertex) -> list[Vertex]:
    # 广度优先遍历BFS
    # 使用邻接表来表示图，以便获取指定顶点的所用邻接顶点
    # 顶点遍历序列
    res = []
    # 哈希表，用于记录已被访问过的顶点
    visited = set[Vertex]([start_vet])
    # 队列用于实现BFS
    que = deque[Vertex]([start_vet])
    # 以顶点vet为起点，循环直至访问完所有顶点
    while len(que) > 0:
        vet = que.popleft()
        # 队首顶点出队
        res.append(vet)
        # 记录访问顶点
        # 遍历该顶点的所有邻接顶点
        for adj_vet in graph.adj_list[vet]:
            if adj_vet in visited:
                continue  # 跳过已被访问的顶点
            que.append(adj_vet)
            # 只入队未访问的顶点
            visited.add(adj_vet)  # 标记该顶点已被访问
            # 返回顶点遍历序列
    return res


def dfs(graph: GraphAdjList, visited: set[Vertex], res: list[Vertex], vet: Vertex):
    "深度优先遍历DFS辅助函数"
    res.append(vet)  # 记录访问顶点
    visited.add(vet)  # 标记该顶点已被访问
    # 遍历该顶点的所有临界顶点
    for adjVet in graph.adj_list[vet]:
        if adjVet in visited:
            continue  # 跳过已被访问的顶点

        # 递归访问邻接顶点
        return(graph, visited, res, adjVet)

def graph_dfs(graph:GraphAdjList,start_vet:Vertex)->list[Vertex]:
    #深度优先遍历DFS
    #使用邻接表来表示图，以便获取指定顶点的所用邻接顶点
    #顶点遍历序列
    res=[]
    #哈希表，用于记录已被访问过的顶点
    visited=set[Vertex]()
    dfs(graph,visited,res,start_vet)
    return res


