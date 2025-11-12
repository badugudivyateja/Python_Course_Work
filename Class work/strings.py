# 1. Defining Strings
s = ''
s = ""
s = ''' '''
s = "' '"

# 2. Concatenation
name = 'Ajay'
name1 = "Krishna"
print(name + name1)        # AjayKrishna
print(name + ' ' + name1)  # Ajay Krishna

# 3. Repetition
print(name * 10)
print('*' * 100)
print('-' * 10)

# 4. Indexing
name = 'Ajay Kumar'
print(name[3])   # y
print(name[-2])  # a
print(name[-5])  # K
print(name[1])   # j

# 5. Slicing
names = 'AjayKrishnaSatishNishithaPreethiRuchitha'
print(names[0:4])   # Ajay
print(names[:4])    # Ajay
print(names[4:11])  # Krishna
print(names[11:17]) # Satish
print(names[17:25]) # Nishitha
print(names[25:32]) # Preethi
print(names[32:40]) # Ruchitha
print(names[32:])   # Ruchitha
print(names[0:4:2]) # Aa
print(names[::3])   # Ayinasiiaehuia
print(names[-8:])   # Ruchitha

# Reverse string
print(names[::-1])  # ahtihcuRihteerPahtihsiNhsitaSanhsirKyajA

# Reverse partial sections
print(names[4::-1])   # KyajA
print(names[3::-1])   # yajA
print(names[10:4:-1]) # anhsir
print(names[10:3:-1]) # anhsirK
print(names[16:10:-1])# hsitaS
print(names[24:16:-1])# ahtihsiN
print(names[31:24:-1])# ihteerP
print(names[39:31:-1])# ahtihcuR

# 6. Membership Operators
print('Ajay' in names)      # True
print('nithin' in names)    # False
print('priya' in names)     # False
print('sahithi' not in names) # True

# 7. Case Methods
print(names.upper())
print(names.lower())
print(names.swapcase())

l = 'python programming language'
print(l.capitalize())  # Python programming language
print(l.title())       # Python Programming Language
print("ß".casefold())  # ss

# 8. Alignment Methods
print(l.center(100, '*'))
print(l.center(50, '*'))
print(l.center(50, '-'))
print(l.center(50, '_'))
print(l.ljust(50, '-'))
print(l.ljust(50, ' ') + ':')
print(l.rjust(50, '-'))

# 9. Zero Fill
print('2'.zfill(6))       # 000002
print('202'.zfill(6))     # 000202
print('202123'.zfill(6))  # 202123

# 10. Searching and Counting
print(names.find('j'))     # 1
print(names.find('a'))     # 2
print(names.find('Ajay'))  # 0
print(names.find('z'))     # -1
print(names.rfind('a'))    # 39
print(names.index('K'))    # 4
print(names.index('a'))    # 2
print(names.rindex('a'))   # 39
print(names.count('a'))  # 5
print(names.count('e'))  # 2
print(names.count('i'))  # 6

# 11. Replace
print(names.replace('a', '*'))
print(names.replace('sh', ''))
print(names.replace('sh', '00'))
print(names.replace('sh', '-00-'))
print(names.replace('Ajay', 'Anirudh'))
