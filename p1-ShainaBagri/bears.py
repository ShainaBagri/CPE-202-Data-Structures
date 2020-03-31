# int -> booelan
# Given integer n, returns True or False based on reachabilty of goal
def bears(n):

    #Base case where goal cannot be reached
    if n<42:
        return False

    #Base case where goal can be reached
    if n==42:
        return True

    #Checks if n is divisible by 2
    if n%2==0:
        result = bears(n/2)
        if result:
            return True

    # Checks if n is divisible by 3 or 4
    if (n%3==0 or n%4==0) and ((n%10)*((n%100)//10))!=0:
        result = bears(n-((n%10)*((n%100)//10)))
        if result:
            return True

    # Checks if n is divisible by 5
    if n%5==0:
        result = bears(n-42)
        if result:
            return True

    #Goal cannot be reached
    return False
