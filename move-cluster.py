import sys, getopt
    
def main(argv):
    opts, arg = getopt.getopt(argv[1:], "s:d")
    print("arguments:")
    for opt, arg in opts:
        print("\t", opt, " -> ", arg)

if __name__ == "__main__":
    main(sys.argv)



