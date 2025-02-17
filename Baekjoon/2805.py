# 나무자르기(이진탐색)
# 나무 개수(N)와 요청한 나무 길이(M)을 입력
n, m = list(map(int, input().split()))

# 각 떡의 개별 높이 정보를 입력
array = list(map(int, input().split()))

# 1. 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array) # 자를 수 있는 나무의 최대 높이

# 이진 탐색 수행 (반복적)
result = 0
while(start <= end):
    total = 0
    # 2. 절단기 높이(중간값 구하기)
    mid = (start + end) // 2
    # 3. 잘랐을 때의 나무의 길이 계산
    for x in array:
        if x > mid:
            total += x - mid
    # 4. 나무의 길이가 부족한 경우 절단기 높이를 낮추기 (왼쪽 부분 탐색)
    if total < m:
        end = mid - 1
    # 5. 나무의 길이가 충분한 경우 절단기 높이를 높이기(오른쪽 부분 탐색)
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
        start = mid + 1
        
print(result)        
    