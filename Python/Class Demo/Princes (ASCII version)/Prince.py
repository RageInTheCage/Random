class Prince:
    siblings = []

    def __init__(self, name, son_of):
        self.name = name
        self.son = son_of

    def announce(self):
        print(f"I am {self.name}, son of {self.son}")

        for sibling in self.siblings:
            print(f"I am also the brother of {sibling} but we don't talk about him")

    def add_sibling(self, sibling_of):
        self.siblings.append(sibling_of)
