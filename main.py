class computer:
    def __init__(self):
        self.cpu=cpu
        self.ram=ram
    def config(self):
        print("config is", self.cpu, self.ram)

comp1 = computer()
comp2 = computer()
comp1.config()
comp2.config()
