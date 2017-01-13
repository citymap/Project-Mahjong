#!/usr/bin/env python3

from TenhouDecoder import tileToByte

assert tileToByte("1m") == 0b00000001
assert tileToByte("2m") == 0b00000010
assert tileToByte("3m") == 0b00000011
assert tileToByte("4m") == 0b00000100
assert tileToByte("5m") == 0b00000101
assert tileToByte("6m") == 0b00000110
assert tileToByte("7m") == 0b00000111
assert tileToByte("8m") == 0b00001000
assert tileToByte("9m") == 0b00001001

assert tileToByte("1p") == 0b00010001
assert tileToByte("2p") == 0b00010010
assert tileToByte("3p") == 0b00010011
assert tileToByte("4p") == 0b00010100
assert tileToByte("5p") == 0b00010101
assert tileToByte("6p") == 0b00010110
assert tileToByte("7p") == 0b00010111
assert tileToByte("8p") == 0b00011000
assert tileToByte("9p") == 0b00011001

assert tileToByte("1s") == 0b00100001
assert tileToByte("2s") == 0b00100010
assert tileToByte("3s") == 0b00100011
assert tileToByte("4s") == 0b00100100
assert tileToByte("5s") == 0b00100101
assert tileToByte("6s") == 0b00100110
assert tileToByte("7s") == 0b00100111
assert tileToByte("8s") == 0b00101000
assert tileToByte("9s") == 0b00101001

assert tileToByte("ew") == 0b00110001
assert tileToByte("sw") == 0b00110010
assert tileToByte("ww") == 0b00110011
assert tileToByte("nw") == 0b00110100
assert tileToByte("rd") == 0b00110101
assert tileToByte("wd") == 0b00110110
assert tileToByte("gd") == 0b00110111

assert tileToByte("1m1") == 0b01000001
assert tileToByte("2m1") == 0b01000010
assert tileToByte("3m1") == 0b01000011
assert tileToByte("4m1") == 0b01000100
assert tileToByte("5m1") == 0b01000101
assert tileToByte("6m1") == 0b01000110
assert tileToByte("7m1") == 0b01000111
assert tileToByte("8m1") == 0b01001000
assert tileToByte("9m1") == 0b01001001
assert tileToByte("1p1") == 0b01010001
assert tileToByte("2p1") == 0b01010010
assert tileToByte("3p1") == 0b01010011
assert tileToByte("4p1") == 0b01010100
assert tileToByte("5p1") == 0b01010101
assert tileToByte("6p1") == 0b01010110
assert tileToByte("7p1") == 0b01010111
assert tileToByte("8p1") == 0b01011000
assert tileToByte("9p1") == 0b01011001
assert tileToByte("1s1") == 0b01100001
assert tileToByte("2s1") == 0b01100010
assert tileToByte("3s1") == 0b01100011
assert tileToByte("4s1") == 0b01100100
assert tileToByte("5s1") == 0b01100101
assert tileToByte("6s1") == 0b01100110
assert tileToByte("7s1") == 0b01100111
assert tileToByte("8s1") == 0b01101000
assert tileToByte("9s1") == 0b01101001
assert tileToByte("ew1") == 0b01110001
assert tileToByte("sw1") == 0b01110010
assert tileToByte("ww1") == 0b01110011
assert tileToByte("nw1") == 0b01110100
assert tileToByte("rd1") == 0b01110101
assert tileToByte("wd1") == 0b01110110
assert tileToByte("gd1") == 0b01110111

print("Pass!")

