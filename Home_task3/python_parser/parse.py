import json

from log_parser import Parser, open_and_write, open_and_write_json

print('Input path')
path = input()
print('Json? (True/False)')
json = input()
parser = Parser(path, json)

# parser = Parser(
#     path='/Users/igorkhotyanovich/projects/' +
#          '2020-1-Atom-QA-Python-I-Khotianovich/Home_task3/data',
#     json=False)

parser.is_file_func()
parser.gen_list()
cmd = None

print('Keys')
print('-a - Total number of requests')
print('-b - Number of queries by type')
print('-c - Top 10 Biggest Queries')
print('-d - Top 10 quantity requests that ended with a client error')
print('-e - Top 10 requests that ended with a client error by size')
print('Input exit to exit\n')

while cmd != 'exit':
    cmd = input()

    if cmd == '-a':
        if parser.json:
            f = open('res/res-a.json', 'w')
            json.dump(parser.count_number_of_requests(), f)
            f.close()
        else:
            f = open('res/res-a.txt', 'w')
            f.write(parser.count_number_of_requests())
            f.close()
        print('Finished')
        print()

    elif cmd == '-b':
        if parser.json:
            f = open('res/res-b.json', 'w')
            json.dump(parser.number_of_each_type(), f)
        else:
            f = open('res/res-b.txt', 'w')
            res = parser.number_of_each_type()
            for i in range(len(res)):
                f.write(str(res[i]))
                f.write('\n')
            f.close()
        print('Finished')
        print()

    elif cmd == '-c':
        if parser.json:
            open_and_write_json('res/res-c.json', parser.top_of_size())
        else:
            open_and_write('res/res-c.txt', parser.top_of_size())

    elif cmd == '-d':
        if parser.json:
            open_and_write_json('res/res-d.json',
                                parser.top_quantity_client_error())
        else:
            open_and_write('res/res-d.txt', parser.top_quantity_client_error())

    elif cmd == '-e':
        if parser.json:
            open_and_write_json('res/res-e.json',
                                parser.top_quantity_client_error_by_size())
        else:
            open_and_write('res/res-e.txt',
                           parser.top_quantity_client_error_by_size())

    elif cmd == 'exit':
        print('\nBy!\n')
    else:
        print('Bad key\n')
