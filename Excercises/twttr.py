input_str = input("Input: ")
for i in input_str:
    if i in ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']:
        continue
    print (i, sep='', end='')
