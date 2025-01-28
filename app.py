from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        # Get data from form fields
        fullname = request.form.get('fullname')
        username = request.form.get('username')
        email = request.form.get('email')
        phone_number = request.form.get('phone-number')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm-password')
        gender = request.form.get('gender')

        # Here you can process the data, for example, save to a database or check if passwords match
        if password != confirm_password:
            return "Passwords do not match!", 400

        # Add logic to handle saving to a database or any other processing
        print(f"Registration data: {fullname}, {username}, {email}, {phone_number}, {gender}")

        return redirect(url_for('success'))

    return render_template('registration.html')

@app.route('/success')
def success():
    return "Registration successful!"

if __name__ == "__main__":
    app.run(debug=True)
