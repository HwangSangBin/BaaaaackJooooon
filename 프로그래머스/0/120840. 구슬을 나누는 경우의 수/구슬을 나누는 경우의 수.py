def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
def solution(balls, share):
    if balls == share:
        return 1
    else:
        answer = factorial(balls) // (factorial(balls - share) * factorial(share))
        return answer