# -*- coding: utf-8 -*-
from __future__ import division
from . import models
from ._builtin import Page, WaitPage
from otree.common import Currency as c, currency_range
from .models import Constants
from django.utils.safestring import mark_safe



def vars_for_all_templates(self):
    return {'instructions': 'bertrand_competition/Instructions.html'}


class Introduction(Page):

    template_name = 'global/Introduction.html'

    def is_displayed(self):
        return self.subsession.round_number == 1


class Question1(Page):
    template_name = 'global/Question.html'
    form_model = models.Player
    form_fields = ['training_my_profit']
    question = '''Suponga que decide que el precio de su producto es 40 puntos y la otra\
        empresa 50 puntos, ¿Qué beneficio tendrías?'''

    def is_displayed(self):
        return self.subsession.round_number == 1

    def vars_for_template(self):
        return {'question': self.question}


class Feedback1(Page):
    template_name = 'global/Feedback.html'

    def is_displayed(self):
        return self.subsession.round_number == 1

    def vars_for_template(self):
        p = self.player
        return {
            'answer': [p.training_my_profit, 40],
            'explanation': mark_safe(Question1.question + '''
                <strong>Solución:</strong> 40 puntos
                <strong>Explicación:</strong> Como su precio era inferior\
                al precio de la otra empresa, el comprador a comprado su producto. Por lo que su\
                beneficio será el precio, que era <strong>40\
                puntos</strong>.''')
        }


class Decide(Page):

    form_model = models.Player
    form_fields = ['price']


class ResultsWaitPage(WaitPage):

    body_text = "Esperando al otro participante."


    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):

    def vars_for_template(self):
        return {
            'table': [
                ('', 'Puntos'),
                ('Su precio', self.player.price),
                ('Precio más bajo', min(
                    p.price for p in self.group.get_players())),
                ('¿Su producto fue vendido?',
                    'Sí' if self.player.is_a_winner else 'No'),
                ('Su beneficio', self.player.payoff - Constants.bonus),
                ('Además, tiene una compensación por participar de', Constants.bonus),
                ('Con todo, sus beneficios finales son de', self.player.payoff),
            ]
        }


page_sequence = [Introduction,
            Question1,
            Feedback1,
            Decide,
            ResultsWaitPage,
            Results]
