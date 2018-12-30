import os
import pytest
import python_mercadolibre as pyme
from python_mercadolibre.questions.models import QuestionModel


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
