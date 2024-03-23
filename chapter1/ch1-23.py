23. 피보나치 수열을 효과적으로 계산하기 위하여 큐를 이용할 수 있다. 처음에는 큐에 F(0)와 F(1)의 값이 들어가 있고,
    F(2)를 계산할 때 F(0)을 큐에서 제거해야 하고, 새로 계산된 F(2)=F(0)+F(1)가 다시 큐에 들어간다. 피보나치 수열은
    다음과 같이 정의된다. 큐를 이용하여 피보나치 수열을 계산하는 프로그램을 작성하라.
    F(0)=0, F(1)=1
    F(n)=F(n-1)+F(n-2)

import collections

Q = collections.deque()         #Q를 생성하여 초기화
Q.append(0)                     #큐에 값 0을 추가
Q.append(1)                     #큐에 값 1을 추가

print("F(0) = 0")
print("F(1) = 1")

for i in range(2, 11):          #(2~10)까지 반복하여 피보나치수열 계산
    first = Q.popleft()         #큐에서 먼저 한개의 값을 꺼내 저장
    second = Q.popleft()        #큐에서 그 다음 값을 꺼내 저장
    val = first + second        #꺼낸 두 값을 더해 저장
    Q.appendleft(second)        #2번째로 꺼낸 값은 다음 계산을 위해 다시 추가
    Q.append(val)               #두 값의 합을 큐에 추가
    print("F(%d) ="%i, val)     #i는 수열의 항 번호이고 각각의 값을 출력