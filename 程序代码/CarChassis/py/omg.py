#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys

def prdef():
    print('print by def')
    return

def main():
    word = len(sys.argv)
    print('hello world')
    prdef()

if __name__ == '__main__':
    main()
