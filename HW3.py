# HW3
#Due Date: 03/13/2021, 11:59PM

"""                                   
### Collaboration Statement:
             
"""

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                          

#=============================================== Part I ==============================================

class Stack:
    '''
        >>> x=Stack()
        >>> x.pop()
        >>> x.push(2)
        >>> x.push(4)
        >>> x.push(6)
        >>> x
        Top:Node(6)
        Stack:
        6
        4
        2
        >>> x.pop()
        6
        >>> x
        Top:Node(4)
        Stack:
        4
        2
        >>> len(x)
        2
        >>> x.peek()
        4
    '''
    def __init__(self):
        self.top = None
    
    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__


    def isEmpty(self):
        # YOUR CODE STARTS HERE
        if self.top == None:
            return True
        else:
            return False

    def __len__(self): 
        # YOUR CODE STARTS HERE
        if self.isEmpty() == True:
            return 0
        else:
            current = self.top
            length = 0
            while current:
                length += 1
                current = current.next
            return length

    def push(self,value):
        # YOUR CODE STARTS HERE
        newNode = Node(value)
        if self.isEmpty() == True:
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode

     
    def pop(self):
        # YOUR CODE STARTS HERE
        if self.isEmpty() == True:
            return None
        else:
            top = self.top.value
            self.top = self.top.next
            return top


    def peek(self):
        # YOUR CODE STARTS HERE
        return self.top.value


#=============================================== Part II ==============================================

