import sys
args=sys.argv[1:]
num_args=len(sys.argv)-1

if num_args>1:#can only handle 1 file at a time for now
    print("too many input files")
    sys.exit()

infile=open(args[1],'r')

def printcols(file):
    pass

infile.close()
