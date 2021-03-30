def add_it_up(n):
    a = 0
    if n.isint():
        for i in range(0, n+1):
            a = a + i
        return(a)
    else:
        return 0

print(add_it_up(input("Enter a number: ")))


    
