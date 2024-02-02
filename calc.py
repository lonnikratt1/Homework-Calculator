print("welcome to Leon's calculator!")
def calculator():
  myvar = input("Enter addition, subtraction, multiplication, division, exponent, root, percent, slope, y=mx+b, pythagora's theorem, point-slope, fraction-decimal, decimal-fraction:")
  if myvar == "addition":
      myvariable = input("Enter a number:")
      myvariable2 = input("Enter another number:")
      print(int(myvariable) + int(myvariable2))
  if myvar == "subtraction":
      myvariable = input("Enter a number:")
      myvariable2 = input("Enter another number:")
      print(int(myvariable) - int(myvariable2))
  if myvar == "multiplication":
      myvariable = input("Enter a number:")
      myvariable2 = input("Enter another number:")
      print(int(myvariable) * int(myvariable2))
  if myvar == "division":
      myvariable = input("Enter a number:")
      myvariable2 = input("Enter another number:")
      print(int(myvariable) / int(myvariable2))
  if myvar == "exponent":
      myvariable = input("Enter a number:")
      myvariable2 = input("Enter an exponent:")
      print(int(myvariable)**int(myvariable2))
  if myvar == "pythagora's theorem":
    a = input("Enter a:")
    b = input("Enter b:")
    c = ((int(a)**2 + int(b)**2))**0.5
    print("{}".format(c))
  if myvar == "chunkeemunkee":
      print("Yay! you found the secret code!")
      print("Here is a secret link")
      print("https://www.youtube.com/watch?v=dQw4w9WgXcQ&pp=ygUHcmlja3Jvbw%3D%3D")
  if myvar == "root":
      myvariable = input("Enter a number:")
      myvariable2 = input("Enter a root:")
      print(int(myvariable) ** (1/int(myvariable2)))
  if myvar == "percent":
      myvariable = input("Enter a number:")
      myvariable2 = input("Enter a percent:")
      print(int(myvariable) * (int(myvariable2) / 100))
  if myvar == "slope":
      myvariable = input("Enter x1:")
      myvariable2 = input("Enter y1:")
      myvariable3 = input("Enter x2:")
      myvariable4 = input("Enter y2:")
      print((int(myvariable4) - int(myvariable2)) / (int(myvariable3) - int(myvariable)))
  if myvar == "y=mx+b":
      x1 = input("Enter x1:")
      y1 = input("Enter y1:")
      x2 = input("Enter x2:")
      y2 = input("Enter y2:")
      m = (int(y2) - int(y1)) / (int(x2) - int(x1))
      b = (- int(x1)) * m + int(y1)
      print("Your equation is: y={}x+{}".format(m, b))
  if myvar == "point-slope":
      myvariable = input("Enter x:")
      myvariable2 = input("Enter y:")
      myvariable3 = input("Enter slope:")
      m = int(myvariable3)
      int(myvariable2)
      int(myvariable)
      print("Your equation is: y-{}={}(x-{})".format(myvariable2, m, myvariable))
  if myvar == "fraction-decimal":
      numerator = input("Enter numerator:")
      denominator = input("Enter denominator:")
      print(int(numerator) / int(denominator))
  if myvar == "decimal-fraction":
      from fractions import Fraction
      def decimal_to_fraction(decimal):
          fraction = Fraction(decimal).limit_denominator()
          return fraction
        # Get user input for the decimal
      decimal_input = float(input("Enter a decimal: "))
 # Convert the decimal to a fraction
      result_fraction = decimal_to_fraction(decimal_input)
 # Display the result
      print(f"Your fraction is: {result_fraction}")
# y-intercept=-x*m+y
  if myvar == "bug":
    x = (0)
    y = (0)
    bug2 = int(x) / int(y)
    bug3 = bug2 / bug2
    bug4 = bug3 / bug3
    bug5 = bug4 / bug4
    print("{}{}{}{}".format(bug5, bug4, bug3, bug2, bug2))
    
calculator()
myvar2 = input("Would you like to use the calculator again? yes/no:")
while myvar2 == "yes":
    print("Okay!")   
    calculator()
    # y-intercept=-x*m+y
    myvar2 = input("Would you like to use the calculator again? yes/no:")
if myvar2 == "no":
    print("Okay!")
    print("Powering down...")
    print("Power off. Have a nice day!")
calculator()
