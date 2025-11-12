#Defining Strings
s=''
s=""
s=''' '''
s="' '"
#operations on Strings:
#1.Concatenation:
name='Ajay'
name1="Krishna"
print(name + name1)
'AjayKrishna'
name+ ' '+ name1
'Ajay Krishna'
name
'Ajay'
name * 10
'AjayAjayAjayAjayAjayAjayAjayAjayAjayAjay'
'*'*100
'****************************************************************************************************'
'-'*10
'----------'
name='Ajay Kumar'
name[3]
'y'
name[-2]
'a'
name[-5]
'K'
name[1]
'j'
names='AjayKrishnaSatishNishithaPreethiRuchitha'
names
'AjayKrishnaSatishNishithaPreethiRuchitha'
names[0:4]
'Ajay'
names[:4]
'Ajay'
names[4:11]
'Krishna'
names[11:17]
'Satish'
names[17:25]
'Nishitha'
names[25:32]
'Preethi'
names[32:40]
'Ruchitha'
names[32:]
'Ruchitha'
names[0:4:2]
'Aa'
names[::3]
'Ayinasiiaehuia'
names[-8:]
'Ruchitha'
names
'AjayKrishnaSatishNishithaPreethiRuchitha'
names[-15:-8]
'Preethi'
names[-23:-15]
'Nishitha'
names[-29:-23]
'Satish'
names[-36:-29]
'Krishna'
names[-40:-36]
'Ajay'
names[::-1]
'ahtihcuRihteerPahtihsiNhsitaSanhsirKyajA'
names
'AjayKrishnaSatishNishithaPreethiRuchitha'
names[4::-1]
'KyajA'
names[3::-1]
'yajA'
names[10:4]
''
names[10:4:-1]

'anhsir'
names[10:3:-1]
'anhsirK'
names[16:10:-1]
'hsitaS'
names[24:16:-1]
'ahtihsiN'
names[31:24:-1]
'ihteerP'
names[39:31:-1]
'ahtihcuR'
names
'AjayKrishnaSatishNishithaPreethiRuchitha'
'Ajay' in names
True
'nithin' in names
False
'priya' in names
False
'sahithi' not in names
True
names
'AjayKrishnaSatishNishithaPreethiRuchitha'
names.upper()
'AJAYKRISHNASATISHNISHITHAPREETHIRUCHITHA'
names.lower()
'ajaykrishnasatishnishithapreethiruchitha'
names.swapcase()
'aJAYkRISHNAsATISHnISHITHApREETHIrUCHITHA'
l='python programming language'
l.capitalize()
'Python programming language'
l.title()
'Python Programming Language'
"ß".casefold()
'ss'
'priya' in names
False

l
'python programming language'
l.center(100,'*')
'************************************python programming language*************************************'
l.center(50,'*')
'***********python programming language************'
l.center(50,'-')
'-----------python programming language------------'
l.center(50,'_')
'___________python programming language____________'
l.ljust(50,'-')
'python programming language-----------------------'
l.ljust(50,' ')+':'

'python programming language                       :'
l.rjust(50,'-')
'-----------------------python programming language'
'2'.zfill(6)
'000002'
'202'.zfill(6)
'000202'
'202123'.zfill(6)
'202123'
names
'AjayKrishnaSatishNishithaPreethiRuchitha'
names.find('j')
1
names.find('a')
2
names.find('Ajay')
0
names.find('z')
-1
names.rfind('a')
39
names.index('K')
4
names.index('a')
2
names.rindex('a')
39
names
'AjayKrishnaSatishNishithaPreethiRuchitha'
names.count('a')
5
names.count('e')
2
names.count('i')
6
names
'AjayKrishnaSatishNishithaPreethiRuchitha'
names.replace('a','*')
'Aj*yKrishn*S*tishNishith*PreethiRuchith*'
names.replace('sh','')
'AjayKrinaSatiNiithaPreethiRuchitha'
names.replace('sh','00')
'AjayKri00naSati00Ni00ithaPreethiRuchitha'
names.replace('sh','-00-')
'AjayKri-00-naSati-00-Ni-00-ithaPreethiRuchitha'
names.replace('Ajay','Anirudh')
'AnirudhKrishnaSatishNishithaPreethiRuchitha'
names
'AjayKrishnaSatishNishithaPreethiRuchitha'
names
'AjayKrishnaSatishNishithaPreethiRuchitha'
names.replace('a','*')
'Aj*yKrishn*S*tishNishith*PreethiRuchith*'
names.replace('sh','')
'AjayKrinaSatiNiithaPreethiRuchitha'
names.replace('sh','00')
'AjayKri00naSati00Ni00ithaPreethiRuchitha'
names.replace('sh','-00-')
'AjayKri-00-naSati-00-Ni-00-ithaPreethiRuchitha'
names.replace('Ajay','Anirudh')
'AnirudhKrishnaSatishNishithaPreethiRuchitha'
names
'AjayKrishnaSatishNishithaPreethiRuchitha'




