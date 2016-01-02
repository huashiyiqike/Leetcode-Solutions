class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        if A > C:
            C, A = A, C
            B, D = D, B
        if E > G:
            E, G = G, E
            F, H = H, F

        res = (D - B) * (C - A) + (H - F) * (G - E)
        height = min(D, H) - max(B, F)
        width = min(C, G) - max(A, E)
        if height > 0 and width > 0:
            return res - height * width
        else:
            return res


class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        row = sorted([A, C, E, G])
        col = sorted([B, D, F, H])
        res = (D - B) * (C - A) + (H - F) * (G - E)
        if A >= G or B >= H or C <= E or D <= F:
            return res
        else:
            return res - (row[2] - row[1]) * (col[2] - col[1])
