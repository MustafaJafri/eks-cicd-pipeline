from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome to the AL=Nafi!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

# Additional code
@app.route('/about')
def about():
    return 'About AL Nafi: We are an online e-learning platform.'

@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}! Welcome to AL Nafi!'

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f'Thank you, {name}, for submitting the form!'
    return '''
        <form method="post">
            Name: <input type="text" name="name"><br>
            <input type="submit" value="Submit">
        </form>
    '''

