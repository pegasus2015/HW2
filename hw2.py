#!/usr/bin/env python3
lower_bound        = float(input("Enter lower bound "))
upper_bound        = float(input("Enter upper bound "))
number_of_polygons = int(input("Number of polygons "))

# Function to integrate
def F(x):
    return 3 * (x * x)        

def F_integral(a, b):
   return ((b * b * b) - (a * a * a))
   
def Approximate_area(lower_bound, upper_bound, number_of_polygons):    
    delta_x = (upper_bound - lower_bound) / number_of_polygons    
    #print("Delta x is: " + str(delta_x))
    sum = 0
    approx_area = 0
    y = []    
    x = lower_bound
    y.append(F(x))
    #print ("x first point: " + str(x))
    while(x < upper_bound):
        x = x + delta_x
        if (x < upper_bound):
            #print("x point: " + str(x))
            y.append(F(x))        
    
    x = upper_bound
    #print ("x point last: " + str(x))
    y.append(F(x))
        
    # Sum the y values
    for n in y:
       if (n == y[0] or n == y[len(y) - 1]):
          sum = sum + n        
       else:
          sum = sum + (2 * n)
          
    # Approximate the area using the Trapezoidal Rule
    approx_area = (delta_x / 2) * sum
    
    return approx_area

approx = Approximate_area(lower_bound, upper_bound, number_of_polygons)
truevalue = F_integral(lower_bound, upper_bound)
error = (approx - truevalue) / truevalue

#print ("lower bound: " + str(lower_bound))
#print("upper bound: " + str(upper_bound))
print ("approximate area  is: " + str(approx))
print ("exact integral value: " + str(truevalue))
print ("error value: " + str(error))    
