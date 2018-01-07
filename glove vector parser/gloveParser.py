# encoding=utf8
import ast
import dictionaryReader
import getopt
import sys

reload(sys)
sys.setdefaultencoding('utf8')


def main(argv):
    inputWords = []
    outputFile = ''
    gloveFile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:g:", ["ifile=", "ofile=", "gfile="])
    except getopt.GetoptError:
        print 'gloveParser.py -i <inputWords> -o <outputFile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'gloveParser.py -i <inputWords> -o <outputFile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputWords = ast.literal_eval(arg)
        elif opt in ("-o", "--ofile"):
            outputFile = arg
        elif opt in ("-g", "--gfile"):
            gloveFile = arg
    dictionaryReader.parseDictionary(inputWords, outputFile, gloveFile)


if __name__ == "__main__":
    main(sys.argv[1:])
