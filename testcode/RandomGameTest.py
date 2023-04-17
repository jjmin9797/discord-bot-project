import sys, os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from service.RandomGameSuggestion import RandomGameSuggestion

r = RandomGameSuggestion()
print(r.gameSuggestion())
