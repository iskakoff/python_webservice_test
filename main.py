
# import system module to read command line arguments
import sys

# import local modules
import PubMedParse
import REACHProcess
import ParseException

# We should have at least one PMID
if len(sys.argv) < 2:
    raise Exception("You should provide at least one PMID as command line argument.")

# initialize PubMed parser
parser = PubMedParse.PubMedParser()
# initialize REACH web-service processing
reach = REACHProcess.REACHProcessor()

# iterate over all available PMIDs
for PMID in sys.argv[1:]:
    try:
        print ("Get data for PMID {0:s}".format(PMID))
        # extract abstract for the specific PMID
        Abstract = parser.parse(PMID)
        # get REACH data for the specific Abstract
        reach_result = reach.process_REACH(PMID, Abstract)
        # write result into a file
        json_file = open("{0:s}.json".format(PMID), 'w+')
        json_file.write(reach_result)
        json_file.close()
    except ParseException.ParseException as err:
        print("There is an parsing error: {0:s}".format(err.message))
        sys.exit(255)

