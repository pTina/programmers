# 코딩테스트연습 > 해시 > 전화번호 목록


pBook = ["12","123","1235","567","88"]
pBook2 = ["99", "1234", "1947", "8671", "12122", "19478", "787486"]
pBook3 = ["119", "123192", "88838333", "1234", "123200"] 
pBook4 = ["4321", "432", "122", "1334"] 
pBook5 = ['1']

def solution(phone_book):
    answer = True
    total = len(phone_book)

    if total == 1:
        return answer

    # 문자열로된 숫자를 정렬하면
    # 이전 문자열이랑만 비교하면 됨!
    phone_book.sort()

    for i in range(1, total):
        bNum = phone_book[i-1]
        if bNum == phone_book[i][0:len(bNum)]:
            answer = False
    
    return answer
            
print(solution(pBook))