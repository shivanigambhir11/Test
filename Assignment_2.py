#Great programs you've written here. I especially like the changes you've made to the ordering program. The discount is a creative twist. Well done and keep up the good work!

                 #HOME WORK


'''Ques 1:First, write a program that takes in raw inputs and prints out the result of some manipulation'''

print ("Q1: Program that takes raw inputs and print out Sum ")
a = int(input ("Enter value of a: "))
b = int(input ("Enter value of b: "))
Sum = a+b;
print (Sum)


'''Ques 2 Second,use some boolean logic to make it more
interesting'''
print ("Q2: Boolean logic")
a= int (input ("Enter value of a:"))
b= int (input("Enter value of b: "))
if a>b:
 print (a>b)
elif a==b:
  print (" everthing is equal")
else:
  print ('false')

#Extra If else
'''a= int (input ("Enter value of a:"))
b= int (input("Enter value of b: "))
if a>b:
  print ("A is powerful")
else:
  print ("B is powerful")'''



'''Ques 3: Extra Challenge: build off of the “Order up” example and make more complicated orders with multiple items- PRINTS 10% DISCOUNT ON TOTAL OF 3 ITEMS'''

print ("Q3: Order Total")

print (".....Order Menu.....")
print ("coffee : 1")
print ("burger : 2")
print ("pancake : 3")
print ("dessert : 4")

print ("You can order 3 things ")
print ("write in lower case")
print ("****IF you order any 3 things there will be a discount of 10% on order total**** ")

item1 = input ("Enter item1: ")
if item1 == "coffee":
  price = 1.0
elif item1 =="burger":
  price = 2.0
elif item1 =="pancake":
  price = 3.0
else:
  price =4.0


item2 = input ("Enter item2: ")
if item2 == "coffee":
  price2 = 1.0
elif item2 =="burger":
  price2 = 2.0
elif item2 =="pancake":
  price2 = 3.0
else:
  price2 =4.0

item3 = input ("Enter item3: ")
if item3 == "coffee":
  price3 = 1.0
elif item3 =="burger":
  price3 = 2.0
elif item3 =="pancake":
  price3 = 3.0
else:
  price3 =4.0

sum =  (price + price2 + price3)

print ("your discounted price is :" + str (sum - 0.10 * sum))






