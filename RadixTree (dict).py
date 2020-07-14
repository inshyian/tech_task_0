# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 00:31:04 2020

@author: Igorion
"""


# DictRadixTree

_end = '_end_'

class CodeNotExist(Exception):
    pass

class RadixTree():    
    def __init__(self, *args) -> None:
        self.root = dict()
        if len(args) > 0:
            self.insert_codes(*args)
    
    def insert_codes(self, *codes) -> None:           
        for code in codes:
            current_dict = self.root
            i = 0
            while i < len(code):
                # try to find matches key in current dictionary 
                # (by comparing first char in current 'key' with current char in 'code')
                keys = current_dict.keys()
                for key in keys:
                    if key[0] == code[i]:      
                        current_key = key
                        ii = 0
                        # iterators moves synchronously to skip same chars in 'code' and in 'current_key':
                        while i < len(code) and ii < len(current_key) and code[i] == current_key[ii]:
                            i += 1
                            ii += 1
                        # if 'code' and 'current_key' ended, creates _end entry (mark word's ending):
                        if i == len(code) and ii == len(current_key):
                            current_dict = current_dict[current_key]
                            current_dict[_end] = _end
                        # if 'code' ended, split's current_key, creates new dict, 
                        # adds _end entry (to mark word's ending):
                        elif i == len(code):
                            current_dict[current_key[:ii]] = {current_key[ii:]:current_dict.pop(current_key)}
                            current_dict[current_key[:ii]][_end] = _end
                        # if 'current_key' ended, go depth to next dict:
                        elif ii == len(current_key):
                            current_dict = current_dict[current_key]
                        # if code[i] != current_key[ii] split's 'current_key' and moves depth 
                        # to new dict
                        else:                  
                            current_dict[current_key[:ii]] = {current_key[ii:]:current_dict.pop(current_key)}
                            current_dict = current_dict[current_key[:ii]]
                        break
                # if failed to find matches key, create new dict {code[i:]:{_end:_end}}
                else:       
                    current_dict = current_dict.setdefault(code[i:], {_end:_end})
                    i = len(code)
         
    def __get_codes_depth(self, root, prefix, codes_found) -> None:
        if _end in root:
            codes_found.add(prefix)
        for key in root.keys():
            if key != _end:
                self.__get_codes_depth(root[key], prefix + key, codes_found)        
    
    def print_all_codes(self) -> None:
        codes_found = set()
        self.__get_codes_depth(self.root, '', codes_found)
        print(sorted(codes_found))
        
    def children(self, code) -> set():
        codes_found = set()
        prefix = ''
        current_dict = self.root
        i = 0
        while i < len(code):
            for key in current_dict.keys():
                if key[0] == code[i]:
                    ii = 0
                    # iterators moves synchronously to skip same chars and writes
                    # current char in 'code' to 'prefix' to save in 'codes_found'
                    while i < len(code) and ii < len(key) and code[i] == key[ii]:
                        prefix += code[i]
                        i += 1
                        ii += 1
                    # call f to find and save all codes from current_dict[key] and deeper
                    if i == len(code) and ii == len(key):
                        self.__get_codes_depth(current_dict[key], code, codes_found)
                    elif i == len(code):
                    # call f to find and save all codes from current_dict[key] and deeper
                        self.__get_codes_depth(current_dict[key], prefix + key[1:], codes_found)
                    elif ii == len(key):
                    # go to deeper to next dict
                        current_dict = current_dict[key]
                    elif code[i] != key[ii]:
                        CodeNotExist()
                    break
            else:
                raise CodeNotExist()
        return codes_found              
    
    def parents(self, code) -> set():
        codes_found = set()
        prefix = ''
        current_dict = self.root
        i = 0
        while i < len(code):
            for key in current_dict.keys():
                if key[0] == code[i]:
                    ii = 0
                    # iterators moves synchronously to skip same chars and writes
                    # current char in 'code' to 'prefix' to save in 'codes_found'
                    while i < len(code) and ii < len(key) and code[i] == key[ii]:
                        prefix += code[i]
                        i += 1
                        ii += 1
                    # if current 'key' is end of word add this to 'codes_found'
                    if i == len(code) and ii == len(key):
                        if _end in current_dict[key].keys():
                            codes_found.add(prefix + key[1:])
                        break
                    # 'code' ended, word end did not reached -> nothing to add to 'codes_found'
                    elif i == len(code):
                        break
                    # if current 'key' is end of word add this to 'codes_found'
                    # and go deeper to next dict
                    elif ii == len(key):
                        if _end in current_dict[key].keys():
                            codes_found.add(prefix + key[1:])
                        current_dict = current_dict[key]
                    elif code[i] != key[ii]:
                        CodeNotExist()
                    break
            else:
                raise CodeNotExist()
        return codes_found

# Testing    
rt_new = RadixTree('12', '13', '123', '12345', '123465', '145678')
rt_new.insert_codes("word1", 'word2', 'word22')
rt_new.insert_codes('test', 't', 'testing', 'testers', '123465', '145678')

rt_new.print_all_codes()

rt_new.parents('1234')

rt_new.children('123')

rt_new.root
