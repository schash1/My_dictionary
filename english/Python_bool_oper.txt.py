Booleans represent one of two values: True or False.

Boolean Values
In programming you often need to know if an expression is True or False.

You can evaluate any expression in Python, and get one of two answers, True or False.

When you compare two values, the expression is evaluated and Python returns the Boolean answer:

Example
print(10 > 9)
print(10 == 9)
print(10 < 9)
When you run a condition in an if statement, Python returns True or False:

Example
Print a message based on whether the condition is True or False:

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
Evaluate Values and Variables
The bool() function allows you to evaluate any value, and give you True or False in return,

Example
Evaluate a string and a number:

print(bool("Hello"))
print(bool(15))
Example
Evaluate two variables:

x = "Hello"
y = 15

print(bool(x))
print(bool(y))
Most Values are True
Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.

Example
The following will return True:

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
Some Values are False
In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.

Example
The following will return False:

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:

Example
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))
Functions can Return a Boolean
You can create functions that returns a Boolean Value:

Example
Print the answer of a function:

def myFunction() :
  return True

print(myFunction())
You can execute code based on the Boolean answer of a function:

Example
Print "YES!" if the function returns True, otherwise print "NO!":

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:

Example
Check if an object is an integer or not:

x = 200
print(isinstance(x, int))
Test Yourself With Exercises
Exercise:
The statement below would print a Boolean value, which one?

print(10 > 9)



Start the Exercise
Python Operators
Python Operators
Operators are used to perform operations on variables and values.

In the example below, we use the + operator to add together two values:

Example
print(10 + 5)
Python divides the operators in the following groups:

Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators
Python Arithmetic Operators
Arithmetic operators are used with numeric values to perform common mathematical operations:

Operator	Name	Example	Try it
+	Addition	x + y
-	Subtraction	x - y
*	Multiplication	x * y
/	Division	x / y
%	Modulus	x % y
**	Exponentiation	x ** y
//	Floor division	x // y
Python Assignment Operators
Assignment operators are used to assign values to variables:

Operator	Example	Same As	Try it
=	x = 5	x = 5
+=	x += 3	x = x + 3
-=	x -= 3	x = x - 3
*=	x *= 3	x = x * 3
/=	x /= 3	x = x / 3
%=	x %= 3	x = x % 3
//=	x //= 3	x = x // 3
**=	x **= 3	x = x ** 3
&=	x &= 3	x = x & 3
|=	x |= 3	x = x | 3
^=	x ^= 3	x = x ^ 3
>>=	x >>= 3	x = x >> 3
<<=	x <<= 3	x = x << 3
Python Comparison Operators
Comparison operators are used to compare two values:

Operator	Name	Example	Try it
==	Equal	x == y
!=	Not equal	x != y
>	Greater than	x > y
<	Less than	x < y
>=	Greater than or equal to	x >= y
<=	Less than or equal to	x <= y
Python Logical Operators
Logical operators are used to combine conditional statements:

Operator	Description	Example	Try it
and 	Returns True if both statements are true	x < 5 and  x < 10
or	Returns True if one of the statements is true	x < 5 or x < 4
not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)
Python Identity Operators
Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

Operator	Description	Example	Try it
is 	Returns True if both variables are the same object	x is y
is not	Returns True if both variables are not the same object	x is not y
Python Membership Operators
Membership operators are used to test if a sequence is presented in an object:

Operator	Description	Example	Try it
in 	Returns True if a sequence with the specified value is present in the object	x in y
not in	Returns True if a sequence with the specified value is not present in the object	x not in y
Python Bitwise Operators
Bitwise operators are used to compare (binary) numbers:

Operator	Name	Description	Example	Try it
& 	AND	Sets each bit to 1 if both bits are 1	x & y
|	OR	Sets each bit to 1 if one of two bits is 1	x | y
^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y
~	NOT	Inverts all the bits	~x
<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2
>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2
Operator Precedence
Operator precedence describes the order in which operations are performed.

Example
Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first:

print((6 + 3) - (6 + 3))
Example
Multiplication * has higher precedence than addition +, and therefor multiplications are evaluated before additions:

print(100 + 5 * 3)
The precedence order is described in the table below, starting with the highest precedence at the top:

Operator	Description	Try it
()	Parentheses
**	Exponentiation
+x  -x  ~x	Unary plus, unary minus, and bitwise NOT
*  /  //  %	Multiplication, division, floor division, and modulus
+  -	Addition and subtraction
<<  >>	Bitwise left and right shifts
&	Bitwise AND
^	Bitwise XOR
|	Bitwise OR
==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators
not	Logical NOT
and	AND
or	OR
If two operators have the same precedence, the expression is evaluated from left to right.

Example
Addition + and subtraction - has the same precedence, and therefor we evaluate the expression from left to right:

print(5 + 4 - 7 + 3)
Test Yourself With Exercises
Exercise:
Multiply 10 with 5, and print the result.

print(10
 5)

Start the Exercise