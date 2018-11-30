import time 

def showStack(stack):
    print('-----')
    for item in stack:
        print(item)
    print('-----')
    time.sleep(1)
    print()
    print()

def rpn(expr, debug=False):
    tokens = expr.split()
    stack = []
    for token in tokens:
        if token == '+':
            # What should the rpn calculator do when it encounters a +?
            op1 = stack.pop(0)
            op2 = stack.pop(0)
            result = op1 + op2
            stack.insert(0, result)
        elif token == '-':
            # What should the rpn calculator do when it encounters a -?
            pass
        elif token == '*':
            # What should the rpn calculator do when it encounters a *?
            pass
        elif token == '/':
            # What should the rpn calculator do when it encounters a /?
            pass
        else:
            # It is assumed that if it is not +,-,*, or / token is a number
            # so it converts the string token to a float
            stack.insert(0, float(token))
        if debug:
            showStack(stack)

    return stack[0]


print(rpn('3 4 +', debug=True))
