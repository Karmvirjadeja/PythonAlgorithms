def swap(elements,i,j):
    if(elements[i]>elements[j]):
        temp=elements[i]
        elements[i]=elements[j]
        elements[j]=temp





def bubble_sort(elements):
    size=len(elements)
    print(size)
    for i in range(size):
        for j in range(size-i-1):
            if(elements[j]>elements[j+1]):
               print(elements[j],elements[j+1])
               tmp=elements[j]
               elements[j]=elements[j+1]
               elements[j+1]=tmp
               print(elements[j],elements[j+1])
            
    print(elements)
    
   
           
 
            
        
    
    
if __name__=='__main__':
    elements=[3,2,4,1,25,5,18]
    bubble_sort(elements)
    