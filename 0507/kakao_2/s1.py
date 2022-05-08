from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    queue1_sum = sum(queue1)
    queue2_sum = sum(queue2)

    target = (queue1_sum + queue2_sum)

    # target값이 홀수일경우 return -1
    if target % 2:
        return -1
    target //= 2

    # 처리 불가능일 경우 if분기
    max_num = max(max(queue1), max(queue2))
    if max_num > queue1_sum + queue2_sum - max_num:
        return -1

    count = 0

    for i in range(600000):
        if queue1_sum == queue2_sum:
            return count
        # 본 코드 시작
        if queue1_sum >= queue2_sum:
            pop_num = queue1.popleft()
            queue2.append(pop_num)
            queue1_sum -= pop_num
            queue2_sum += pop_num
        else:
            pop_num = queue2.popleft()
            queue1.append(pop_num)
            queue1_sum += pop_num
            queue2_sum -= pop_num
        count += 1
    else:
        return -1
    return count