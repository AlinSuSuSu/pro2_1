from flask_wtf import FlaskForm
from wtforms import FileField,SubmitField
from flask_wtf.file import FileRequired,FileAllowed
from flask_uploads import UploadSet

files=UploadSet('files')
class FileForm(FlaskForm):
    file=FileField(validators=[FileAllowed(files,'上传默认类型'),FileRequired('文件未上传')])
    submit=SubmitField('上传')