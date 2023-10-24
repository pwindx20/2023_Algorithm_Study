# 5204
# 입력: T/ N/ ai
# 출력: #t N//2번째 원소, 오른쪽 원소가 먼저 복사되는 경우의 수
def merge(l_lst, r_lst):
    global cnt
    result = []
    lp = rp = 0
    while lp<len(l_lst) and rp<len(r_lst):
        if l_lst[lp]<r_lst[rp]:
            result.append(l_lst[lp])
            lp += 1
        else:
            result.append(r_lst[rp])
            rp += 1
            
    # 같은 숫자가 있을 경우를 제외
    if result[-1] !=l_lst[-1] and lp<len(l_lst): 
        cnt+= 1
    
    result += l_lst[lp:]
    result += r_lst[rp:]
    
    return result
    

def merge_sort(lst):
    N = len(lst)
    if N ==1:
        return lst
    m = N//2
    left_lst = merge_sort(lst[:m])
    right_lst = merge_sort(lst[m:])
    
    return merge(left_lst, right_lst)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    cnt = 0
    arr = merge_sort(arr)
    print(f'#{tc} {arr[N//2]} {cnt}')