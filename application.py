from flask import Flask, render_template, request, jsonify
from boredboy import train_model, apply_model

def create_app():
    app = Flask(__name__)
    def run_on_start(*args, **argv):
        url = "http://127.0.0.1:5000"
        train_model()
    run_on_start()
    return app
app = create_app()

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/api/apply_model', methods=['POST'])
def say_name():
    json = request.get_json()
    orgname = json['orgname']
    repname = json['repname']
    response = "This open-source codebase is considered: "+apply_model(orgname+"/"+repname)+". Reload this page to check a new repository!"
    return jsonify(response=response)


if __name__ == "__main__":
    app.run(debug=True)
