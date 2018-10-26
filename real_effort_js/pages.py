from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class RealEffortTask(Page):
    form_model = 'player'
    form_fields = ['num_seen', 'num_correct']

    timeout_seconds = Constants.real_effort_time_limit

class Results(Page):
    pass

page_sequence = [
    RealEffortTask,
    Results
]
