# 2527
# 왼쪽 아래 꼭짓점 좌표 x,y 오른쪽 위 꼭짓점 좌표 p,q 항상 x<p, y<q
# 두 직사각형의 겹치는 부분이 직사각형: a, 선분: b, 점: c, 공통부분이 없음:d
# 입력: 테스트케이스 4 / 첫번째 직사각형 , 두번째 직사각형
# 출력: 코드문자 4줄

for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = list(map(int, input().split()))
    

    # 공통부분 없음
    if p1<x2 or q1<y2 or p2<x1 or q2<y1:
        print('d')
    
    # 선분, 점
    elif p1==x2 or q1==y2 or y1==q2 or x1==p2:
        if (p1==x2 and q1==y2) or (p1==x2 and y1==q2) or (x1==p2 and y1==q2) or (x1==p2 and q1==y2):
            print('c')
        else:
            print('b')
    
    # 직사각형
    else:
        print('a')