class Calculator:
    def __init__(self):
        self.__expr = None


    @property
    def getExpr(self):
        return self.__expr

    def setExpr(self, new_expr):
        if isinstance(new_expr, str):
            self.__expr=new_expr
        else:
            print('setExpr error: Invalid expression')
            return None

    def _isNumber(self, txt):
        '''
            >>> x=Calculator()
            >>> x._isNumber(' 2.560 ')
            True
            >>> x._isNumber('7 56')
            False
            >>> x._isNumber('2.56p')
            False
        '''
        # YOUR CODE STARTS HERE
        try:
            float(txt)
            return True
        except: 
            return False



    def _getPostfix(self, txt):
        '''
            Required: _getPostfix must create and use a Stack for expression processing
            >>> x=Calculator()
            >>> x._getPostfix('2 ^ 4')
            '2.0 4.0 ^'
            >>> x._getPostfix('2')
            '2.0'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4.45')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.45 +'
            >>> x._getPostfix('2 * 5.34 + 3 ^ 2 + 1 + 4')
            '2.0 5.34 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('( 2.5 )')
            '2.5'
            >>> x._getPostfix ('( ( 2 ) )')
            '2.0'
            >>> x._getPostfix ('2 * ( ( 5 + -3 ) ^ 2 + ( 1 + 4 ) )')
            '2.0 5.0 -3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('( 2 * ( ( 5 + 3 ) ^ 2 + ( 1 + 4 ) ) )')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix('2 * ( -5 + 3 ) ^ 2 + ( 1 + 4 )')
            '2.0 -5.0 3.0 + 2.0 ^ * 1.0 4.0 + +'

            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            # If you are veryfing the expression in calculate before passing to postfix, this cases are not necessary

            >>> x._getPostfix('2 * 5 + 3 ^ + -2 + 1 + 4')
            >>> x._getPostfix('2 * 5 + 3 ^ - 2 + 1 + 4')
            >>> x._getPostfix('2    5')
            >>> x._getPostfix('25 +')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^ 2 + ( 1 + 4 ')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^ 2 + ) 1 + 4 (')
            >>> x._getPostfix('2 * 5% + 3 ^ + -2 + 1 + 4')
        '''

        # YOUR CODE STARTS HERE
        postfixStack = Stack()  # method must use postfixStack to compute the postfix expression
        postfix = []
        txtlist = txt.split()
        precedence = {'(':0, ')': 0, '+':1, '-':1, '*':2, '/':2, '^':3} 
        operatorlist = ['+', '-', '*', '/', '^']
        floatcount = 0
        opcount = 0
        for char in txtlist:
            if self._isNumber(char):
                floatcount += 1
            elif char in operatorlist:
                opcount += 1
            elif char not in precedence:
                return None
        if opcount >= floatcount:
            return None
        elif opcount == 0 and floatcount > 1:
            return None
        elif opcount < (floatcount -1) and floatcount > 1:
            return None
        else: 
            for char in txtlist:
                if self._isNumber(char):
                    postfix.append(float(char))
                elif postfixStack.isEmpty() or char == '(' or char == '^':
                    postfixStack.push(char)
                elif char == ')':
                    current = postfixStack.top
                    while current != None and current.value != '(': #the purpose of this while loop is to make sure that parantheses are balanced by checking if there is already a left parantheses established before the right is called.
                        current = current.next
                    if current == None:
                        return None 
                    elif postfixStack.peek() != '(':
                        while postfixStack.peek() != '(':
                            operand = postfixStack.pop()
                            postfix.append(operand)
                        postfixStack.pop()
                    else:
                        postfixStack.pop()
                else:
                    if (precedence[char] > precedence[postfixStack.peek()]) or (postfixStack.isEmpty()):
                        postfixStack.push(char)
                    elif precedence[char] <= precedence[postfixStack.peek()]:
                        while postfixStack.isEmpty() == False and precedence[char] <= precedence[postfixStack.peek()]:
                            operand = postfixStack.pop()
                            postfix.append(operand)
                        postfixStack.push(char)
            current = postfixStack.top
            while current:
                if current.value == '(': # there would only be a parantheses in the stack left after the loop if there was never a right parantheses called after a left. 
                    return None
                postfix.append(postfixStack.pop())
                current = current.next
            return ' '.join(map(str, postfix))






    @property
    def calculate(self):
        '''
            Required: calculate must call postfix
                      calculate must create and use a Stack to compute the final result as shown in the video lecture
            >>> x=Calculator()
            >>> x.setExpr('4 + 3 - 2')
            >>> x.calculate
            5.0
            >>> x.setExpr('-2 + 3.5')
            >>> x.calculate
            1.5
            >>> x.setExpr('4 + 3.65 - 2 / 2')
            >>> x.calculate
            6.65
            >>> x.setExpr('23 / 12 - 223 + 5.25 * 4 * 3423')
            >>> x.calculate
            71661.91666666667
            >>> x.setExpr(' 2 - 3 * 4')
            >>> x.calculate
            -10.0
            >>> x.setExpr('7 ^ 2 ^ 3')
            >>> x.calculate
            5764801.0
            >>>  
            >>> x.calculate
            12.0
            >>> x.setExpr('8 / 4 * ( 3 - 2.45 * ( 4 - 2 ^ 3 ) ) + 3')
            >>> x.calculate
            28.6
            >>> x.setExpr('2 * ( 4 + 2 * ( 5 - 3 ^ 2 ) + 1 ) + 4')
            >>> x.calculate
            -2.0
            >>> x.setExpr(' 2.5 + 3 * ( 2 + ( 3.0 ) * ( 5 ^ 2 - 2 * 3 ^ ( 2 ) ) * ( 4 ) ) * ( 2 / 8 + 2 * ( 3 - 1 / 3 ) ) - 2 / 3 ^ 2')
            >>> x.calculate
            1442.7777777777778
            

            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            >>> x.setExpr(" 4 + + 3 + 2") 
            >>> x.calculate
            >>> x.setExpr("4  3 + 2")
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 * ( 2 - 3 * 2 ) )')
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 * / ( 2 - 3 * 2 )')
            >>> x.calculate
            >>> x.setExpr(' ) 2 ( * 10 - 3 * ( 2 - 3 * 2 ) ')
            >>> x.calculate

            # For extra credit only. If not attemped, these cases must return None
            >>> x.setExpr('( 3.5 ) ( 15 )') 
            >>> x.calculate
            52.5
            >>> x.setExpr('3 ( 5 ) - 15 + 85 ( 12 )') 
            >>> x.calculate
            1020.0
            >>> x.setExpr("( -2 / 6 ) + ( 5 ( ( 9.4 ) ) )") 
            >>> x.calculate
            46.666666666666664
        '''

        if not isinstance(self.__expr,str) or len(self.__expr)<=0:
            print("Argument error in calculate")
            return None

        calcStack = Stack()   # method must use calcStack to compute the  expression

        # YOUR CODE STARTS HERE
        if self._getPostfix(self.__expr) == None:
            return 
        postfix = self._getPostfix(self.__expr)
        operatorslist = ['^', '*', '/', '+', '-']
        postfixlist = postfix.split()
        for char in postfixlist:
            if self._isNumber(char) == True:
                calcStack.push(char)
            else:
                poppednumbers = []
                poppednumbers.append(float(calcStack.pop()))
                poppednumbers.append(float(calcStack.pop()))
                if char == '^':
                    newnumber = poppednumbers[1]**poppednumbers[0]
                elif char == '*':
                    newnumber = poppednumbers[1]*poppednumbers[0]
                elif char == '/':
                    newnumber = poppednumbers[1]/poppednumbers[0]
                elif char == '+':
                    newnumber = poppednumbers[1]+poppednumbers[0]
                elif char == '-':
                    newnumber = poppednumbers[1]-poppednumbers[0]
                calcStack.push(newnumber)

        return calcStack.peek()





#=============================================== Part III ==============================================

