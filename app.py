from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

patients = []

@app.route('/')
def index():
    return render_template('index.html', patients=patients)

@app.route('/add_patient', methods=['GET', 'POST'])
def add_patient():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        condition = request.form['condition']
        patients.append({'name': name, 'age': age, 'condition': condition})
        return redirect(url_for('index'))
    return render_template('add_patient.html')

@app.route('/edit_patient/<int:index>', methods=['GET', 'POST'])
def edit_patient(index):
    patient = patients[index]
    if request.method == 'POST':
        patient['name'] = request.form['name']
        patient['age'] = request.form['age']
        patient['condition'] = request.form['condition']
        return redirect(url_for('index'))
    return render_template('edit_patient.html', patient=patient, index=index)

@app.route('/delete_patient/<int:index>')
def delete_patient(index):
    del patients[index]
    return redirect(url_for('index'))

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/diseases')
def diseases():
    return render_template('diseases.html')

@app.route('/diagnostics')
def diagnostics():
    return render_template('diagnostics.html')

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)