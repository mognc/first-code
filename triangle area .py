def area_triangle(base, height):
    '''
     (number1, number2) -> number
    return area of triangle by dividing the product of num1 and num2.
    >>>area_triangle = (5, 10)
    25.0
    >>>area_traingle = (10, 10)
    50.0
    '''
    return (base * height) * 1/2

def side3_triangle(side1, side2):
    '''
(number1 , number2) -> number
return 3rd side of a triangle which is c means hyponetese by pythagora's theorem which states a**2 + b**2 = c**2
>>> side3_triangle = (5, 5)
50
>>> side3_triangle(6, 6)
72
'''
    return (side1 ** 2 + side2 ** 2)

def side1_triangle(side3, side2):
    '''
(number1, number2) => number
return 1st side of a triangle which is A means base of a traingle by pythagora's theorem which state that a**2 = c**2 - b**2
>>> side1_triangle = (5, 5)
0
>>> side1_triangle = (6, 5)
11
'''
    return (side3 ** 2 - side2 ** 2)


def side2_triangle(side3, side1):
    '''
(number1, number2) -> number
return 2nd side of a triangle which is B means perpendicular of a triangle by pythagora's triangle which states that b**2 = c**2 - a**2
>>> side2_triangle = (5, 5)
0
>>> side2_triangle = (6, 5)
11
'''
    return (side3 ** 2 - side1 ** 2)


def perimeter_triangle(side1, side2, side3):
    '''
   (number1, number2, number3) -> number
 return the perimeter of a triangle by adding all three sides of a  triangle.
 >>>perimeter_triangle(5, 6, 7)
 18
 '''
    return (side1 + side2 + side3)

def sin_right_triangle(opposite, hypotenese):
    '''
(number1, number2) -> number
return the sin value of a right angle triangle by dividing opposite side by hypotenese.
>>>sin_right_triangle(30,6)
5
'''
    return(opposite/hypotenese)
def cos_right_triangle(adjecent,hypotenese):
    '''
(number1, number2) -> number
return the value of cos of right angle triangle by dividing adjecent side by hypotenese.
>>>cos_right_triangle(25,5)
5
'''
    return(adjecent/hypotenese)
def tan_right_triangle(opposite, adjacent):
    '''
(number1, number2) -> number
return the value of tan of right angle triangle by dividing opposite side by adjacent.
>>>tan_right_triangle(25,5)
5
'''
    return(opposite,adjacent)



