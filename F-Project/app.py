from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # مفتاح سري لتشفير الجلسة

@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username  # حفظ اسم المستخدم في الجلسة
        return redirect(url_for('login'))
    if 'username' in session:
        return render_template('login.html', username=session['username'])
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('username', None)  # حذف اسم المستخدم من الجلسة
    return render_template('logout.html')

if __name__ == '__main__':
    app.run(debug=True)