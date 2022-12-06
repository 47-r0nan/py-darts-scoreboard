class Player:

    def __init__(self, name):
        self.__name = name
        self.__score = 501
        self.__turn = 0
        self.__dart1 = 0
        self.__dart2 = 0
        self.__dart3 = 0

    def resetAll(self):
        self.__score = 501
        self.__turn = 0
        self.__dart1 = 0
        self.__dart2 = 0
        self.__dart3 = 0

    def resetDarts(self):
        self.__dart1 = 0
        self.__dart2 = 0
        self.__dart3 = 0

    def recordDarts(self, sum):
        self.__score = sum
        self.__turn += 1
        self.resetDarts()

    def getDart1(self):
        return self.__dart1

    def getDart2(self):
        return self.__dart2

    def getDart3(self):
        return self.__dart3

    def getName(self):
        return self.__name

    def getScore(self):
        return self.__score

    def getTurn(self):
        return self.__turn

    def updateName(self, new):
        self.__name = new
