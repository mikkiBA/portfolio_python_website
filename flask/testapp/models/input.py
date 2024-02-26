from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Length, Email

class ContactForm(FlaskForm):
    user_name = StringField('お名前', validators=[InputRequired(),
                                                Length(min=1, max=60, message='1文字以上60文字以内で入力してください。')])
    
    email = StringField('返信先メールアドレス',
                       validators=[InputRequired(),
                                   Length(min=10, max=255, message='10文字以上255文字以内で入力してください。'),
                                   Email()])

    message = TextAreaField('お問い合わせ内容',
                            validators=[InputRequired(),
                                        Length(min=5, max=255, message='5文字以上255文字以内で入力してください。')])
    
    submit = SubmitField('送信')

class WorkForm(FlaskForm):
    name = StringField('作品名', validators=[InputRequired(), Length(max=255, message='255文字以内で入力')])

    description = StringField('作品詳細', validators=[InputRequired(), Length(max=255, message='255文字以内で入力')])

    url_link = StringField('作品URL', validators=[InputRequired(), Length(max=255, message='255文字以内で入力')])

    submit = SubmitField('追加')
