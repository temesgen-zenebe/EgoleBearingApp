#!/usr/bin/python
# - *- coding: utf- 8 - *-

from django.apps import AppConfig


class PaymentConfig(AppConfig):
    name = 'payment'
    verbose_name = 'Оплата'

    def ready(self):
        import payment.signals
