colors=['주황','초록','파랑','보라','빨강','노랑']
def push(data):
    global size, top, stack
    top +=1
    if top < size:
        stack[top]=data
    else:
        return
def pop():
    global size,top,stack
    if top != -1:
        data = stack[top]
        stack[top]=None
        top-=1
        return data
    else:
        return
if __name__ == "__main__":
    top=-1
    size=len(colors)
    stack=[None for _ in range(len(colors))]
    for color in colors:
        push(color)
    print("과자집에 가는 길 : ",end= ' ')
    for st in stack:
        print(f'{st} -->',end = ' ')
    print('과자집')
    print('우리집에 오는 길 : ',end=' ')
    for _ in colors:
        print(pop(),'-->',end=' ')
    print('우리집')
