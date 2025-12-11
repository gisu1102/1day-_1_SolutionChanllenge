import math
def solution(n, w, num):
    answer = 0
    
    height = math.ceil(n/w)
    box_layer = [[0 for _ in range(w)] for _ in range(height)]
    
    current = 1
    for row in range(height):
        #짝수층쌓기
        if row%2 == 0:
            for column in range(w):
                if current > n:
                    break
                box_layer[row][column] = current
                current+=1
        #홀수층쌓기
        else:
            for column in range(w):
                if current > n:
                    break
                box_layer[row][w-1-column] = current
                current+=1
    
    target_row = math.ceil(num/w) -1

    #01234 -1
    if target_row%2 == 0:
        idx = num%w -1
    #-1 -2 -3 -4 -5 0
    else:
        idx = (num%w) * -1
    print("num:", num, "idx", idx)
    
    for h in range(target_row, height):
        if box_layer[h][idx] !=0:
            print("idx:",idx,"targwt_row:",target_row,"box:",box_layer[h][idx])
            answer+=1
    
    return answer