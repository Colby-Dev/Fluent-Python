
def f(a, b):
    a += b
    return a

x = 1 
y = 2

w = [1, 2]
z = [3, 4]

if __name__ == "__main__": 
    
    print(f(x, y))

    #The number x is unchanged even though the function runs to assign it to a new cumulative value
    print(x, y)

    print(f(w,z))

    #The list will be changed because mutable objects are able to be changed but the list and var name will not be
    print(w,z) 
