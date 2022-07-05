from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


@app.route("/")
def index():
    users = User.query.all()
    return render_template("index.html", users=users)


@app.route('/user/<int:id>')
def user(id):
    user = User.query.filter_by(id=id).first()
    return render_template('user.html', user=user)


@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    user = User.query.filter_by(id=id).first()
    if request.method == "POST":
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('delete.html', user=user)


@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':
        user = User()
        user.username = request.form['username']
        user.email = request.form['email']
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)