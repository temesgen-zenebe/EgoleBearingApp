#!/usr/bin/python
# - *- coding: utf- 8 - *-

from celery import shared_task 
from django.core.mail import send_mail
from .models import Order

@shared_task
def OrderCreated(order_id):
    """
    Отправка Email сообщения о создании покупке
    """
    order = Order.objects.get(id=order_id)
    subject = 'hello {}'.format(order.id)
    message = 'message {}'.format(order.first_name, order.id)
    mail_send = send_mail(subject, message, 'admin@myshop.ru', [order.email])
    return mail_send
