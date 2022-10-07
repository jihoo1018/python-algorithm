''' * 금액을 입력받은 후 우리나라 화폐종류별로 해당 갯수를 표기하는 프로그램
    * [요구사항] 금융업을 하는 고객사로부터 프로그램 개발요청이 들어왔습니다.
    * 금액을 입력받은 후 우리나라 화폐종류별로 해당 갯수를 표기하는 프로그램입니다.
    * 예를들어, 125,520 원을 입력하면 화면에 이렇게 보이게 하면 됩니다.
    * 표시하고 10원미만은 절삭
                ### 화폐교환 ###
            ******************************************************
                요청금액 : 126520 원
                5만원 : 2매
                1만원 : 2매
                5천원 : 1매
                1천원 : 1매
                5백원 : 1개
                백원 : 0개
                오십원 : 0개
                십원 : 2개
            ********************************************************'''


# class Solution :
#     def solution(self, money):
#         title = "### 화폐교환 ###"
#         aster = "*" *30
#         answer = f" 요청금액 : {money}원"
#         answer2 = int(money / 50000)
#         answer3 = int(money % 50000 / 10000)
#         answer4 = int(money % 10000 / 5000)
#         answer5 = int(money % 5000 / 1000)
#         answer6 = int(money % 1000 / 500)
#         answer7 = int(money % 500 / 100)
#         answer8 = int(money % 100 / 50)
#         answer9 = int(money % 50 / 10)

#         result = (
#         f"{title}\n {aster}\n {answer}\n {aster}\n"
#         f"5만원 : {answer2}\n"
#         f"1만원 : {answer3}\n"
#         f"5천원 : {answer4}\n"
#         f"1천원 : {answer5}\n"
#         f"5백원 : {answer6}\n"
#         f"백원 : {answer7}\n"
#         f"오십원 : {answer8}\n"
#         f"십원 : {answer9}\n"
#         f"{aster}"
#         )

#         return result

# if __name__=="__main__":
#     solution = Solution()
#     money = int(input("화폐교환할 금액 입력"))
#     print(solution.solution(money))




class Solution :
    def solution(self, m):
        title = "### 화폐교환 ###"
        aster = "*" *30
        answer = f" 요청금액 : {m}원"
        a = [50000,10000,5000,1000,500,100,50,10]
        cnt = 0
        dc = {}
        for i in a :
            cnt = m // i
            dc[i] = cnt 
            m = m % i
        print('### 화폐교환 ###')
        print("*" *30)
        print(f"요청금액 : (money)원")
        for k,v in dc.items() :
            print(f"{k}원 : {v}매")
        print("*" *30)
        return 

if __name__=="__main__":
    solution = Solution()
    money = int(input("화폐교환할 금액 입력"))
    print(solution.solution(money))