def bfs(s):
    q = []
    v = [0] * 101

    q.append(s) #빈 큐에다가 시작점 넣기
    v[s] = 1    #방문했음 표시
    ans = s #아무도 없으면 내가 답

    while q:
        c = q.pop(0) #current는 선입선출값
        #더 늦게 연락 받거나 동시에 최종연락이면 큰 값
        if v[ans] < v[c] or (v[ans] == v[c]) and ans < c:
            ans = c

        for n in contact[c]: #연결된
            if not v[n]: #미방문
                q.append(n) #큐에 넣고
                v[n] = v[c]+1 #n까지 경로의 길이
    return ans


for test_case in range(1, 11):
    N, S = map(int, input().split())
    #입력 받는 데이터 길이, 시작점

    #받은 데이터를 연결 형태로 바꾸기
    #contact의 값이 1이면 서로 연결됨
    lst = list(map(int, input().split()))
    contact = [[] for _ in range(101)]
    for i in range(0, N, 2):
        p, c = lst[i], lst[i+1]
        contact[p].append(c)

    ans = bfs(S)
    print(f'#{test_case} {ans}')

