from functools import reduce

def __get_num_digits(A):
    m=0
    for item in A:
        m=max(item,0)
    return len(str(m))

def radix(A):
    
    max1=max(A)
    exp=1
    while max1 // exp>0:
        countingSort(A,exp)
        exp*=10
   
  
        

def main():
    A=[55,45,3,289,213,1,288,53,2]
    num_digits=__get_num_digits(A)
    A=radix(A,num_digits)
    print(A)
    
main()