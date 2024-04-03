def prime_sleve(n):
    ans=[]
    is_prime=[True]*(n+1)
    for i in range(2,n+1):
        if is_prime[i]:
            ans.append(i)
        for pri in ans:
            if pri*i>n:
                break
            is_prime[pri*i]=False
            # i已经被筛过
            if i%pri==0:
                break
    return ans

print(prime_sleve(13))