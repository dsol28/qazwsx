from flask import Flask, render_template
from flask import request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired



app = Flask(__name__)
app.config['SECRET_KEY'] = 'zxczxczxc'

class LoginForm(FlaskForm):
    surname = StringField('Имя', validators=[DataRequired()])
    name = StringField('Фамилия', validators=[DataRequired()])
    education = SelectField('Образование', choices=[('Начальное','Начальное'),
                                                    ('Среднее', 'Среднее'),
                                                    ('Средне-специальное', 'Средне-специальное'),
                                                    ('Высшее', 'Высшее')])
    profession = SelectField('Профессия', choices=[('Пилот','Пилот'),
                                                    ('Строитель', 'Строитель'),
                                                    ('Экзобиолог', 'Экзобиолог'),
                                                    ('Киберинженер', 'Киберинженер')])
    sex = SelectField('Пол', choices=[('Мужчина','Мужчина'),
                                                    ('Женщина', 'Женщина')])
    motivation = StringField('Мотивация', validators=[DataRequired()])
    ready = SelectField('Готов остаться на марте?', choices=[('ДА','ДА'),
                                                    ('НЕТ', 'НЕТ')])
    submit = SubmitField('Войти')

@app.route('/answer', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return render_template('auto_answer.html', form=form)
    return render_template('login.html', title='Авторизация', form=form)

'''@app_route('/success')
def success():'''

@app.route('/<user_input>')
def zxc(user_input):
    params = {
        'title': user_input,
        'news':['qwe', 'asd', 'fgh']
    }
    return render_template('index4.html', **params)
@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести! "
@app.route('/image_mars')
def image_mars():
    return render_template("index.html")
@app.route('/promotion')
def promotion():
    return "Человечество вырастает из детства.     <br>Человечеству мала одна планета.<br>Мы сделаем обитаемыми безжизненные пока планеты.<br>И начнем с Марса!<br>Присоединяйся!"
@app.route('/promotion_image')
def promotion_image():
    return render_template("index2.html")

@app.route('/training/<zxc>')
def training(zxc):
    return render_template("index5.html", zxc=zxc)
@app.route('/list_prof/<zxc>')
def list_prof(zxc):
    return render_template("index6.html", zxc=zxc)
@app.route('/asronaut_selection', methods=['GET', 'POST'])
def asronaut_selection():
    if request.method == 'GET':
        return render_template("index3.html")
    elif request.method == 'POST':
        for key, value in request.form.items():
            print(value)
        return render_template("index3.html")


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)