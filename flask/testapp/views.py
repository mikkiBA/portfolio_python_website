from flask import render_template, request, redirect, url_for
from .models.input import ContactForm, WorkForm
from .models.site_db import Works, Contacts
from . import db
from . import app

#index page
@app.route('/')
def index():
    my_name = '馬鳥瑞季'
    my_furigana = 'バトリミズキ'
    my_dict = {
        'prof_outline': ['神奈川県民', '大人しい性格'],
        'prof_likes': ['鳥類の観察', 'テレビゲーム', '読書'],
    }
    return render_template('testapp_t/index.html', my_name=my_name, my_furigana=my_furigana, my_dict=my_dict)

#skill page
@app.route('/skills')
def skills():
    my_skills = {
        'language': ['日本語：母国語', '英語：第二言語', 'Python', 'SQL'],
        'tools': ['VScode', 'Flask', 'OneNote', 'Excel', 'Word', 'PowerPoint', 'Outlook', 'Access', 'JIRA'],
        'database': ['SQLite', 'PostgreSQL']
    }
    return render_template('testapp_t/skills.html', my_skills=my_skills)

#my work list
@app.route('/works', methods=['GET', 'POST'])
def works_list():
    works = Works.query.all()
    return render_template('testapp_t/works_list.html', works=works)

#my work list to add
@app.route('/works_add', methods=['GET', 'POST'])
def works_add():
    work_form = WorkForm()
    if request.method == 'GET':
        return render_template('testapp_t/works_add.html', work_form=work_form)
    
    if request.method == 'POST':
        if work_form.validate_on_submit():
            work_name = request.form.get('name')
            work_description = request.form.get('description')
            work_url_link = request.form.get('url_link')           

            works = Works(
                name = work_name,
                description = work_description,
                url_link = work_url_link
            )

            db.session.add(works)
            db.session.commit()

            result = {
                'work_name': work_name,
                'work_description': work_description,
                'work_url_link': work_url_link
                }
            
            title = '作品情報の追加が完了しました'
            return render_template('testapp_t/works_add_complete.html', result=result, title=title)
        
    title = '入力内容に誤りがあります'
    return render_template('testapp_t/works_add.html', work_form=work_form, title=title)

#my work list to edit
@app.route('/works/<int:id>/edit', methods=['GET'])
def works_edit(id):
    works = Works.query.get(id)
    return render_template('testapp_t/works_edit.html', works=works)

#my work list to update
@app.route('/works/<int:id>/update', methods=['POST'])
def works_update(id):
    works = Works.query.get(id)
    works.name = request.form.get('name')
    works.description = request.form.get('description')
    works.url_link = request.form.get('url_link')

    db.session.merge(works)
    db.session.commit()

    return redirect(url_for('works_list'))


#my work list to delete
@app.route('/works/<int:id>/delete', methods=['GET'])
def works_delete(id):
    works = Works.query.get(id)

    db.session.delete(works)
    db.session.commit()

    return redirect(url_for('works_list'))


#contact page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    contact_form = ContactForm()
    if request.method == 'GET':
        title = '各項目を入力してください'
        return render_template('testapp_t/contact.html', contact_form=contact_form, title=title)
    
    if request.method == 'POST':
        if contact_form.validate_on_submit():
            form_user_name = request.form.get('user_name')
            form_email = request.form.get('email')
            form_message = request.form.get('message')

            contacts = Contacts(
                user_name = form_user_name,
                mail = form_email,
                message = form_message
            )

            db.session.add(contacts)
            db.session.commit()

            result = {
                'contact_name': form_user_name,
                'contact_email': form_email,
                'contact_message': form_message
                }
            
            title = 'お問い合わせありがとうございました'

            return render_template('testapp_t/response.html', result=result, title=title)
        
    title = '入力内容に誤りがあります'
    return render_template('testapp_t/contact.html', contact_form=contact_form, title=title)

