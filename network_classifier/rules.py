from .maintain import read_file
class Rules:
    
    def __init__(self, rule_file):
        self.rule_file = rule_file 
    
    def create_rule_dict(self):
        """
        The method create_rule_dict create the rule dict with multi_rule (if exist) -> dict

        """
        rule_dict = dict()
        file_list = read_file(self.rule_file)
        if file_list != []: 
            for rule in file_list:
                if rule[1] == 'multi_rules':
                    arg_dict = self.multi_rule(file_list, rule)
                    for key, val in arg_dict.items():
                        rule_dict[key] = [val,rule[3]]
                else:
                    rule_dict[rule[1]] = [rule[2],rule[3]]
        return rule_dict

    
    def multi_rule(self, file_list, this_rule):
        '''
        multi_rule(list,list ) -> dict
        '''
        arg_dict = dict()
        args = this_rule[2]
        args_to_find_list = args.split('-')
        for rule in file_list:
            if this_rule[0] == rule[0]:
                break
            else:
                if rule[0] in args_to_find_list:
                    arg_dict[rule[1]] = rule[2]
        return arg_dict


