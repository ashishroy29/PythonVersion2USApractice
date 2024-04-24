s = "Ashish"
print(type(s))
type(s)

s[0]
s[1]
s[2]
s[3]

s[-1]
s[-2]
s[-6]

a = 'my name is ashish'
a[100]

a[0:10]

b = "ineuron"
b[0:3]
b[0:300]

b[-1:-4]

a = 'kumar'
a[0:3]
a[0:300]
a[0:300:1]
a[0:300:2]
a[0:300:3]
a[0:100:-1]
a[-1:-4:-1]
a[0:-10:-1]
a[::]
a[-2:]
a[-2:-1]
a[::-1]
a[-1::-1]
a = 'I am working with teleperformance'
a[-1::-1]
a[::-1]
a[-1::-1] == a[::-1]
a[-5:5]
a[-5:5:-1]
a[-2:-10:-1]
a[0:100:3]
"Ashish"*3
"Ashish"+"Roy"
a
len(a)
a
"ash"*4
a
a.find('a')
a.find('I')
a.find('Ia')
a.find('in')
a.find('tele')
a.count('i')
type(a)
a.count('x')
a
a.split()
type(a.split())
z = a.split()
z[0]
z[1]
z[2]
z[3]
z[4]
z[5]

z[0:2]
z[0::2]
z[0:5:2]
a.split('w')
a.split('wo')
a.upper()
a.lower()
s = 'ashi'


list1 = ['1','ashi','boy']

def sorting(Input_list):
    for i in Input_list:
        if type(i) == int:
            print(f'{i} is an Integer')
        elif type(i) == str:
            print(f'{i} is a String')
        else:
            print(f'{i} is a complex number')

sorting(list1)

s = 'aShi'

s.swapcase()
s.title()
s.capitalize()

b = 'ashi'
c = 'roy'

b.join(c)

" ".join('ashi')

z = reversed('ashi')

for i in 'ashi':
    print(i)

for i in reversed('ashi'):
    print(i)

a = 'ashi'

a[::-1]

a.rstrip()

a.lstrip()

a.strip()

a.replace('a','sjsjs')

z = 'acv'

z.replace('a', 'sjsjs')

'ashi\troy'.expandtabs()

s = 'ashi'

s.center(40,'t')

s.center(40,'$')

s = "             Indians are the best"
s.strip()

s.split()

a = 'ashi'

a.isupper()

a.islower()

a = "Ashi"

a.isupper()
a.islower()

a = "ASHI"

a.islower()

a.isupper()

a.isspace()

a = "      ashi"
a.isspace()

a = "    "
a.isspace()

a.isdigit()

a = 'assd12323'
a.isdigit()

a = '12345'
a.isdigit()

s = 'sudh'
s.endswith('h')

s.endswith('x')

s.startswith('t')

s.startswith('s')

s.title()

s.istitle()

s= 'Sudh'
s.istitle()

s.encode()

### List

s = 'hahahahah hah shdasjdhsakhjk ahsd hdashd jkashdkjhas jha dhsajhd ja'

s = ["ashi","roy",3545, 4+6j,True,345.45]

type(s)

s[0]

s[-1]

s[-5]

s[0:4]

s[::-1]

s[-1:6]

for i in reversed(s):
    print(i)




#List Slicing and indexing

l1 = ["zsd","hshas",4545345]
l2 = ['asc',"pzs",123123]

l1 + l2

l1+'ashi'
l1 + ['ashi']

l1*4

l1

l1[0] = 'ashish'
l1

l1[1][0]

l1

l1[1] = 'kumar'

l1

s = 'ashi'
s.replace('a','b')

len(l1)

"kumar" in l1

345 in l1

l2

l2.pop()

l2.pop(1)

l1

l1.pop()

l1

l1.append(2822)

l1

l1.insert(1,'asshhis')


l1.insert(3,[23,22.3,23,23,34,3])

l1

l1[3][4]

l1.reverse()


l1[1][0]

l1.count('ashish')

l1.count('ashh')

l1.append('asjasj')

l1

l1.append([2,3,3,4])

l1

l1.extend(['s',1,2,3,4,4])

l1