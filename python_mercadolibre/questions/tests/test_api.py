import pytest
import os
from python_mercadolibre.questions.models import QuestionModel
from python_mercadolibre.questions.api import Question
from python_mercadolibre.users.api import User

user = User()
profile = user.profile()
question = Question()


@pytest.mark.parametrize("input, expected", [
    (profile, QuestionModel),
    (profile.id, QuestionModel),
    (str(os.environ.get("USER_ID")), QuestionModel),
    (int(os.environ.get("USER_ID")), QuestionModel),
])
def test_by_seller_inputs(input, expected):
    questions_by_seller = question.by_seller(input)
    assert isinstance(questions_by_seller, expected)


@pytest.mark.parametrize("input", [[], {}, ()])
def test_by_seller_invalid_inputs(input):
    with pytest.raises(TypeError):
        question.by_seller(input)
