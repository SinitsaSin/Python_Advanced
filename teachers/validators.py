from django.core.exceptions import ValidationError


def phone_number_validator(phone_number):
    from .models import Teachers
    result = Teachers.objects.filter(phone_number=phone_number).exists()
    if result:
        raise ValidationError(f'Phone number {phone_number} is not unique.')
