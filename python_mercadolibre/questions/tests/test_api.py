import pytest
import os
from python_mercadolibre.questions.models import QuestionModel
from python_mercadolibre.questions.api import Question
from python_mercadolibre.users.api import User


@pytest.mark.vcr()
def test_by_seller_accepts_profile():
    user = User()
    profile = user.profile()
    question = Question()
    questions_by_seller = question.by_seller(profile)
    assert isinstance(questions_by_seller, QuestionModel)


def test_by_seller_accepts_integer():
    question = Question()
    questions_by_seller = question.by_seller(int(os.environ.get("USER_ID")))
    assert isinstance(questions_by_seller, QuestionModel)


def test_by_seller_accepts_string():
    question = Question()
    questions_by_seller = question.by_seller(str(os.environ.get("USER_ID")))
    assert isinstance(questions_by_seller, QuestionModel)


def test_by_seller_accepts_boolean():
    question = Question()
    with pytest.raises(TypeError):
        question.by_seller(False)
