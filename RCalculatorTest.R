# Program make a simple calculator
# that can add, subtract, multiply
# and divide using functions

cat("\014")

add <- function(x, y) {
  return(x + y)
}

subtract <- function(x, y) {
  return(x - y)
}

multiply <- function(x, y) {
  return(x * y)
}

divide <- function(x,y) {
  if(y == 0){
    return ("Cannot Divide By zero")
  } else {
    return(x/y)
  }
}

squareroot <- function(x) {
  if(x < 0){
    return ("Cannot get square root of negative number")
  } else {
    return(sqrt(x))
  }
}


square <-function(x) {
  return (x*x)
}

getfactorial <- function(num) {
  if (num < 0) {
    print ("Sorry, factorial does not exist for negative numbers")
  } else if (num ==0){
    print ("The factorial of 0 is 1")
  } else if (num %% 1!=0) {print ("Input must be an integer")
  } else {
    factorial = 1
    for(i in 1:num) {
      factorial = factorial * i
    }
    return (factorial)
  }
}


cosine <- function(x) {
  return(cos(x*pi/180))
}

sine <- function(x) {
  return(sin(x*pi/180))
}

tangent <- function(x) {
  if(x %% 180 ==0){
    return (0)
  } else if(x%% 90 ==0){
    return ("Cannot get Tan of 90 or multiples of 90 that are not multiples of 180")
  } else {
    return (tan(x*pi/180))
  }
}


#############################################################################################
add(1,3)
add(-4,6)
add(-6,-6)
subtract(1,3)
subtract(-4,-6)
subtract(-5,8)
multiply(-3,0)
multiply(6,4)
multiply(-8,-2)
divide(2,3)
divide(1,0)
divide(10,-2)
squareroot(100)
squareroot(-36)
squareroot(0)
square(-3)
square(2.4)
square(5)
sine(30)
sine(390)
sine(-45)
cosine(0)
cosine(45)
cosine(180)
tangent(45)
tangent(90)
tangent(180)
getfactorial(4)
getfactorial(15)
getfactorial(-3)
getfactorial(2.2)
