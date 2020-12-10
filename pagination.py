def abbreviated_pages(n, page):

    # Build set of pages to display
    if n <= 5:
        pages = range(1, n + 1)

    elif(page==n):
        pages = range(max(1, page - 4),min(page+1, n+1))
    elif(page==n-1):
        pages = range(max(1, page - 3), min(page + 2, n+ 1))
    elif(page==1):
        pages = range(max(1, page), min(page + 5, n + 1))
    elif(page==2):
        pages = range(max(1, page - 1), min(page + 4, n + 1))
    else:
        pages = range(max(1, page - 2), min(page + 3, n + 1))
    # Display pages in order with ellipses
    def display():
        last_page = 0
        for p in sorted(pages):
            if p != last_page + 1: yield ''
            yield ('[{0}]' if p == page else '{0}').format(p)
            last_page = p

    return(' '.join(display()))


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
    
