
class TR:
    def __init__(self, title, id, column, old, new):
        self.title = title
        self.id = id
        self.column = column
        self.old = old
        self.new = new 


    def get_title(self):
        return self.title

    def get_id(self):
        return self.id
    
    def get_column(self):
        return self.column
    
    def get_old(self):
        return self.old
    
    def get_new(self):
        return self.new