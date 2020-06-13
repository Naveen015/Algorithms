s_m=0
def partition(a,n,p):
   #a[n-1]=a[0]
   #a[0]=p
   i=1
   for j in range(1,n):
	if a[j]<p:
	   temp=a[j]
	   a[j]=a[i]
	   a[i]=temp
	   i+=1
   a[0]=a[i-1]
   a[i-1]=p
   if i==1:
	return [],a[i:],n-1
   elif i==n:
	return a[0:i-1],[],n-1
   else:
	return a[0:i-1],a[i:],n-1

def quickSort(a,n):
   if n<=1: return 0
   global s_m
   s_m+=(n-1)
   p=a[0]
   B,C,Z=partition(a,n,p)
   n1=len(B)
   X = quickSort(B,n1)
   n2=len(C)
   Y = quickSort(C,n2)
   return s_m

file1 = open("quicksort.txt","r")
a=[]
siz=10000
for i in range(siz):
   a.append(int(file1.readline()))
cnt=quickSort(a,siz)
print(cnt)



'''
   if n%2==0:
      mid=n//2 -1
   else:
      mid=n//2
   t = [(a[0],0),(a[mid],mid),(a[n-1],n-1)]
   t.sort()
   p = t[1][0]
   med = t[1][1]
   
'''
