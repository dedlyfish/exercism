def on_square(integer_number):
    if integer_number not in range(1,65): 
        raise ValueError()
    return 2**(integer_number - 1)

def total_after(integer_number):
    if integer_number not in range(1,65): 
        raise ValueError()
    return 2**integer_number - 1
