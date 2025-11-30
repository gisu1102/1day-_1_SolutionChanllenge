"""
1,2 3,4,5, 6, 7,8,9
[1 2 5 3 4]
+- 1
+- 2
+++- 3 4 5
X 3 4
"""
def stack_sequence(n, sequence):
    # 이 곳을 채워보세요!
    stack_sequence = []
    k = 0
    push_pop = []
    for i in range (1, n+1):
        stack_sequence.append(i)
        push_pop.append('+')
        while stack_sequence and stack_sequence[-1] == sequence[k]:
            stack_sequence.pop()
            push_pop.append('-')
            k += 1

    if stack_sequence != []:
        print("NO")
        return
        

    for char in push_pop:
        print(char)
        
    return
        





sequence = list()
n = int(input())
for _ in range(n):
    sequence.append(int(input()))
stack_sequence(n, sequence)