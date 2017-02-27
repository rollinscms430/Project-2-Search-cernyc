from random import choice

 
class Boggle(object):
    
    def __init__(self, board = [
                                    ['u', 'n', 't', 'h'],
	                                ['g', 'a', 'e', 's'],
	                                ['s', 'r', 't', 'r'],
	                                ['h', 'm', 'i', 'a']
                               ]):
                                   
        self.size = 4
        self.board = board
        
 
    def play(self, tree, found):
        for r in range(0, self.size):
            for c in range(0, self.size):
                self.search_r(tree, found, r, c)
 
    def search_r(self, tree, found, row, col, path=None, node=None, word=None):
        letter = self.board[row][col]
        
        if node is None or path is None or word is None:
            node = tree.find_letter(letter)
            path = [(row, col)]
            word = letter
            
        else:
            node = node.find_letter(letter)
            path.append((row, col))
            word = word + letter
        if node is None:
            return
        elif node.stop:
            found.add(word)
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if (r >= 0 and r < self.size
                        and c >= 0 and c < self.size 
                        and not (r == row and c == col) 
                        and (r, c) not in path):
                    self.search_r(tree, found, r, c, path[:], node, word[:])
 
    def __repr__(self):
        return "Boggle(,size={0} board={1})".format(self.size, self.board)







class PrefixTree(object):
    def __init__(self, letter=None):
        self.letter = letter
        self.children = {}
        self.stop = False
 
    def add_word_tree(self, new_word):
        if len(new_word):
            letter = new_word[0]
            new_word = new_word[1:]
            if letter not in self.children:
                self.children[letter] = PrefixTree(letter);
            return self.children[letter].add_word_tree(new_word)
        else:
            self.stop = True
            return self
 
    def find_letter(self, letter):
        if letter not in self.children:
            return None
        return self.children[letter]
 
    def __repr__(self):
        return "PrefixTree(letter={0}, stop={1})".format(self.letter, self.stop)



def load_tree(tree):
    list_words = []
    f = open('words.txt', 'r')
    
    for line in f:
        if (len(line)) < 10:
            word = line.rstrip()
            tree.add_word_tree(word)
 
def main():
    boggle = Boggle()
    tree = PrefixTree()
    load_tree(tree)
    found = set()
    boggle.play(tree, found)
    for word in sorted(found):
        print word
    #print boggle
 
if __name__ == '__main__':
    main()