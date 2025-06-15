def counting_sort(elements):
    
    count=[0 for i in range(43)]
  
    for i in range(len(elements)):
        count[elements[i]]+=1
       
        
        
     
    for i in range(len(count)):
        if count[i]!=0:
            while count[i]:
                print(i)
                count[i]-=1
                
        pass    





if __name__=="__main__":
    elements=[42,1,1,6,6,4,2]
    counting_sort(elements)