class bt:
    def __init__(self, bt):
        self.bt = bt

    def isOperator(self,op):
        return op in "+-*/"
    
    def precedence(self, op):
        if op == '+' or op == '-':
            return 1
        if op == '*' or op == '/':
            return 2
        return 0 
    
    def applyOperation(self, a, b, op):
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a*b
        else:
            if b == 0:
                raise Exception("Nhập b != 0")
            return a/b
        
    def giaTri(self, queue):
        stack = []
        result = 0
        i = 0
        while i < len(queue):
            if not isinstance(queue[i], str):
                stack.append(queue[i])
            else:                                                                                                                                                                                                     
                b = stack.pop()
                a = stack.pop()
                result = self.applyOperation(a,b,queue[i])

                stack.append(result)
            i += 1
        return stack.pop()

    def hauTo(self):
        i = 0
        stack = []
        queue = []
        while i < len(self.bt):
            if self.bt[i].isdigit():
                tmp = ""
                while i < len(self.bt) and self.bt[i].isdigit():
                    tmp += self.bt[i]
                    i += 1
                queue.append(int(tmp))
                continue

            elif self.isOperator(self.bt[i]):
                while stack and self.precedence(stack[-1]) >= self.precedence(self.bt[i]):
                    queue.append(stack.pop())
                stack.append(self.bt[i])

            elif self.bt[i] == "(":
                stack.append(self.bt[i])

            elif self.bt[i] == ")":
                while stack and stack[-1] != "(":
                    queue.append(stack.pop())
                stack.pop()  #Xóa dấu "("

            i += 1  

        while stack:
            queue.append(stack.pop())

        return queue

    
bieuThuc = "8+2-6*3+1/3"
bieuThuc = bt(bieuThuc)
queue = bieuThuc.hauTo()
print("Giá trị của biểu thưc: ")
print(bieuThuc.giaTri(queue))
print("Biểu thức hậu tố: ")
print(queue)



                

