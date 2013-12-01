import os,sys
from batch import *
from globalvar import *
from multiprocessing import Pool, Manager
def getfile(path):
    p = str( path )
    if p=="":
        return [ ]
#    p = p.replace( "/","\\")
    if p[-1] != "/":
        p = p+"/"
    a = os.listdir( p )
    b = [ p+x for x in a if os.path.isfile( p + x ) ]
    return b

def autocompiler(f,para,cpath):
    fname , fext = os.path.splitext(f)
    di , fname = os.path.split(fname)
    if fext == ".c":
        print(fname)
        os.system("gcc -o " + cpath + fname + ".exe" + " -g " + f )
    if fext == ".cpp":
        print(fname)
        os.system("g++ -o " + cpath + fname + ".exe" + " -g " + f )
#    if fext == ".java":
#        string += "javac " + GetJaveName(f, i) + "\n"
#        nofile = False
def main(pid,path,cpath):
    cpp = getfile(path)
    pool = Pool(processes=16)
    cpp.sort()
    for f in cpp:
        pool.apply_async(autocompiler, (f,pid,cpath))
    pool.close()
    pool.join()

if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2],sys.argv[3])
    print("END?")

