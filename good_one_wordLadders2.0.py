from collections import defaultdict
from collections import Counter


class Ladder(object):
    
    def __init__(self, file = None):
        
        print "Be patient, this program can take few seconds"
        
        self.file = "words.txt"
        self.track = []
        self.sameN = []
        self.visited = []
        
        self.queue = []
    
        self.not_found = True
        
        self.start_list = []
        self.new_list = []
        self.target_list =[]
        self.new_level = []
         
        f = open('words.txt', 'r')
        
        for word in f:
            word = word.strip()
            if len(word) == 6:
                self.sameN.append(word)
    
    
        #print len(self.sameN)
        
        self.word_list1 = self.changeLetter("snakes")
        self.word_list2 = self.changeLetter("brains")
        #for r in self.word_list2:
            #print r
            
            
            
            
    
    def findtrack(self):
        
        #print "in findtrack function"
        
        
        for q in self.word_list1:
            self.queue.append(q)
            
        
        while self.not_found and len(self.queue) > 0:
            
            word_to_check = self.queue.pop(0)
            
            #if word_to_check in self.sameN:
                #print word_to_check
            self.track.append(word_to_check)
            
            #print word_to_check
                
            if word_to_check in self.word_list2:
                self.not_found = False
                print "success"
                #for p in self.track:
                    #print p
                break
                
            else:
                self.check_new_level(word_to_check)
            
    
    
    def check_new_level (self, upper_level_word):
        
        #print "in check new level function"
        
        word = upper_level_word
        new_list = Ladder.changeLetter(self, upper_level_word)
        
        for k in new_list:
            
            if k not in self.visited:
                self.visited.append(k)
                self.queue.append(k)
        
    
    def changeLetter(self, base_word):
        
        #print "in changeLetter function"

        
        alphabet = ("a", "b", "c", "d", "e","f","g","h","i","j","k","l"
        ,"m","n","o","p","q","r","s","t","u","v","w","x","y","z")
        
        new_word_list = []
        s = list(base_word)
        
        for w in range(0,6):
            
            for l in range(26):
                
                s[w] = alphabet[l]
                
                new_word = "".join(s)
                
                if new_word in self.sameN:
                    new_word_list.append(new_word)
                
            s = list(base_word)
            
        return new_word_list


def main():
    ladder = Ladder()
    ladder.findtrack()
    

if __name__=='__main__':
    main()
