from flask import Flask , render_template , redirect , request , url_for
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods= ['GET' , 'POST'])


def index():
    if request.method=='POST':
        birth_date_str=request.form['birth_date']
        birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d')
        today=datetime.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return redirect(url_for('result', age=age))
    return render_template('index.html')



@app.route('/result')
def result():
    age=request.args.get('age',None)
    return render_template('result.html', age = age)




if __name__ == '__main__':
    app.run(debug=True)



