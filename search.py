def index(number, numbers):
    ''' return the index of the number in the list of integers numbers

    The function returns -1 if the number is not present in the numbers,
    or the list is empty.
    '''
    if number not in numbers or numbers == []:
        return -1
    for x in range(len(numbers)):
        if number == numbers[x]:
            return x
    
