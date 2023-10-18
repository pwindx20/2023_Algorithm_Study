# 입력: 문자열 배열 빈칸: ".", 파일:"#"
# 출력: [lux, luy, rdx, rdy]
# 최소한의 이동거리를 갖는 한번의 드래그로 모든 파일을 선택해서 한번에 지우려고 할때
# 바탕화면의 격자점 S(lux, luy)를 클릭한 상태로 격자점E(rdx,rdy)로 이동
# 드래그한 거리는 |rdx-ldx|+|rdy-ldy|
def solution(wallpaper):
    N, M = len(wallpaper), len(wallpaper[0])
    answer = [N, M, 0, 0]
    for i in range(N):
        for j in range(M):
            if wallpaper[i][j]=="#":
                if i<=answer[0]:
                    answer[0] = i
                if j<=answer[1]:
                    answer[1] = j
                if i>=answer[2]:
                    answer[2] = i+1
                if j>=answer[3]:
                    answer[3] = j+1
    return answer



wall = [".....", 
        "....#"]
print(solution(wall))