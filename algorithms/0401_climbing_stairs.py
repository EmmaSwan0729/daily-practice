def climb_stairs(n:int) -> int:
    '''
    calculate number of different ways to climb stairs
    you can climb 1 or 2 steps everytime.
    args: n(int), number of stair steps
    return: int: total number of distinct ways     
    '''
    
    if n<=2:
        return n
    a,b = 1,2
    for _ in range(3, n+1):
        a,b = b, a+b
    return b