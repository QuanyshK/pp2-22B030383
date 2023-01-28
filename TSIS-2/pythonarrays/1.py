#lists as arrays
cars = ["Ford", "Volvo", "BMW"]
#call array's element
cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
#or change
cars = ["Ford", "Volvo", "BMW"]
cars[0] = "Toyota"
#looping array elements
for x in cars:
  print(x)
#add array elements
cars = ["Ford", "Volvo", "BMW"]
cars.append("Honda")
#remove
cars.pop(1)
#or
cars.remove("Volvo")
