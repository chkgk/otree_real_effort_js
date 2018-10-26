from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Christian König gen. Kersting'

doc = """
Real Effort Task on a single page. Inspired by EconomiCurtis
"""


class Constants(BaseConstants):
    name_in_url = 'real_effort_js'
    players_per_group = None
    num_rounds = 1

    real_effort_time_limit = 20     # seconds
    num_chars = 4                   # number of characters per task


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    num_seen = models.IntegerField(doc="Number of tasks seen")
    num_correct = models.IntegerField(doc="Number of tasks solved correctly")
