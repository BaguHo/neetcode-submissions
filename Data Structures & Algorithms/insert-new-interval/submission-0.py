class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # newInterval end가 리스트의 특정 start보다 작을 때
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # newInterval start가 리스트의 특정 end보다 클 때 
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
    
        # 마지막까지 갔는데 끝나지 않았다면 병합된 구간을 마지막에 추가
        res.append(newInterval)
        return res