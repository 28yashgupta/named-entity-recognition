from flask import Flask,request,render_template
import spacy
from spacy import displacy
nlp = spacy.load('en_core_web_sm')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/entity', methods=['POST', 'GET'])
def entity():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            readable_file = file.read().decode('utf-8', errors='ignore')
            docs = nlp(readable_file)
            html = displacy.render(docs, style='ent', jupyter=False)
            return render_template('index.html', html=html, text=readable_file)

    # If it's a GET request or the file wasn't provided, you may want to handle it appropriately.
    return render_template('index.html', html=None, text=None)


if __name__=='__main__':
    app.run(debug=True)