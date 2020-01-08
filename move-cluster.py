import sys, getopt

source_url = None
source_user = None
source_pass = None
dest_url = None
dest_user = None
dest_pass = None

opts, arg = getopt.getopt(sys.argv[1:], "s:d")
print("arguments:")
for opt, arg in opts:
    print("\t", opt, " -> ", arg)


