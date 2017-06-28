class ParseException(Exception):

    def __init__(self, msg):
        super(ParseException, self).__init__(self, msg)
        self.message = msg
