def oscillate():
    for i in range(-3, 5):
        if i < 0:
            print(i, -i, end='\t')
        elif i == 0:
            print("0\t0", end='\t')
        else:
            print(i, -i, end='\t')

oscillate()
