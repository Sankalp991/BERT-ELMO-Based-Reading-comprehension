from flask import Flask, render_template, request, send_file
import warnings
warnings.filterwarnings("ignore")
from bert import QA

DEBUG = False
app = Flask(__name__)
app.config.from_object(__name__)


model = QA("model")

@app.route('/')
def single_people_code():
    return render_template('index.html')

@app.route("/",methods=['POST','GET'])
def predict():
    if request.method == 'POST':

        form = request.form
        results = request.form

        doc = results['passage']

        q = results['question']

        try:


            out = model.predict(doc,q)
            print(out['best_span_str'])
            res = str(out['best_span_str'])

        except Exception as e:
            res = e
    return render_template('index.html',messages=res,passage=doc,question=q)

if __name__ == "__main__":
    app.run('127.0.0.1',port=8000)