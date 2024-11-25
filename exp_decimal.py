# Experimentation with the decimal module
import decimal

# Show how decimals have a precision of 28 decimal digits verses float's 18
float_division=4/3
decimal_devision=decimal.Decimal(4)/decimal.Decimal(3) 
print("Result for float division of 4 by 3:")
print(float_division)
print("Result for decimal division of 4 by 3:")
print(decimal_devision)

# Show how floating point values yield different results for different calculation due to approximation
x=1.2
y=2.2
z=3.4
a=x+y
print("x:",x)
print("y:",y)
print("z:",z)
print("x+y:",a)
print("x+y==z?:",a==z)

# Show how you can round numbers to certain digits using the round() function
num1=decimal.Decimal(4)
num2=decimal.Decimal(3)
print("First number is:",num1)
print("Second number is:",num2)
num3=num1/num2
print("num1 divided by num2 is:",num3)
num4=round(num3,2)
print("Rounded value upto two decimal points is:",num4)

# Show how comparing decimals is more precise than comparing floats
# Also shows how you can convert strings to decimals. If we convert a floating point number to decimal, the approximation error is propagated to the decimal number and we will not get the desired output.
x=decimal.Decimal("1.2")
y=decimal.Decimal("2.2")
z=decimal.Decimal("3.4")
a=x+y
print("x:",x)
print("y:",y)
print("z:",z)
print("x+y:",a)
print("x+y==z?:",a==z)

# Show predefined context for decimal and how to change it
print(decimal.getcontext())

decimal.getcontext().prec=3
print(decimal.getcontext())

decimal.getcontext().rounding="ROUND_HALF_DOWN"
print(decimal.getcontext())