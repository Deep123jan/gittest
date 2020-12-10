def get_pages(current, total, n = 5):
    assert(0 < current <= total)
    pages = []      
    if total <= n:
        pages = range(1, total + 1)
        print("if")
    else:
        slop = (n - 1)//2
        print(slop)
        left = current - slop
        right = current + slop
       
        if current - slop < 1:
            left = 1
            right = current + slop + (slop - (current - 1))
           
        elif (current == total):
            left = (current - (current + slop + (slop - (current - 1)))) + 1 
            right = total 
        elif (current == total-1):
            left = (current - (current + slop + (slop - (current - 1)))) + 2 
            right = total 
        pages = range(left, (right + 1))   

    return list(pages)
    # display = []    
    # for i in list(pages):
    #     if i == current:
    #         display.append('{%d}' % i)
    #     else:
    #         display.append((i))
    # return display
    
