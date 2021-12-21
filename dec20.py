# You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

def find_outlier(integers):
    odd = []
    even = []
    for i in integers:
        if i% 2 != 0:
            odd.append(i)
        elif i% 2 == 0:
            even.append(i)
    if len(odd) < len(even):
        return odd[0]
    else:
        return even[0]
        
# or another sollution:

def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]