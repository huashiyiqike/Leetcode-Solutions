class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        cur = 0
        maxl = 0
        last = 0
        step = 0
        while cur < len(A) - 1:
            maxl = max(maxl, cur + A[cur])
            for i in range(last, cur):
                maxl = max(maxl, i + A[i])
            last = cur
            cur = maxl
            step += 1
        return step


class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        if len(A) <= 1:
            return 0
        ref = [0 for i in A]
        ref[0] = 0
        maxs = 0
        for idx, item in enumerate(A):
            if idx + item > maxs:

                for i in range(maxs + 1, idx + item + 1):
                    if i < len(ref):
                        ref[i] = ref[idx] + 1

                maxs = idx + item

        return ref[-1]
