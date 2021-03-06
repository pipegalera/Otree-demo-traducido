# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division
from otree.db import models
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer

from otree import widgets
from otree.common import Currency as c, currency_range
import random
# </standard imports>


doc = """
This is the familiar playground game "Matching Pennies". In this
implementation, players are randomly grouped in the beginning and then continue
to play against the same opponent for 3 rounds. Their roles alters between
rounds.<br/>
The game is preceded by one understanding question (in a real experiment, you
would often have more of these).
"""


class Constants(BaseConstants):
    name_in_url = 'matching_pennies'
    players_per_group = 2
    num_rounds = 3
    base_points = c(50)
    training_1_correct = 'El Jugador 1 obtiene 100 puntos, el Jugador 2 obtiene 0 puntos'
    feedback1_explanation = 'El Jugador 1 obtiene 100 puntos, el Jugador 2 obtiene 0 puntos'
    training_question_1 = 'Suponga que el Jugador 1 ha elegido "Cara" y el Jugador 2 ha imaginado "Cruz", ¿Cuál es el beneficio los jugadores 1 y 2, respectivamente?'

class Subsession(BaseSubsession):

    def before_session_starts(self):
        if self.round_number % 2 == 0:
            for group in self.get_groups():
                players = group.get_players()
                players.reverse()
                group.set_players(players)

class Group(BaseGroup):


    def set_payoffs(self):
        p1 = self.get_player_by_role('Jugador 1')
        p2 = self.get_player_by_role('Jugador 2')

        if p2.penny_side == p1.penny_side:
            p2.payoff = 100
            p1.payoff = 0
            p2.is_winner = True
            p1.is_winner = False
        else:
            p2.payoff = 0
            p1.payoff = 100
            p2.is_winner = False
            p1.is_winner = True


class Player(BasePlayer):

    training_question_1 = models.CharField(max_length=100,
                                           choices=['El Jugador 1 obtiene 0 puntos, el Jugador 2 obtiene 0 puntos',
                                                    'El Jugador 1 obtiene 100 puntos, el Jugador 2 obtiene 100 puntos',
                                                    'El Jugador 1 obtiene 100 puntos, el Jugador 2 obtiene 0 puntos',
                                                    'El Jugador 1 obtiene 0 puntos, el Jugador 2 obtiene 100 puntos'],
                                           widget=widgets.RadioSelect())

    def is_training_question_1_correct(self):
        return self.training_question_1 == Constants.training_1_correct

    penny_side = models.CharField(
        choices=['Cara', 'Cruz'],
        doc="""Heads or tails""",
        widget=widgets.RadioSelect()
    )

    is_winner = models.BooleanField(
        doc="""Whether player won the round"""
    )

    def other_player(self):
        """Returns the opponent of the current player"""
        return self.get_others_in_group()[0]

    def role(self):
        if self.id_in_group == 1:
            return 'Jugador 1'
        if self.id_in_group == 2:
            return 'Jugador 2'

