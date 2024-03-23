파이썬 복습(wikidoces 21번-함수)
함수를 사용하여 시급과 근무시간을 계산하는 프로그램

def weeklyPay( rate, hour ):
    money = 0
    if (hour > 30):
        money = rate*30 + 1.5*rate*(hour-30)    # 근무시간이 30시간초과면 1.5배
    else:
        money = rate*hour
    return money

rate = int(input("시급을 입력하세요: "))
hour = int(input("근무 시간을 입력하세요: "))
print("주급은 " + str(weeklyPay(rate,hour)))