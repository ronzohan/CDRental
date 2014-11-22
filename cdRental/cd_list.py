class CDList(object):
    def __init__(self):
        self.cds = {}

    def add_cd(self, cd):
        self.cds[cd.id] = cd

    def get_cd_data(self, id):
        return self.cds.get(id)