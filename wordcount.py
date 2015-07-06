# put your code here.


def wordcount(filename):
    opened_file = open(filename)
    # print opened_file
    all_lines_together=""
    for line in opened_file:
        stripped_line = line.replace('\n',' ')
        all_lines_together +=stripped_line
    word_count_dict = {}
    all_lines_together_list = all_lines_together.split(" ")
    for word in all_lines_together_list:
        if word is "":
            pass
        else:
            word_count_dict[word] = all_lines_together_list.count(word)
    print word_count_dict
    print all_lines_together_list

wordcount("test.txt")