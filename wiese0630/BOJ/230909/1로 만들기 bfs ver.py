from collections import deque

# 그래프 정의 (딕셔너리로 표현)
graph = {
    '1': ['2', '2', '3'],
    '2': ['3', '4', '6'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def bfs(graph, start):
    visited = set()  # 방문한 노드를 저장하기 위한 집합
    queue = deque()  # BFS를 위한 큐

    visited.add(start)  # 시작 노드 방문 처리
    queue.append(start)  # 시작 노드를 큐에 넣음

    while queue:
        node = queue.popleft()  # 큐에서 노드를 하나 꺼냄
        print(node, end=' ')  # 노드 출력

        # 현재 노드와 연결된 인접 노드들을 방문
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)  # 방문한 노드로 표시
                queue.append(neighbor)  # 큐에 삽입

# BFS 시작 노드를 선택하여 호출
start_node = 'A'
print("BFS 탐색 순서:")
bfs(graph, start_node)