class AdvancedCalculator:
    '''
        >>> C = AdvancedCalculator()
        >>> C.states == {}
        True
        >>> C.setExpression('a = 5;b = 7 + a;a = 7;c = a + b;c = a * 0;return c')
        >>> C.calculateExpressions() == {'a = 5': {'a': 5.0}, 'b = 7 + a': {'a': 5.0, 'b': 12.0}, 'a = 7': {'a': 7.0, 'b': 12.0}, 'c = a + b': {'a': 7.0, 'b': 12.0, 'c': 19.0}, 'c = a * 0': {'a': 7.0, 'b': 12.0, 'c': 0.0}, '_return_': 0.0}
        True
        >>> C.states == {'a': 7.0, 'b': 12.0, 'c': 0.0}
        True
        >>> C.setExpression('x1 = 5;x2 = 7 * ( x1 - 1 );x1 = x2 - x1;return x2 + x1 ^ 3')
        >>> C.states == {}
        True
        >>> C.calculateExpressions() == {'x1 = 5': {'x1': 5.0}, 'x2 = 7 * ( x1 - 1 )': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        True
        >>> print(C.calculateExpressions())
        {'x1 = 5': {'x1': 5.0}, 'x2 = 7 * ( x1 - 1 )': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        >>> C.states == {'x1': 23.0, 'x2': 28.0}
        True
        >>> C.setExpression('x1 = 5 * 5 + 97;x2 = 7 * ( x1 / 2 );x1 = x2 * 7 / x1;return x1 * ( x2 - 5 )')
        >>> C.calculateExpressions() == {'x1 = 5 * 5 + 97': {'x1': 122.0}, 'x2 = 7 * ( x1 / 2 )': {'x1': 122.0, 'x2': 427.0}, 'x1 = x2 * 7 / x1': {'x1': 24.5, 'x2': 427.0}, '_return_': 10339.0}
        True
        >>> C.states == {'x1': 24.5, 'x2': 427.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;C = A + B;A = 20;D = A + B + C;return D - A')
        >>> C.calculateExpressions() == {'A = 1': {'A': 1.0}, 'B = A + 9': {'A': 1.0, 'B': 10.0}, 'C = A + B': {'A': 1.0, 'B': 10.0, 'C': 11.0}, 'A = 20': {'A': 20.0, 'B': 10.0, 'C': 11.0}, 'D = A + B + C': {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}, '_return_': 21.0}
        True
        >>> C.states == {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;2C = A + B;A = 20;D = A + B + C;return D + A')
        >>> C.calculateExpressions() is None
        True
        >>> C.states == {}
        True
    '''
    def __init__(self):
        self.expressions = ''
        self.states = {}

    def setExpression(self, expression):
        self.expressions = expression
        self.states = {}

    def _isVariable(self, word):
        '''
            >>> C = AdvancedCalculator()
            >>> C._isVariable('volume')
            True
            >>> C._isVariable('4volume')
            False
            >>> C._isVariable('volume2')
            True
            >>> C._isVariable('vol%2')
            False
        '''
        # YOUR CODE STARTS HERE
        firstLetter = word[0]
        if str.isalpha(firstLetter) == True and str.isalnum(word) == True:
            return True
        else:
            return False
       

    def _replaceVariables(self, expr):
        '''
            >>> C = AdvancedCalculator()
            >>> C.states = {'x1': 23.0, 'x2': 28.0}
            >>> C._replaceVariables('1')
            '1'
            >>> C._replaceVariables('105 + x')
            >>> C._replaceVariables('7 * ( x1 - 1 )')
            '7 * ( 23.0 - 1 )'
            >>> C._replaceVariables('x2 - x1')
            '28.0 - 23.0'
        '''
        # YOUR CODE STARTS HERE
        exprList = expr.split()
        index = 0
        exprVariables = []
        for char in exprList:
            if self._isVariable(char) == True:
                exprVariables.append(char)
        for char in exprVariables:
            if char not in self.states:
                return None
        for key in self.states:
            if key in exprList:
                variable = str(self.states[key])
                variableIndex = exprList.index(key)
                exprList[variableIndex] = variable
        return ' '.join(exprList)


    
    def calculateExpressions(self):
        self.states = {} 
        calcObj = Calculator()     # method must use calcObj to compute each expression
        # YOUR CODE STARTS HERE
        finalExpr = {}
        expressionlist = self.expressions.split(';')
        returnstatement = expressionlist[-1]
        expressionlist.remove(returnstatement) #removing the return statement and then doing it after the for loop
        for expression in expressionlist:
            sentenceExpr = expression.split(' = ')
            variable = sentenceExpr[0]
            expr = sentenceExpr[1]
            newExpr = self._replaceVariables(expr)
            if calcObj._isNumber(newExpr) == True:
                calcExpr = float(newExpr)
            else:
                calcObj.setExpr(newExpr)
                calcExpr = calcObj.calculate
            if self._isVariable(variable) == False: #checking if the variable is a valid variable
                return None
            self.states[variable] = calcExpr
            finalExpr[expression] = self.states.copy()
        splitreturnstatement = returnstatement.split()
        returnvariable = splitreturnstatement[1:]
        returnstr = ''
        for char in returnvariable:
            returnstr += char
            returnstr += ' '
        returnexpr = self._replaceVariables(returnstr)
        calcObj.setExpr(returnexpr)
        returnvalue = calcObj.calculate
        finalExpr['_return_'] = float(returnvalue)
        return finalExpr
