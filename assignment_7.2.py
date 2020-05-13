fname = input("Enter file name: ")
fh = open(fname,"r")
lines = 0
b = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") :
        lines +=1
        a = line.find("0")
        b += float(line[a:a+6])
avg = (b/float(lines))

print("Average spam confidence:",avg)
