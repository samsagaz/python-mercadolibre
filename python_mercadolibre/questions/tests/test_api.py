import pytest
from python_mercadolibre.questions.models import QuestionModel
from python_mercadolibre.questions.api import Question
from python_mercadolibre.users.api import User


@pytest.fixture
@pytest.mark.vcr()
def user():
    return User()


@pytest.fixture
@pytest.mark.vcr()
def profile(user):
    return user.profile()


@pytest.fixture
@pytest.mark.vcr()
def question():
    return Question()


@pytest.mark.vcr()
def test_by_seller_inputs(question, profile):
    questions_by_seller = question.by_seller(profile.id)
    assert isinstance(questions_by_seller, QuestionModel)


@pytest.mark.vcr()
@pytest.mark.parametrize("test_input", [profile, user, str, [], {}, (), bool])
def test_invalid_inputs_by_seller(test_input):
    with pytest.raises(Exception):
        question.by_seller(test_input)
