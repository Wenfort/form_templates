from flask import Flask, request

from logic.database_logic import get_correct_form_template_from_database
from logic.validators import validate_form

app = Flask(__name__)


@app.route('/get_form', methods=['POST'])
def get_form():
    validated_form = validate_form(request.form)
    validated_form_fields = set(validated_form.items())
    return get_correct_form_template_from_database(validated_form_fields) or validated_form


if __name__ == '__main__':
    app.run()
