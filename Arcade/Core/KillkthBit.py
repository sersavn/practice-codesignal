n = 37
k = 4

#k: 13
#def killKthBit(n, k):
#a = str(bin(n)[2:2+k])+'0'+str(bin(n)[3+k:])
a = str(bin(n))
a = a[2:]
print(a)


#b = str(bin(n)[2:-k:])+'0'+str(bin(n)[-k:-1:])

#c = int(str(bin(n)[2:2+k-1])+str(0)+str(bin(n)[3+k-1:]),2)
#c = int(str(bin(n)[2:2+k])+str(0)+str(bin(n)[3+k:]),2)
#print(c)
#print(b)
#print(int(b,2))
#c = str(bin(n))[2:]
#print(c)
#print(a)
#print(a[-k])
#print(int(a,2))

#print(killKthBit(37, 3))
