import csv
import os
import socket
path_to_files = os.path.join(os.getcwd() ,'files')


def read_file(filename):
    global path_to_files
    file_str_list = list()
    try:
        with open(os.path.join(path_to_files, filename), 'r') as csvfile:
            reader = csv.reader(csvfile, skipinitialspace=True)
            for row in reader:
                if row:
                    file_str_list.append(row)
    except FileNotFoundError:
        print("Sorry, the file {} does not exist.".format(filename))
    return file_str_list

def parse_file_name(filename):
    file_name = str(filename).split('=')
    my_file = file_name[1][1:-2]
    return my_file

def write_output(filename, ouput_line_list):
    try:
        with open(os.path.join(path_to_files,filename), 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            for line in ouput_line_list:
                writer.writerow(line)
    except FileNotFoundError:
        print("Sorry, the file {} does not exist.".format(filename))

def is_ip(website_name):
        ip = ''
        try:
            ip = socket.gethostbyname(website_name)
        except socket.error:
            print("Invalid IP: {}".format(ip))
        return ip

def is_subnet(sub_val):
    ip_list = list()
    if "/" in sub_val:
        ip_list = sub_val.split('/')
    return ip_list

def files_name(args):
    file1 = ''
    file2 = ''
    if args: 
        files_name_list = str(args).split(',')
        file1_list = files_name_list[0].split('=')
        file1 = file1_list[1][1:-1]
        file2_list = files_name_list[1].split('=')
        file2 = file2_list[1][1:-2]
        return file1, file2