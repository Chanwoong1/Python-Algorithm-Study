'''
https://programmers.co.kr/learn/courses/30/lessons/62048
'''

import math
def solution(w,h):
    answer = w * h - (w + h - math.gcd(w, h))
    return answer