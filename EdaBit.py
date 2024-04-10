##def interview(lst, tot):
##    if len(lst)==8:
##        if tot<=120:
##            if lst[0]<=5 and lst[1]<=5 and lst[2]<=10 and lst[3]<=10 and lst[4]<=15 and lst[5]<=15 and lst[6]<=20 and lst[7]<=20:
##                return "qualified"
##        else:
##            return "disqualified"
##    return "disqualified"
##
##print(interview([5, 5, 10, 10, 15, 15, 20, 20], 120))
##print(interview([2, 3, 8, 6, 5, 12, 10, 18], 64))
##print(interview([5, 5, 10, 10, 25, 15, 20, 20], 120))
##print(interview([5, 5, 10, 10, 15, 15, 20], 120))
##print(interview([5, 5, 10, 10, 15, 15, 20, 20], 130))


##def row_sum(n):
##    if n==1:
##        return 1
##    else:
##        first_of_row=1
##        for i in range(n):
##            first_of_row+=i
##        suma=0
##        for j in range(n):
##            suma+=first_of_row
##            first_of_row+=1
##    return suma
##
##print(row_sum(1))
##print(row_sum(2))
##print(row_sum(4))
##
##
##def get_domain(ip_address):
##    import socket
##    
##    result = socket.gethostbyaddr(ip_address)
##    
##    return list(result)[0]
##print(get_domain("8.8.8.8"))
##print(get_domain("8.8.4.4"))


##def snakefill(n):
##    length=1
##    times=0
##    if n==1:
##        return times
##    while(length<n*n):
##        length*=2
##        times+=1
##    if length==n*n:
##        return times
##    return times-1
##
##print(snakefill(3))
##print(snakefill(6))
##print(snakefill(24))



##def is_powerful(n):
##    for i in range(2,n//2+1,1):
##        is_Prime=True
##        if n%i==0:
##            for j in range(2, int(i**0.5) + 1):
##                if i%j==0:
##                    is_Prime=False
##                    break
##            if is_Prime==True:
##                if n%(i*i)!=0:
##                    return False
##    return True
##
##print(is_powerful(36))
##print(is_powerful(27))
##print(is_powerful(674))
##


def arithmetic_operation(n):
    op=""
    num1=""
    num2=""
    i=0
    while n[i]!=" ":
        num1+=n[i]
        i+=1

    i+=1
    while n[i]!=" ":
        op+=n[i]
        i+=1

    i+=1
    while i<len(n):
        num2+=n[i]
        i+=1
    if op=="//" and num2=="0":
        return -1

    n1=0
    n2=0
    j=1
    
    for i in range(len(num1)-1,-1,-1):
        n1+=j*int(num1[i])
        j*=10

    j=1    
    for i in range(len(num2)-1,-1,-1):
        n2+=j*int(num2[i])
        j*=10
    
    if op=="+":
        return n1+n2
    elif op=="-":
        return n1-n2
    elif op=="*":
        return n1*n2
    return n1//n2

print(arithmetic_operation("12 + 12"))
print(arithmetic_operation("12 - 12"))
print(arithmetic_operation("12 * 12"))
print(arithmetic_operation("12 // 12"))
