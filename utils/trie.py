#!/usr/bin/env python 2.7
# -*- coding: utf-8 -*-

#
# Copyright (c) 2021 PanXu, Inc. All Rights Reserved
#

import collections

class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

class Trie:
    """
    构建一个 Trie 用来进行查找，判断一个词是否在 Trie 里面
    """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        
        current = self.root
        for letter in word:
            current = current.children[letter]
        current.is_word = True

    def search(self, word):
        current = self.root
        for letter in word:
            current = current.children.get(letter)

            if current is None:
                return False
        return current.is_word

    def startsWith(self, prefix):
        current = self.root
        for letter in prefix:
            current = current.children.get(letter)
            if current is None:
                return False
        return True

    def enumerateMatch(self, word, space="_", backward=False):
        matched = []
        ## while len(word) > 1 does not keep character itself, while word keed character itself
        while len(word) > 1:
            if self.search(word):
                matched.append(space.join(word[:]))
            del word[-1]
        return matched

