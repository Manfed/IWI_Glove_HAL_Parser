# encoding=utf8
import sys
import gensim
import io

reload(sys)
sys.setdefaultencoding('utf8')


def parseDictionary(inputWords, outputFile="output.txt", gloveFile=""):

    gensimModel = gensim.models.KeyedVectors.load_word2vec_format(gloveFile, binary=False)

    with io.open(outputFile, 'w', encoding='utf-8') as output:
        for word in inputWords:
            most_similar_words = gensimModel.wv.most_similar(positive=[word], topn=50)
            output.write(u"\n" + word + " -> " + ", ".join(__filterResults__(most_similar_words)))


def __filterResults__(listOfSimilarWords):
    newList = []
    for tuple in listOfSimilarWords:
        newList.append(str(tuple[0]).encode('utf-8'))
    return newList