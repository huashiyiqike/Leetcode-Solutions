<backquote><pre>
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
</backquote></pre>

Similar with Wildcard Matching, but eaiser. The cases are easy to think of.
Dynamic programming can also work but recursive call is easier to write. Just see the code.

<backquote><pre>
   def isMatch(self, s, p):
        if not s and not p:
            return True
        elif not p:
            return False
        if s and s[0] == p[0]:
            if len(p) > 1 and p[1] == '*':
                return self.isMatch(s, p[2:]) or self.isMatch(s[1:], p)
            else:
                return self.isMatch(s[1:], p[1:])
        if s and p[0] == '.':
            if len(p) > 1 and p[1] == '*':
                return self.isMatch(s, p[2:]) or self.isMatch(s[1:], p)
            else:
                return self.isMatch(s[1:], p[1:])
        if len(p) > 1 and p[1] == '*':
            return self.isMatch(s, p[2:])
        return False
</backquote></pre>