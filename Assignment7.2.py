fname = input("Enter file name: ")
fh = open(fname)
count=0
n = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pos = line.find("0.")
    val = float(line[pos:])
    n = n+val
    count = count+1
print("Average spam confidence:",n/count )