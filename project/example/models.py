from django.db import models

from django.utils.translation import gettext_lazy as _


POLISH_PROVINCE_CHOICES = (
    ('DSL', 'Dolnośląskie'),
    ('K-P', 'Kujawsko-pomorskie'),
    ('LBL', 'Lubelskie'),
    ('LBU', 'Lubuskie'),
    ('LDZ', 'Łódzkie'),
    ('MAZ', 'Mazowieckie'),
    ('MLP', 'Małopolskie'),
    ('OPO', 'Opolskie'),
    ('PDL', 'Podlaskie'),
    ('PKR', 'Podkarpackie'),
    ('POM', 'Pomorskie'),
    ('SL', 'Śląskie'),
    ('SW', 'Świętokrzyskie'),
    ('WLP', 'Wielkopolskie'),
    ('W-M', 'Warmińsko-mazurskie'),
    ('ZPM', 'Zachodniopomorskie')
)


class Address(models.Model):
    company = models.CharField(
        _('company'), max_length=100, blank=True
    )
    first_name = models.CharField(
        _('first name'), max_length=150, blank=True
    )
    last_name = models.CharField(
        _('last name'), max_length=150, blank=True
    )
    street_address = models.CharField(
        _('street address'), max_length=200, blank=True
    )
    locality = models.CharField(
        _('locality'), max_length=50, blank=True
    )
    province = models.CharField(
        _('province'),
        max_length=3,
        choices=POLISH_PROVINCE_CHOICES,
        blank=True
    )
    postal_code = models.CharField(
        _('postal_code'), max_length=12, blank=True
    )
    phone_number = models.CharField(
        _('phone number'), max_length=20, blank=True
    )
