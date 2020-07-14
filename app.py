from flask import Flask, render_template, url_for, request
import translation
from sample import name

app = Flask(__name__)

@app.route('/sample',methods=['POST','GET'])
def sample():
    if request == 'POST':
        n = request.form['name']
        a = str(name(n))
        return render_template('abc.html',value = str(n))
    return render_template('abc.html',abc = name('Armughan'))


@app.route('/', methods=['POST','GET'])
def new():
    result = ""
    text = ""
    language_key = translation.languages().keys()
    language_value = translation.languages().values()
    language_name = request.form.get('languages')
    if request.method == 'POST':
        text = request.form['to_translate']
        result = translation.eng_to_urdu(text)
        language_name = request.form.get('languages')
    return render_template('sample.html', title='New',  translated=str(result), lang_keys=list(language_key) , languages=list(language_value),text_value=text,len = len(language_value))

if __name__ == "__main__":
    app.run(debug=True)