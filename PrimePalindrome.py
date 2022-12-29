def primePalin(n,num=1):
    primes = []
    counter = 0
    while True:
        flag = 0
        num = num + 1
        tmp = num
        #testing code if num is prime
        for prime in primes:
            if num%prime == 0:
                flag += 1
        #testing code if num is palindromic
        rev = 0
        while(tmp > 0):  
            dig = tmp % 10  
            rev = rev * 10 + dig  
            tmp = tmp // 10 

        if flag == 0:
            primes.append(num)
            if num == rev:
                counter += 1
        if counter == n:
            return num

count = int(input("Enter the Nth Term: "))

print(f"The {count}th Prime Palindrome Number is: {primePalin(count)}")
