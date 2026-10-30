
'''
n=input("Enetr the string:")
for i in n:
    if n.count(i)==1:
        print(i)
        break
'''
'''
a=input("Enter a word:")
for ch in a:
    if a.count(ch)==1:
        print(ch)
        break
'''
'''
a=input("Enetr a word:")
for ch in set(a):
    if a.count(ch)>1:
        print(ch)
'''
'''
        s=input("Enter your string:")
print(s[-3: ])
'''
'''
text="H el loworld"
print(text.replace("H el loworld","Helloworld"))
'''
'''
text=input("Enter your string:")
t2=text.split()
print(len(t2))
'''
'''
text=input("Enter your string:")
vowels="aeiou AEIOU"
consonant="bcdfghjklmnprstvwxyz BCDFGHJKLMNPQRSTVWXYZ"
v=0
c=0
for i in text:
    if i in vowels:
        v+=1
    if i in consonant:
        c+=1
print(v,c)
'''
'''
text=input("Enter the string:")
print(text.replace("education","*d*c*t**n"))
'''
'''
s=input()
print(s.replace(" ",""))
'''
'''
s1=input("Enetr the str:")
s2=input("Enter the str:")
if sorted(s1.lower())==sorted(s2.lower()):
    print("Anogram")
else:
    print("Not Anogram")
'''
'''
jewels=input()
stones=input()
c=0
for i in stones:
    if i in jewels:
        c+=1
print(c)
'''
'''
s=input()
count=0
for ch in s:
    if s.count(ch)>1:
        count+=1
print(ch)
print(count().ch)
'''
'''
s=input("Enter a string:")
result=""
for i in s:
    if 'A'<=i<='Z':
        result+=chr(ord('i')+32)
    elif 'a'<=i<='z':
        result+=chr(ord('i')-32)
    
    print(result)

a=[]
num = list(map(int, input().split()))
total=0
for i in num:
    total+=i
    a.append(total)
print(a)'''

'''a = []
num = list(map(int, input().split()))
total = 0

for i in num:
    total += i
    a.append(total)

print(a)'''

'''n=[]
a=list(map(int,input().split()))
for i in a:
    if i==0:
        n.append(i)
print(n)'''

'''s=list(map(int,input().split()))
arr=[]
sum=0
for i in s:
    sum+=i
    arr.append(sum)
print(arr)'''

'''nums=[0,1,0,3,12]
for i in range(len(nums)):
    if nums[i]==0:
        nums.append(nums[i])
        nums.remove(nums[i])
print(nums)    '''

'''a=[0,18,21]
n=[]
z=[]
for i in a:
    if i==0:
        n.append(i)
    else:
        z.append(i)
print(z+n)'''

'''num=input()
a=num.split()
unique_num=list(set(a))
print(unique_num)'''

'''a=input()
count=0
for i in a:
    if a.count(i)>1:
        print("True")
        break
else:
    print("False")'''

num1=int(input())
num2=int(input())
num3=num1&num2
count=count(num3)
print(count)            






































    
