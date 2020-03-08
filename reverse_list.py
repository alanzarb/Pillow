def reverse_list(elems): 
    new_list = [] 
    for i in range(len(elems)): 
        # (Fill in the missing line here) 
        new_list.append(elems[len(elems) - i - 1]) 
    return new_list 

lst = [1,4,7,9,12,14] 

if __name__ == "__main__":
    print (reverse_list(lst))
