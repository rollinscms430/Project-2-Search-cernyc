from collections import defaultdict
from collections import Counter


def test():
    
    print "Be patient, this program can take few minutes"
    
    track = []
    sameN = []
 
    newL = changeLetter("snakes")
    newA = changeLetter("brains")
    
    word_list1 = []
    word_list2 = []

    not_found = True
    
    
    
    
    f = open('words.txt', 'r')
    
    for word in f:
        if len(word) == 7:
            sameN.append(word)
          
    for q in newL:
        for a in sameN:
            if q in a:
                word_list1.append(q)
                
                
    for m in newA:
        for n in sameN:
            if m in n:
                word_list2.append(m)
                
                
    find_track (word_list1, word_list2, sameN)
    
    
                
def find_track (start_list, end_list, sameN):
    
    y = 0
    track = []
    start = start_list
    end = end_list
    temp_list = []
    visited = []
    
    found = False
    
    while found != True:
        
        for k in start:
            
            if found == True:
                break
            
            visited.append(k)
            temp = changeLetter(k)
            
            track.append(k)
            
            for h in temp:
                if found == True:
                    break
               
                if h not in visited:
                    for a in sameN:
                        if found == True:
                            break
                        if h in a and h not in visited:
                            visited.append(h)
                            #print h
                            temp_list.append(h)
                            if h in end_list:
                                print h
                                found = True
                                print "success"
                                #for u in track:
                                    #print u
                                break
                            #else:
                                #if not track:
                                    #track.pop()
            
            
        start = temp_list
        #track.pop()

def changeLetter(base_word):
    
    alphabet = ("a", "b", "c", "d", "e","f","g","h","i","j","k","l"
    ,"m","n","o","p","q","r","s","t","u","v","w","x","y","z")
    
    new_word_list = []
    s = list(base_word)
    
    for w in range(0,6):
        
        for l in range(26):
            
            s[w] = alphabet[l]
            
            new_word = "".join(s)
            
            new_word_list.append(new_word)
            
        s = list(base_word)
            
    return new_word_list
                
        
    


test()