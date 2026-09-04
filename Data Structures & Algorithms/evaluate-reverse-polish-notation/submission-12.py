class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers=[]
        symbols=[]
        cal=0
        def check_number(x):
            try:
                int(x)
                return True
            except:
                return False
        for i in tokens:
            if check_number(i):
                numbers.append(int(i))
            else:
                if len(numbers)>1:
                    a=int(numbers[len(numbers)-1])
                    b=int(numbers[len(numbers)-2])
                    if i=='+':
                        temp=b+a
                    elif i=='*':
                        temp=a*b
                    elif i=='-':
                        temp=b-a
                    else:
                        temp=int(b/a)
                    numbers=numbers[:len(numbers)-2]
                    numbers.append(temp)
            #print(numbers)
        #print(numbers)
        #print(numbers)
        return numbers[0]

        