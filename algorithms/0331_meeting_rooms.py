# 输入：会议列表，每个元素是 [开始时间, 结束时间]
meetings = [[0, 30], [5, 10], [15, 20]]
# 输出：False（[0,30] 和 [5,10] 冲突）

meetings = [[7, 10], [2, 4]]
# 输出：True（没有冲突）

def can_attend_all(meetings) -> bool:
    meetings.sort(key=lambda x: x[0])

    for i in range(len(meetings) -1):
        if meetings[i][1] > meetings[i+1][0]:
            return False
    return True

meetings_test_a = [[3,9], [7,11]]
meetings_test_b = [[3,5], [7,11]]
print(can_attend_all(meetings_test_a))
print(can_attend_all(meetings_test_b))