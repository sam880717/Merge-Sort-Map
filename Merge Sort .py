import random
import sys
import matplotlib.pyplot as plt
import time

def merge(low,mid,high):
	i=low;j=mid+1;k=low
	while i<=mid and j<=high:
		if S[i]<S[j]:
			U[k]=S[i]
			i+=1
		else:
			U[k]=S[j]
			j+=1
		k+=1
	if i>mid:
		for a in range(j,high+1):
			U[k]=S[a]
			k+=1
	else:
		for b in range(i,mid+1):
			U[k]=S[b]
			k+=1
	for c in range(low,high+1):
		S[c]=U[c]
	map()	
			
def mergesort(low,high):
	if low<high:
		mid=int((low+high)/2)
		mergesort(low,mid)
		mergesort(mid+1,high)
		merge(low,mid,high)
		

		

def map():
	global first,fig
	plt.ion()
	plt.clf()
	plt.plot(range(1,1001),S,1000,1000)
	plt.pause(0.00000000000000000000000000000000000001)
	plt.ioff()
	

sys.setrecursionlimit(9000000)

first=1
S=[i for i in range(1,1001)]
U=[0 for i in range(1,1001)]
S=random.sample(S, len(S))
#print(S)

mergesort(0,999)
plt.show()




	
