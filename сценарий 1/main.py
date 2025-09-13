from flask import Flask, render_template  #подключение библиотеки flask

app = Flask(__name__)  #иницилизируем

@app.route('/')  #app.route - это значит что это что будет выполняться
#когда пользователь заходит на главную страницу  
@app.route('/home') #если надо чтобы оди и тот же код хостил 2 части
def index():  #функция
    return "Hello world"  # пишем текст на сайте

@app.route('/a')  #пример для загрузки готового html файла (обязательно кидать в папку templates)
def a():
    return render_template("a.html")

@app.route('/apple')
def apple():
    return render_template("index.html")


if __name__ == "__main__":  #говорим что наш файл кореной и все дела
    app.run(debug=True)  #запуск проэкта с включенным режимом отсладкиr instead.
