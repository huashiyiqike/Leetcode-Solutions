#http://articles.leetcode.com/2011/11/longest-palindromic-substring-part-i.html
#http://articles.leetcode.com/2011/11/longest-palindromic-substring-part-ii.html
class Solution:
    #Manacher algorithm
    #http://en.wikipedia.org/wiki/Longest_palindromic_substring

    def longestPalindrome(self, s):
        # Transform S into T.
        # For example, S = "abba", T = "^#a#b#b#a#$".
        # ^ and $ signs are sentinels appended to each end to avoid bounds checking
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range (1, n-1):
            P[i] = (R > i) and min(R - i, P[2*C - i]) # equals to i' = C - (i-C)
            # Attempt to expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]

        # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]

class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        sets = set()
        begin = 0
        maxlen = 0
        for i in range(len(s)-1,-1,-1):
            for j in range(i,len(s)):
                if (j <= i+1 or (i+1, j-1) in sets) and s[i] == s[j]:
                    sets.add((i, j))
                    if j-i+1 > maxlen:
                        maxlen = j-i+1
                        begin = i
        return s[begin:(begin+maxlen)]

# java not TLE
class Solution:
    # @param s, a string
    # @return a list of lists of string
    def longestPalindrome(self, s):
        dp = [[False]*len(s) for i in range(len(s))]
        res = start = end = 0
        for i in range(len(s)):
            for j in range(i, -1, -1):
                if i == j:
                    dp[i][j] = True
                elif j+1 == i and s[j] == s[i]:
                    dp[i][j] = True
                elif dp[i-1][j+1] and s[j] == s[i]:
                    dp[i][j] = True
                if dp[i][j]:
                    if i-j+1 > res:
                        res = i-j+1
                        start = j
                        end = i

        return s[start:end+1]


#TLE
class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        matrix=[ [False for i in range(len(s)) ] for j in range(len(s))]
        maxlen=0
        res=""
        for i in range(len(s)-1,-1,-1):
            for j in range(i,len(s)):
                if (j<=i+1 or matrix[i+1][j-1]) and s[i]==s[j]:
                    matrix[i][j]=True
                if j-i+1>maxlen:
                    maxlen=j-i+1
                    res=s[i:(j+1)]
        return res

class Solution:
    def check(self,s,l,r):
        while 0<=l and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1
        return s[(l+1):r]
    
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        i=j=(len(s)-1)/2
        longest=""
        
        while i>=0 and j<len(s):
            args=[(s,i,i),(s,i,i+1),(s,j,j),(s,j,j+1)]
            for arg in args:
                tmpres=self.check(*arg)
                if len(tmpres)>len(longest):
                    longest=tmpres 
            
            if len(longest)>=2*i:
                return longest 
            i,j=i-1,j+1
        return longest



class Solution:
    def check(self,s,l,r):
        while 0<=l and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1
        return s[(l+1):r]
     
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        i=j=(len(s)-1)/2
        longest=""
         
        while i>=0 and j<len(s):
            args=[(s,i,i),(s,i,i+1),(s,j,j),(s,j,j+1)]
            for arg in args:
                tmpres=self.check(*arg)
                if len(tmpres)>len(longest):
                    longest=tmpres 
             
            if len(longest)>=2*i:
                return longest 
            i,j=i-1,j+1
        return longest
#  
#          
class Solution:
    def doublecheck(self,idx,s,res):
        lens=2
        left=idx-2
        right=idx+1
        while left>=0 and right<len(s):
            if s[left]!=s[right]:
                break
            lens+=2
            left-=1
            right+=1
        if lens>self.maxlen:
            self.maxlen=lens
            return s[left+1:right]
        else:
            return res
         
    def check(self,idx,s,res):
        lens=1
        left=idx-1
        right=idx+1
        while left>=0 and right<len(s):
            if s[left]!=s[right]:
                break
            lens+=2
            left-=1
            right+=1
        if lens>self.maxlen:
            self.maxlen=lens
            return s[left+1:right]
        else:
            return res
         
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        self.maxlen=0
        i=0
        res=""
        while i<len(s):
            res=self.check(i,s,res)
            if i>0 and s[i]==s[i-1]:
                res=self.doublecheck(i,s,res)
            i+=1
        return res
    
