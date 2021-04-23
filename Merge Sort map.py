import random
import sys
import matplotlib.pyplot as plt
import time

def merge(low,mid,high):
	global sum
	i=low;j=mid+1;k=low
	while i<=mid and j<=high:		#小的數值往前擺放
		if S[i]<S[j]:
			U[k]=S[i]
			i+=1
		else:
			U[k]=S[j]
			j+=1
		k+=1
		sum+=1
	if i>mid:						#如果其中一邊數值都比較完了，將另一邊剩餘數值都排到後面
		for a in range(j,high+1):
			U[k]=S[a]
			k+=1
			sum+=1
	else:
		for b in range(i,mid+1):
			U[k]=S[b]
			k+=1
			sum+=1
	for c in range(low,high+1):
		S[c]=U[c]
		sum+=1

			
def mergesort(low,high):			#不斷分割，分割到2個數值互相比較，再做4個互相比較、8個互相比較，以此類推
	if low<high:
		mid=int((low+high)/2)
		mergesort(low,mid)
		mergesort(mid+1,high)
		merge(low,mid,high)
		map()
	

def map():
	plt.ion()							#使matplotlib的顯示模式轉換為互動（interactive）模式
	plt.clf()							#清除前面所畫的圖
	plt.plot(range(1,1001),S,'.')					#畫點圖
	#plt.bar(range(1,1001),S,)					#畫長條圖
	plt.pause(0.00000000000000000000000000000000000001)		#暫時暫停，否則看不到圖
	#plt.ioff()							#最後動態跑完後仍然會留下圖
	starttime = time.process_time()
sys.setrecursionlimit(900000)		#用來設定遞迴最多能到幾層

sum=0					#計算運算次數
S=[i for i in range(1,1001)]		#一個數值1~1000的list
U=[0 for i in range(1,1001)]		#一個數值全部是0的list
S=random.sample(S, len(S))		#將list不重複地打亂順序

map()				#先秀出最初沒排序樣子
time.sleep(2)
mergesort(0,999)		#開始合併排序法
endtime = time.process_time()

print("合併排序法共花"+str(endtime-starttime)+"秒，共執行"+str(sum)+"次運算。")
