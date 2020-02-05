#!/bin/bash

unspendable_test() {

: ..

T="DD  DDDDDDDDD"
for X in 1 2 3 4 5 6 7 8 9s 9t 9u 9v 9w 9x 9y 9z A B C D DC DCx E F G H J K mv
do
./unspendable.py $X "$T"
done  } 

unspendable_test

# This should always result in 020203

unspendable_test | sum | grep 9902023
