"""
7-有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。
包括空行和注释，但是要分别列出来。
"""

import os
import re
def walk_dir(path,endwith):
    file_path=[]
    for root,dirs,files in os.walk(path):
        for f in files:
            if f.lower().endswith(endwith):
                file_path.append(os.path.join(root,f))
    return file_path


def lines_of_program(filepath):
    pline,blank,note=0,0,0
    note_flag=False
    file_name=os.path.basename(filepath)
    with open(filepath,'rb') as f:
        for line in f.read().split(b'\n'):
            pline+=1
##            print(line,len(line))
##            print(line.strip(),len(line.strip()))
##            
            if line.strip().startswith(b'\"\"\"') and not note_flag:
                note_flag=True
                note+=1
                continue

            elif line.strip().startswith(b'\"\"\"'):
                note_flag=False
                note+=1
            elif line.strip().startswith(b'#')or  note_flag:
                note+=1
            elif len(line.strip())==0:
                blank+=1
    
    print("在%s中，共有%s行代码，其中有%s空行，有%s行注释"%(file_name,pline,blank,note))

if __name__=='__main__':
    files=walk_dir('.','py')
    print(files)
    for f in files:
        lines_of_program(f)
