def Input(day):
    '''Open this day's input file.'''
    filename = 'input{}.txt'.format(day)
    try:
        return open(filename)
    except FileNotFoundError:
        print("No input file found for day", day)

def MaxN(l, n=1):
    '''Find top N elements in list'''
    return sorted(l, reverse=True)[:n]
