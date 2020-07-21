# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 08:54:26 2020

@author: Igorion
"""


from src import RadixTreeSet


def test_init():
    a = RadixTreeSet.RadixTree('12', '13', '123', '12345', '123465', '145678')
    b = {'12', '13', '123', '12345', '123465', '145678'}
    assert repr(sorted(a)) == repr(sorted(b))


def test_repr():
    a = RadixTreeSet.RadixTree('a', 'asd3asd', 'dsf', '12312', '123', '1')
    b = {'a', 'asd3asd', 'dsf', '12312', '123', '1'}
    assert repr(sorted(a)) == repr(sorted(b))


def test_len():
    a = RadixTreeSet.RadixTree('a', 'asd3asd', 'dsf', '12312', '123', '1')
    b = {'a', 'asd3asd', 'dsf', '12312', '123', '1'}
    assert len(a) == len(b)


def test_extend():
    a = RadixTreeSet.RadixTree()
    b = {'a', 'asd3asd', 'dsf', '12312', '123', '1', '123'}
    a.extend(b)
    assert repr(sorted(a)) == repr(sorted(b))


def test_copy():
    a = RadixTreeSet.RadixTree('a', 'asd3asd', 'dsf', '12312', '123', '1')
    b = a.copy()
    assert sorted(a) == sorted(b)
    b.add('dsfasdas')
    assert sorted(a) != sorted(b)


def test_clear():
    a = RadixTreeSet.RadixTree('a', 'asd3asd', 'dsf', '12312', '123', '1', '123')
    b = RadixTreeSet.RadixTree()
    a.clear()
    assert repr(a) == repr(b)


def test_union_iter():
    a = RadixTreeSet.RadixTree('12', '13')
    b = RadixTreeSet.RadixTree('12', '123')
    c = {'12', '13'}
    d = {'12', '123'}
    assert sorted(a.union(b)) == sorted(c.union(d))


def test_difference():
    a = RadixTreeSet.RadixTree('12', '13', '_')
    b = RadixTreeSet.RadixTree('12', '123', '1234', 'a')
    c = {'12', '13', '_'}
    d = {'12', '123', '1234', 'a'}
    assert sorted(a.difference(b)) == sorted(c.difference(d))
    assert sorted(b.difference(a)) == sorted(d.difference(c))
    assert sorted(a.difference(d)) == sorted(c.difference(b))
    assert sorted(d.difference(a)) == sorted(b.difference(c))


def test_difference_update():
    a = RadixTreeSet.RadixTree('12', '13', '_')
    b = RadixTreeSet.RadixTree('12', '123', '1234', 'a')
    c = {'12', '13', '_'}
    d = {'12', '123', '1234', 'a'}
    a.difference_update(b)
    c.difference_update(d)
    assert sorted(a) == sorted(c)


def test_discard():
    a = RadixTreeSet.RadixTree('12', '13', '_')
    b = RadixTreeSet.RadixTree('12', '123', '1234', 'a')
    c = {'12', '13', '_'}
    d = {'12', '123', '1234', 'a'}
    a.discard(b)
    c.discard(d)
    assert sorted(a) == sorted(c)


def test_intersection():
    a = RadixTreeSet.RadixTree('12', '13', '_')
    b = RadixTreeSet.RadixTree('12', '123', '1234', 'a')
    c = {'12', '13', '_'}
    d = {'12', '123', '1234', 'a'}
    assert sorted(a.intersection(b)) == sorted(c.intersection(d))


def test_intersection_update():
    a = RadixTreeSet.RadixTree('12', '13', '_')
    b = RadixTreeSet.RadixTree('12', '123', '1234', 'a')
    c = {'12', '13', '_'}
    d = {'12', '123', '1234', 'a'}
    a.intersection_update(b)
    c.intersection_update(d)
    assert sorted(a) == sorted(c)


def test_isdisjoint():
    a = RadixTreeSet.RadixTree('12', '13', '_')
    b = RadixTreeSet.RadixTree('12', '14', '15', 'a')
    c = RadixTreeSet.RadixTree('112', '126', '15', 'c')
    d = {'12', '13', '_'}
    e = {'12', '14', '15', 'a'}
    f = {'112', '126', '15', 'c'}
    assert a.isdisjoint(b) == d.isdisjoint(e)
    assert a.isdisjoint(c) == d.isdisjoint(f)
    assert b.isdisjoint(c) == e.isdisjoint(f)


def test_issubset():
    a = RadixTreeSet.RadixTree('12', '13', '14')
    b = RadixTreeSet.RadixTree('12', '13', '15', '14')
    c = RadixTreeSet.RadixTree('112', '12', '13', '14')
    d = {'12', '13', '14'}
    e = {'12', '13', '15', '14'}
    f = {'112', '12', '13', '14'}
    assert a.issubset(b) == d.issubset(e)
    assert a.issubset(c) == d.issubset(f)
    assert b.issubset(c) == e.issubset(f)


def test_issuperset():
    a = RadixTreeSet.RadixTree('12', '13', '14', '15')
    b = RadixTreeSet.RadixTree('12', '13', '14')
    c = RadixTreeSet.RadixTree('112', '12', '13', '14')
    d = {'12', '13', '14', '15'}
    e = {'12', '13', '14'}
    f = {'112', '12', '13', '14'}
    assert a.issuperset(b) == d.issuperset(e)
    assert a.issuperset(c) == d.issuperset(f)
    assert b.issuperset(c) == e.issuperset(f)


    # fails sometimes with more than one item, probably due to different order in set() and RadixTree()
def test_pop():
    a = RadixTreeSet.RadixTree('15')
    b = {'15'}
    assert a.pop() == b.pop()
    assert sorted(a) == sorted(b)


def test_remove():
    a = RadixTreeSet.RadixTree('12', '13', '14', '15')
    b = {'12', '13', '14', '15'}
    a.remove('13')
    b.remove('13')
    assert sorted(a) == sorted(b)


def test_symmetric_difference():
    a = RadixTreeSet.RadixTree('12', '13', '14', '15')
    b = RadixTreeSet.RadixTree('12', '13', '18', '20')
    c = {'12', '13', '14', '15'}
    d = {'12', '13', '18', '20'}
    assert sorted(a.symmetric_difference(b)) == sorted(c.symmetric_difference(d))


def test_symmetric_difference_update():
    a = RadixTreeSet.RadixTree('12', '13', '14', '15')
    b = RadixTreeSet.RadixTree('12', '13', '18', '20')
    c = {'12', '13', '14', '15'}
    d = {'12', '13', '18', '20'}
    a.symmetric_difference_update(b)
    c.symmetric_difference_update(d)
    assert sorted(a) == sorted(c)


def test_update():
    a = RadixTreeSet.RadixTree('1')
    b = RadixTreeSet.RadixTree('2')
    c = RadixTreeSet.RadixTree('13', '14')
    a_ = {'1'}
    b_ = {'2'}
    c_ = {'13', '14'}
    c__ = ['13', '14', '1000']
    a.update(b)
    a_.update(b)
    assert sorted(a) == sorted(a_)
    a.update(b_, c_, c__)
    a_.update(b, c, c__)
    assert sorted(a) == sorted(a_)


def test_print_items(capsys):
    a = RadixTreeSet.RadixTree('a', 'asd3asd', 'dsf', '12312', '123', '1', '123')
    b = {'a', 'asd3asd', 'dsf', '12312', '123', '1', '123'}
    a.print_items()
    captured = capsys.readouterr()
    a_out = captured.out
    print(sorted(b))
    captured = capsys.readouterr()
    b_out = captured.out
    assert a_out == b_out


def test_add():
    a = RadixTreeSet.RadixTree('a', 'asd3asd', 'dsf', '12312', '123', '1', '123')
    b = RadixTreeSet.RadixTree()
    b.add('asd3asd')
    b.add('a')
    b.add('123')
    b.add('1')
    b.add('12312')
    b.add('dsf')
    c = {'a', 'asd3asd', 'dsf', '12312', '123', '1', '123'}
    assert a.root == b.root
    assert repr(sorted(b)) == repr(sorted(c))
    
    
def test_get_len():
    a = RadixTreeSet.RadixTree('a', 'asd3asd')
    assert a.get_len() == 2
    a.add('23')
    assert a.get_len() == 3
    a.remove('asd3asd')
    assert a.get_len() == 2
    
    
def test_op_add():
    a = RadixTreeSet.RadixTree('a', 'asd3asd')
    b = RadixTreeSet.RadixTree('dsf', '12312', '123', '1', '123')
    c = RadixTreeSet.RadixTree('a', 'asd3asd', 'dsf', '12312', '123', '1', '123')
    d = a + b
    assert sorted(c) == sorted(d)
    
    
def test_op_lt():
    a = RadixTreeSet.RadixTree('a')
    b = RadixTreeSet.RadixTree('a', 'asd3asd')
    c = RadixTreeSet.RadixTree('a', 'asd3asd', '23')
    assert (a < b) == True
    assert (b < b) == False
    assert (c < b) == False
    
    
def test_op_gt():
    a = RadixTreeSet.RadixTree('a')
    b = RadixTreeSet.RadixTree('a', 'asd3asd')
    c = RadixTreeSet.RadixTree('a', 'asd3asd', '23')
    assert (a > b) == False
    assert (b > b) == False
    assert (c > b) == True
    
    
def test_op_et():
    a = RadixTreeSet.RadixTree('a')
    b = RadixTreeSet.RadixTree('a', 'asd3asd')
    c = RadixTreeSet.RadixTree('a', 'asd3asd', '23')
    assert (a == b) == False
    assert (b == b) == True
    assert (c == b) == False
    

def test_children():
    a = RadixTreeSet.RadixTree('12', '13', '123', '12345', 'a', '123465', '145678')
    assert a.children('123') == {'123', '12345', '123465'}
    

def test_parents():
    a = RadixTreeSet.RadixTree('12', '13', '123', '12345', 'a', '123465', '145678')
    assert a.parents('1234') == {'12', '123'}
