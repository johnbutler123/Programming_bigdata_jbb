#John Butler 10353776
# Program make a simple calculator
# that can add, subtract, multiply and divide two numbers
# and calculate the sine, cosine and tan of an angle
# and claculate the square root, square and factorial of a number
rm(list=ls()) 



#####Simple Calculation functions that require two inputs
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


####Calculation functions that require two inputs
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


#####Trignometric functions that require input angle in degrees
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


####Functions that support procesing of user inputs
process_two_numbers<-function(num1,num2,choice) {
  num1 = as.numeric(readline(prompt="Enter first number: "))  
  num2 = as.numeric(readline(prompt="Enter second number: "))
  operator <- switch(choice,"+","-","*","/")
  result <- switch(choice, add(num1, num2), subtract(num1, num2), multiply(num1, num2), divide(num1, num2))
  print(paste(num1, operator, num2, "=", result))
}

process_degrees<-function(uinput,choice) {
  uinput = as.numeric(readline(prompt="Enter input angle in degrees: "))
  operator <- switch(choice-4,"Sine","Cosine","Tan")
  result <- switch(choice-4, sine(uinput), cosine(uinput), tangent(uinput))
  print(paste(operator, uinput, "=", result))
}

process_one_number<-function(uinput,choice) {
  uinput = as.numeric(readline(prompt="Enter input number: "))
  operator <- switch(choice-7,"SquareRoot","Square","Factorial")
  result <- switch(choice-7, squareroot(uinput), square(uinput), getfactorial(uinput))
  print(paste(operator, uinput, "=", result))
}

########### USER INTERFACE ########

# take input from the user
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Sine")
print("6.Cosine")
print("7.Tan")
print("8.SquareRoot")
print("9.Square")
print("10.Factorial")

####Create loop to ensure user can perform multiple calculations before deciding to exit
loop <- TRUE
while (loop) {
choice = as.integer(readline(prompt="Enter choice[1/2/3/4/5/6/7/8/9/10]: "))

###Processing of inputs
if(choice<=4) {
  process_two_numbers(num1,num2,choice)
} else if(choice<= 7) {
  process_degrees(uinput,choice)
} else if(choice<= 10) {
  process_one_number(uinput,choice)
} else {print ("invalid number")}
ask = readline(prompt = "Type 'c' to continue or any other key to quit")
if (ask != "c")
  {print ("Goodbye")
  loop <- FALSE}
else {
  print("Select operation.")
  print("1.Add")
  print("2.Subtract")
  print("3.Multiply")
  print("4.Divide")
  print("5.Sine")
  print("6.Cosine")
  print("7.Tan")
  print("8.SquareRoot")
  print("9.Square")
  print("10.Factorial")
}
  }



