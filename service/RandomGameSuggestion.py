import random


class RandomGameSuggestion:
    SEPARATOR = ","
    gameList = []

    def __init__(self):
        f = open("./service/gameDB.txt", "r")
        games = f.readline()
        print(games)
        self.gameList = list(games.split(","))
        print(self.gameList)
        f.close

    def addRandomGame(self, gameName):
        f = open("./service/gameDB.txt", "a")
        f.write(self.SEPARATOR + gameName)
        f.close

    def gameSuggestion(self):
        return random.choice(self.gameList)

    def findAllGame(self):
        return self.gameList
