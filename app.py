from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    test_string = request.form['test_string']
    regex_pattern = request.form['regex_pattern']
    matches = re.findall(regex_pattern, test_string)
    
    if not matches:
        matches = ['No match found']
        
    return render_template('index.html', matches=matches)

@app.route('/validate_email', methods=['POST'])
def validate_email():
    email = request.form['email']
    if not email:
        email_result = 'Please provide an email to be validated'
    elif re.match(r'^[\w\.-]+@[\w\.-]+$', email):
        email_result = 'Valid email'
    else:
        email_result = 'Invalid email'
    return render_template('index.html', email_result=email_result)

if __name__ == '__main__':
    app.run(debug=True)
