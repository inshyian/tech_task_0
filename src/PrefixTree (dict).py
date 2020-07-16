# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 00:26:04 2020

@author: Igorion
"""


# DictPrefixTree

_end = '_end_'

class CodeNotExist(Exception):
    pass

class DictPrefixTree():    
    def __init__(self, *args) -> None:
        self.root = dict()
        if len(args) > 0:
            self.insert_codes(*args)
        
    def insert_codes(self, *codes) -> None:           
        for code in codes:
            current_dict = self.root
            for char in code:
                current_dict = current_dict.setdefault(char, {})
            current_dict[_end] = _end   
            
    def __get_codes_depth(self, root, prefix, codes_found):
        if _end in root:
            codes_found.add(prefix)
        for char in root.keys():
            if char != _end:
                self.__get_codes_depth(root[char], prefix + char, codes_found)        
    
    def print_all_codes(self) -> None:
        results = set()
        self.__get_codes_depth(self.root, '', results)
        print(sorted(results))
            
    def children(self, prefix) -> set:
        current_dict = self.root
        for char in prefix:
            if char in current_dict.keys():
                current_dict = current_dict[char]
            else:
                raise CodeNotExist
        results = set()
        self.__get_codes_depth(current_dict, prefix, results)
        return results
            
    def parents(self, prefix) -> set:
        current_dict = self.root
        results = set()
        code = ''
        for char in prefix:
            if char in current_dict.keys():
                code = code + char
                if _end in current_dict[char]:
                    results.add(code)
                current_dict = current_dict[char]
            else:
                raise CodeNotExist
        return results
    
    
# Testing
trie = DictPrefixTree('12', '13', '123', '12345', '123465', '145678')
trie.insert_codes("word1", 'word2', 'word22')
trie.insert_codes('test', 't', 'testing', 'testers', '123465', '145678')

trie.print_all_codes()

trie.children('123')

trie.parents('1234')

trie.parents('12345')

trie.parents('14567')

trie.root
