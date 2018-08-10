from menuitem import MenuItem


class Menu(object):
    def __init__(self, MenuitemsList):
        self.menuitems = MenuitemsList

    def __len__(self):
        return len(self.menuitems)

    def __str__(self):
        retval = ""
        for item in self.menuitems:
            retval = retval + str(item) +"\n"
        return retval


def main():
    a = MenuItem("Chicken Zinger", 200, 4.8)
    b = MenuItem("Chicken Popcorn", 100, 4.7)
    menu = Menu([b, a])
    # lst=[3, 2, 5, 4, 1]
    # (menu.menuitems).sort()
    # for movie in
    menu.menuitems.sort(reverse=True)
    print(menu)
    print(menu.menuitems[0])


if __name__ == "__main__":
    main()