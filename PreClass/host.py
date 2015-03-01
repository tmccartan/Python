

class Host(object):

    def __init__(self, ip, note):
        self.note = note
        self.type = "host"
        self.ip = ip