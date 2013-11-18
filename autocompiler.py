import os,subprocess,sys
from batch import *
from globalvar import *

def autocompiler(para):
    batch(para[1])
    p = subprocess.call("sh "+shellpath+"cmd.sh",shell=True)
def move(para):
    movefile(para[1])
    p = subprocess.call("sh "+shellpath+"mov.sh" , shell= True)
if __name__ == "__main__":
    autocompiler(sys.argv)
    move(sys.argv)
