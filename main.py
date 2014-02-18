import sys
debug=True

def debug_print(x):
    if debug==True:
        print("DEBUG PRINTER")
        print(x)

arg=sys.argv[1]

debug_print("arg is "+arg)

num_args=len(sys.argv)-1
color_list=[]

if num_args>1:#can only handle 1 file at a time for now
    print("too many input files")
    sys.exit()

def get_colors(input_file):
    for line in input_file:
        if "#" in line:
            #append hex code to color_list
            hexcode=line[line.index("#"):line.index("#")+7]
            #debug_print(hexcode)
            color_list.append(hexcode)

def print_colors(collist):
    pass

input_file=open(arg,'r')
get_colors(input_file)
input_file.close()

