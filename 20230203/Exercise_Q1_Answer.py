# Q1 Answer

def solution1(lottos, win_nums):
    answer = []
    same = 0
    unknown = 0
    for n in lottos:
        if n == 0:
            unknown += 1
            continue
        for wn in win_nums:
            if n == wn:
                same += 1
    
    confirmed = 7-same
    able = 7-same-unknown
    
    if able > 6: able = 6
    if confirmed > 6: confirmed = 6
    
    answer.append(able)        
    answer.append(confirmed)

    return answer
  
  
  def solution2(lottos, win_nums):
    answer = []
    same = 0
    unknown = 0
    for n in lottos:
        if n == 0:
            unknown += 1
            continue
        if n in win_nums: same += 1
    
    answer.append(min(7-same-unknown, 6))
    answer.append(min(7-same, 6))
    
    return answer
