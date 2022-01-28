def calculatePay():
    
    # This first line is provided for you
    hrs = input("Enter Hours: ")
    rate = input("Enter Rate: ")
    h = float(hrs)
    r = float(rate)
    if h <= 40:
        pay = h * r
    else:
        pay = (h - 40) * (r * 1.5) + (40 * r)
    print(pay)
    
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
## calculatePay()