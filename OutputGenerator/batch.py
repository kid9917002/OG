import re,os
from globalvar import *

def GetJaveName(javafile, i):
    java = open(path+javafile,"r")
    jdata = java.read()
    java.close()
    PUBLICCLASS = re.search( r'public class ([^\s{]+)', jdata, re.M|re.I)
    if PUBLICCLASS:
#       print(PUBLICCLASS.group(1))
       newfname = PUBLICCLASS.group(1)
#       print(newfname)
       MAINCLASS = re.search( r'public static void main', jdata, re.M|re.I)
       if MAINCLASS:
          if newfname in programtype:  # not same fname but same public class
             java = open(path+javafile,"w")
             jdata = jdata.replace(newfname,newfname+"_"+str(i))
             java.write(jdata)
             java.close()
             newfname = newfname+"_"+str(i)
             programtype[newfname] = "java"
          else:     # not same fname and not same public class
             programtype[newfname] = "java"
          os.rename(path+javafile,path+newfname+".java")
#          print("JavaName : %s --> %s.java"%(javafile,newfname))
          return newfname+".java"
       else: print("No main in public class")
    else: print("No public class")

def getfile(path):
    p = str( path )
    if p=="":
        return [ ]
#    p = p.replace( "/","\\")
    if p[-1] != "/":
        p = p+"/"
    a = os.listdir( p )
    b = [ x for x in a if os.path.isfile( p + x ) ]
    return b

def collection_sameuser( cpp ):
    collection_sameuser_list = list()
    complie_file = list()
    cpp.sort()
    while cpp:  #while cpp is not empty
        current_userid = ""
        while cpp:
            f = cpp[0]
            sp = f.split('.') # sp is a list
            if not current_userid: #string is empty
                current_userid = sp[2]
            
            if sp[2] == current_userid:
                collection_sameuser_list.append(f)
                cpp.remove(f)
            else :
                break
        complie_file.append(max(collection_sameuser_list))
        collection_sameuser_list.clear()
#    print(complie_file)
    return complie_file

def batch(para):
    cpp = getfile(path)
    i = 1
    string = ""
    nofile = True
    string = string + "cd " + path +"\n"
    cpp = collection_sameuser(cpp)
    for f in cpp:
        fname , fext = os.path.splitext(f)
        i+=1
        if fext == ".c":
            string += "gcc -o " + fname + ".exe" + " -g " + f + "\n"
            nofile = False
        if fext == ".cpp":
            string += "g++ -o " + fname + ".exe" + " -g " + f + "\n"
            nofile = False
        if fext == ".java":
            string += "javac " + GetJaveName(f, i) + "\n"
            nofile = False

    if nofile:  string = string + "echo no \"c\" or \"cpp\" \"java\" files to complie\n"+"pause"
    else: string = string + "exit"
    batch = open(shellpath+"cmd.sh","w")
    batch.write(cmdproglue)
    batch.write(string)
    batch.close()

def movefile(para):
    mov_exe = getfile(path)
    mov_string = ""
    for exe in mov_exe:
        ename , eext = os.path.splitext(exe)
        if eext == ".exe":
           mov_string += "mv -f " + path + exe + " " + newdir + para + "/\n"
        if eext == ".class":
           mov_string += "mv -f " + path + exe + " " + newdir + para + "/\n"
    mov = open(shellpath+"mov.sh","w")
    mov.write(cmdproglue)
    mov.write(mov_string)
    mov.write("rm -r "+path+"\n")
    mov.write("mkdir "+path+"\n")
    mov.write("sudo chmod 777 "+path+"\n")
    mov.close()

