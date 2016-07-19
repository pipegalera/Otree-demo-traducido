import os
from os import environ

import dj_database_url
from boto.mturk import qualification

import otree.settings


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# the environment variable OTREE_PRODUCTION controls whether Django runs in
# DEBUG mode. If OTREE_PRODUCTION==1, then DEBUG=False
if environ.get('OTREE_PRODUCTION') not in {None, '', '0'}:
    DEBUG = False
else:
    DEBUG = True

ADMIN_USERNAME = 'admin'

# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')


# don't share this with anybody.
SECRET_KEY = 'vv81j2uxfcr*1%q7#aes3gcee_*u!2177$kni@ykngf48wfuvy'

PAGE_FOOTER = ''

# To use a database other than sqlite,
# set the DATABASE_URL environment variable.
# Examples:
# postgres://USER:PASSWORD@HOST:PORT/NAME
# mysql://USER:PASSWORD@HOST:PORT/NAME

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
    )
}

# AUTH_LEVEL:
# If you are launching a study and want visitors to only be able to
# play your app if you provided them with a start link, set the
# environment variable OTREE_AUTH_LEVEL to STUDY.
# If you would like to put your site online in public demo mode where
# anybody can play a demo version of your game, set OTREE_AUTH_LEVEL
# to DEMO. This will allow people to play in demo mode, but not access
# the full admin interface.

AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')


# setting for integration with AWS Mturk
AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')


# e.g. EUR, CAD, GBP, CHF, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True


# e.g. en, de, fr, it, ja, zh-hans
# see: https://docs.djangoproject.com/en/1.9/topics/i18n/#term-language-code
LANGUAGE_CODE = 'en'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = []

# SENTRY_DSN = ''

DEMO_PAGE_INTRO_TEXT = """
<ul>
    <li>
        <a href="https://github.com/oTree-org/otree" target="_blank">
            C&oacute;digo fuente
        </a> de los juegos originales.
    </li>
    <li>
        <a href="https://github.com/pipegalera/Otree-demo-traducido" target="_blank">
            C&oacute;digo fuente
        </a> de los juegos traducidos.
    </li>
    <li>
        <a href="http://www.otree.org/" target="_blank">
            P&aacute;gina oficial de oTree
        </a>.
    </li>
</ul>
<p>
    A su derecha tiene varios juegos implementados por oTree. Estos juegos son de c&oacute;digo abierto
    por lo que pueden ser modificados como quiera para crear variaciones. Pulse cualquiera para
    aprender m&aacute;s y ejecutarlos.
</p>
"""

# from here on are qualifications requirements for workers
# see description for requirements on Amazon Mechanical Turk website:
# http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_QualificationRequirementDataStructureArticle.html
# and also in docs for boto:
# https://boto.readthedocs.org/en/latest/ref/mturk.html?highlight=mturk#module-boto.mturk.qualification

mturk_hit_settings = {
    'keywords': ['easy', 'bonus', 'choice', 'study'],
    'title': 'Title for your experiment',
    'description': 'Description for your experiment',
    'frame_height': 500,
    'preview_template': 'global/MTurkPreview.html',
    'minutes_allotted_per_assignment': 60,
    'expiration_hours': 7*24, # 7 days
    #'grant_qualification_id': 'YOUR_QUALIFICATION_ID_HERE',# to prevent retakes
    'qualification_requirements': [
        # qualification.LocaleRequirement("EqualTo", "US"),
        # qualification.PercentAssignmentsApprovedRequirement("GreaterThanOrEqualTo", 50),
        # qualification.NumberHitsApprovedRequirement("GreaterThanOrEqualTo", 5),
        # qualification.Requirement('YOUR_QUALIFICATION_ID_HERE', 'DoesNotExist')
    ]
}

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 0.01,
    'participation_fee': 1.00,
    'num_bots': 12,
    'doc': "",
    'mturk_hit_settings': mturk_hit_settings,
}


