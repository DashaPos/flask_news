from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'

news = [{'title': 'Удивительное событие в школе',
         'text': 'Вчера в местной школе произошло удивительное событие - все '
                 'ученики одновременно зевнули на уроке математики. '
                 'Преподаватель был так поражен этим коллективным зевком, '
                 'что решил отменить контрольную работу.'},
        {'title': 'Случай в зоопарке',
         'text': 'В зоопарке города произошел необычный случай - ленивец '
                 'решил не лениться и взобрался на самое высокое дерево в '
                 'своем вольере. Посетители зоопарка были поражены такой '
                 'активностью и начали снимать ленивца на видео. В итоге он '
                 'получил свой собственный канал на YouTube, где он размещает '
                 'свои приключения.'},
        {'title': 'Самый красивый пёс',
         'text': 'Сегодня в парке прошел необычный конкурс - "Самый красивый '
                 'пёс". Участники конкурса были так красивы, что судьи не '
                 'могли выбрать победителя. В итоге, конкурс был объявлен '
                 'ничейным, а участники получили награды за участие, '
                 'в том числе - пакетики конфет и игрушки в виде косточек. '
                 'Конкурс вызвал большой интерес у посетителей парка, '
                 'и его решили повторить в более масштабном формате.'}]


@app.route('/')
def index():
    return render_template('index.html',
                           news=news)


@app.route('/news_detail/<int:id>')
def news_detail(id):
    title = news[id]['title']
    text = news[id]['text']
    return render_template('news_detail.html',
                           title=title,
                           text=text)



class FeedbackForm(FlaskForm):
    name = StringField('Название',
                       validators=[DataRequired(message="Поле не должно быть пустым")])
    text = TextAreaField('Текст',
                         validators=[DataRequired(message="Поле не должно быть пустым")])
    submit = SubmitField('Добавить')
    a={'title':str(name),'text':str(text)}
    news.append(a)


@app.route('/add_news/', methods=['GET', 'POST'])
def add_news():
    form = FeedbackForm()
    if form.validate_on_submit():
        name = form.name.data
        text = form.text.data
        print(name, text)
        return redirect('/')
    return render_template('add_news.html', form=form)





if __name__ == '__main__':
    app.run(debug=True)