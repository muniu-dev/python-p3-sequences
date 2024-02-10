# In lib/sequences.py

def print_fibonacci(length):
    seq = []

    while len(seq) < length:
        if len(seq) == 0:
            seq.append(0)
        elif len(seq) == 1:
            seq.append(1)
        else:
            seq.append(seq[-1] + seq[-2])

    print(seq)