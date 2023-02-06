def push(data):
    global top, stack, size
    if top < size:
        top+=1
        stack[top]=data
    else:
        return
def pop():
    global top,stack,size
    if top != -1:
        data = stack[top]
        stack[top]=None
        top-=1
        return data
if __name__=="__main__":
    poem='''진달래꽃\n나 보기가 역겨워 가실 때에는\n말없이 고이 보내드리오리다.'''
    size = len(poem)
    top=-1
    stack=[None for _ in range(len(poem))]
    print('-----원본-----')
    for i in poem:
        push(i)
    print(''.join(stack))
    print('-----거꾸로 처리된 결과-----')
    for i in range(len(poem)):
        print(pop(),end='')