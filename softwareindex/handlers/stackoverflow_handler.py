# This is a software index handler for stackoverflow
# 
# Inputs:
# - softwareidentifier (String)
# 
# Outputs:
# - score (Number)
# - description (String)
import requests
import json

class stackoverflow_handler:


    def get_score(self, software_identifier):
        if isinstance(software_identifier, basestring):
			r  = requests.get("https://api.stackexchange.com/2.2/search/advanced?order=desc&sort=activity&body="+software_identifier+"&site=stackoverflow")

			data = r.text
			jsonStr = json.loads(data)

			items = jsonStr['items']
			view_sum = 0;
			for question_number in range(len(items)):
				question_view_count = items[question_number][u'view_count']
				view_sum = view_sum+question_view_count	
			print("number of views: "+str(view_sum))
			return view_sum
        else:
            return -1

    def get_description(self):
        return 'Score based on total number of views of related questions on stackoverflow'
