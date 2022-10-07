def solution() :
    a = [500, 100, 50, 10]
    money = 1660
    count = 0
    for i in a :
        count = int(money / i)
        money = money % i
        print(f"{i}원 짜리 : {count}개")

if __name__ == "__main__" :
    solution()



