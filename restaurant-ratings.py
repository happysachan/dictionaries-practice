# your code goes here

def restaurant_rating(filename):
    open_file = open(filename)
    rest_dict = {}
    for line in open_file:
        rest_list = line.split(":")
        rest_dict[rest_list[0]] = rest_list[1].rstrip()
    for rest_name,rating in sorted(rest_dict.items()):
        print "%s: %s" % (rest_name, rating)

restaurant_rating("scores.txt")