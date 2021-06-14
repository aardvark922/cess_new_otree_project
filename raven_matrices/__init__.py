from otree.api import *
import csv
import json

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'raven_matrices'
    players_per_group = None
    num_rounds = 1

    with open('raven_matrices/static/raven_matrices/data/raven_matrices.csv') as raven_file:
        content=csv.DictReader(raven_file)
        raven_matrices = list(content)

        #raven_matrices=list(csv.DictReader(raven_file))
        print(raven_matrices)

    num_matrices=len(raven_matrices[:3])
    matrices_name=['SPM-'+row['R1']+str(row['R2']) for row in raven_matrices]
    matrices_answers=[int(row['Answer']) for row in raven_matrices]
    six_options_matrics=matrices_name[0:22]

    num_options=dict(small=6, large=8)
class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
  curr_matrix=models.IntegerFields(initial=1)
  answers=models.StringField() #store answer from participants
  score=models.IntegerFields(initial=0)

#FUNCTIONS
def creating_session(subsession: Subsession):
    if subsession.round_number==1:
        for p in subsession.get_players():
            #p.participant.vars['raven_matrices_answers']=[]
            p.participant.raven_matrices_answers=[]

def set_matrix(player:Player, const:Constants):
    curr_matrix=player.curr_matrix
    matrix_name=const.matrices_name[curr_matrix-1]
    num_options=const.num_options['small'] if matrix_name in const.six_options_matrics else const.num_options['small']
    return dict(
        curr_matrix=curr_matrix,
        matrix_name=matrix_name,
        num_options=num_options
    )

def set_score(player: Player,const:Constants):
    if answer==const
# PAGES
class Instructions(Page):
    pass

class Task(Page):
    @staticmethod
    def vars_for_template(player: Player):
        const=Constants
        return dict(
            small_options=range(const.num_options['small']),
            large_options=range(const.num_options['large']),
            matrix=set_matrix(player, const)
        )
    pass

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [Instructions, ResultsWaitPage, Results]
