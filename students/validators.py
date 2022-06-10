from django.core.exceptions import ValidationError


def phone_number_validator(phone_number):
    from .models import Students
    result = Students.objects.filter(phone_number=phone_number).exists()
    if result:
        raise ValidationError(f'Phone number {phone_number} is not unique.')
