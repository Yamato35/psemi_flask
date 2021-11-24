from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    s = "abc"
    lis = ["a1", "a2", "a3"]
    dictionary = {"name": "John", "age": 24}
    flag = True

    return render_template('indexjinja.html', s=s, lis=lis, dictionary=dictionary, flag=flag)


if __name__ == "__main__":
    app.debug = True
    app.run()

    a = 0
    for i in range(10):
        a = i
        list.insert(i, a)

 'return render_template('', lis=lis, dictionary=dictionary, flag=flag)'
'dictionary = {"nickname": "yam", "age": "20", "address": "Tokyo"}'