from .maintain import read_file, write_output, is_ip, is_subnet
import asyncio
import time
classifivation_num = 0
ouput_line_list = []
class Classifier_work:

    def __init__(self, traffic_file, rule_dict):
       self.rule_file = traffic_file
       self.rule_dict = rule_dict

    def parse_traffic(self):
        """
        the method parse_traffic is the main method that save output in file, every time row is insert to communication scv it will checked by rule and write the output to file classification.csv
        """
        global ouput_line_list
        ouput_line_list = list()
        file_list_old = []
        while True:
            file_list = read_file(self.rule_file)
            if file_list == file_list_old:
                # await asyncio.sleep(5)
                time.sleep(10)
            if file_list != file_list_old:
                new_list = file_list[len(file_list_old):len(file_list)]
                for traffic_line in new_list:
                    if self.rule_communicating_protocol(traffic_line, self.rule_dict['communicating_protocol']):
                        continue
                    elif self.rule_communicating_with(traffic_line, self.rule_dict['communicating_with']):
                        continue
                    elif self.rule_communicating_with_subnet(traffic_line,self.rule_dict['communicating_with_subnet']):
                        continue
                    elif self.rule_communicating_with_domain(traffic_line,self.rule_dict['communicating_with_domain']):
                        continue
                    else:
                        print("no rule for this traffic line:{}" .format(traffic_line))
                write_output('classifications.csv', ouput_line_list)
                file_list_old.extend(new_list)


    def clasification(self, classification_str):
        """
        clasification(string) -> string
        """
        temp = 'unknown'
        if classification_str != '':
            temp = classification_str
        return temp

    def rule_communicating_protocol(self, traffic_line, val_list):
        """
        method rule_communicating_protocol(list, list)->boolen 
        """
        global classifivation_num
        global ouput_line_list
        if traffic_line != [] and val_list != []:
            if traffic_line[3]== val_list[0]:
                classifivation_num = classifivation_num+1
                ouput_line =  [str(classifivation_num) + ',' + str(traffic_line[2]) + ',' +  self.clasification(val_list[1])]
                ouput_line_list.append(ouput_line)
                return True
        return False

    def rule_communicating_with(self, traffic_line, val_list):
        """
        rule_communicating_with(list, list)->boolean
        """
        global classifivation_num
        global ouput_line_list
        if traffic_line != [] and val_list != []:
            if traffic_line[4] == val_list[0]:
                classifivation_num = classifivation_num+1
                ouput_line = [str(classifivation_num) + ',' + str(traffic_line[2]) + ',' + self.clasification(val_list[1])]
                ouput_line_list.append(ouput_line)
                return True
        return False

    def rule_communicating_with_subnet(self, traffic_line, val_list):
        """
        rule_communicating_with_subnet(list, list)->boolean
        """
        global classifivation_num
        global ouput_line_list
        if traffic_line != [] and val_list != []:
            subnet_list = is_subnet(val_list[0])
            if subnet_list != []:
                traffic_start_id = traffic_line[4]
                subnet_start_id = subnet_list[0]
                last_num_rule = subnet_list[1]
                last_num_list = traffic_start_id.split('.')
                last_num = last_num_list[len(last_num_list)-1]
                try:
                    if int(last_num) <= int(last_num_rule) and subnet_start_id[:-2] == traffic_start_id[:-2]:
                        classifivation_num = classifivation_num+1
                        ouput_line = [str(classifivation_num) + ',' + str(traffic_line[2]) + ',' + self.clasification(val_list[1])]
                        ouput_line_list.append(ouput_line)
                        return True
                except:
                    return False
        return False

                    
    def rule_communicating_with_domain(self, traffic_line, val_list):
        """
        rule_communicating_with_domain(list, list)->boolean
        """
        global classifivation_num
        if traffic_line != [] and val_list != []:
            trafic_ip = traffic_line[4]
            if trafic_ip == is_ip(val_list[0]):
                classifivation_num = classifivation_num+1
                ouput_line = [str(classifivation_num) + ',' + str(traffic_line[2]) + ',' + self.clasification(val_list[1])]
                ouput_line_list.append(ouput_line)
                return True
        return False

    
