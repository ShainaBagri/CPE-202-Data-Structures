from stack_array import Stack

# You should not change this Exception class
class PostfixFormatException(Exception):
    pass

def postfix_eval(input_str):
    """Evaluates a postfix expression"""

    """Input argument:  a string containing a postfix expression where tokens 
    are space separated.  Tokens are either operators + - * / ** << >> or numbers (integers or floats)
    Returns the result of the expression evaluation. 
    Raises an PostfixFormatException if the input is not well-formed"""
    if input_str=="":
        raise PostfixFormatException("Insufficient operands")
    stack = Stack(30)
    arr = str.split(input_str)
    i = 0
    while i<len(arr):
        #checks if number
        try:
            stack.push(float(arr[i]))
        except:
            #checks if operator and performs operation
            if arr[i]=="+":
                if stack.size() < 2:
                    raise PostfixFormatException("Insufficient operands")
                int1 = stack.pop()
                int2 = stack.pop()
                stack.push(int1 + int2)
            elif arr[i]=="-":
                if stack.size() < 2:
                    raise PostfixFormatException("Insufficient operands")
                int1 = stack.pop()
                int2 = stack.pop()
                stack.push(int2 - int1)
            elif arr[i]=="**":
                if stack.size() < 2:
                    raise PostfixFormatException("Insufficient operands")
                int1 = stack.pop()
                int2 = stack.pop()
                stack.push(int2**int1)
            elif arr[i]=="*":
                if stack.size() < 2:
                    raise PostfixFormatException("Insufficient operands")
                int1 = stack.pop()
                int2 = stack.pop()
                stack.push(int1*int2)
            elif arr[i]=="/":
                if stack.size() < 2:
                    raise PostfixFormatException("Insufficient operands")
                int1 = stack.pop()
                int2 = stack.pop()
                if int1==0:
                    raise ValueError
                stack.push(int2/int1)
            elif arr[i]=="<<":
                if stack.size() < 2:
                    raise PostfixFormatException("Insufficient operands")
                int1 = stack.pop()
                int2 = stack.pop()
                try:
                    stack.push(int2<<int1)
                except:
                    raise PostfixFormatException("Invalid bitshift operation")
            elif arr[i]==">>":
                if stack.size() < 2:
                    raise PostfixFormatException("Insufficient operands")
                int1 = stack.pop()
                int2 = stack.pop()
                try:
                    stack.push(int2>>int1)
                except:
                    raise PostfixFormatException("Invalid bitshift operation")
            #entry is neither number nor operator, so is invalid
            else:
                raise PostfixFormatException("Invalid token")
        i += 1
    #checks if any leftover numbers
    if stack.size() > 1:
        raise PostfixFormatException("Too many operands")
    return stack.pop()


def infix_to_postfix(input_str):
    """Converts an infix expression to an equivalent postfix expression"""

    """Input argument:  a string containing an infix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** << >> or numbers (integers or floats)
    Returns a String containing a postfix expression """
    stack = Stack(30)
    arr = str.split(input_str)
    rpn = ""
    i = 0
    while i<len(arr):
        #checks if number
        try:
            float(arr[i])
            if rpn=="":
                rpn = arr[i]
            else:
                rpn = rpn + " " + arr[i]
        except:
            if arr[i]=="(":
                stack.push(arr[i])
            elif arr[i]==")":
                while stack.peek()!="(":
                    rpn = rpn + " " + stack.pop()
                stack.pop()
            #checks if operator
            elif arr[i]=="+" or arr[i]=="-" or arr[i]=="**" or arr[i]=="*" or arr[i]=="/" or arr[i]=="<<" or arr[i]==">>":
                if arr[i]=="**":
                    while not stack.is_empty() and (stack.peek()=="+" or stack.peek()=="-" or stack.peek()=="**" or stack.peek()=="*" or stack.peek()=="/" or stack.peek()=="<<" or stack.peek()==">>") and prec(arr[i])<prec(stack.peek()):
                        rpn = rpn + " " + stack.pop()
                else:
                    while not stack.is_empty() and (stack.peek()=="+" or stack.peek()=="-" or stack.peek()=="**" or stack.peek()=="*" or stack.peek()=="/" or stack.peek()=="<<" or stack.peek()==">>") and prec(arr[i])<=prec(stack.peek()):
                        rpn = rpn + " " + stack.pop()
                stack.push(arr[i])
        i += 1
    while not stack.is_empty():
        rpn = rpn + " " + stack.pop()
    return rpn

#determines precedence of operator
def prec (op):
    if op=="+" or op=="-":
        return 0
    elif op=="*" or op=="/":
        return 1
    elif op=="**":
        return 2
    elif op=="<<" or op==">>":
        return 3


def prefix_to_postfix(input_str):
    """Converts a prefix expression to an equivalent postfix expression"""
    """Input argument: a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** << >> or numbers (integers or floats)
    Returns a String containing a postfix expression(tokens are space separated)"""
    stack = Stack(30)
    arr = str.split(input_str)
    i = len(arr)-1
    while i>=0:
        #checks if number
        try:
            float(arr[i])
            stack.push(arr[i])
        except:
            #checks if operator
            if arr[i] == "+" or arr[i] == "-" or arr[i] == "**" or arr[i] == "*" or arr[i] == "/" or arr[i] == "<<" or arr[i] == ">>":
                int1 = stack.pop()
                int2 = stack.pop()
                temp = int1 + " " + int2 + " " + arr[i]
                stack.push(temp)
        i -= 1
    return stack.pop()



