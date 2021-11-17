from .rules import multi_rule
from .classifier_work import clasification, rule_communicating_protocol, rule_communicating_with, rule_communicating_with_subnet, rule_communicating_with_domain
from maintain import read_file

class Test:

    def test_multi_rule():
        assert multi_rule([], '') == {}
        assert multi_rule(['3', 'multi_rules', '1-2', 'bla bla'], {'communicating_protocol': ['http', 'rakefet rosen'], 'communicating_with': ['10.1.1.1', 'bla bla'], 'communicating_with_domain': ['www.apple.com', 'iphone'], 'communicating_with_subnet': ['10.1.1.0/24', 'ct']}) == {'communicating_protocol': 'http', 'communicating_with': '10.1.1.1'}
    
    def test_clasification():
        assert clasification('') == 'unknown'
        assert clasification('1.0.0.1') == '1.0.0.1'

    def test_rule_communicating_protocol():
        assert rule_communicating_protocol([],[])== False
    def test_rule_communicating_with():
        assert rule_communicating_with([],[])== False
    def test_rule_communicating_with_subnet():
        assert rule_communicating_with_subnet([],[])== False
    def test_rule_communicating_with_domain():
        assert rule_communicating_with_domain([],[])== False
    
    def read_file():
        assert read_file('classifications_rules.csv1')