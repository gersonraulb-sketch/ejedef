def next_permutation(seq):
    seq=list(seq)
    i=len(seq)-2
    while i>=0 and seq[i]>=seq[i+1]:
        i-=1
    if i==-1:
        return []
    j=len(seq)-1
    while seq[j]<=seq[i]:
        j-=1
    seq[i],seq[j]=seq[j],seq[i]
    seq[i+1:]=reversed(seq[i+1:])
    return seq

print(next_permutation([1,2,3]))
