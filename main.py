import toga

class Team:
    Team_list = []

    def __init__(self, name):
        self.name = name
        self.score = 0

    @classmethod
    def add_team(cls, new_team):
        cls.Team_list.append(new_team)

    @classmethod
    def get_winning_team(cls):
        return max(cls.Team_list, key=lambda team: team.score)

class Score:

    def __init__(self, current_score):
        self.current_score = current_score

    @classmethod
    def add_score(cls, current_score, new_score):
        return current_score + new_score

    def __str__(self):
        return str(self.current_score)

class Rounds:
    Round = 1

    def __init__(self, total_r):
        self.total_r = total_r

    @classmethod
    def new_round(cls):
        cls.Round += 1

    @classmethod
    def current_round(cls):
        print(cls.Round)

def on_enter(widget):
    team_name = input_team.value.strip()
    if team_name.lower() == 'stop':
        main_window.close()
        return

    Team.add_team(Team(team_name))
    input_team.value = ""

def on_round_submit(widget):
    try:
        round_score = int(input_score.value)
        team.score = Score.add_score(team.score, round_score)
        input_score.value = ""
    except ValueError:
        print("Please enter a valid integer")

def on_round_end(widget):
    Rounds.new_round()
    if Rounds.Round > Rounds.total_r:
        winning_teams = Team.get_winning_team()
        if len(winning_teams) == 1:
            print(f"The winning Team is {winning_teams[0].name} with a score of {winning_teams[0].score}")
        else:
            print("It's a tie! The winning teams are:")
            for team in winning_teams:
                print(f"{team.name} with a score of {team.score}")

app = toga.App('Game App', 'org.example.gameapp', startup=on_enter)

input_team = toga.TextInput(on_enter=on_enter, placeholder='Enter team name')
button_team = toga.Button('Add Team', on_press=on_enter)

input_score = toga.TextInput(placeholder='Enter score')
button_score = toga.Button('Submit Score', on_press=on_round_submit)

button_end_round = toga.Button('End Round', on_press=on_round_end)

box = toga.Box(children=[input_team, button_team, input_score, button_score, button_end_round])

main_window = toga.MainWindow('Game Window', size=(300, 150))
main_window.content = box

app.main_loop()