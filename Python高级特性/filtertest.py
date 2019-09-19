#!/usr/ben/env python3

pp = [('Leborn James',98),('Kevin Durant',97),('James Harden',96),('Stephen Curry',95),('Anthony Davis',94)]

def a(i):
    if i[1] >= 96:
        return True
    else:
        return False
    
list(filter(a,pp))


#list(filter(lambda x:x[1] , pp))



