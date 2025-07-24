from flask import Flask, render_template, redirect, url_for,request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.utils import secure_filename
import os
from utils import admin_required
from models import db, User
from forms import LoginForm, RegisterForm, EditProfileForm, AdminCreateUserForm
from werkzeug.security import generate_password_hash,check_password_hash
import hashlib
app = Flask(__name__)
app.config.from_pyfile('config.py')


db.init_app(app)
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

# Create tables if they don't exist
with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=hashed_password,  # Password should be hashed in production!
            # Don't store confirm_password — it's only for form validation
            profile_image='default.png'  
        )
        db.session.add(user)
        db.session.commit()
        flash('Registration successful.')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)
        
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login failed. Check your email and password.', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('index'))

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')
@app.route('/edit-profile', methods=['GET', 'POST'])
@login_required 
def edit_profile():
    form = EditProfileForm(obj=current_user)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        if form.profile_image.data:
            img_file = form.profile_image.data
            filename = secure_filename(form.profile_image.data.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            img_file.save(filepath)
            current_user.profile_image = filename
        db.session.commit()
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('profile'))
    return render_template('edit_profile.html', form=form)
# Admin Routes
@app.route('/admin/dashboard')
@login_required
@admin_required
def admin_dashboard():
    users = User.query.filter_by(is_admin=False).all()
    return render_template('admin/dashboard.html', users=users)
@app.route('/admin/create', methods=['GET', 'POST'])
@login_required
@admin_required
def create_user():
    form = AdminCreateUserForm()
    if form.validate_on_submit():
        
        admin_user = User(
        username='admin',
        email='admin@example.com',
        password=generate_password_hash('admin123'),  # secure in prod!
        is_admin=True
    )
        db.session.add(admin_user)
        db.session.commit()
        flash('User created successfully!', 'success')
        return redirect(url_for('admin_dashboard'))
    return render_template('admin/create_user.html', form=form)
@app.route('/admin/delete/<int:user_id>',methods=['POST'])
@login_required
@admin_required
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    if user.is_admin:
        flash('Cannot delete an admin user.', 'danger')
        return redirect(url_for('admin_dashboard'))
    db.session.delete(user)
    db.session.commit()
    flash('User deleted successfully!', 'success')
    return redirect(url_for('admin_dashboard'))
from flask import jsonify
from werkzeug.security import generate_password_hash
from models import db, User

@app.route('/delete-wrong-admin')
def delete_wrong_admin():
    user = User.query.filter_by(email='admin@example.com', is_admin=False).first()
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify(message="Mistaken admin deleted successfully.")
    return jsonify(message="No such mistaken admin found.")

    
if __name__ == '__main__':
    app.run(debug=True)
    