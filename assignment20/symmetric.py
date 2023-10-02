
array=[]

while True:
    data=input("enter array or type end:")
    if data=="end":
        break
    else:
        array.append(data)
        
    print("input array=", array)
    n=len(array)

    for data in range(n//2):
        if array[data] != array[n-data-1]:
          print("the array is not symmetric") 
          break 

    else:
        print("the array is symmetric")
    
        
