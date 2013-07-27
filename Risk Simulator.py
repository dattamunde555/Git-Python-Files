# Risk Simulator
# Simulates the game of Risk so as to hone strategies

class Player(object):
    """A class which defines general characteristics for each competitor"""
    # use dicts? to keep track of a player's territories and armies
    def __init__(self, numPlayers):
        if numPlayers == 3:
            self.armies = 35
        elif numPlayers == 4:
            self.armies = 30
        elif numPlayers == 5:
            self.armies = 25
        elif numPlayers == 6:
            self.armies = 20

    def attack(self, aCountry, defender, dCountry):

    def battle(self, numAttack, numDefend):
        

class Territory(object):
    """General characteristics of each territory"""
    # I want each territory to be its own object.
    # Make owner of territory a property of the territory.
    # Where to create them?
    NORTH_AMERICA = ["Quebec","Central America","Eastern United States",
                     "Alberta","Western United States","Northwest Territory",
                     "Ontario","Alaska","Greenland"]
    SOUTH_AMERICA = ["Argentina","Peru","Brazil","Venezuela"]
    AFRICA = ["South Africa","Madagascar","Congo","East Africa",
              "North Africa","Egypt"]
    EUROPE = ["Western Europe","Ukraine","Northern Europe",
              "Southern Europe","Scandinavia","Iceland","Great Britain"]
    ASIA = ["Irkutsk","Japan","Ural","Kamchatka","Middle East",
            "Yakutsk","India","Siberia","China","Afghanistan",
            "Mongolia","Siam"]
    AUSTRALIA = ["New Guinea","Indonesia","Western Australia",
                 "Eastern Australia"]

def createTerritories():
    # North America
    QUEBEC = Territory()
    CENTRAL_AMERICA = Territory()
    EASTERN_UNITED_STATES = Territory()
    ALBERTA = Territory()
    WESTERN_UNITED_STATES = Territory()
    NORTHWEST_TERRITORY = Territory()
    ONTARIO = Territory()
    ALASKA = Territory()
    GREENLAND = Territory()
    # South America
    ARGENTINA = Territory()
    PERU = Territory()
    BRAZIL = Territory()
    VENEZUELA = Territory()
    # Africa
    SOUTH_AFRICA = Territory()
    MADAGASCAR = Territory()
    CONGO = Territory()
    EAST_AFRICA = Territory()
    NORTH_AFRICA = Territory()
    EGYPT = Territory()
    # Europe
    WESTERN_EUROPE = Territory()
    UKRAINE = Territory()
    NORTHERN_EUROPE = Territory()
    SOUTHERN_EUROPE = Territory()
    SCANDINAVIA = Territory()
    ICELAND = Territory()
    GREAT_BRITAIN = Territory()
    # Asia
    IRKUTSK = Territory()
    JAPAN = Territory()
    URAL = Territory()
    KAMCHATKA = Territory()
    MIDDLE_EAST = Territory()
    YAKUTSK = Territory()
    INDIA = Territory()
    SIBERIA = Territory()
    CHINA = Territory()
    AFGHANISTAN = Territory()
    MONGOLIA = Territory()
    SIAM = Territory()
    # Australia
    NEW_GUINEA = Territory()
    INDONESIA = Territory()
    WESTERN_AUSTRALIA = Territory()
    EASTERN_AUSTRALIA = Territory()


    

def start():
    """Starts the game by getting the number of players."""
    while True:
        try:
            numPlayers = int(input("How many players (3-6)?"))
            if numPlayers <= 6 and numPlayers >= 3:
                break
            else:
                print("You must pick a number from 3 to 6.")
        except:
            print("You must pick a number from 3 to 6.")
                         
    redguy = Player(numPlayers)
    blueguy = Player(numPlayers)
    greenguy = Player(numPlayers)
    if numPlayers > 3:
        yellowguy = Player(numPlayers)
    if numPlayers > 4:
        purpleguy = Player(numPlayers)
    if numPlayer > 5:
        pinkguy = Player(numPlayers)
