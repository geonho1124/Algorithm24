26. 위 문제와 같이 구현된 집합에서 A가 B의 진부분집합인지를 검사하는 함수를 구현하라.
    단, A가 B의 부분집합이지만 A와 B가 같지 않은 경우 A는 B의 진부분집합이다.

def proper_subset(A, B):
    if set(A) == set(B):             # 집합A와 B가 같은지(진부분집합이 아닌지)검사
        return False
    elif set(A).issubset(set(B)):    #issubset매소드를 사용하여 A가 B의 부분집합인지 검사
        return True
    else:
        return False

A = [1, 2]
B = [1, 2, 3, 4, 5]
print("A가 B의 진부분집합인가요?", proper_subset(A, B))