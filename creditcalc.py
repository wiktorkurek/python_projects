import math
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--type", action="store")
parser.add_argument("--payment", action="store", type=float)
parser.add_argument("--principal", action="store", type=float)
parser.add_argument("--periods", action="store", type=int)
parser.add_argument("--interest", action="store", type=float)
args = parser.parse_args()

credit_principal = args.principal
count_of_periods = args.periods
monthly_payment = args.payment
credit_interest = args.interest
if credit_interest != None:
    i = credit_interest / (12 * 100)

if len(sys.argv) < 5:
    print("Incorrect parameters")
    exit()
elif args.type == None:
    print("Incorrect parameters")
    exit()
elif args.type not in ["diff", "annuity"]:
    print("Incorrect parameters")
    exit()
elif args.type == "diff" and args.payment != None:
    print("Incorrect parameters")
    exit()
elif args.type == "diff":
    if args.principal == None or args.periods == None or args.interest == None:
        print("Incorrect parameters")
        exit()
    else:
        if args.principal < 0 or args.periods < 0 or args.interest < 0:
            print("Incorrect parameters")
            exit()
        else:
            d = []
            for m in range(1, count_of_periods + 1):
                d.append(math.ceil((credit_principal / count_of_periods) + i * (credit_principal - (credit_principal * (m - 1) / count_of_periods))))
                print("Month " + str(m) + ": paid out ", d[m -1])
            print("")
            print("Overpayment = ", sum(d) - credit_principal)
elif args.type == "annuity":
    if (args.principal == None or args.periods == None or args.interest == None) and args.payment == None:
        print("Incorrect parameters")
        exit()
    elif args.principal != None and args.periods!= None and args.interest != None:
        if args.principal < 0 or args.periods < 0 or args.interest < 0:
            print("Incorrect parameters")
            exit()
        else:
            annuity_payment = math.ceil(credit_principal * ((i * pow(1 + i, count_of_periods))) / (pow(1 + i, count_of_periods) - 1))
            print("Your annuity payment = ", math.ceil(annuity_payment), "!")
            print("")
            print("Overpayment = ", annuity_payment * count_of_periods - credit_principal)
    elif monthly_payment != None and count_of_periods != None and credit_interest != None:
        if monthly_payment < 0 or count_of_periods < 0  or credit_interest < 0:
            print("Incorrect parameters")
            exit()
        else:
            principal = math.floor(monthly_payment / ((i * pow(1 + i, count_of_periods)) / (pow(1 + i, count_of_periods) - 1)))
            print("Your credit principal = ", principal, "!")
            print("")
            print("Overpayment = ", int(args.payment * args.periods - principal))
    elif monthly_payment != None and credit_principal != None and credit_interest!= None:
        if monthly_payment < 0 or credit_principal < 0 or credit_interest < 0:
            print("Incorrect parameters")
            exit()
        else:
            count_of_periods = math.log(monthly_payment / (monthly_payment - i * credit_principal), (1 + i))
            rounded_n = math.ceil(count_of_periods)
            years = math.floor(rounded_n / 12)
            months = rounded_n % 12
            if years == 0:
                print("You need " + str(months) + " months to repay this credit!")
            else:
                if months == 0:
                    print("You need " + str(years) + " years to repay this credit!")
                else:
                    print("You need " + str(years) + " years and " + str(months) + " months to repay this credit!")
            print("Overpayment = ", int(monthly_payment * rounded_n - credit_principal))