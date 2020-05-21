class CoffeeMachine():
    water_in_machine = 400
    milk_in_machine = 540
    beans_in_machine = 120
    money_in_machine = 550
    disposable_cups = 9
    status = False

    def __init__(self):
        self.action = None
        if not self.status:
            self.move()

    def machine_remaining(self):
        print("")
        print("The coffee machine has:")
        print(CoffeeMachine.water_in_machine, "of water")
        print(CoffeeMachine.milk_in_machine, "of milk")
        print(CoffeeMachine.beans_in_machine, "of coffee beans")
        print(CoffeeMachine.disposable_cups, "of disposable cups")
        print("$" + str(CoffeeMachine.money_in_machine), "of money")
        print("")


    def buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
        buy = input()
        if buy == "1":
            if CoffeeMachine.water_in_machine < 250:
                print("Sorry, not enough water!")
                print("")
            elif CoffeeMachine.beans_in_machine < 16:
                print("Sorry, not enough coffee beans!")
                print("")
            elif CoffeeMachine.disposable_cups < 1:
                print("Sorry, not enough disposable cups!")
                print("")
            else:
                print("I have enough resources, making you a coffee!")
                print("")
                CoffeeMachine.water_in_machine -= 250
                CoffeeMachine.beans_in_machine -= 16
                CoffeeMachine.money_in_machine += 4
                CoffeeMachine.disposable_cups -= 1
        elif buy == "2":
            if CoffeeMachine.water_in_machine < 350:
                print("Sorry, not enough water!")
                print("")
            elif CoffeeMachine.milk_in_machine < 75:
                print("Sorry, not enough milk!")
                print("")
            elif CoffeeMachine.beans_in_machine < 20:
                print("Sorry, not enough coffee beans!")
                print("")
            elif CoffeeMachine.disposable_cups < 1:
                print("Sorry, not enough disposable cups!")
                print("")
            else:
                print("I have enough resources, making you a coffee!")
                print("")
                CoffeeMachine.water_in_machine -= 350
                CoffeeMachine.milk_in_machine -= 75
                CoffeeMachine.beans_in_machine -= 20
                CoffeeMachine.money_in_machine += 7
                CoffeeMachine.disposable_cups -= 1
        elif buy == "3":
            if CoffeeMachine.water_in_machine < 200:
                print("Sorry, not enough water!")
                print("")
            elif CoffeeMachine.milk_in_machine < 100:
                print("Sorry, not enough milk!")
                print("")
            elif CoffeeMachine.beans_in_machine < 12:
                print("Sorry, not enough coffee beans!")
                print("")
            elif CoffeeMachine.disposable_cups < 1:
                print("Sorry, not enough disposable cups!")
                print("")
            else:
                print("I have enough resources, making you a coffee!")
                print("")
                CoffeeMachine.water_in_machine -= 200
                CoffeeMachine.milk_in_machine -= 100
                CoffeeMachine.beans_in_machine -= 12
                CoffeeMachine.money_in_machine += 6
                CoffeeMachine.disposable_cups -= 1
        elif buy == "back":
            pass


    def fill(self):
        print("Write how many ml of water do you want to add: ")
        water = int(input())
        CoffeeMachine.water_in_machine += water
        print("Write how many ml of milk do you want to add: ")
        milk = int(input())
        CoffeeMachine.milk_in_machine += milk
        print("Write how many grams of coffee beans do you want to add: ")
        beans = int(input())
        CoffeeMachine.beans_in_machine += beans
        print("Write how many disposable cups of coffee do you want to add: ")
        cups = int(input())
        CoffeeMachine.disposable_cups += cups
        print("")


    def take(self):
        print("")
        print("I gave you $" + str(CoffeeMachine.money_in_machine))
        print("")
        CoffeeMachine.money_in_machine = 0

    def move(self):
        CoffeeMachine.status = True
        while CoffeeMachine.status:
            print("Write action (buy, fill, take, remaining, exit): ")
            self.action = input()
            if self.action == "buy":
                self.buy()
            elif self.action == "fill":
                self.fill()
                continue
            elif self.action == "take":
                self.take()
                continue
            elif self.action == "remaining":
                self.machine_remaining()
                continue
            elif self.action == "exit":
                print("")
                CoffeeMachine.status = False

CoffeeMachine()