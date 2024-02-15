from flask import Flask, render_template
from flask import request
app = Flask(__name__)

@app.route('/<user_input>')
def zxc(user_input):
    params = {
        'title': user_input,
        'news':['qwe', 'asd', 'fgh']
    }
    return render_template('index4.html', **params)
@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"
@app.route('/image_mars')
def image_mars():
    return render_template("index.html")
@app.route('/promotion')
def promotion():
    return "Человечество вырастает из детства.    <br>Человечеству мала одна планета.<br>Мы сделаем обитаемыми безжизненные пока планеты.<br>И начнем с Марса!<br>Присоединяйся!"
@app.route('/promotion_image')
def promotion_image():
    return render_template("index2.html")
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