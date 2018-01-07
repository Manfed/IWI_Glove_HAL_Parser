# encoding=utf8
import io
import sys

reload(sys)
sys.setdefaultencoding('utf8')


def compare(hal_file, glove_file, output_file):
    with io.open(output_file, 'w', encoding='utf-8') as output_f:
        hal_vector = __create_hal_vector__(hal_file)
        glove_vector = __create_glove_vector__(glove_file)
        for key, value in hal_vector.iteritems():
            if key in glove_vector:
                hal = hal_vector[key]
                glove = glove_vector[key]
                length = min(len(hal), len(glove))
                file_content = u"\nhal\tdiff\tglove"
                for i in range(0, length):
                    position = __check_position__(hal[i], glove)
                    if position != -1:
                        file_content = "%s\n%s\t%d\t%s" % (file_content, hal[i], abs(i-position), glove[i])
                    else:
                        file_content = "%s\n%s\t-\t%s" % (file_content, hal[i], glove[i])
                output_f.write(file_content)


def __create_hal_vector__(hal_file):
    hal_vector = {}
    with io.open(hal_file, encoding='utf-8') as hal_f:
        for line in hal_f:
            if len(line) > 1:
                similar_words = []
                word, vector = line.split(' -> ')
                for similar_word in str(vector).split('], '):
                    s_word, value = similar_word.split(',')
                    similar_words.append(s_word[1:])
                hal_vector[word] = similar_words
        return hal_vector


def __create_glove_vector__(glove_file):
    glove_vector = {}
    with io.open(glove_file, encoding='utf-8') as glove_f:
        for line in glove_f:
            if len(line) > 1:
                similar_words = []
                word, vector = line.split(' -> ')
                for similar_word in str(vector).split(','):
                    similar_words.append(similar_word.replace(' ', ''))
                glove_vector[word] = similar_words
    return glove_vector


def __check_position__(word, glove_vector):
    if word in glove_vector:
        return glove_vector.index(word)
    else:
        return -1
