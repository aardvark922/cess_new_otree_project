from otree.api import *
from math_quiz import Constants as mathConstants  ### this way we could inherit constants from other APP
c = Currency

doc = """
This is a dictator game!
"""


class Constants(BaseConstants):   #in-build attributes
    name_in_url = 'econ_experiment'   #don't want to show ss what we are looking at !! has to be unique
    players_per_group = 2
    num_rounds = 1
    instructions_template='dictator/instructions.html'   #string of path loacted in our project
    #endowment=cu(100)   #displayed in templates of real-world currency
    endowment=dict(high=cu(100),low=cu(10))   #if we have different treatments
       #use_fixed_roles=2


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):   #specific list of players in a certain round of a specific application
    kept=models.CurrencyField(
        label=f"Hey, how much do you want to keep for yourself of yours {Constants.endowment['high']}?"  #define how the question will be presented
        min=0,
        max=Constants.endowment['high'],
        blank=True
    )


class Player(BasePlayer):   #the higher level of individuality in a certain round of a specific application
    ## def my_method(self):  ##self=current class
     ##   self.payoff=...
    pass

# FUNCTIONS

def set_payoffs(group: Group):
    # The Group class has a method which allows to retrieve each player in the group using their group ID.
    # The group ID is an integer and is assigned to each player based on their position in the list of players
    # that composes the group: the first Player in the list has ID = 1, and so on...
    p1 = group.get_player_by_id(1)
    p2 = group.get_player_by_id(2)
    # Each Player has an in-built attribute called "payoff" which is desgined to store the payoff of the player
    # for a specific round.
    p1.payoff = group.kept
    p2.payoff = Constants.endowment['high'] - group.kept

def set_payoffs(group:Group):
    dictator=group.get_player_by_id(1)
    receiver=group.get_player_by_id(2)

    dictator.payoff=group.kept
    receiver.payoff=Constants.endowment['high']-group.kept


# PAGES
class Offer(Page):
    form_model='group'
    form_fields=['kept']   #define which fields I want to include
    @staticmethod
        def is_displayed(player:Player): ##want to only display this page if id ==1
            return player.id_in_group== 1

class ResultsWaitPage(WaitPage):   ##NB: waitpage does not need a template
    @staticmethod
    def after_all_players_arrive(group:Group):
        ...    # after_all_players_arrive is an otree built-in function


class Results(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]
