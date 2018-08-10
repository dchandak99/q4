from menuitem import MenuItem

class SetMenu(object):
    def __init__(self, MenuitemsList):
        self.menuitems = set()
        for item in MenuitemsList:
            self.menuitems.add(item)

    def __len__(self):
        return len(self.menuitems)

    def __str__(self):
        retval = ""
        for item in self.menuitems:
            retval = retval + str(item) + "\n"
        return retval
