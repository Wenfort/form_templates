from tinydb import TinyDB


def get_form_templates_from_database():
    return TinyDB('db.json')


def get_correct_form_template_from_database(validated_form_fields):
    """
    Функция получает set, состоящий из кортежей вида ('название поля', 'тип поля').
    Затем этот set сравнивается с помощью метода .issubset со всеми аналогичными сетами из базы данных.
    Если совпадение найдено, возвращается название шаблона из БД (хранится в поле 'name')
    """
    form_templates = get_form_templates_from_database()

    for form_template in form_templates:
        form_template_name = form_template.pop('name')
        template_form_fields = set(form_template.items())

        if template_form_fields.issubset(validated_form_fields):
            return form_template_name
