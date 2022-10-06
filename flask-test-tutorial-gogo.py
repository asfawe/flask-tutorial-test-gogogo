from flask import Blueprint, render_template

from pybo.models import Question

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/')
def index():
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template('question/question_list.html', question_list=question_list)

@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question)

# return_template의 첫번째 아규먼트는 사용자에게 보여줄 html이고, 두번째는 사용자에게 보여줄 html에 어떤 데이터를 보낼지 적는 겁니다.