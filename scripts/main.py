from flask import Flask

app = Flask(_name_)

@app.route("/")
def Hello():
    return "Hello, This is combat.py file!"

if _name_ == 'main':
    app.run()