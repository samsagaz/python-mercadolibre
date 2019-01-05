import pytest
from python_mercadolibre.questions.models import QuestionModel
from python_mercadolibre.questions.api import Question
from python_mercadolibre.users.api import User

user = User()
profile = user.profile()
question = Question()


def test_by_seller_inputs():
    questions_by_seller = question.by_seller(profile)
    assert isinstance(questions_by_seller, QuestionModel)


@pytest.mark.parametrize("input", [int, str, [], {}, (), bool])
def test_by_seller_invalid_inputs(input):
    with pytest.raises(Exception):
        question.by_seller(input)
