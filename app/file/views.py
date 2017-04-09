from flask import render_template,url_for
from app.file import file
from .forms import FileForm
@file.route('/file')
def file():
    form =FileForm()
    return render_template('/file/file.html',form=form)
