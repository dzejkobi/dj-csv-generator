from django.utils.translation import gettext_lazy as _

from csv_generator.generator import CsvGenerator


class AddressCsv(CsvGenerator):
    field_names = (
        'company',
        'first_name',
        'last_name',
        'street_address',
        'locality',
        'province',
        'postal_code',
        'phone_number'
    )
    header_row = {
        'company': _('Company'),
        'first_name': _('First name'),
        'last_name': _('Last name'),
        'street_address': _('Street address'),
        'locality': _('Locality'),
        'province': _('Province'),
        'postal_code': _('Postal code'),
        'phone_number': _('Phone number')
    }

    def get_province(self, obj):
        return obj.get_province_display()
