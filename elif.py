money = input("how much is it? ")
debt = 10000

if int(money) < debt:
    print("Your money isn't enought")
elif int(money) == debt:
    print("Payment success")
else:
    print("Your money is too much")
