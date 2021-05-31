A = input("f(x) = ")        # f(x)를 A로 정의

plus1 = A.index("+")        # + 기호의 위치를 찾음
plus2 = A.index("+", plus1+1)

a = A[:plus1-3]         # 이차항의 계수 a
if a == "":     # 이차항의 계수가 1이라서 생략되어 있을 때 이차항의 계수 변수인 a를 1로 설정해주는 코드
    a = 1  

b = A[plus1+1:plus2-1]      # 일차항의 계수 b
c = A[plus2+1:]         # 상수항의 계수 c

print(a,b,c)