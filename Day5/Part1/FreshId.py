class FreshId(object):

    def __init__(self, start, end):
        self.start = start
        self.end = end

    
    def check_Id_for_freshness(self, id):
        if self.start <= id and id <= self.end:
            return True
        
        return False