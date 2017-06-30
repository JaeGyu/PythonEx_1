"""
순차적으로 하나씩 위치(인덱스) 고정(선택)시켜 놓고
가장 작은것이 오도록 쭉 바꿔 나간다.
"""
def selectionSort(seq):
    for i in range(0, len(seq)):
        for j in range(i+1, len(seq)):
            if seq[i] > seq[j]:
                seq[i], seq[j] = seq[j], seq[i]
    
    return seq


if __name__ == "__main__":
    l = [5,4,3,2,1]

    print(selectionSort(l))
    