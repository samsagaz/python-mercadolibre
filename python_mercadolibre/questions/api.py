from python_mercadolibre.base import PyMe
from python_mercadolibre.questions.models import QuestionModel, QuestionPostModel


class Question(PyMe):
    """
    Mercadolibre API Questions and Answers Funcionality
    See: https://api.mercadolibre.com/questions

    """
    question_url = '/questions'
    question_by_id = "/"
    questions_by_seller = "/search?seller_id="
    questions_by_item = "/search?item="
    my_questions = "/my/received_questions/search"

    def full_url(self, relativ_url, *args):
        total_args = '&'.join(args)
        url = f"{self.question_url}{relativ_url}{total_args}"
        return url

    def by_seller(self, seller_id):
        """ Get questions from registered user."""
        url = self.full_url(self.questions_by_seller, seller_id)
        data = self._call_api('get', url)
        if not data:
            return "Question not found"
        return [QuestionModel(**question) for question in data['questions']]

    def by_item(self, item_id):
        """ Get questions from item."""
        url = self.full_url(self.questions_by_item, item_id)
        data = self._call_api('get', url)
        if not data:
            return "Question not found"
        return [QuestionModel(**question) for question in data['questions']]

    def by_customer_and_item(self, customer_id, item_id):
        """ Get questions from item from specific customer """
        url = self.full_url(self.questions_by_item, item_id, 'from='+customer_id)
        data = self._call_api('get', url)
        if not data:
            return "Question not found"
        return [QuestionModel(**question) for question in data['questions']]

    def by_question(self, question_id):
        """ Get questions by question ID """
        url = self.full_url(self.question_by_id, question_id)
        data = self._call_api('get', url)
        print('123123123 ---- ' + str(data))
        if not data:
            return "Question not found"
        return [QuestionModel(**data)]

    def received(self):
        """ Get questions """
        url = self.my_questions
        data = self._call_api('get', url)
        if not data:
            return "Question not found"
        return [QuestionModel(**question) for question in data['questions']]

    def create_question(self, item_id, text):
        data = {
            'item_id': item_id,
            'text': text
            }
        url = self.full_url(self.question_by_id, item_id)
        data = self._call_api('post', url, data)
        return QuestionPostModel(**data)

    def __repr__(self):
        return "<PyMe-Api-Question>"
