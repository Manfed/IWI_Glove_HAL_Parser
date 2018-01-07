# encoding=utf8
import sys
import getopt
import methodsComparator

reload(sys)
sys.setdefaultencoding('utf8')

def main(argv):
    glove_vector_file = ''
    hal_vector_file = ''
    output_file = ''

    try:
        opts, args = getopt.getopt(argv, "hg:x:o:", ["gfile=", "hfile=", "ofile="])
    except getopt.GetoptError:
        print 'halGloveComparator.py -g <glove_vector_file> -x <hal_vector_file> -o <output_file>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'halGloveComparator.py -g <glove_vector_file> -x <hal_vector_file> -o <output_file>'
            sys.exit()
        elif opt in ("-g", "--gfile"):
            glove_vector_file = arg
        elif opt in ("-o", "--ofile"):
            output_file = arg
        elif opt in ("-x", "--hfile"):
            hal_vector_file = arg
    methodsComparator.compare(hal_vector_file, glove_vector_file, output_file)

if __name__ == "__main__":
    main(sys.argv[1:])