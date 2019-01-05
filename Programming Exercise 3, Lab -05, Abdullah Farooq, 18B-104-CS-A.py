print('Programming Exercise 3')

def arithSeq(a, d):
    #a is the first term of the sequence,d is the common difference
    n = eval(input('Enter the nth term of the sequence: '))
    nterm = (a+(n-1)*d)
    print('The nth term of the sequence is: ',nterm)
    prompt = input('Do you want to continue: ')
    while prompt == 'yes':
        n = eval(input('Enter the next nth term of the sequence:' ))
        nterm = (a+(n-1)*d)
        print('The nth term of the sequence is: ',nterm)
        prompt = input('Do you want to continue: ')
    else:
        print('End.')
