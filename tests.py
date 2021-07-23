import requests


def first_test_case():
    """
    Первое тестовый случай отправляет правильный запрос, который содержит только те поля, которые находятся
        в первом шаблоне в БД. Ожидается, что в качестве ответа должно быть получено название шаблона
        'User Contact Form'
    """
    test_post_data = {
        'user_name': 'I am just an user',
        'user_email': 'myemail@gmail.com',
        'user_phone': '+71112223333',
    }

    r = requests.post('http://127.0.0.1:5000/get_form', test_post_data)
    assert r.text == 'User Contact Form'
    print(f'Running first_test_case ... Success!')


def second_test_case():
    """
    Второй тестовый случай тоже отправляет правильный запрос, но содержит дополнительное поле, которое находится
        в первом шаблоне в БД. Ожидается, что в качестве ответа должно быть получено название шаблона
        'User Contact Form', поскольку остальные поля полностью совпадают.
    """
    test_post_data = {
        'user_name': 'I am just an user',
        'user_email': 'myemail@gmail.com',
        'user_phone': '+71112223333',
        'cat_name': 'Sonya'
    }

    r = requests.post('http://127.0.0.1:5000/get_form', test_post_data)
    assert r.text == 'User Contact Form'
    print(f'Running second_test_case ... Success!')


def third_test_case():
    """
    Во третьем тестовом случае в форме отправляется некорретный e-mail. Ожидается, что в качестве ответа должен быть
    получен JSON вида:
        {
            "user_email":"text",
            "user_name":"text",
            "user_phone":"phone"
        }

    Что указывает на то, что в поле user_email на самом деле передан текст, а не валидный e-mail. В БД не будет найдено
        ни одного подходящего шаблона.
    """
    test_post_data = {
        'user_name': 'I am just an user',
        'user_email': 'myemailgmail.com',
        'user_phone': '+71112223333',
    }

    r = requests.post('http://127.0.0.1:5000/get_form', test_post_data)
    assert r.text == '{"user_email":"text","user_name":"text","user_phone":"phone"}\n'
    print(f'Running third_test_case ... Success!')


def fourth_test_case():
    """
    В четвертом тестовом случае в форме отправляются некорретный e-mail и номер телефона. Ожидается, что в качестве
    ответа должен быть получен JSON вида:
        {
            "user_email":"text",
            "user_name":"text",
            "user_phone":"text"
        }

    Что указывает на то, что в поле user_email и user_phone на самом деле переданы данные типа "текст",
    а не валидный e-mail и номер телефона. В БД не будет найдено ни одного подходящего шаблона.
    """
    test_post_data = {
        'user_name': 'I am just an user',
        'user_email': 'myemailgmail.com',
        'user_phone': '+7111222333',
    }

    r = requests.post('http://127.0.0.1:5000/get_form', test_post_data)
    assert r.text == '{"user_email":"text","user_name":"text","user_phone":"text"}\n'
    print(f'Running fourth_test_case ... Success!')


def fifth_test_case():
    """
    В пятом тестовом случае проверяется работа другого шаблона из БД. Тестируется отработка варианта, когда пользователь
        запросил возврат средств. Данные заведомо корректны, ожидается что в качестве ответа должно быть получено
        название шаблона 'User Moneyback Order'
    """
    test_post_data = {
        'user_name': 'I am an angry user!',
        'user_order_date': '2020-02-10',
        'expected_moneyback_date': '2020-02-20',
        'moneyback_reason': 'GIVE MY MONEY BACK!'
    }

    r = requests.post('http://127.0.0.1:5000/get_form', test_post_data)
    assert r.text == 'User Moneyback Order'
    print(f'Running fifth_test_case ... Success!')


def sixth_test_case():
    """
    В шестом тестовом случае проверяется работа корректная работа альтернативного формата ввода времени.
    Данные заведомо корректны, ожидается что в качестве ответа должно быть получено название шаблона
    'User Moneyback Order'
    """
    test_post_data = {
        'user_name': 'I am an angry user!',
        'user_order_date': '02.10.2020',
        'expected_moneyback_date': '20.10.2020',
        'moneyback_reason': 'GIVE MY MONEY BACK!'
    }

    r = requests.post('http://127.0.0.1:5000/get_form', test_post_data)
    assert r.text == 'User Moneyback Order'
    print(f'Running sixth_test_case ... Success!')


def seventh_test_case():
    """
    В седьмом тестовом случае пользователь забыл указать причину возврата денег. Хоть это поле и не требует валидации,
    но является обязательным для применения шаблона 'User Moneyback Order'.
    Ожидается, что в качестве ответа будет получен JSON вида:
    {
        "expected_moneyback_date":"date",
        "user_name":"text",
        "user_order_date":"date"
    }

    Поскольку из-за не указанной причины возврата денег, ни один из шаблонов не подходит.
    """
    test_post_data = {
        'user_name': 'I am an angry user!',
        'user_order_date': '2020-02-10',
        'expected_moneyback_date': '2020-02-20',
    }

    r = requests.post('http://127.0.0.1:5000/get_form', test_post_data)
    assert r.text == '{"expected_moneyback_date":"date","user_name":"text","user_order_date":"date"}\n'
    print(f'Running seventh_test_case ... Success!')


def eight_test_case():
    """
    В восьмом тестовом случае пользователь указал тринадцатый месяц. Данные являются не валидными
    Ожидается, что в качестве ответа будет получен JSON вида:
    {
        "expected_moneyback_date":"date",
        "moneyback_reason":"text",
        "user_name":"text",
        "user_order_date":"text"
    }

    Поскольку дата заказа не прошла валидацию, ни один из шаблонов в БД не подходит.
    """
    test_post_data = {
        'user_name': 'I am an angry user!',
        'user_order_date': '02.13.2020',
        'expected_moneyback_date': '20.10.2020',
        'moneyback_reason': 'GIVE MY MONEY BACK!'
    }

    r = requests.post('http://127.0.0.1:5000/get_form', test_post_data)
    assert r.text == '{"expected_moneyback_date":"date","moneyback_reason":"text","user_name":"text","user_order_date":"text"}\n'
    print(f'Running eight_test_case ... Success!')


def run_all_tests():
    first_test_case()
    second_test_case()
    third_test_case()
    fourth_test_case()
    fifth_test_case()
    sixth_test_case()
    seventh_test_case()
    eight_test_case()
    print(f'8\8 tests are successfull!')


if __name__ == '__main__':
    run_all_tests()
