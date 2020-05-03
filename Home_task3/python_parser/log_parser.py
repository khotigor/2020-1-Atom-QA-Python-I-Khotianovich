"""
My parser for .log files
"""
import os
import json


def open_and_write(file, list_to_write):
    f = open(file, 'w')
    for i in range(len(list_to_write)):
        f.write(str(list_to_write[i][6]) + ' ' + str(
            list_to_write[i][8]) + ' ' + str(list_to_write[i][9]))
        f.write('\n')
    f.close()
    print('Finished')
    print()


def open_and_write_json(file, list_to_write):
    f = open(file, 'w')
    for i in range(len(list_to_write)):
        res = list_to_write[i][6:10]
        json.dump(res, f)
    f.close()
    print('Finished')
    print()


class Parser(object):
    """
    My parser for .log files.
    It works, amazingly...
    Maybe its not good to write files in a list. But, if we want to use a few
    functions, it is much better to work with list, than parse a the same file
    few times with different 'with open'... We create one list for all the time
    of program cycle.
    Controversial decision. But it is much easier to work with a list,
    than with a file.
    """

    def __init__(self, path, json):
        self.path = path  # just a path for file or dir
        self.json = json  # use json?
        self.is_file = None  # True for file, False for dir
        self.log_list = None  # all logs

    def is_file_func(self):
        """check is it file or a dir"""
        if self.path[-1:] == "/":  # i'm too lazy, to handle all exceptions
            raise IOError("Path is bad")
        self.is_file = (self.path[-4:] == ".log")

    def gen_list(self):
        """read all from file and generate list from file or files from dir"""
        if self.is_file:  # work with file
            with open(self.path) as file:
                res = [row.strip() for row in file]
            result = []
            for i in range(len(res)):
                result.append(res[i].split(' '))
            self.log_list = result
        else:  # work with dir
            files = os.listdir(self.path)
            logs = filter(lambda x: x.endswith('.log'), files)
            log_files_list = list(logs)
            result = []
            for i in range(len(log_files_list)):
                path = self.path + '/' + log_files_list[i]
                with open(path) as file:
                    res = [row.strip() for row in file]
                for j in range(len(res)):
                    result.append(res[j].split(' '))
            self.log_list = result

    def print_log_list(self):
        """useless method to print all logs as a list"""
        print(self.log_list)

    def count_number_of_requests(self):
        """-a - Total number of requests"""
        return int(len(self.log_list))

    def number_of_each_type(self):
        """-b - Number of queries by type"""
        result = ["GET", None, "HEAD", None, "POST", None, "PUT", None,
                  "DELETE", None, "TRACE", None, "OPTIONS", None, "CONNECT",
                  None, "PATCH", None]
        # no comments, looks horribly, but it is easy
        for i in range(len(result)):
            if i % 2 == 0:
                number = 0
                for j in range(len(self.log_list)):
                    number += self.log_list[j].count('"' + result[i])
                result[i + 1] = number
        return result

    def top_of_size(self):
        """-c - Top 10 Biggest Queries"""
        top_of_size_list = sorted(self.log_list, key=lambda x: x[9],
                                  reverse=True)
        result = top_of_size_list[0:9]
        return result

    def top_quantity_client_error(self):
        """
        -d - Top 10 quantity requests that ended with a client error
        its terrible, once i will make it better
        """
        res_list = []
        for i in range(len(self.log_list)):
            if int(self.log_list[i][8]) >= 400 and int(
                    self.log_list[i][8]) <= 499:
                res_list.append(self.log_list[i])
        list_no_repeats = []
        for i in res_list:
            if i not in list_no_repeats:
                list_no_repeats.append(i)
        tmp = []
        for i in range(len(list_no_repeats)):
            number_of_repeats = 0
            for j in range(len(res_list)):
                if list_no_repeats[i] == res_list[j]:
                    number_of_repeats += 1
            tmp.append([i, number_of_repeats])
        tmp = sorted(tmp, key=lambda x: x[1], reverse=True)
        tmp = tmp[0:10]
        result = []
        for i in range(len(tmp)):
            result.append(res_list[tmp[i][1]])
        return result

    def top_quantity_client_error_by_size(self):
        """
        -e - Top 10 requests that ended with a client error by size
        """
        sorted_list = sorted(self.log_list, key=lambda x: x[9], reverse=True)
        res_list = []
        for i in range(len(sorted_list)):
            if int(sorted_list[i][8]) >= 400 and int(
                    sorted_list[i][8]) <= 499:
                res_list.append(self.log_list[i])
        result = res_list[0:10]
        return result
