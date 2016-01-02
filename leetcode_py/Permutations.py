class Solution:
    def next(self, cur):
        for j in range(len(cur) - 2, -1, -1):
            for i in range(len(cur) - 1, j, -1):
                if cur[i] > cur[j]:
                    cur[i], cur[j] = cur[j], cur[i]
                    cur[j + 1:] = cur[j + 1:][::-1]
                    return cur
        return False

    def permute(self, num):
        num = sorted(num)
        res = [num[::]]
        while num:
            num = self.next(num)
            if num:
                res.append(num[::])
        return res


class Solution:
    def dfs(self, num, path, res, flag):
        if len(path) == len(num):
            res.append(path[:])
            return
        for i in range(len(num)):
            if not flag[i]:
                flag[i] = True
                path.append(num[i])
                self.dfs(num, path, res, flag)
                flag[i] = False
                path.pop()

    def permute(self, num):
        res, flag = [], [False for i in num]
        self.dfs(num, [], res, flag)
        return res


if __name__ == "__main__":
    a = Solution()

    print a.permute([2, 34])
    print a.permute([3, 1, 2])
    print a.permute([1, 2, 3, 4])
