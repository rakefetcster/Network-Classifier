from network_classifier.rules import Rules
from network_classifier.classifier_work import Classifier_work
from network_classifier.maintain import files_name
import argparse


def get_files_name():
    parser = argparse.ArgumentParser()                                               
    parser.add_argument("file_rules",  type=str)
    parser.add_argument("file_traffic",  type=str)
    try:
        args = parser.parse_args()
    except SystemExit:
        print("you need 2 exist  files for input")
    file1, file2 = files_name(args)
    return file1, file2

def create_dict(file1):
    rule_dict = dict()
    rule_obj = Rules(file1)
    rule_dict = rule_obj.create_rule_dict()
    return rule_dict

def create_ouput(file2, rule_dict):
    classifier_obj = Classifier_work(file2, rule_dict)
    classifier_obj.parse_traffic()

def main():
    rule_dict = dict()
    file1, file2 = get_files_name()
    if file1 != '' and file2 != '':
        rule_dict = create_dict(file1)
        create_ouput(file2, rule_dict)
    else:
        print("missing files in input")

if __name__== "__main__":
    main()