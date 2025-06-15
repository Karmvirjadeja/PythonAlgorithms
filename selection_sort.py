
def selection_sort(elements):
    n=len(elements)
    print(n)
    for i in range (n):
        min_index=i
        
        for j in range(i+1,n):
            if elements[min_index]>elements[j]:
             min_index=j
            
        
        temp=elements[i]
        elements[i]=elements[min_index]
        elements[min_index]=temp




if __name__=="__main__":
    elements=[1,32,4,3,2]
    selection_sort(elements)
    print(elements)