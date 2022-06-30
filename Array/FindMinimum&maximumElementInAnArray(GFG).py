
def getMinMax( a, n):
    #O(nlogn) solution
    # a = sorted(a)
    # return a[0],a[len(a) - 1]
    

    min_ = a[0]
    max_ = a[0]
    
    for i in range (len(a)):
        if (a[i] >= max_):
            max_ = a[i]
        if (a[i] <= min_):
            min_ = a[i]
    return min_ , max_  
        

   
    #     min_ = min(a)
    #     max_ = max(a)
    # return min_ , max_    
        
    
    
