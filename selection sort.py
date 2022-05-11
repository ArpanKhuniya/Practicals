#selection sort

def selection_sort(lst):
  n=len(lst)
  for i in range(n-1):
    min=i
    for j in range (i+1,n):
      if(lst[j]<lst[min]):
        min=j
    lst[i],lst[min]=lst[min],lst[i]
  for i in range(n):
    print(lst[i])

selection_sort([1,8,3,5,2])

    
    