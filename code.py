# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def minandmax(i, j, m, M, ops):
    mi=float('inf')
    ma=float('-inf')
    for k in range(i, j):
        a=evalt(M[i][k], M[k+1][j], ops[k-1])
        b=evalt(M[i][k], m[k+1][j], ops[k-1])
        c=evalt(m[i][k], M[k+1][j], ops[k-1])
        d=evalt(m[i][k], m[k+1][j], ops[k-1])
        #print(a,b,c,d)
        mi=min(mi, a, b, c, d)
        ma=max(ma, a, b, c, d)
    return (mi, ma)

def get_maximum_value(data):
    digits=data[::2]
    ops=data[1::2]
    #print(digits)
    #print(ops)
    m=[[None for i in range(len(digits)+1)] for j in range(len(digits)+1)]
    M=[[None for i in range(len(digits)+1)] for j in range(len(digits)+1)]
    for i in range(1, len(digits)+1):
        m[i][i]=int(digits[i-1])
        M[i][i]=int(digits[i-1])
    for s in range(1, len(digits)):
        for i in range(1, len(digits)-s+1):
            j=i+s
            m[i][j], M[i][j]=minandmax(i, j, m, M, ops)
    return M[1][len(digits)]

if __name__ == "__main__":
    print(get_maximum_value(input()))
