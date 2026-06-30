try:
    a=10
    b=0
    c=a/d
    print(c)
except Exception as e:
    print("Error :",e)

finally:
    print("I always run...")


# ZeroDivisionError: division by zero
# NameError: name 'w' is not defined
# TypeError: unsupported operand type(s) for /: 'int' and 'str'