# 5205
# 입력: T/ N/ N개의 정수 Ai
# 출력: N개의 정수 정렬, #t N/2번 원소 출력
def hpar(s, e):
    p, i, j = s, s, e
    while i<=j:
        while i<=j and arr[i] <= arr[p]:
            i+=1
        while  i<=j and arr[j] >= arr[p]:
            j-= 1
        if i<j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[p], arr[j] = arr[j], arr[p]   
    return j

def quick_sort(s, e):
    if s>=e:
        return -1
    pivot = hpar(s,e)
    quick_sort(s, pivot-1)
    quick_sort(pivot+1, e)    

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick_sort(0, N-1)
    print(f'#{tc} {arr[N//2]}')
    