from testapp import db
from datetime import datetime

class Works(db.Model):
    #bind_key指定をしない場合はSQLALCHEMY_DATABASE_URIを参照する
    __tablename__ = 'my_works'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))  # 作品名
    description = db.Column(db.String(255))  # 作品詳細
    url_link = db.Column(db.String(255)) #作品URL
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)  # 作成日時
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)  # 更新日時

class Contacts(db.Model):
    __bind_key__ = 'contacts_db' #辞書型で設定したcontacts用のdbを指定
    __tablename__ = 'contacts'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(60))  # ユーザー名
    mail = db.Column(db.String(255))  # メール
    message = db.Column(db.String(255))  # 問い合わせ内容
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)  # 作成日時
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)  # 更新日時