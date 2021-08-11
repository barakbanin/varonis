class MagicList:
    def __init__(self, cls_type=None):
        if not cls_type:
            self.lst = list()
        else:
            self.lst = cls_type
        self.counter=0
        def __setitem__(self, i, item):
            if len(self.lst)==0:
                self.lst.append(item)
                self.counter+=1
        def __getitem__(self, i):
            return self.lst[i]
