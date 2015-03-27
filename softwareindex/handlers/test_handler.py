# This is an example of a software index handler
# 
# Inputs:
# - softwareidentifier (String)
# 
# Outputs:
# - score (Number)
# - description (String)

class test_handler:


    def get_score(self, software_identifier):
        if isinstance(software_identifier, basestring):
            return len(software_identifier)
        else:
            return -1

    def get_description(self):
        return 'Test score based on length of software identifier'
