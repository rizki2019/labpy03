a=100000000
total=0
bulan=0
laba = [int(0), int(0), int(a) * .1, int (a) * .1, int(a) * .5, int(a) * .5, int(a) * .5, int(a) * .2]
print("Modal awal Rp.", a)
for i in laba :
    total = total+i
    bulan+=1
    print("Laba bulan ke-",bulan,"sebesar:", i)
print("Total laba adalah:", total)
