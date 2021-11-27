from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    lis = []

    for i in range(10):
        a = i
        lis.insert(i, a)

    dictionary = {"nickname": "yam", "age": 20, "address": "Tokyo"}
    flag = True

    return render_template('flaskQ.html', lis=lis, dictionary=dictionary, flag=flag)


if __name__ == "__main__":
    app.debug = True
    app.run(port = 8000)

# flaskQ.pyというファイル名ではなぜか実行できなかったです。
# しかし他のファイル名で実行したら成功したので、課題内容は達成していると思います。
