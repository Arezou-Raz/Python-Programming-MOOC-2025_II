import json

class Application:
    def __init__(self):
        self.filename = input("file name: ")
        with open(self.filename) as file:
            data = file.read()
        self.data = json.loads(data)
        print(f"read the data of {len(self.data)} players")

    def output(self, key=None, value=None, amount=None, sort_by="points"):
        players = [player for player in self.data if key is None or player[key] == value]

        if sort_by == "goals":
            sorted_players = sorted(players, key=lambda player: (-player["goals"], player["games"]))
        else:
            sorted_players = sorted(players, key=lambda player: (-player["goals"] - player["assists"], -player["goals"]))

        if amount:
            sorted_players = sorted_players[:amount]

        for player in sorted_players:
            print(f'{player["name"]:<20} {player["team"]:>3} {player["goals"]:>3} + {player["assists"]:>2} = {player["goals"] + player["assists"]:>3}')

    def help(self):
        print()
        print("commands:")
        print("0 quit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals")

    def search_player(self):
        name = input("name: ")
        self.output("name", name)

    def list_teams(self):
        teams = set()
        for player in self.data:
            teams.add(player["team"])
        for team in sorted(teams):
            print(team)

    def list_countries(self):
        countries = set()
        for player in self.data:
            countries.add(player["nationality"])
        for country in sorted(countries):
            print(country)

    def list_players_team(self):
        team = input("team: ")
        self.output("team", team)

    def list_players_country(self):
        country = input("country: ")
        self.output("nationality", country)

    def most_points(self):
        amount = int(input("how many: "))
        self.output(amount=amount)

    def most_goals(self):
        amount = int(input("how many: "))
        self.output(amount=amount, sort_by="goals")

    def execute(self):
            self.help()

            while True:
                print("")
                command = input("command: ")
                if command == "0":
                    break
                elif command == "1":
                    self.search_player()
                elif command == "2":
                    self.list_teams()
                elif command == "3":
                    self.list_countries()
                elif command == "4":
                    self.list_players_team()
                elif command == "5":
                    self.list_players_country()
                elif command == "6":
                    self.most_points()
                elif command == "7":
                    self.most_goals()
                else:
                    self.help()

Application().execute()
