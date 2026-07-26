def sieve(n): #10

    prime = [True]*(n+1) 
    prime[0]=prime[1]=False 
    p=2

    while p*p <=n: #4
        if prime[p]:
            for i in range(p*p, n+1, p):
                prime[i]=False

        p+=1 
    res = []

    for i in range(2, n+1):
        if prime[i]:
            res.append(i)

    return res

n= int(input())
print(sieve(n))