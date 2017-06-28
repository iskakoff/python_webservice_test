# import HTTP requests module
import requests
# import XML DOM parser
from xml.dom import minidom

import ParseException


# PubMed records web-service parser
class PubMedParser:
    # construct parser with default web URL
    def __init__(self, webserviceurl="https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"):
        self.ws_url = webserviceurl

    # Obtain and parse data from remote
    def parse(self, PMID):
        # send post request to PubMed web-service
        pub_med_response = requests.post(self.ws_url, data={'db': 'PubMed', 'retmode': 'XML', 'id': PMID})
        # enforce Unicode encoding in response
        pub_med_response.encoding = 'UTF-8'
        # construct DOM tree from the response
        pub_med_article = minidom.parseString(pub_med_response.content)
        # get all elements for AbstractText field
        abstract_text_node = pub_med_article.getElementsByTagName("AbstractText")
        # throw an exception if there is no abstracts in the response
        if len(abstract_text_node) <= 0:
            raise ParseException.ParseException("Wrong PMID.")
        # throw an exception if there is too many abstracts to parse
        if len(abstract_text_node) > 1:
            raise ParseException.ParseException("Too many abstracts in the response.")
        # get abstract text from the DOM node
        abstract = abstract_text_node[0].firstChild.nodeValue
        return abstract
