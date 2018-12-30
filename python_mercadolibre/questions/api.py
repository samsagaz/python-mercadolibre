from python_mercadolibre.base import PyMe
from python_mercadolibre.questions.models import QuestionModel
from python_mercadolibre.users.models import Profile


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

    def by_seller(self, seller):
        """ Get questions from registered user."""
        seller_id = str(seller)
        if isinstance(seller, Profile):
            seller_id = str(seller.id)

        url = self.full_url(self.questions_by_seller, seller_id)
        data = self._call_api('get', url)
        if not data:
            return "Question not found"
        return QuestionModel(**data)

    def by_item(self, item_id):
        """ Get questions from item."""
        url = self.full_url(self.questions_by_item, item_id)
        data = self._call_api('get', url)
        if not data:
            return "Question not found"
        return QuestionModel(**data)

    def by_customer_in_item(self, item_id, seller):
        """ Get questions from item from specific customer """
        seller_id = str(seller)
        if isinstance(seller, Profile):
            seller_id = str(seller.id)

        url = self.full_url(self.questions_by_item, item_id, 'from='+seller_id)
        data = self._call_api('get', url)
        if not data:
            return "Question not found"
        return QuestionModel(**data)

    def by_question_id(self, question_id):
        """ Get questions by question ID """
        url = self.full_url(self.question_by_id, question_id)
        data = self._call_api('get', url)
        if not data:
            return "Question not found"
        return QuestionModel(**data)

    def received(self):
        """ Get questions """
        url = self.my_questions
        data = self._call_api('get', url)
        if not data:
            return "Question not found"
        return QuestionModel(**data)

    def __repr__(self):
        return "<PyMe-Api-Question>"
