r=5
h=10
s=10
v=3.14*r*r*h
print(v)
t=int(input("enter the time:"))
vs=s*t
if vs<v:
    print("underflow vol. remain",(v-vs))
elif vs>v:
    print("overflow extra vol.",(vs-v))
else:
    print("full")