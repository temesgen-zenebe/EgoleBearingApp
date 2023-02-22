#!/usr/bin/python
# - *- coding: utf- 8 - *-

from django.shortcuts import get_object_or_404
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from orders.models import Order
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from io import BytesIO



def PaymentNotification(sender, **kwargs):
    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        order = get_object_or_404(Order, id=ipn_obj.invoice)
        order.paid = True
        order.save()

        # Отправка Email
        subject = 'hello  {}'.format(order.id)
        message = 'messag'
        email = EmailMessage(subject, message, 'admin@mayshop.com', [order.email])

        # Генерация PDF
        html = render_to_string('orders/order/pdf.html', {'order': order})
        out = BytesIO()

        # Прикрепляем pdf
        email.attach('order_{}.pdf'.format(order.id), out.getvalue(), 'application/pdf')
        email.send()

    valid_ipn_received.connect(PaymentNotification)
