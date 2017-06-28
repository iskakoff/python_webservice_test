# import HTTP requests module
import requests
# import JSON utils to
import json


# REACH web-service processing
class REACHProcessor:
    # construct REACH web-service processor for specific URL
    def __init__(self, reach_url="http://agathon.sista.arizona.edu:8080/odinweb/api/text"):
        self.ws_url = reach_url

    def process_REACH(self, pmid, abstract):
        # send post request to REACH web-service
        reach_response = requests.post(self.ws_url, data={'text': abstract, 'output': 'fries'})
        # enforce UTF-8 encoding
        reach_response.encoding = 'UTF-8'
        # process statistics
        self.statistics(reach_response.content)
        # return REACH data
        return str(reach_response.text)

    # process REACH file to get some statistics
    def statistics(self, reach_data):
        # load data as json object
        stats = json.loads(reach_data)
        # Get statistics according to fries-data-representation-spec-3 format
        print ("Number of events: {0:d}\nNumber of entities: {1:d}\nNumber of sentences: {2:d}\n" \
            .format(len(stats['events']['frames']),
                    len(stats['entities']['frames']),
                    len(stats['sentences']['frames'])))
