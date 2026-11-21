''' Program to open a text file and count the no.of
vowels, special characters and consonants along with
finding the total number of lines in the file '''
file=open(r"C:/Users/PRADEEP/OneDrive/Desktop/sturec.txt","r")
display=file.read()
vcount=0
ccount=0
scount=0
v=['a','e','i','o','u','A','E','I','O','U']
for i in display:
    if i in v:
        vcount+=1
    elif i.isalpha():
        ccount+=1
    else:
        scount+=1
print("The number of vowels in the file is: ",vcount)
print("The number of special characters in the file is: ",scount)
print("The number of consonants in the file is: ",ccount)
# read() reads entire file and file-pointer comes to last letter
file.seek(0)# seek() move the file-pointer to the start of the file
t=file.readlines()
line=len(t)
print("The number of lines in the given file is: ",line)
file.close()
