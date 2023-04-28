""""""
"""
File - A medium to store something permanently on storage device
Operations over the file -
1.Create
2.Open
3.Close
4.Edit or Update
5.Read 
6.Write

We can implement all of the above options using a Built-in function
=> open(filename,mode)

Which file format can we handle
1.Text (.txt) default
2.Binary

Modes available in open()
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing(only ones)
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)

To create a new file we 3 options
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
"""
# Now Using above modes lets create text
#1.using 'w' mode
open('a.txt',mode='w')
#2.using 'a' mode (append)
open('b.txt',mode='a')
#3.using 'x' mode (exclusive)
#open('c.txt',mode='x')

#Lets check the 'Properties of file' using f
f = open('a.txt') #default we have read mode
print(f) #f is called as handle
print(f.name)
print(f.mode)
print(f.readable()) #Boolean Output
print(f.writable()) #Boolean Output
#Check file is closed or not
print('Closed:',f.closed)
#Now Close the file
f.close() #Close the file
print('After Closed:',f.closed) #After closed - check whether its closed or not

#Lets perform write operations on a.txt
f = open('a.txt','w')
#Start with operations
print(f.writable())
#We can perform write operations using 2 options
#1.Write - Accepts any String
f.write('My name is Pretesh\nI live in Mumbai\nI am studying Python\n')
f.write('My contact details : 9876543210')
#2.Writeline -
f.writelines('\nFor more Details Contact')
f.close()
print('After Close:',f.closed)
#------------------------------------------------
#Difference between 'w' vs 'a' vs 'x'
#'w' mode
f = open('a.txt','w')
#1.Truncate the files
#2.Removes the content if present in file
#3.If you want to add new contents so use write() or writeline() options
f.write('123')
f.writelines('\n456')
f.close()

#'a' mode
f = open('a.txt','a')
#Append Mode
#1.Doesn't Truncate
#2.It keeps old content as it is (if any)
#3.We can add new content as well
f.write('\nGood evening Omkar\n')
#4.If we go on execute write option with 'a' mode again and again then it will append content multiple times
f.close()

#'x' mode
#Exclusive Mode
#1.Using this mode we can create a file only once (single time execution)
#f = open('a_1.txt','x')
#f.write('Exclusive mode on')
#2.Still if try to create a file using same name and same mode then it will show error *FileExistserror
#Output - Not able to return above script

#Operations on file for creation we have 3 modes
#1.'w' - create + truncate
#2.'a' - create + append
#3.'x' - creates only once

#write() - only accepts data of str form
#writelines() - accepts str + list['str']
#Let's create a new file
f = open('new.txt','w')
f.write('Any string\n')
f.writelines('Any string using writelines\n')
#We can also supply list of str
f.writelines(['This is python\n','Simple and easy to use']) #We cannot supply list in write()

#Read Operation - Default mode in open() is read
#It has 3 options
#1.read() - read total file/charactres
#2.readline() - read a single line
#3.readlines() - read the lines as a list of str
f = open('new.txt') #we can default read the file
#print(f.read())
#print(f.readline())
#print(f.readlines())
#If we want to read only few blocks
#print(f.read(3))

"""
Q1.Count vowels present in new.txt
Sol- 
f = open('new.txt')
data = f.read()
count = 0
for i in data:
    if i in 'aieou':
        print(i,count)
        count += 1

Q2. Using readline
Sol-
f = open('new.txt')
data = f.readline()
count = 0
for i in data:
    if i in 'aieou':
        print(i,count)
        count += 1

Q3. Using Readlines
Sol - 
f = open('new.txt')
data = f.readlines()
count = 0
for i in data:
    if i in 'aieou':
        print(i,count)
        count += 1

Q4.Find out the numbers from new.txt
f = open('new.txt')
data = f
for i in data:
    if i.isnumeric():
        print(i,end='')
"""
f = open('new.txt')
print('Before Closed:',f.closed)
f.close()
print('After Closed:',f.closed)
#Auto close option in python
#Syntax - with open() as handle_name
with open('new.txt') as f:
    print('Inside:',f.closed)
print('Outside:',f.closed)

#CSV Operations
#Write Operation
import csv
with open('sample.csv','w',newline='') as f:
    wr = csv.writer(f) #wr - name of writer object
    #writer() is a method of csv module to perform write operation
    wr.writerow(['Name','Age','Place'])
    wr.writerow(['Sagar',24,'NewZealand'])

#Read operation
import csv
with open('sample.csv') as f:
    rd = csv.reader(f) #rd - name of reader object
    #reader() is a method of read csv module to perform read operation
    print(list(rd))
    
