# https://leetcode.com/problems/reorder-data-in-log-files/
# 로그파일 재정렬 - 43ms 14.1MB
class Solution:
    @staticmethod
    def reorderLogFiles(logs: list[str]) -> list[str]:
        check_dig = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        dig, let = [], []
        # 공백으로 나눠서 logs_split에 담기
        logs_split = [log.split() for log in logs]
        # 식별자 뒤에 수가나오면 dig에 담고 아니면 let에 담기
        for log in logs_split:
            check = log[1]
            for num in check_dig:
                if num in check:
                    dig.append(log)
                    break
            else:
                let.append(log)
        # 레터 로그는 내용에 따라 사전순으로 정렬된다 => 내용이 동일하면 식별자를 기준으로 사전순으로 정렬
        let.sort(key=lambda x: (x[1:], x[0]))
        temp = let + dig
        # 결과출력
        result = [' '.join(s for s in log) for log in temp]
        return result