import re
import datetime


def validate_form(form):
    """
    Функция валидирует каждое поле из формы присланной пользователем и сохраняет результат в словарь validated_form
    """
    validated_form = dict()
    for form_field, form_field_value in form.items():
        validated_form[form_field] = check_type(form_field_value)

    return validated_form


def check_type(form_field_value):
    """
    После валидации возвращает тип данных в форме. Если ни одна из валидаций не пройдена, тип данных считается text
    """
    return is_date_type(form_field_value) or is_phone_type(form_field_value) or is_email_type(
        form_field_value) or 'text'


def is_date_type(date):
    """
    Функция проверяет дату на соответствие формату YYYY-MM-DD или DD.MM.YYYY
    В случае успеха возвращает 'date' как тип данных.
    """
    if check_valid_date_with_format(date, '%Y-%m-%d') or check_valid_date_with_format(date, '%d.%m.%Y'):
        return 'date'


def check_valid_date_with_format(date, date_format):
    """
    Функция проверяет полученную дату на соответствие формату.
    Пример валидной комбинации:
        date = '2012-01-01'
        date_format = '%Y-%m-%d'
    Выбран вариант валидации с помощью datetime, т.к. регулярка получается слишком громоздкой и нечитаемой.
    """
    try:
        datetime.datetime.strptime(date, date_format)
        return True
    except:
        return False


def is_phone_type(phone):
    """
    Функция проверяет телефон с помощью регулярки.
    В случае успеха возвращает 'phone' как тип данных.
    """
    phone_validator_mask = r"^\+?[78][-\(]?\d{3}\)?-?\d{3}-?\d{2}-?\d{2}$"
    if re.match(phone_validator_mask, phone):
        return 'phone'


def is_email_type(email):
    """
    Функция проверяет email с помощью регулярки.
    В случае успеха возвращает 'email' как тип данных.
    """
    email_validator_mask = r"^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$"
    if re.match(email_validator_mask, email):
        return 'email'
