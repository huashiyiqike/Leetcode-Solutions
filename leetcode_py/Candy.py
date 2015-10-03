class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        lists = sorted(range(len(ratings)), cmp=lambda x, y: ratings[x]-ratings[y])
        res = [1] * len(ratings)
        for idx, item in enumerate(lists, start=1):
            if item > 0 and ratings[item] > ratings[item-1]:
                    res[item] = res[item-1] + 1
            if item < len(ratings)-1 and ratings[item] > ratings[item+1]:
                    res[item] = max(res[item], res[item+1] + 1)
        return sum(res)

# class Solution:
#     # @param ratings, a list of integer
#     # @return an integer
#     def candy(self, ratings):
#         pos=[1 for i in ratings]
#         neg=[1 for i in ratings]
#         for idx,item in enumerate(ratings):
#             if idx>0 and item>ratings[idx-1]:
#                 pos[idx]=1+pos[idx-1]
#         for i in range(len(ratings)-2,-1,-1):
#             if  ratings[i]>ratings[i+1]:
#                 neg[i]=1+neg[i+1]
#
#         print pos
#         print neg
#         return sum(map(lambda x,y:max(x,y),pos,neg ))
#
if __name__=="__main__":
    a=Solution()
    print a.candy([1,2,2])
    print a.candy([1,3,4,3,2,1])
    print a.candy([4,2,3,4,1])
    print a.candy([1,2,4,4,3])
    print a.candy([1,2,2])
    print a.candy([1,1,1])
    print a.candy([1,0,1])
    print a.candy([0,0,1])

    print a.candy([2,1,2])
    print a.candy([3,2,1])
