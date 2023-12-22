#numeric
a=10                           #int,float.complex
b=12.2
c=2+7j
print(a,type(a))
print(b,type(b))
print(c,type(c))
print("")
print("")

#boolean                            
d=True                         #True, False
e=False
print(d,type(d))
print(e,type(e))

print(a==b)
print(d+e)
print("")
print("")


 
#sequence                       string,list,tuple,range
f="Akanksha"                    #'''akanksha''',"""akanksha""",'akanksha'
g=[1,2,2,"abc"]                   #mutable,single quotte standard form o/p
g[1]=7
print(g,type(g))
h=(1,2,3,2,"ashish")          #immutable
print(h,type(h))
i=range(5)
print(i,type(i))
print("")
print("")


#set                            set,frozen set
j={1,2,2,3,4,5,6,"abc","abc"}
print(j,type(j))                #changable
k=set()
print("k:",type(k))
print("")
print("")
s={1,2,2,3,4,5,6,"abc","abc"}
print(s,type(s))                #unchangable
t=frozenset(s)
print(t,type(t))
print("")
print("")




#map(dictionary)
l={}
m={1:"abc" ,'a':'apple'}
print(type(l))
print(m,type(m))
m[1]="akanksha"                   #we can only change value not key
print(m)
print(m["a"])
print("")
print("")




#none type
n=None
print(a,type(n))
print("")
print("")




#byte (0 to 256)                 bytes,bytearray
o=[10,20,30]
p=bytes(o)
print(type(p))
#q=[10,20,255,256,30]             #error will ocur as 256 is present
#r=bytes(q)                       #immutable r[3]=12 not allowed
#print(r[3])


q=[10,20,30]
r=bytearray(q)
print("q:",q,type(q))
print("r:",r,type(q))
r[0]=255
print("r:",r)






































