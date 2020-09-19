import hashlib
import math
 
rotate_amounts = [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
                  5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20,
                  4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
                  6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21]
 
consts = [int(abs(math.sin(i+1)) * 2**32) & 0xFFFFFFFF for i in range(64)]
 
buffer_inits = [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476]
 
funcs =     16 * [lambda x, y, z: (x & y) | (~x & z)] + \
            16 * [lambda x, y, z: (z & x) | (~z & y)] + \
            16 * [lambda x, y, z: x ^ y ^ z] + \
            16 * [lambda x, y, z: y ^ (x | ~z)]
 
index_funcs =     16 * [lambda i: i] + \
                  16 * [lambda i: (5*i + 1) % 16] + \
                  16 * [lambda i: (3*i + 5) % 16] + \
                  16 * [lambda i: (7*i) % 16]
 
def left_rotate(x, amount):
    x &= 0xFFFFFFFF
    return ((x<<amount) | (x>>(32-amount))) & 0xFFFFFFFF
 
def md5(message):
 
    # Шаг 1
    message = bytearray(message)            
    orig_len_in_bits = (8 * len(message)) & 0xFFFFFFFFFFFFFFFF
    message.append(0x80)
    while len(message) % 64 != 56:
        message.append(0)
     
    # Шаг 2
    message += orig_len_in_bits.to_bytes(8, byteorder='little')
    
    # Шаг 3
    hash_pieces = buffer_inits[:]
 
    # Шаг 4
    for chunks in range(0, len(message), 64):
        a, b, c, d = hash_pieces
        chunk = message[chunks:chunks+64]
        
        for i in range(64):
            f = funcs[i](b, c, d)
            g = index_funcs[i](i)
            to_rotate = a + f + consts[i] + int.from_bytes(chunk[4*g:4*g+4], byteorder='little')
            new_b = (b + left_rotate(to_rotate, rotate_amounts[i])) & 0xFFFFFFFF
            a, b, c, d = d, new_b, b, c
            
        for i, val in enumerate([a, b, c, d]):
            hash_pieces[i] += val
            hash_pieces[i] &= 0xFFFFFFFF
            
    digest = sum(x<<(32*i) for i, x in enumerate(hash_pieces))
    
    # Шаг 5
    raw = digest.to_bytes(16, byteorder='little')
    return '{:032x}'.format(int.from_bytes(raw, byteorder='big'))
 
if __name__ == '__main__':
    message = input('Данные: ')
    message = bytes(message, encoding = 'utf-8')
    message_copy = bytearray(message)
    message_copy = hashlib.md5(message_copy).hexdigest()

    print('Резултат собственной функции: {}'.format(md5(message)))
    print('Резултат встроенной функции:  {}'.format(message_copy))