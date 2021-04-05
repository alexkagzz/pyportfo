from flask import Flask, render_template, request
import csv

app = Flask(__name__)


@app.route('/')
@app.route('/<string:page_name>')
def html_page(page_name=None):
    if page_name:
        return render_template(f'{page_name}.html')
    else:
        return render_template('index.html')


def write_to_txt(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', mode='a',newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2,delimiter=",", quotechar='"' , quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods = ['POST','GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # write_to_txt(data)
            write_to_csv(data)
            return render_template('thankyou.html')
        except:
            return 'Wasn''t saved to Database'
    else:
        return 'Form Submission was UnSuccessful'
