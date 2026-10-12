 hi
# # name = "ayman baig"
# # name = "hamza"
# # phone_number = "hamza"
# # num = 2
# # num2 = 3

# # print (num + num2)
# # print("this is my no 85845")

# a = "abc10"
# b = 2
# c = 3
# d = 4
# e = "abc12"
# f = "abc13"
# h = a +" "+ e +" "+ f
# i = b + c + d
# j =a +" " +str( b) +" "+ f
# print(h)
# print(i)
# print(j)
# Input two numbers from the user
# # Input length and breadth from the user
# length = float(input("Enter length: "))
# breadth = float(input("Enter breadth: "))

# # Calculate and display the area
# area = length * breadth
# print("Area of the rectangle:", area)
# Take name and marks as input
# 
# Input the radius from the user
# 
# Take name and age as input
#list - mutable
# fruits = ["apple","grapes","pineapple","carrot","raddish","potato"]
# vegitables = ["carrot","raddish","potato"]
# print(fruits )
# print (fruits[0:])
#slicing
# print (fruits[0:5])
# print (fruits[:3])
# print (fruits[::3]) #step slicing
# #q
# phone = ["ultra","pro","redmi","vivo ","OnePlus","Apple ","iPhone","Google Pixel","Motorola ","iQOO","samsung"]
# car = ["Toyota ","Honda Civic","musda","ford","jeep","land c","ferrari","lambo","bugati"]
# print(phone)
# print (car)
# print(phone[-1])
# print (phone[3:13])

# # add values
# phone.append("yoo")
# print(phone)

#insert
# a = ["car","bike","truck"]
# a.insert (2,"auto")
# print(a)
# #values change
# a = [1,2,3,4,5]
# a[1] = 20
# print(a)
#q
phone = ["ultra","pro","redmi","vivo ","OnePlus","Apple ","iPhone","Google Pixel","Motorola ","iQOO","Toyota ","Honda Civic","musda","ford","jeep","land c","ferrari","lambo","bugati","samsung"]
phone.append("s24 ultra")
phone.insert(5,"jeep32")
phone[-2] = "nokia black"
print(phone)
# phone = ["ultra","pro","redmi","vivo ","OnePlus","Apple ","iPhone","Google Pixel","Motorola ","iQOO","Toyota ","Honda Civic","musda","ford","jeep","land c","ferrari","lambo","bugati","samsung"]
# phone.append("s24 ultra")
# phone.insert(5,"jeep32")
# phone[-2] = "nokia black"
# print(phone)

#q

# item_1 = int(input("enter the name of the item prize :"))
# item_2 = int(input("enter the name of the item prize:"))
# item_3 = int(input("enter the name of the item prize :"))
# subtotal_items = (item_1)+ (item_2) + (item_3) 
# gst =  subtotal_items * 18/100
# total = subtotal_items+gst 
# print(total)


#q

# items = ["Burger", "Pizza", "Pasta", "Fries"]
# prices = [150, 300, 250, 100]
# print("Menu:", items)
# print("Prices:", prices)
# item1 = input("\nEnter first item: ")
# item2 = input("Enter second item: ")
# p1 = prices[items.index(item1)]
# p2 = prices[items.index(item2)]
# total = p1 + p2
# gst = total * 0.18
# final = total + gst
# print("\nTotal:", total)
# print("GST (18%):", gst)
# print("Final Bill:", final)




#06/06/2026 Q/A
# ticket_categories = ["silver","gold","platinium"]
# prices = [2000,10000,5000]
# ticket1 = input("Enter first ticket categorie: ")
# ticket2 = input("Enter second ticket categorie: ")
# total_ticket1 = int(input("enter how many tickets u need: "))
# total_ticket2 = int(input("enter how many tickets u need: "))
# total = total_ticket1 + total_ticket2
# gst = total * 0.12
# final = total + gst
# print("\nTotal:", total)
# print("GST (12%):", gst)
# print("Final Bill:", final)


# p = [1,2,35,4,5]
# print(p)
# p.extend ([6,7,8,9])
# print(p)
# p.pop()
# print(p)
# p.clear
# del p[2]
# print(len(p))


# q = [1,2,35,4,5]
# q.sort(reverse=1)
# print(q)


#q

# marks = int(input("enter the marks:"))
# if marks>=90:
#     grade ="A"
# elif marks>=80:
#     grade ="b"
# elif marks>=70:
#     grade ="c"
# elif marks>=60:
#     grade ="d"
# else:
#      grade ="f"
# print(f"marks={marks} grade = {grade}")

#q

# age = int(input("enter the age:"))
# has_id = True
# if age >=18:
#     if has_id:
#         print("granted")
#     else:
#         print("id req")
# else:
#     print("denied")        

#q
# temp = int(input("enter the temp:"))
# is_sunny = True
# # and-both should be true
# if temp>=30 and is_sunny:
#     print("hot & sunny day")

# # or-least bone should be true
# if temp>=40 or not is_sunny:
#     print("extremely high")
# else:
#     print("fine")    

# #q code in one line
# mark = 55
# result = "pass" if mark>=50 else "fail"
# print("result")

#for loop 
scores = [88,55,22,66,96]
for result in scores:
    print(result)

#range
for i in range (1,6):
    print(f"studend {i}")

#multiplication
for o in range (1,11):
    print(f"3 x {o} = {3 * o}")
#q
for o in range (1,11,2):
    
    print(f"6 x {o} = {6 * o} ")
    
