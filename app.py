from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Тимчасова база даних для збереження інформації про пацієнтів
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
    if index < len(patients):
        patient = patients[index]
        if request.method == 'POST':
            patient['name'] = request.form['name']
            patient['age'] = request.form['age']
            patient['condition'] = request.form['condition']
            return redirect(url_for('index'))
        return render_template('edit_patient.html', patient=patient, index=index)
    else:
        return "Patient with index {} not found".format(index), 404


@app.route('/login')
def login():
    return "Login Page"

@app.route('/diseases')
def diseases():
    return "Diseases Page"

@app.route('/chat')
def chat():
    return "Chat Page"

@app.route('/about')
def about():
    return "About Page"

if __name__ == '__main__':
    app.run(debug=True)
