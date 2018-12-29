from python_mercadolibre.questions.models import QuestionModel


def test_question_ok():
    kwargs = {'item_id': 'MLA123123123'}
    question = QuestionModel(**kwargs)

    assert question.item_id == 'MLA123123123'
