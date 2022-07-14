# 기본 시간, 기본 요금, 단위 시간, 단위 요금
# 출차된 내역 없으면 23:59에 출차된 것으로 간주
# 나누어 떨어지지 않으면 올림

# 누적 주차 시간 <= 기본 시간 : 기본 요금
# 누적 주차 시간 > 기본 시간
#   기본 요금 + 초과한 시간 요금(=> 단위 시간*단위 요금)

# 주차 요금 정수 배열: fees
# 자동차 입출차 내역: records
# 차량 번호가 작은 자동차부터 청구할 주차 요금을 차례대로 정수 배열에 담아 return

import math

f = [180, 5000, 10, 600]
r = [
    "05:34 5961 IN", 
    "06:00 0000 IN",
    "06:34 0000 OUT",
    "07:59 5961 OUT",
    "07:59 0148 IN",
    "18:59 0000 IN",
    "19:09 0148 OUT",
    "22:59 5961 IN",
    "23:00 5961 OUT" ]


def totalTime(timeList):
    total = 0
    
    while timeList:
        outH, outM = timeList.pop().split(':')
        inH, inM = timeList.pop().split(':')
        h = int(outH) - int(inH)
        m = int(outM) - int(inM)
        if m < 0 :
            m = m+60
            h = h-1
        total = total + m + (h*60)
    
    return total

def getItem(t):
    return t[1]

def solution(fees, records):
    dTime, dFee, cTime, cFee = fees

    dic = dict()

    for r in records:
        time, carNum, state = r.split()
        carNum = int(carNum)

        if carNum in dic:
            dic[carNum].append(time)
        else:
            dic[carNum] = [time]

    for k, v in dic.items():
        if len(v) % 2 != 0:
            dic[k].append('23:59')
        cct = totalTime(v)
        
        totalFee = 0
        if dTime - cct > 0:
            totalFee = dFee
        else:
            totalFee += dFee
            overTime = cct - dTime
            num = math.ceil(overTime/cTime)
            totalFee += (num*cFee)
        dic[k] = totalFee
    
    dic = sorted(dic.items())
    answer = list(map(getItem, dic))
    print(answer)

solution(f, r)



