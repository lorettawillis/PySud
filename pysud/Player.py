__author__ = 'loretta'


class Player:
    def __init__(self, name):
        self.name = name


#----------------------------------------------------------------------------------------------------------------------#
def main():
    name = raw_input('Tell me your name -> ')
    player = Player(name)
    print 'Your name is:', player.name

if __name__ == "__main__":
    main()

