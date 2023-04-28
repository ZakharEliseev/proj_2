from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import LoginForm

list_endpoints = ['main_index', 'index', 'login', 'logout', 'register', 'edit_profile', 'user', 'main_admins',
                  'administrators', 'experts', 'bak', 'it', 'admins', 'baks', 'its']
for i in list_endpoints:
    if i in app.view_functions:
        del app.view_functions[i]


@app.route('/')
@app.route('/index', endpoint='index')
def main_index():
    return render_template('index.html')


@app.route('/admins', endpoint='admins')
def main_admins():
    return render_template('administrators.html')


@app.route('/experts', endpoint='experts')
def main_experts():
    return render_template('experts.html')


@app.route('/baks', endpoint='baks')
def main_baks():
    return render_template('bak.html')


@app.route('/its', endpoint='its')
def main_its():
    return render_template('it.html')


@app.route('/login', endpoint='login', methods=['GET', 'POST'])
def main_login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
