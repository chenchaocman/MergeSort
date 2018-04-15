
 # -*- coding: utf-8 -*- 

#两个排好顺序的数组归并在一起。（规模最小情况下，每个数组都只有一个元素）
def Merge(a,b):
	result = []
	i=0
	j=0

	while i<len(a) and j<len(b):
		if a[i]<b[j]:
			result.append(a[i])
			i+=1
		else:
			result.append(b[j])
			j+=1

#在while的判断条件下，一定是有一个数组遍历完了
	result+=a[i:]
	result+=b[j:]

	return result

def mergeSort(arry):
	if len(arry)<=1:
		return arry
	
	middle = len(arry)/2
	left = mergeSort(arry[:middle])
	right = mergeSort(arry[middle:])
	return Merge(left,right)
	




if __name__ == '__main__':
	print("a")
	print(mergeSort([8, 6, 2, 3, 1, 5, 7, 4]))






































