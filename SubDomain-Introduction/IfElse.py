def ifelse(n):
    if(n%2 == 0):
        if(n>1 and n<6):
            return 'Not Weird'
        elif(n>5 and n<21):
            return 'Weird'
        elif(n>20):
            return 'Not Weird'
    else:
        return 'Weird'

n= int(input())
print(ifelse(n))
