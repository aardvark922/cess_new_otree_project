from os import environ

SESSION_CONFIGS = [
    dict(
        name='entry_survey',
        display_name='Entry Survey',
        app_sequence=['entry_survey'],
        num_demo_participants=3
    ),
    dict(
        name='math_quiz',
        display_name='Math Quiz',
        app_sequence=['math_quiz'],
        num_demo_participants=2
    ),
    dict(
        name='dictator',
        display_name='Dictator Game',
        app_sequence=['dictator'],
        num_demo_participants=4
    ),
    # dict(
    #     name='public_goods',
    #     app_sequence=['public_goods', 'payment_info'],
    #     num_demo_participants=3,
    # ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '3188500026145'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
