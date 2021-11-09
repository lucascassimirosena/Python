# This app will verify the price of something and say if I can buy it or not

money = (input("How much money do you have? "))
price = [50, 100, 200, 300, 400, 500]

for value in price:
    if price > money:
        print("You can't buy it, sorry")
    else:
        print("Go ahead, it's yours already")