class Certificate (object):
    def __init__(self, id, name, rank, date):
        self.id = id
        self.name = name
        self.rank = rank
        self.date = date  # ngay nhan bang

    def getcertificate(self):
        dairy = {"ID ": self.id, "Name": self.name, "Rank": self.rank, "Date": self.date}
        return dairy
