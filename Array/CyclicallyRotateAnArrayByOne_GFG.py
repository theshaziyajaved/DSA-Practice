def rotate( arr, n):
    arr[::] = arr[-1:]+arr[0:-1]
    return 

def rotate( arr, n):
    arr.insert(0,arr[n-1])
    arr.pop()
    # # By default, if there is no index specified, the pop() method will remove the last item that 
    # # is contained in the list.
    return arr