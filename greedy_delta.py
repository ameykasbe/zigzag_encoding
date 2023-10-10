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

#                     3 bits                       3 bits                                       4 bits                       3 bits
array = [-2, 1, -3, -4, -2, 2, -3, 1, 1, -4,   2, -3, -2, 1, 2, -3, -2, 1, 2, -3,      3, -4, 5, -6, 7, -8, 2, 1,    2, -3, -2, 1, 2, -3, -2, 1, 2, -3, ]
        
def is_possible_3_encoding_samples(start, end):
    
    
    # import pdb; pdb.set_trace()
    while(end < len(array)):
        
        if end - start + 1 == 10: # Represents the number of samples
            print("3 bit encoding: ", array[start:end+1]) # send 10 samples [start, end] with 3 bits encoding
            (start, end) = is_possible_3_encoding_samples(end+1, end+1) # begin again with new start and new end
            
        elif is_in_range_3(array[end]): 
            end += 1 # Increment number of samples
        else:
            (start, end) = is_possible_4_encoding_samples(start, end) # Not possible to encode the next sample with 3 bits
    return (start, end)		
		

def is_possible_4_encoding_samples(start, end):
    while(end < len(array)):
        if end - start + 1 >= 8: # Represents the number of samples
            end = start + 8 - 1
            print("4 bit encoding: ", array[start:end+1]) # send 8 samples [start, end] with 4 bits encoding
            (start, end) = is_possible_3_encoding_samples(end + 1, end+1) # begin again with new start and new end
            
        elif is_in_range_4(array[end]): 
            end += 1 # Increment number of samples
        else:
            (start, end) = is_possible_8_encoding_samples(start, end) # Not possible to encode the next sample with 4 bits
    return (start, end)	


def is_possible_8_encoding_samples(start, end):
	pass

def is_possible_10_encoding_samples(start, end):
	pass

def is_possible_16_encoding_samples(start, end):
	pass


def main():
    is_possible_3_encoding_samples(0, 0)
    
	


if __name__ == "__main__":
	main()



		
