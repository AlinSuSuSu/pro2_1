from flask import render_template,url_for
from app.file import file
from .forms import FileForm
from flask_uploads import UploadSet
from flask_uploads import UploadSet


files=UploadSet('files')
@file.route('/file')
def file():
    form =FileForm()
    if form.validate_on_submit():
        filename=files.save(form.file.data)
        file_url=files.url(filename)
    else:
        file_url=None
    return render_template('/file/file.html',form=form)
