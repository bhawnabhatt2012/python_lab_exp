import re
f_name= input('enter the python  filename:')
newf_name=input(('entre the new file name:'))
try:
    f=open(f_name,'r')
    f1=open(newf_name,'w')
    for line in f.readlines():
        if not re.search('#(.*)',line):
            f1.write(line)
            f1.close()

            f2=open(newf_name,'r')
            print("contents in a new file :")
            for line in f2.readlines():
                print(line)
except IOError:
    print("file not found")