SESSION_CONFIGS = [
    {
        'name': 'public_goods',
        'display_name': "Bienes Publicos",
        'num_demo_participants': 3,
        'app_sequence': ['public_goods', 'payment_info'],
    },
    {
        'name': 'public_goods_simple',
        'display_name': "Public Goods (simple version from tutorial)",
        'num_demo_participants': 3,
        'app_sequence': ['public_goods_simple', 'survey', 'payment_info'],
    },
    {
        'name': 'trust',
        'display_name': "Juego de Confianza",
        'num_demo_participants': 2,
        'app_sequence': ['trust', 'payment_info'],
    },
    {
        'name': 'trust_simple',
        'display_name': "Trust Game (simple version from tutorial)",
        'num_demo_participants': 2,
        'app_sequence': ['trust_simple'],
    },
    {
        'name': 'beauty',
        'display_name': "Concurso de Belleza",
        'num_demo_participants': 5,
        'num_bots': 5,
        'app_sequence': ['beauty', 'payment_info'],
    },
    {
        'name': 'survey',
        'display_name': "Preguntas de compresión lectora (survey)",
        'num_demo_participants': 1,
        'app_sequence': ['survey', 'payment_info'],
    },
    {
        'name': 'prisoner',
        'display_name': "Dilema del Prisionero",
        'num_demo_participants': 2,
        'app_sequence': ['prisoner', 'payment_info'],
    },
    {
        'name': 'ultimatum',
        'display_name': "Ultimatum (aleatorio: estratégia vs. respuesta directa)",
        'num_demo_participants': 2,
        'app_sequence': ['ultimatum', 'payment_info'],
    },
    {
        'name': 'ultimatum_strategy',
        'display_name': "Ultimatum (con estratégia)",
        'num_demo_participants': 2,
        'app_sequence': ['ultimatum', 'payment_info'],
        'treatment': 'strategy',
    },
    {
        'name': 'ultimatum_non_strategy',
        'display_name': "Ultimatum (con respuesta directa)",
        'num_demo_participants': 2,
        'app_sequence': ['ultimatum', 'payment_info'],
        'treatment': 'direct_response',
    },
    {
        'name': 'battle_of_the_sexes',
        'display_name': "Batalla de Sexos",
        'num_demo_participants': 2,
        'app_sequence': [
            'battle_of_the_sexes', 'payment_info'
        ],
    },
    {
        'name': 'vickrey_auction',
        'display_name': "Subasta Vickrey",
        'num_demo_participants': 3,
        'app_sequence': ['vickrey_auction', 'payment_info'],
    },
    {
        'name': 'volunteer_dilemma',
        'display_name': "Dilema del Voluntario",
        'num_demo_participants': 3,
        'app_sequence': ['volunteer_dilemma', 'payment_info'],
    },
    {
        'name': 'cournot_competition',
        'display_name': "Duopolio de Cournot",
        'num_demo_participants': 2,
        'app_sequence': [
            'cournot_competition', 'payment_info'
        ],
    },
    {
        'name': 'principal_agent',
        'display_name': "Juego Agente-Principal",
        'num_demo_participants': 2,
        'app_sequence': ['principal_agent', 'payment_info'],
    },
    {
        'name': 'dictator',
        'display_name': "Dictator Game",
        'num_demo_participants': 2,
        'app_sequence': ['dictator', 'payment_info'],
    },
    {
        'name': 'matching_pennies',
        'display_name': "Matching Pennies",
        'num_demo_participants': 2,
        'app_sequence': [
            'matching_pennies', 'payment_info'
        ],
    },
    {
        'name': 'matching_pennies_tutorial',
        'display_name': "Matching Pennies (tutorial version)",
        'num_demo_participants': 2,
        'app_sequence': [
            'matching_pennies_tutorial',
        ],
    },
    {
        'name': 'traveler_dilemma',
        'display_name': "Traveler's Dilemma",
        'num_demo_participants': 2,
        'app_sequence': ['traveler_dilemma', 'payment_info'],
    },
    {
        'name': 'bargaining',
        'display_name': "Bargaining Game",
        'num_demo_participants': 2,
        'app_sequence': ['bargaining', 'payment_info'],
    },
    {
        'name': 'common_value_auction',
        'display_name': "Common Value Auction",
        'num_demo_participants': 3,
        'app_sequence': ['common_value_auction', 'payment_info'],
    },
    {
        'name': 'stackelberg_competition',
        'display_name': "Stackelberg Competition",
        'real_world_currency_per_point': 0.01,
        'num_demo_participants': 2,
        'app_sequence': [
            'stackelberg_competition', 'payment_info'
        ],
    },
    {
        'name': 'bertrand_competition',
        'display_name': "Bertrand Competition",
        'num_demo_participants': 2,
        'app_sequence': [
            'bertrand_competition', 'payment_info'
        ],
    },
    {
        'name': 'stag_hunt',
        'display_name': "Stag Hunt",
        'num_demo_participants': 2,
        'app_sequence': ['stag_hunt', 'payment_info'],
    },
    {
        'name': 'real_effort',
        'display_name': "Real-effort transcription task",
        'num_demo_participants': 1,
        'app_sequence': [
            'real_effort',
        ],
    },
    {
        'name': 'lemon_market',
        'display_name': "Lemon Market Game",
        'num_demo_participants': 3,
        'app_sequence': [
            'lemon_market', 'payment_info'
        ],
    },
    {
        'name': 'asset_market',
        'display_name': "Mercado de Activos",
        'num_demo_participants': 2,
        'app_sequence': [
            'asset_market', 'payment_info'
        ],
    },
]

# anything you put after the below line will override
# oTree's default settings. Use with caution.
otree.settings.augment_settings(globals())
