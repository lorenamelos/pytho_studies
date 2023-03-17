def computepay(hours,rate):
    # print("In computepay", hours, rate)
    if hours > 40 :
        reg = rate * hours
        overtime = (hours - 40.0) * (rate *0.5)
        pay = reg + overtime
    else:
        pay = hours * rate
    # print("Returning", pay)
    return pay

sh = input("Enter Hour: ")
sr = input("Enter Rate: ")
fh = float(sh)
fr = float(sr)

#calling the function:
xp = computepay(fh,fr)

