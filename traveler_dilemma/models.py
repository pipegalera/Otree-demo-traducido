# -*- coding: utf-8 -*-
from __future__ import division

"""Documentation at https://github.com/oTree-org/otree/wiki

"""

from otree.db import models
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer

from otree.common import Currency as c, currency_range
from otree import widgets

doc = """
Kaushik Basu's famous traveler's dilemma (
<a href="http://www.jstor.org/stable/2117865" target="_blank">
    AER 1994
</a>).
It is a 2-player game. The game is framed as a traveler's dilemma and intended
for classroom/teaching use.
"""


class Constants(BaseConstants):
    name_in_url = 'traveler_dilemma'
    players_per_group = 2
    num_rounds = 1

    # Player's reward for the lowest claim"""
    reward = c(2)

    # Player's deduction for the higher claim
    penalty = reward

    # The maximum claim to be requested
    max_amount = c(100)

    # The minimum claim to be requested
    min_amount = c(2)

    bonus = c(10)



class Subsession(BaseSubsession):

    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):


    training_answer_mine = models.CurrencyField(verbose_name='Mi compensación sería de')
    training_answer_others = models.CurrencyField(verbose_name="La compensación del otro viajero sería de")

    # claim by player
    claim = models.CurrencyField(
        min=Constants.min_amount, max=Constants.max_amount,
        doc="""
        Cada viajero declara
        """,
        verbose_name='Por favor, introduzca una cantidad de 0 a 100'
    )

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):
        other = self.other_player().claim
        if self.claim < other:
            self.payoff = Constants.bonus + self.claim + Constants.reward
        elif self.claim > other:
            self.payoff = Constants.bonus + other - Constants.penalty
        else:
            self.payoff = Constants.bonus + self.claim
