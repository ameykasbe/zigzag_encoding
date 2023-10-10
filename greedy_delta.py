def is_in_range_3(value):
    return value >= -4 and value <= 3
def is_in_range_4(value):
    return value >= -8 and value <= 7
def is_in_range_8(value):
    return value >= -128 and value <= 127
def is_in_range_10(value):
    return value >= -512 and value <= 511
def is_in_range_16(value):
    return value >= -32768 and value <= 32767

#                     3 bits                       3 bits                                       4 bits                       3 bits                             8 bits              10 bits             16 bit             16 bit                   3 bits
array = [-2, 1, -3, -4, -2, 2, -3, 1, 1, -4,   2, -3, -2, 1, 2, -3, -2, 1, 2, -3,      3, -4, 5, -6, 7, -8, 2, 1,    2, -3, -2, 1, 2, -3, -2, 1, 2, -3,    -100, 100, -7, 2,     -500, 500, 2,      2, -30000,         -500, -30000,       2, 2, -2, -1, 0, 0, 0, 1, 2, -2]
        
def _3_bits_encoding(start, end):
    # import pdb; pdb.set_trace()
    while(end < len(array)):
        
        if end - start + 1 == 10: # Represents the number of samples
            print("3 bit encoding: ", array[start:end+1]) # send 10 samples [start, end] with 3 bits encoding
            (start, end) = _3_bits_encoding(end+1, end+1) # begin again with new start and new end
            
        elif is_in_range_3(array[end]): 
            end += 1 # Increment number of samples
        else:
            (start, end) = _4_bits_encoding(start, end) # Not possible to encode the next sample with 3 bits
    return (start, end)		
		

def _4_bits_encoding(start, end):
    while(end < len(array)):
        if end - start + 1 >= 8: # Represents the number of samples
            end = start + 8 - 1 # Fixing end if sample size is >8
            print("4 bit encoding: ", array[start:end+1]) # send 8 samples [start, end] with 4 bits encoding
            (start, end) = _3_bits_encoding(end + 1, end+1) # begin again with new start and new end
            
        elif is_in_range_4(array[end]): 
            end += 1 # Increment number of samples
        else:
            (start, end) = _8_bits_encoding(start, end) # Not possible to encode the next sample with 4 bits
    return (start, end)	

def _8_bits_encoding(start, end):
    while(end < len(array)):
        if end - start + 1 >= 4: # Represents the number of samples
            end = start + 4 - 1 # Fixing end if sample size is >4
            print("8 bit encoding: ", array[start:end+1]) # send 4 samples [start, end] with 8 bit encoding
            (start, end) = _3_bits_encoding(end + 1, end+1) # begin again with new start and new end
        elif is_in_range_8(array[end]): 
            end += 1 # Increment number of samples
        else:
            (start, end) = _10_bits_encoding(start, end) # Not possible to encode the next sample with 4 bits
    return (start, end)	

def _10_bits_encoding(start, end):
    while(end < len(array)):
        if end - start + 1 >= 3: # Represents the number of samples
            end = start + 3 - 1 # Fixing end if sample size is >3
            print("10 bit encoding: ", array[start:end+1]) # send 3 samples [start, end] with 10 bits encoding
            (start, end) = _3_bits_encoding(end + 1, end+1) # begin again with new start and new end
            
        elif is_in_range_10(array[end]): 
            end += 1 # Increment number of samples
        else:
            (start, end) = _16_bits_encoding(start, end) # Not possible to encode the next sample with 4 bits
    return (start, end)	

def _16_bits_encoding(start, end):
    while(end < len(array)):
        if end - start + 1 >= 2: # Represents the number of samples
            end = start + 2 - 1 # Fixing end if sample size is >2
            print("16 bit encoding: ", array[start:end+1]) # send 8 samples [start, end] with 16 bits encoding
            (start, end) = _3_bits_encoding(end + 1, end+1) # begin again with new start and new end
            
        elif is_in_range_16(array[end]): 
            end += 1 # Increment number of samples
        else:
            print("Out of range: array[end]")
    return (start, end)	



def main():
    _3_bits_encoding(0, 0)
    
	


if __name__ == "__main__":
	main()



		
