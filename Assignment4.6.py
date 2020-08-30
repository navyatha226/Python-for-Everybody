hrs = input("Enter hours")
h = float(hrs)
rate_per_hour = input("Enter rate per hours")
r = float(rate_per_hour)
def computepay(h,r):
      if h<40:
          return 40*r
      else:
          b=(h-40)*r*1.5
          return 40*r+b
p = computepay(h,r)
print("Pay",p)