if __name__=="__main__":
    a=Solution()
    print a.longestPalindrome("bb")
    print a.longestPalindrome("abaccd123456")
    print a.longestPalindrome("gphyvqruxjmwhonjjrgumxjhfyupajxbjgthzdvrdqmdouuukeaxhjumkmmhdglqrrohydrmbvtuwstgkobyzjjtdtjroqpyusfsbjlusekghtfbdctvgmqzeybnwzlhdnhwzptgkzmujfldoiejmvxnorvbiubfflygrkedyirienybosqzrkbpcfidvkkafftgzwrcitqizelhfsruwmtrgaocjcyxdkovtdennrkmxwpdsxpxuarhgusizmwakrmhdwcgvfljhzcskclgrvvbrkesojyhofwqiwhiupujmkcvlywjtmbncurxxmpdskupyvvweuhbsnanzfioirecfxvmgcpwrpmbhmkdtckhvbxnsbcifhqwjjczfokovpqyjmbywtpaqcfjowxnmtirdsfeujyogbzjnjcmqyzciwjqxxgrxblvqbutqittroqadqlsdzihngpfpjovbkpeveidjpfjktavvwurqrgqdomiibfgqxwybcyovysydxyyymmiuwovnevzsjisdwgkcbsookbarezbhnwyqthcvzyodbcwjptvigcphawzxouixhbpezzirbhvomqhxkfdbokblqmrhhioyqubpyqhjrnwhjxsrodtblqxkhezubprqftrqcyrzwywqrgockioqdmzuqjkpmsyohtlcnesbgzqhkalwixfcgyeqdzhnnlzawrdgskurcxfbekbspupbduxqxjeczpmdvssikbivjhinaopbabrmvscthvoqqbkgekcgyrelxkwoawpbrcbszelnxlyikbulgmlwyffurimlfxurjsbzgddxbgqpcdsuutfiivjbyqzhprdqhahpgenjkbiukurvdwapuewrbehczrtswubthodv")
    print a.longestPalindrome("esbtzjaaijqkgmtaajpsdfiqtvxsgfvijpxrvxgfumsuprzlyvhclgkhccmcnquukivlpnjlfteljvykbddtrpmxzcrdqinsnlsteonhcegtkoszzonkwjevlasgjlcquzuhdmmkhfniozhuphcfkeobturbuoefhmtgcvhlsezvkpgfebbdbhiuwdcftenihseorykdguoqotqyscwymtjejpdzqepjkadtftzwebxwyuqwyeegwxhroaaymusddwnjkvsvrwwsmolmidoybsotaqufhepinkkxicvzrgbgsarmizugbvtzfxghkhthzpuetufqvigmyhmlsgfaaqmmlblxbqxpluhaawqkdluwfirfngbhdkjjyfsxglsnakskcbsyafqpwmwmoxjwlhjduayqyzmpkmrjhbqyhongfdxmuwaqgjkcpatgbrqdllbzodnrifvhcfvgbixbwywanivsdjnbrgskyifgvksadvgzzzuogzcukskjxbohofdimkmyqypyuexypwnjlrfpbtkqyngvxjcwvngmilgwbpcsseoywetatfjijsbcekaixvqreelnlmdonknmxerjjhvmqiztsgjkijjtcyetuygqgsikxctvpxrqtuhxreidhwcklkkjayvqdzqqapgdqaapefzjfngdvjsiiivnkfimqkkucltgavwlakcfyhnpgmqxgfyjziliyqhugphhjtlllgtlcsibfdktzhcfuallqlonbsgyyvvyarvaxmchtyrtkgekkmhejwvsuumhcfcyncgeqtltfmhtlsfswaqpmwpjwgvksvazhwyrzwhyjjdbphhjcmurdcgtbvpkhbkpirhysrpcrntetacyfvgjivhaxgpqhbjahruuejdmaghoaquhiafjqaionbrjbjksxaezosxqmncejjptcksnoq")
    print a.longestPalindrome("miycvxmqggnmmcwlmizfojwrurwhwygwfykyefxbgveixykdebenzitqnciigfjgrzzbtgeazyrbiirmejhdwcgjzwqolrturjlqpsgunuqerqjevbheblmbvgxyedxshswsokbhzapfuojgyfhctlaifrisgzqlczageirnukgnmnbwogknyyuynwsuwbumdmoqwxprykmazghcpmkdcjduepjmjdxrhvixxbfvhybjdpvwjbarmbqypsylgtzyuiqkexgvirzylydrhrmuwpmfkvqllqvekyojoacvyrzjevaupypfrdguhukzuqojolvycgpjaendfetkgtojepelhcltorueawwjpltehbbjrvznxhahtuaeuairvuklctuhcyzomwrrznrcqmovanxmiyilefybkbveesrxkmqrqkowyrimuejqtikcjfhizsmumajbqglxrvevexnleflocxoqgoyrzgqflwiknntdcykuvdcpzlakljidclhkllftxpinpvbngtexngdtntunzgahuvfnqjedcafzouopiixw")