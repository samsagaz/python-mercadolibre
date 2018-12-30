import os
import pytest
import python_mercadolibre as pyme
from python_mercadolibre.questions.models import QuestionModel, QuestionPostModel


@pytest.mark.vcr()
def test_by_seller():
    questions = pyme.Question()
    response = questions.by_seller(os.environ.get("USER_ID"))
    assert all(isinstance(question, QuestionModel) for question in response)


@pytest.mark.vcr()
def test_by_item():
    questions = pyme.Question()
    response = questions.by_item(os.environ.get("ITEM_ID"))
    assert all(isinstance(question, QuestionModel) for question in response)


@pytest.mark.vcr()
def test_by_customer_and_item():
    questions = pyme.Question()
    response = questions.by_customer_and_item(
        os.environ.get("USER_ID"),
        os.environ.get("ITEM_ID"))
    assert all(isinstance(question, QuestionModel) for question in response)


@pytest.mark.vcr()
def test_by_question():
    questions = pyme.Question()
    response = questions.by_question(os.environ.get("QUESTION_ID"))
    assert all(isinstance(question, QuestionModel) for question in response)


@pytest.mark.vcr()
def test_received():
    questions = pyme.Question()
    response = questions.received()
    assert all(isinstance(question, QuestionModel) for question in response)


@pytest.mark.vcr()
def test_create_question():
    questions = pyme.Question()
    response = questions.create_question('MLA716819109', 'Tienen Stock?')
    assert isinstance(response, QuestionPostModel)


@pytest.mark.vcr()
def test_answer_question():
    questions = pyme.Question()
    response = questions.answer_question('6019488162', 'En Arroyito')
    assert all(isinstance(question, QuestionModel) for question in response)
