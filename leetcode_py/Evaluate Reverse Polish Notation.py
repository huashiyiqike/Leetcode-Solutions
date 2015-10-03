class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        list=[]
        for i in tokens:
            if i not in set(["+","-","*","/"]):
                list.append(int(i))
            else:
                if i=="+":
                    list[-2]=list[-1]+list[-2]
                elif i=="-":
                    list[-2]=list[-2]-list[-1]
                elif i=="*":
                    list[-2]=list[-1]*list[-2]
                elif i=="/":
                    list[-2]=int(list[-2]*1.0/list[-1] )  # convert for python negative div
                list.pop()
        assert(len(list)==1)        
        return list[0]        

if __name__=='__main__':
    	a=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]  
    	tmp=Solution()
    	print tmp.evalRPN(a)
#import operator
class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        list ,operators=[],{"+":operator.add,"-":operator.sub,"*":operator.mul,"/":operator.div}
        for item in tokens:
            if item not in operators:
                list.append(int(item))
            else:
                x,y=list.pop(),list.pop()
                list.append(int(operators[item](y*1.0,x)))
        return list.pop()
