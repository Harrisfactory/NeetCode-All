class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        if len(tokens) == 1:
            return int(tokens[0])
        
        operand_stack = []

        operators = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv }

        final_result = 0

        #attempted rules:
            #if operand found, 
                #pop last two operands and execute, then append result to stack
            #else:
                #tokens[i] is operand, append to operand stack

        for i in range(len(tokens)):
            if tokens[i] in operators:
                val_1 = int(operand_stack.pop())
                val_2 = int(operand_stack.pop())
                result = operators[tokens[i]](val_2,val_1)
                operand_stack.append(result)
                
            else:
                operand_stack.append(tokens[i])
        
        return int(operand_stack.pop())


        #runtime: O(n) cycles through tokens 1 time