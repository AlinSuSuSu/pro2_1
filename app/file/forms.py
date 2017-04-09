from flask_wtf import FlaskForm
from wtforms import FileField

class FileForm(FlaskForm):
    file=FileField("上传文件")