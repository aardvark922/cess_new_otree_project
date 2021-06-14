from otree.api import *

c = Currency

from markupsafe import Markup           # Class used to avoid escaping text passed to the HTML files
                                        # This allows to write HTML code in this file and pass it as such
                                        # to the template file

doc = """
Entry survey for the CESS oTree Course
"""


class Constants(BaseConstants):
    name_in_url = 'entry_survey'
    players_per_group = None
    num_rounds = 1

    # List of names of input fields, created here for convenience
    survey_fields = [
        'is_student', 'github', 'os', 'programming_languages', 'git', 'web_deployment',
        'has_project', 'project'
    ]
    survey2_fields= ['year_in_program','language']

    survey3_fields =['friend','ethnic']

    # Set of choices available for some of the input fields, created here for convenience
    yes_no_choices = [(1, 'Yes'), (0, 'No')]    # When a list of tuples is passed, the first value is stored in
                                                # the database, the second is the one displayed to participants

    os_choices = ['Linux', 'MacOS', 'Windows']

    year_choices=['year 1', 'year 2','year 3','year 4','year 5']

    ethnic_choices=[
        'American Indian or Alaska Native','Asian','Black or African American','Hispanic or Latino',
        'Native Hawaiian or Other Pacific Islander','White'
    ]

    # TODO: set new options of a new input field (done)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    # TODO: after completing the exercises set in the Player class, set two new input fields in this class.
    friend = models.BooleanField(
        label="Do you have friend also taking this course?",  # The text/question introducing the input field
        choices=Constants.yes_no_choices,  # The list of options/choices for a question
        widget=widgets.RadioSelectHorizontal  # The type of input field: radio buttons, text, number box, and so on
    )
    ethnic= models.StringField(
        label="Which of the following ethnic groups do you believe you belong to?",
        choices=Constants.ethnic_choices # I want to set a dropdown menu
    )


class Player(BasePlayer):
    # Database column used to store values for a single participants, in the current oTree app, in a single round
    # A field is defined as attribute of a class (in this case the Player class) and has minimum two components:
    # - a name
    # - a data type => the data type is defined calling a class from oTree "models": models.ClassName
    # Optional arguments include: "label", "choices", "widget".

    is_student = models.BooleanField(
        label="Are you a student?",             # The text/question introducing the input field
        choices=Constants.yes_no_choices,       # The list of options/choices for a question
        widget=widgets.RadioSelectHorizontal    # The type of input field: radio buttons, text, number box, and so on
    )
    github = models.StringField(
        label=Markup(                           # An example of how to style a label directly from the field definition
            "What is your GitHub username?"     # by using HTML tags
            "<div class='small'>"
            "<i>(This will be used to invite you to the GitHub classroom of the course)</i>"
            "</div>"
        )
    )
    os = models.StringField(
        label="Which Operating System is installed in the computer that you will you use during the course?",
        choices=Constants.os_choices,
        widget=widgets.RadioSelectHorizontal
    )
    programming_languages = models.StringField(
        label="Excluding Python, do you have experience with any programming/markup language ("
              "e.g. R, Matlab, JavaScript, HTML, CSS, Julia, C++)?",
        choices=Constants.yes_no_choices,
        widget=widgets.RadioSelectHorizontal
    )
    git = models.BooleanField(
        label=Markup("Do you have any experience using <i>Git</i> as version control system?"),
        choices=Constants.yes_no_choices,
        widget=widgets.RadioSelectHorizontal
    )
    web_deployment = models.BooleanField(
        label="Do you have any experience with web development?",
        choices=Constants.yes_no_choices,
        widget=widgets.RadioSelectHorizontal
    )

    has_project = models.BooleanField(
        label="Do you already have in mind a particular experimental design that you want to develop in oTree?",
        choices=Constants.yes_no_choices,
        widget=widgets.RadioSelectHorizontal
    )
    project = models.LongStringField(
        label="It would be great if you could briefly describe your experimental design (e.g. tasks involved, "
              "whether it includes real-time interactions among participants, type of treatments and of treatment "
              "randomization, etc...). Part of your design might be included in the collective project that we "
              "will develop during the course(!).",

        blank=True      # An input field is by default mandatory (aka required). It can be set to optional by setting
                        # the "blank" argument equal to True
    )
    year_in_program = models.StringField(
        label="Which year are you in your current program?",
        choices=Constants.year_choices,
        widget=widgets.RadioSelectHorizontal
    )
    language = models.BooleanField(
        label="Is English your first language?",
        choices=Constants.yes_no_choices,
        widget=widgets.RadioSelectHorizontal
    )
    # TODO: set two new fields.
    # One of them should use the choices defined in Constants
    # The label of one of them should be styled using HTML and CSS


# PAGES

# Each page class defined here corresponds to a page that can be displayed to a participant
# A page definition has minimum one component, i.e. its name. It usually inherit from the oTree in-built
# class "Page", which offers several utility methods to control important aspects of an experimental/survey flow

class Survey(Page):
    form_model = 'player'                       # Indicate in which class the page should look for the field definitions
    form_fields = Constants.survey_fields       # Indicate the input fields to be included in this page

class Survey2(Page):
    form_model = 'player'                       # Indicate in which class the page should look for the field definitions
    form_fields = Constants.survey2_fields       # Indicate the input fields to be included in this page

class Survey3(Page):
    form_model = 'group'                       # Indicate in which class the page should look for the field definitions
    form_fields = Constants.survey3_fields      # Indicate the input fields to be included in this page


# TODO: create a new page class and a corresponding HTML file to display the new fields set in the Player class


# TODO: create a new page class and a corresponding HTML file to display the new fields set in the Group class


class EndOfSurvey(Page):
    pass


# The ordered sequence of pages to be actually displayed
# Each page class included in this list must match a HTML file with the same name,
# unless the attribute "template_name" used on the page class
page_sequence = [Survey,Survey2,Survey3, EndOfSurvey]