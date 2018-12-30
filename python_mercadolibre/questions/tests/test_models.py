from python_mercadolibre.questions.models import QuestionModel


def test_question_ok():
    kwargs = {'question_id': 'MLA123123123'}
    question = QuestionModel(**kwargs)
    assert question.question_id == 'MLA123123123'
