import os, shutil
path = '/opt/leetcode/Leetcode/tmp/'
for fname in os.listdir(path):
    print(fname)
    if fname != 'autocreate.py' and fname != '':
        print(fname)
        new_name = ' '.join(fname.split(' ')[0:-1])
        print(new_name)
        os.mkdir(new_name)
        shutil.move(fname, path+new_name+'/'+'README.md')
