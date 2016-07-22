# -*- coding: utf-8 -*-
from __future__ import division
from . import models
from ._builtin import Page, WaitPage
from otree.common import Currency as c, currency_range
from .models import Constants


def vars_for_all_templates(self):

    return {
            'total_q': 1
            }


class Introduction(Page):
    pass

class Question(Page):

    form_model = models.Player
    form_fields = ['training_question_1']

    def vars_for_template(self):
        return {'num_q': 1}


class Feedback(Page):

    def vars_for_template(self):
        return {'num_q': 1,
              #  'answer': self.player.training_question_1,
               # 'correct': Constants.training_1_correct,
                'explanation': """Las unidades total producidas son 20 + 30 = 50. Entonces, el precio de venta por unidad es de 60 - 50 = 10.
                                  El beneficio que obtendría la empresa B sería la cantidad producida por B por el precio de venta de la unidad: 30 x 10 = 300""",
              #  'is_correct': self.player.is_training_question_1_correct()
              }


class ChoiceOne(Page):

    def is_displayed(self):
        return self.player.id_in_group == 1

    template_name = 'stackelberg_competition/ChoiceOne.html'

    form_model = models.Player
    form_fields = ['quantity']


class ChoiceTwoWaitPage(WaitPage):



    def body_text(self):
        if self.player.id_in_group == 1:
            return "Esperando a que el otro participante decida."
        else:
            return 'Eres la segunda empresa en decidir. Por favor, espere que la primera empresa decida.'


class ChoiceTwo(Page):

    def is_displayed(self):
        return self.player.id_in_group == 2

    form_model = models.Player
    form_fields = ['quantity']

    # def vars_for_template(self):
    #     return {'other_quantity': self.player.other_player().quantity}
    #

class ResultsWaitPage(WaitPage):



    body_text = "Esperando al resto de participantes."

    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.set_payoff()


class Results(Page):

    template_name = 'stackelberg_competition/Results.html'

    def vars_for_template(self):
        self.player.set_payoff()

        return {
                'total_quantity': self.player.quantity + self.player.other_player().quantity,
                'total_plus_base': self.player.payoff + Constants.fixed_pay

                }


page_sequence = [Introduction,
            Question,
            Feedback,
            ChoiceOne,
            ChoiceTwoWaitPage,
            ChoiceTwo,
            ResultsWaitPage,
            Results]
