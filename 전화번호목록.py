# 코딩테스트연습 > 해시 > 전화번호 목록
# https://velog.io/@rudnf003/python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%95%B4%EC%8B%9C-%EC%A0%84%ED%99%94%EB%B2%88%ED%98%B8-%EB%AA%A9%EB%A1%9D

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

    phone_book.sort()

    for i in range(1, total):
        bNum = phone_book[i-1]
        if bNum == phone_book[i][0:len(bNum)]:
            answer = False
    
    return answer
            
print(solution(pBook))