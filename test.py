from realQuadratic import realQuadratic


# Real Solutions
# Should print -5.0 & 0.0
def realSolutions():
    print('Real Solutions')
    equation = realQuadratic(1, 5, 0)
    if (equation[0] == -5.0) and (equation[1] == 0.0):
        print(equation[0])
        print(equation[1])
        print('PASS')
        print("-" * 50)
        assert True
    else:
        print(equation[0])
        print(equation[1])
        print('FAIL')
        print("-" * 50)
        assert False


# Complex Solutions
# Should print two complex solutions
def complexSolutions():
    print('Complex Solutions')
    equation = realQuadratic(5, -4, 6)
    if (equation[0] == 0.39999999999999997 - 1.0198039027185568j) and (
            equation[1] == 0.4000000000000001 + 1.0198039027185568j):
        print(equation[0])
        print(equation[1])
        print('PASS')
        print("-" * 50)
        assert True
    else:
        print(equation[0])
        print(equation[1])
        print('FAIL')
        print("-" * 50)
        assert False


# Complex Variables
# Should print two complex solutions
def complexVariables():
    print('Complex Variables')
    equation = realQuadratic(1j, 1j, 1j)
    if (equation[0] == -0.5 + 0.8660254037844386j) and (equation[1] == -0.5 -
                                                        0.8660254037844386j):
        print(equation[0])
        print(equation[1])
        print('PASS')
        print("-" * 50)
        assert True
    else:
        print(equation[0])
        print(equation[1])
        print('FAIL')
        print("-" * 50)
        assert False


# Execute functions
realSolutions()
complexSolutions()
complexVariables()
