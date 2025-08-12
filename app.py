from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "<h2>Hola — Sample App en puerto 8888</h2>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888)
