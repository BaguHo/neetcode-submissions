class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        temp = stones
        while len(temp) > 1:
            first_max_num = max(temp)
            temp.remove(first_max_num)
            second_max_num = max(temp)
            temp.append(first_max_num)
            if first_max_num - second_max_num == 0:
                temp.remove(first_max_num)
                temp.remove(second_max_num)
            else:
                temp.remove(first_max_num)
                temp.remove(second_max_num)
                temp.append(first_max_num - second_max_num)
        if len(temp) == 1:
            return temp[0]
        else:
            return 0