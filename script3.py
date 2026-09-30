numberone = int(input("Enter a number: "))
numbertwo = int(input("Enter another number: "))

product = numberone * numbertwo
if product > 1000:
    print(numberone + numbertwo)
else: print(product)


numbers = ['100', '200', '300', '400', '500', '600', '700', '800', '900']
numbers.sort(reverse=True)
print(numbers)

mylistofnumebrs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
mylistofnumebrs.append(110)
mylistofnumebrs.insert(1,15)
print(mylistofnumebrs)