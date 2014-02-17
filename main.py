import sys

args=sys.argv[1:]
num_args=len(sys.argv)-1
debug=True

if num_args>1:#can only handle 1 file at a time for now
    print("too many input files")
    sys.exit()

def debug_print(x):
    if debug==True:
        print(x)
    
def get_colors(input_file):
    for line in input_file:
        debug_print(line)
        if "#" in line:
            pass

def print_colors(collist):
    pass

input_file=open(args[1],'r')

input_file.close()
