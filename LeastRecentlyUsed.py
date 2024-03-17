def PageFaults(Pages, n, frames):
    s =set() #the current set of page in memory
    index ={} #store the least recently used pages
    page_faults=0 #count the number of page faults

    for i in range(n):
        if len(s)<frames: # if the length of n less than capcity 
            if Pages[i] not in s: #and if the page not in the current set of page in memory
                s.add(Pages[i]) #add it to the set (replace it with the LRU page)
                page_faults += 1 #and increase the faults
                index[Pages[i]]=i
        else:
            if Pages[i] not in s:
                LRU= float('inf')
                #if the set is full
                for page in s:
                    if index[page]<LRU:
                        LRU=index[page]
                        val=page
                s.remove(val)
                s.add(Pages[i])
                page_faults += 1
            index[Pages[i]]=i

        print(f"step {i+1}= {list(s)}")
    return page_faults

Pages=[3,2,3,4,2,1,3,4,2,1,4,3,2,1,5] #page reference string  
n=len(Pages) #the total number of page requstes
frames=3 #the capcity of page frame, how many number of page that can be hold in memory
print(PageFaults(Pages,n,frames))

