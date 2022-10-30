class Human:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi i'm {self.name}")


class Women(Human):
    def cook(self):
        print("cooking")


class Men(Human):
    def work(self):
        print("working")


John = Men("John smith")
John.talk()
John.work()
Jenet = Women("Jenet")
Jenet.talk()
Jenet.cook()