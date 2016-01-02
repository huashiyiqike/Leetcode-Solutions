class Solution:
    # @param {string} path
    # @return {string}
    def simplifyPath(self, path):
        path = path.strip().split('/')
        stack = []
        for idx, item in enumerate(path):
            if item == '.' or item == '':
                continue
            elif item == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(item)
        res = '/'
        for i in stack:
            res += i + '/'
        return res[:-1] if len(res) > 1 else res


class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        if path == '/':
            return '/'
        stack = []
        pre = 1
        p = 1
        while p < len(path):
            while p < len(path) - 1 and path[p] == '/' and path[p - 1] == '/':
                pre = p + 1
                p = pre
            if path[p] == '/':
                if p > pre:
                    stack.append(path[pre:p])
                p += 1
                pre = p
            elif path[p] == '.':
                if p + 2 < len(path) and path[p + 1] == '.' and path[p + 2] != '/':
                    p += 3
                elif p + 1 < len(path) and path[p + 1] == '.':
                    if len(stack) > 0:
                        stack.pop()
                    p += 3
                    pre = p
                elif p + 1 < len(path) and path[p + 1] != '/':
                    p += 1
                else:
                    p += 2
                    pre = p
            else:
                p += 1

        if p > pre:
            stack.append(path[pre:p])
        res = ''
        for i in stack:
            res += '/' + i
        if res == '':
            res = '/'
        return res


if __name__ == "__main__":
    a = Solution()
    #     print a.simplifyPath('/home/a/./../abc/./d////a/../')
    #     print a.simplifyPath('/..hidden')
    #     print a.simplifyPath('/.hidden')
    #     print a.simplifyPath('//.../jom')
    #     print a.simplifyPath('///a')
    print a.simplifyPath('/./')
    print a.simplifyPath('/./g/././//.//h///././/..///')
