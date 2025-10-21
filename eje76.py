def validar_parentesis(s):
    cnt=0
    for ch in s:
        if ch=='(':
            cnt+=1
        elif ch==')':
            cnt-=1
            if cnt<0: return False
    return cnt==0

print(validar_parentesis('(()())'))
