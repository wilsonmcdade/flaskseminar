from flask import Flask, render_template

app=Flask(__name__)

users = ["mcdade","wilnil","klaus","potate","pogman"]

@app.route('/')
def index():
    return render_template("index.html",users=users,currentyear="2020")

if __name__ == "__main__":
    app.run("0.0.0.0",port="8080")
