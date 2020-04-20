import random

def create_name_of_segment(from_what, beg, end):
    return "MySegmentFrom" + from_what + str(random.randint(beg, end))

