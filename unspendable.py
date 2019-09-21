#! /usr/bin/env python3

import sys
import hashlib
import binascii

dhash = lambda x: hashlib.sha256(hashlib.sha256(x).digest()).digest()
b58_digits = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

seeds = [ '0','2','5','7','10','12','15','17','20','22','25',
         '27','30','32','35','37','40','42','45','48','50',
         '53','55','58','60','63','65','68','70','73','75',
         '78','80','83','85','88','91','93','96','98','101',
         '103','106','108','111','113','116','118','121',
         '123','126','128','131','134','136','139','141','144' ]


def base58_check_encode(b, version):
    d = version + b
    address = d + dhash(d)[:4]

    # Convert big‐endian bytes to integer
    n = int('0x0' + binascii.hexlify(address).decode('utf8'), 16)

    # Divide that integer into base58
    res = []
    while n > 0:
        n, r = divmod (n, 58)
        res.append(b58_digits[r])
    res = ''.join(res[::-1])

    # Encode leading zeros as base58 zeros
    czero = 0
    pad = 0
    for c in d:
        if c == czero: pad += 1
        else: break
    return b58_digits[0] * pad + res


def base58_decode (s, version):
    # Convert the string to an integer
    n = 0
    for c in s:
        n *= 58
        if c not in b58_digits:
            raise Exception
        digit = b58_digits.index(c)
        n += digit

    # Convert the integer to bytes
    h = '%x' % n
    if len(h) % 2:
        h = '0' + h
    res = binascii.unhexlify(h.encode('utf8'))

    # Add padding back.
    pad = 0
    for c in s[:-1]:
        if c == b58_digits[0]: pad += 1
        else: break
    k = version * pad + res

    addrbyte, data, chk0 = k[0:1], k[1:-4], k[-4:]
    return data


def generate (prefix_string, name):


    first_char = prefix_string[0]
    seed_ref = b58_digits.find(first_char)
    # print(generate(ps, name , int(keys[index])))

    if first_char == 'D':
        prefix_char_seed = 30
    elif first_char == '1':
        prefix_char_seed = 0
    elif first_char == 'm':
        prefix_char_seed = 111 
    else:
        raise Exception('unknown network')

    prefix_char_seed = int(seeds[seed_ref])

    prefix_bytes = (prefix_char_seed).to_bytes(1, 'big')


    # Pad and prefix.
    prefixed_name = prefix_string + name 
    padded_prefixed_name = prefixed_name.ljust(34, 'Z')

    # Decode, ignoring (bad) checksum.
    decoded_address = base58_decode(padded_prefixed_name, prefix_bytes)

    # Re-encode, calculating checksum.
    address = base58_check_encode(decoded_address, prefix_bytes)

    # Double-check.
    assert base58_decode(address, prefix_bytes) == decoded_address

    return address


if __name__ == '__main__':

    prefix_string = sys.argv[1]
    name = sys.argv[2]
    
    print(generate(prefix_string, name))
