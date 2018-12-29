import os
import pytest
import python_mercadolibre as pyme
from python_mercadolibre.questions.models import QuestionModel


@pytest.mark.vcr()
def test_by_seller():
    questions = pyme.Question()
    response = questions.by_seller(os.environ.get("USER_ID"))
    assert all(isinstance(question, QuestionModel) for question in response)
