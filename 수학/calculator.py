# 계산기
class Solution:
    def solution(self, a, b, c):
        if b == "+":
            answer = a + c
        elif b == "-":
            answer = a - c
        elif b == "*":
            answer = a * c
        elif b == "/":
            answer = a / c
        elif b == "%":
            answer = a % c
        else:
            answer = "잘못된 연산자입니다"
        return answer

if __name__=="__main__":
    solution = Solution()
    a = int(input(" 첫번째 수: "))
    b = input("+, -, *, /, %")
    c = int(input(" 두번째 수: "))
    print(solution.solution(a, b, c))
    
