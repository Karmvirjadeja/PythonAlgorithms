def insertion_sort(bucket):
    for i in range (1,len(bucket)):
        
        j=i-1
        if bucket[i]<bucket[j]:
         tmp=bucket[i]
         bucket[i]=bucket[j]
         bucket[j]=tmp
         
        pass
              


def bucket_sort(arr):
    n=len(arr)
    buckets=[[] for _ in range(n)]
# Put array elements in different buckets
    for num in arr:
        bi=int(n*num)
        buckets[bi].append(num)
 # Sorting the individual buckets 
    for bucket in buckets:
        insertion_sort(bucket)       
    
    index=0
    for bucket in buckets:
        for num in bucket:
            arr[index]=num
            index+=1
    
    




arr = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
bucket_sort(arr)
print(arr)


