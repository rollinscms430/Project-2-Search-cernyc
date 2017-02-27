from collections import defaultdict
from collections import Counter


def test():
    
    print "Be patient, this program can take few minute"
    
    track = []
    sameN = []
    
    word_list1 = []
    word_list2 = []

    not_found = True
    
    
    f = open('words.txt', 'r')
    
    for word in f:
        if len(word) == 7:
            sameN.append(word)
            
    newL = changeLetter("snakes", sameN)
    newA = changeLetter("brains", sameN)
          
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
    
    iterration = 0
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
            temp = changeLetter(k, sameN)
            
            track.append(k)
            
            for h in temp:
                if found == True:
                    break
               
                if h not in visited:
                    visited.append(h)
                    if h in end_list:
                        print 'the last word to be changed is: ' + h
                        found = True
                        print "success"
                        for u in track:
                            print u
                        break
                            #else:
                                #if not track:
                                    #track.pop()
            
            
        start = temp
        #track.pop()
    
    '''levels = []
    while found != True:
        for k in start:
            track.append(k)
            iterration = iterration + 1
            new_list = make_path(k, sameN)
            while iterration < 20:
                
                if compare(new_list, end):
                    found = True
                    print "success"
                    for p in track:
                        print p
                else:
                    print iterration
                    iterration = iterration + 1
                    for r in new_list:
                        track.append(r)
                        n_list = make_path(r, sameN)
                        
                    new_list = n_list
                        
    '''        


def make_path(word, base_list):
    
    new_list = changeLetter(word, base_list)
    return new_list
            

def compare(list1, list2):
    
    for k in list1:
        if k in list2:
            return True
        
            


def changeLetter(base_word, sameN):
    
    alphabet = ("a", "b", "c", "d", "e","f","g","h","i","j","k","l"
    ,"m","n","o","p","q","r","s","t","u","v","w","x","y","z")
    
    new_word_list = []
    s = list(base_word)
    
    for w in range(0,6):
        
        for l in range(26):
            
            s[w] = alphabet[l]
            
            new_word = "".join(s)
            
            if new_word in sameN:
                new_word_list.append(new_word)
            
        s = list(base_word)
            
    return new_word_list
                
        
    


test()