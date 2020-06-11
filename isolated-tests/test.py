from realQuadratic import realQuadratic

# Zero A
# Should print "Error: Cannot divide by zero."
def zeroA():
    print('Zero A')
    content = realQuadratic(0, 0, 0).solution(1)
    if content == "Error: Cannot divide by zero.":
        print(content)
        print('PASS')
        print('---------------------------------------')
        assert True
    else:
        print(content)
        print('FAIL')
        print('---------------------------------------')
        assert False

# Real Solutions
# Should print -5.0 & 0.0
def realSolutions():
    print('Real Solutions')
    equation = realQuadratic(1, 5, 0)
    if (equation.solution(1) == -5.0) and (equation.solution(2) == 0.0):
        print(equation.solution(1))
        print(equation.solution(2))
        print('PASS')
        print('---------------------------------------')
        assert True
    else:
        print(equation.solution(1))
        print(equation.solution(2))
        print('FAIL')
        print('---------------------------------------')
        assert False

# Complex Solutions
# Should print two complex solutions
def complexSolutions():
    print('Complex Solutions')
    equation = realQuadratic(5, -4, 6)
    if (equation.solution(1) == 0.39999999999999997-1.0198039027185568j) and (equation.solution(2) == 0.4000000000000001+1.0198039027185568j):
        print(equation.solution(1))
        print(equation.solution(2))
        print('PASS')
        print('---------------------------------------')
        assert True
    else:
        print(equation.solution(1))
        print(equation.solution(2))
        print('FAIL')
        print('---------------------------------------')
        assert False

# Complex Variables
# Should print two complex solutions
def complexVariables():
    print('Complex Variables')
    equation = realQuadratic(1j, 1j, 1j)
    if (equation.solution(1) == -0.5+0.8660254037844386j) and (equation.solution(2) == -0.5-0.8660254037844386j):
        print(equation.solution(1))
        print(equation.solution(2))
        print('PASS')
        print('---------------------------------------')
        assert True
    else:
        print(equation.solution(1))
        print(equation.solution(2))
        print('FAIL')
        print('---------------------------------------')
        assert False

# Execute functions
zeroA()
realSolutions()
complexSolutions()
complexVariables()
