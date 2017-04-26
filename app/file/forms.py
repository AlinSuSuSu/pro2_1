from flask_wtf import FlaskForm
from wtforms import FileField,SubmitField
from flask_wtf.file import FileRequired,FileAllowed
from ..import photos
class FileForm(FlaskForm):
    photo=FileField(validators=[FileAllowed(photos,'默认上传类型'),FileRequired('文件未上传')])
    submit=SubmitField('上传')