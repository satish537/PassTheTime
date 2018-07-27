'''
Created on 9 Jul 2015

@author: Satish
'''


import os
import sys
global depth, display

'''
Class definition for utility 
member functions for help and
calculation of file size implemented
'''
class util:
    
    def __init__(self):
        self.depth_count = 1
        self.disk_space = 0
        self.filesystemspace = 0

    def file_list(self, path):
        basedir = path
        
        print "\n{0}".format(basedir)
        subdir_list = []
        for item in os.listdir(path):
            fullpath = os.path.join(basedir, item)
            if os.path.isdir(fullpath):
                subdir_list.append(fullpath)
            else:
                filesize = os.path.getsize(fullpath)

                if display == '':
                    print '\t {:>12}  {:>12} B'.format(fullpath, filesize)
                elif display == "KB":
                    print '\t {0:>12s}  {1:10.3f} KB'.format(fullpath, (filesize) / 1024.0)
                elif display == "MB":
                    print '\t {0:>12s}  {1:10.3f} MB'.format(fullpath,
                                                         (os.path.getsize(fullpath) / (1024.0 * 1024)))
                self.disk_space = self.disk_space + filesize
        self.filesystemspace = self.disk_space + self.filesystemspace
        print '\nTotal disk Space for this directory : {:<2.3f} KB'.format(self.disk_space / 1024.0)
        print '\nTotal disk Space file system tree {:<2.3f} KB'.format(self.filesystemspace / 1024.0)
        for d in subdir_list:
            
            if depth == 0 or depth > self.depth_count:
                self.depth_count = self.depth_count + 1
                self.disk_space = 0
                self.file_list(d)
                
            else:
                
                break
    def help(self):
        print "\nUsage of tool \n"
        print "--path -  Provide Directory  Example : C:\ or  \\var\\tmp\\ \n"
        print "--display  - size in KB or MB default it displays in  Bytes Example --display=MB \n"
        print "--depth , -  display the level of file system . For ex : --depth=1 \n"
        print "Valid Usage : python arm_util.py --display=MB --path=C:\ --depth=1\n "
        
        
if __name__ == "__main__":
    
    utility = util()
    depth=0
    path = os.getcwd()
    display = ''
    for args in sys.argv:
        
        try:
            if args.find('path') != -1:
                temp = args.split("=")
                
                path = temp[1]
            elif args.find("depth") != -1:
                
                temp1 = args.split("=")
                #global depth 
                depth = int( temp1[1])
            elif args.find("display") != -1:
                temp3 = args.split("=")
                display = temp3[1]
            elif args.find("help") != -1:
                utility.help()
                sys.exit()
            
        except :
            sys.exit(1)

    utility.file_list(path)
    
    
    
    
