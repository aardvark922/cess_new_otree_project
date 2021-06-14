from otree.api import *
from random import randint

c = Currency

doc = """
Math quiz where participants try to solve equations involving additions
"""

# TODO: after reviewing the existing application:
# 1. Extend the number of questions
# 2. Extend the number of factors in each question
# 3. Calculate the number of correct answers for each participants and store it in a Player field
# 4. Set different questions for each participant
# 4. Write some instructions using HTML and CSS in the Instructions page


class Constants(BaseConstants):
    name_in_url = 'math_quiz'
    players_per_group = None
    num_rounds = 1

    # Set constant vaues to be used in the quiz
    num_questions = 10                                           # Num of questions in the quiz
    quiz_fields = [f'q{n+1}' for n in range(num_questions)]     # Names of input fields (set here for convenience)
    interval = (0, 100)                                         # Extrema of the interval from which to pick
                                                                # randomly numbers for the quiz questions


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    # An alternative way to input fields in a class is to use the funcion locals(), part of the Standard Library
    # of Python. This function allows to set new variables in the current namespace (in this case, the space defined
    # by the Player class).
    for q in Constants.quiz_fields:
        locals()[q] = models.IntegerField(label='')
    del q

    # This field will store the entire list of quiz questions (formatted as a JSON string).
    questions = models.StringField()


# FUNCTIONS

# This function is called when a session is created and it is called one time for each of the rounds set in
# the class Constants as "num_rounds"
def creating_session(subsession: Subsession):

    # Import the function "dumps()" from the json module to encode the list of quiz questions before
    # storing them in the "questions" field defined under the Player class
    from json import dumps

    # Retrieve the Constants
    const = Constants

    # Generate a list of dictionaries each containing the two values to be used in a quiz question
    # Each of the two values is an integer, randomly selected using randint()
    # randint() takes as arguments the two extrema of the interval from where to pick an integer
    # We pass the two arguments needed by unpacking the tuple "interval" defined in Constants.
    # Unpacking means returning the items of a sequence as separate elements.
    # To unpack a sequence when passing it as an argument of a function, we use the star operator
    questions = [{'a': randint(*const.interval), 'b': randint(*const.interval),'c': randint(*const.interval)} for q in range(const.num_questions)]

    # In a for loop, update each dictionary in the list "questions" to include the corresponding solutions
    for q in questions:
        q.update(s=sum(q.values()))


    # After generating the questions AT THE SESSION LEVEL, we assign the same list of questions to each participants

    # The class Subsession has the method "get_players()" to get the list of all the players in a specific round.
    # We iterate though that list and assign to each player ("p") the list of questions
    for p in subsession.get_players():
        p.participant.vars['questions'] = questions     # Assign the list of questions to the participant dictionary "vars"
        p.questions = dumps(questions)                  # Assign the list of questions to the Player field "questions"
                                                        # For preserving a convenient formatting, we assign a JSON encoded
                                                        # string using dumps()


# PAGES
class Instructions(Page):
    pass


class Task(Page):
    form_model = 'player'
    form_fields = Constants.quiz_fields

    # The decorator @staticmethod is completely optional
    # We use it only for improving teh behaviour of the editor
    # oTree's behaviour will not be altered.
    @staticmethod
    def vars_for_template(player: Player):          # This method can generate variables that can be used in the
                                                    # corresponding HTML file
        fields = Constants.quiz_fields
        labels = [f'{d["a"]} + {d["b"]}-{d["c"]} =' for d in player.participant.vars['questions']]

        # The function must return a dictionary. The name of the variables accessible in the HTML
        # are the keys of the returned dictionary.
        return dict(
            questions=list(zip(fields, labels))     # zip() return an sequence (precisely a generator) of tuples,
                                                    # where each tuple includes an element from each of the argument
                                                    # passed to zip(). We passed the returned object to list()
                                                    # in order to loop through it in the HTML file
        )


page_sequence = [Instructions, Task]