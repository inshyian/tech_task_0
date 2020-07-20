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
    def __init__(self, *codes) -> None:
        self.root = dict()
        self.len = 0
        if len(codes) > 0:
            for code in codes:
                self.add(code)

    def __repr__(self) -> str:
        return "%s" % (self.get_items())
        # return "%s(%s)" % (self.__class__.__name__, codes)

    def __iter__(self) -> iter:
        return iter(self.get_items())

    def __len__(self):
        return self.len

    def extend(self, codes) -> None:
        for code in codes:
            self.add(code)

    def copy(self):
        copy = RadixTree()
        copy.extend(self.get_items())
        return copy

    def clear(self):
        self.root = dict()

    def union(self, args):
        new = self.copy()
        for arg in args:
            new.add(arg)
        return new

    def difference(self, arg):
        items = self.get_items()
        new = RadixTree()
        new.extend(items.difference(arg))
        return new

    def difference_update(self, arg) -> None:
        items = self.get_items()
        items.difference_update(arg)
        self.clear()
        self.extend(items)

    def discard(self, arg) -> None:
        items = self.get_items()
        items.discard(arg)
        self.clear()
        self.extend(items)

    def intersection(self, arg):
        items = self.get_items()
        new = RadixTree()
        new.extend(items.intersection(arg))
        return new

    def intersection_update(self, arg) -> None:
        items = self.get_items()
        items.intersection_update(arg)
        self.clear()
        self.extend(items)

    def isdisjoint(self, arg) -> bool:
        items = self.get_items()
        return items.isdisjoint(arg)

    def issubset(self, arg) -> bool:
        items = self.get_items()
        return items.issubset(arg)

    def issuperset(self, arg) -> bool:
        items = self.get_items()
        return items.issuperset(arg)

    def pop(self) -> set():
        items = self.get_items()
        ret_item = items.pop()
        self.clear()
        self.extend(items)
        return ret_item

    def remove(self, arg) -> None:
        items = self.get_items()
        items.remove(arg)
        self.clear()
        self.extend(items)

    def symmetric_difference(self, arg):
        items = self.get_items()
        new = RadixTree()
        new.extend(items.symmetric_difference(arg))
        return new

    def symmetric_difference_update(self, arg) -> None:
        items = self.get_items()
        items.symmetric_difference_update(arg)
        self.clear()
        self.extend(items)

    def update(self, *args) -> None:
        for arg in args:
            self.extend(arg)

    def add(self, code) -> None:
        current_dict = self.root
        i = 0
        while i < len(code):
            keys = current_dict.keys()
            # try to find matches key in current dictionary
            # (by comparing first char in current 'key' with current char in 'code')
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
                        self.len += 1
                    # if 'code' ended, split's current_key, creates new dict,
                    # adds _end entry (to mark word's ending):
                    elif i == len(code):
                        current_dict[current_key[:ii]] = {current_key[ii:]:current_dict.pop(current_key)}
                        current_dict[current_key[:ii]][_end] = _end
                        self.len += 1
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
                self.len += 1
                break

    def __get_codes_depth(self, root, prefix, codes_found) -> None:
        if _end in root:
            codes_found.add(prefix)
        for key in root.keys():
            if key != _end:
                self.__get_codes_depth(root[key], prefix + key, codes_found)

    def get_items(self) -> set():
        items = set()
        self.__get_codes_depth(self.root, '', items)
        return items

    def print_items(self) -> None:
        print(sorted(self.get_items()))

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
                    # call function to find and save all codes from current_dict[key] and deeper
                    elif i == len(code):
                        self.__get_codes_depth(current_dict[key], prefix + key[1:], codes_found)
                    # go to deeper to next dict
                    elif ii == len(key):
                        current_dict = current_dict[key]
                    elif code[i] != key[ii]:
                        raise CodeNotExist()
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
                        raise CodeNotExist()
                    break
            else:
                raise CodeNotExist()
        return codes_found
