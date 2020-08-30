largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try:
        n = int(num)
        if smallest is None and largest is None:
            smallest = n
            largest =n
        elif smallest > n:
            smallest = n
        elif largest < n:
            largest = n
    except:
          print("Invalid input")
          continue
print("Maximum is", largest)
print("Minimum is", smallest)