# -*- coding: utf-8 -*-
from __future__ import division
from otree.common import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
from django.utils.safestring import mark_safe



def vars_for_all_templates(self):
    return {'instructions': 'volunteer_dilemma/Instructions.html'}


class Introduction(Page):

    template_name = 'global/Introduction.html'

    def is_displayed(self):
        return self.subsession.round_number == 1


class Question1(Page):
    template_name = 'global/Question.html'
    form_model = models.Player
    form_fields = ['training_my_payoff']

    question = '''Suponga una situación en la que cada participante toma su elección de forma anónima y dos jugadores deciden ser voluntarios mientras que usted decide no serlo,
                    ¿Cuál sería la cantidad de beneficio que recibiría usted?'''

    def is_displayed(self):
        return self.subsession.round_number == 1

    def vars_for_template(self):
        return {
            'question': self.question
        }


class Feedback1(Page):
    template_name = 'global/Feedback.html'

    def is_displayed(self):
        return self.subsession.round_number == 1

    def vars_for_template(self):
        p = self.player
        return {
            'answer': [p.training_my_payoff, c(60)],
            'explanation': mark_safe(Question1.question + '''
            <strong>Solución:</strong> Su benefición sería de <strong>60 puntos</strong>.
            <strong>Explicación:</strong> Al menos un (de hecho 2)\
            participante se han ofrecido voluntarios, por lo que todos reciben <strong>100</strong>\
            puntos. Ha sido voluntario, por lo que paga <strong>40</strong>\
            puntos. Junto a la recompensa, obtiene <strong>100-40=60</strong> puntos.''')
        }


class Decision(Page):

    form_model = models.Player
    form_fields = ['volunteer']

    def vars_for_template(self):
        return {'general_benefit': Constants.general_benefit,
                'volunteer_cost': Constants.volunteer_cost,
                'num_other_players': Constants.num_other_players}


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):

    def vars_for_template(self):
        return {
                'num_volunteers': len([
                    p for p in self.group.get_players() if p.volunteer])}


page_sequence = [Introduction,
            Question1,
            Feedback1,
            Decision,
            ResultsWaitPage,
            Results]
