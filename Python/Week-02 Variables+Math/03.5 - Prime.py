while True:
    num = input("Which number do you want to check if it is prime?(use STOP to stop)  ")
    if  num == "STOP":
        break
    num = int(num)
    if num > 1:
        for i in range(2, num):
            if(num % i) == 0:
                prime = False
                break
            else:
                prime = True
    else:
        prime = False
    print(prime,num)
