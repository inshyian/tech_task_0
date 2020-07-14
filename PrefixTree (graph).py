# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 00:29:09 2020

@author: Igorion
"""


# GraphPrefixTrie

class CodeNotExist(Exception):
    pass

class TrieNode():
    def __init__(self) -> None:
        self.child = dict()
        self.endOfCode = False

class GraphPrefixTrie():
    def __init__(self, *args) -> None:
        self.root = TrieNode()
        self.insert_codes(*args)
    
    def insert_code(self, code) -> None:
        current = self.root
        for char in code:
            if char in current.child:
                pass
            else:
                current.child[char] = TrieNode()
            current = current.child[char]
        current.endOfCode = True
    
    def insert_codes(self, *args) -> None:
        for code in args:
            self.insert_code(code)

    def __depth_codes(self, node, prefix, results) -> None:
        if node.endOfCode:
            results.add(prefix)
        for char in node.child:
            self.__depth_codes(node.child[char], prefix + char, results)
            
    def print_all_codes(self) -> None:
        results = set()
        self.__depth_codes(self.root, '', results)
        print(sorted(results))
            
    def children(self, prefix) -> set:
        current = self.root
        for char in prefix:
            if char in current.child:
                current = current.child[char]
            else:
                raise CodeNotExist
        results = set()
        self.__depth_codes(current, prefix, results)
        return results
            
    def parents(self, prefix) -> set:
        current = self.root
        results = set()
        code = ''
        for char in prefix:
            if char in current.child.keys():
                code = code + char
                if current.child[char].endOfCode:
                    results.add(code)
                current = current.child[char]
            else:
                raise CodeNotExist
        return results
    
trie_ = GraphPrefixTrie('12', '13', '123', '12345', '123465', '145678')
trie_.insert_codes("word1", 'word2', 'word22')
trie_.insert_codes('test', 't', 'testing', 'testers', '123465', '145678')

trie_.print_all_codes()

trie_.children('123')

trie_.parents('1234')

trie_.parents('14567')

trie_.root