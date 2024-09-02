class Player:
    name: str
    wantsToPlay: bool = True
    winLossRatio: dict = {"Wins": 0, "Losses": 0}

    def __init__(self, givenName="Executioner", wins=0, losses=0):
        self.name = givenName
        self.winLossRatio["Wins"] = wins
        self.winLossRatio["Losses"] = losses
