# 1248. [S/W 문제해결 응용] 3일차 - 공통조상
from collections import defaultdict

T = int(input())

def find_ancestors(node, parent):
    ancestors = set()
    while node in parent: # 부모가 있는 경우
        ancestors.add(node) # 조상 리스트에 현재 노드 추가
        node = parent[node] # 노드를 현재 노드의 부모 노드로 변경
    ancestors.add(node) # 루트 포함(루트는 부모가 없지만 조상이니까 추가 필요)
    return ancestors

def subtree_size(node, tree):
    size = 1
    for child in tree.get(node, []): # 자식이 있으면 그 리스트를 반환, 없으면 빈 리스트 반환)
        size += subtree_size(child, tree) # 자식마다 그 자식의 서브트리 크기를 재귀적으로 구해서 더함)
    return size

for tc in range(1, T + 1):
    V, E, v1, v2 = map(int, input().split())
    edge = list(map(int, input().split()))

    tree = defaultdict(list) # 부모 -> 자식 리스트
    parent = dict() # 자식 -> 부모

    for i in range(0, len(edge), 2):
        p, c = edge[i], edge[i + 1]
        tree[p].append(c)
        parent[c] = p

    # 공통 조상 찾기
    anc1 = find_ancestors(v1, parent)
    while v2 not in anc1: # 공통 조상이 아닐 때까지
        v2 = parent[v2] # v2를 현재 v2의 부모 노드로 변경
    lca = v2 # 공통 조상 발견

    size = subtree_size(lca, tree)

    print(f"#{tc} {lca} {size}")