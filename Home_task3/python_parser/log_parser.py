"""
My parser for .log files
"""


class Parser(object):
    """My parser for .log files"""

    def __init__(self, path):
        self.path = path
        self.is_file = None
        self.log_list = None

    def is_file_func(self):
        self.is_file = (self.path[-4:] == ".log")

    def gen_list(self):
        """read all from file and generate list from file or dir"""
        with open(self.path) as file:
            res = [row.strip() for row in file]
        result = []
        for i in range(len(res)):
            result.append(res[i].split(' '))
        self.log_list = result

    def print_log_list(self):
        print(self.log_list)

    def count_number_of_requests(self):
        return "Total number of request is {number}".format(
            number=len(self.log_list))


parser = Parser('/Users/igorkhotyanovich/projects/2020-1-Atom-QA-Python-I-' +
                'Khotianovich/Home_task3/data/nginx_logs_1.log')

parser.gen_list()
# parser.print_log_list()
