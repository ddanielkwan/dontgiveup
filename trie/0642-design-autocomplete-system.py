# Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character '#').

# You are given a string array sentences and an integer array times both of length n where sentences[i] is a previously typed sentence and times[i] is the corresponding number of times the sentence was typed. For each input character except '#', return the top 3 historical hot sentences that have the same prefix as the part of the sentence already typed.

# Here are the specific rules:

# The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
# The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences have the same hot degree, use ASCII-code order (smaller one appears first).
# If less than 3 hot sentences exist, return as many as you can.
# When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.


class TrieNode:
    def __init__(self):
        self.children = {}
        self.sentences = defaultdict(int)
        #setenneces here will be used to count number of times ach sentence was type

    def add_to_trie(self, sentence, count):
        # 
# O(NL) and sentence inserted into L nodes so its larger
        node = self
        # so at node path "i lo" and "i l" these nodes etncnes will both have "i love you":5
        for c in sentence: #create trie nodes for all characters
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            #add count to current sentence count times
            #at each trie node we have a hshmap, map holds all setnences we have in current path as prefix
            # beacsue we need ot return setnences that have been typed, we need to count sentence

            node.sentences[sentence] += count
class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        for sentence,count in zip(sentences,times):
            self.root.add_to_trie(sentence,count)
        self.curr_sentence = []
        self.curr_node = self.root
        self.dead = TrieNode()

    def input(self, c: str) -> List[str]:
        #currsentence represetes current sentence we are trying to type
        #and curr node which is where we are located, whenver we start new sentence, currnode shoudl be root
        #c == '#' finsihed typing sentence add currstence as stribng to trie and reset vairalbes
        #c != '#' , c is child of currNode there are some existing setencnes that have current setennce we are typeing as prefix, add c to currsetnence, then go to child node and fetch stences have the current setence as prefix, store in ashmap andsort by count
        if c == "#"        :
            curr_sentence = "".join(self.curr_sentence)
            self.root.add_to_trie(curr_sentence, 1) #add one count
            self.curr_sentence = [] #reset
            self.curr_node = self.root #reset
            return []
        self.curr_sentence.append(c) #not finsihed typing so we add to our setnecne
        #if c!='#' but c is not child of currnode, means no existing sentences we are typing as prefix, so we need to add c to currcstence and return empty
        if c not in self.curr_node.children:
            self.curr_node = self.dead#???
            return []
        
        self.curr_node = self.curr_node.children[c] #keep going
        sentences = self.curr_node.sentences #how many sentences we have now
        sorted_sentences = sorted(sentences.items(), key=lambda x: (-x[1],x[0])) #sort by highest number and alphabeticla for key

        ans = []
        for i in range(min(3, len(sorted_sentences))):
            ans.append(sorted_sentences[i][0])
        return ans

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)