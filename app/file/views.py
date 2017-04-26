from flask import abort,redirect,render_template,request,send_from_directory,url_for
from app.file import file
from .forms import FileForm
from .. import photos
from app.models import File
import app
from app import db
import config
@file.route('/download',methods=['GET','POST'])
def download():
    form =FileForm()
    query = File.query.all()

    if form.validate_on_submit():
        filename=photos.save(form.photo.data)
        file_url=photos.url(filename)
        rec=File(filename=filename)
        db.session.add(rec)
        db.session.commit()
        return redirect(url_for('file.download'))
        #return redirect(url_for('file.show'),id=rec.id)
    else:
        file_url=None

    return render_template('/file/file.html',form=form,file_url=file_url,query=query)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1] in config['ALLOWED_EXTENSIONS']

@file.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(config['UPLOAD_FOLDER'],filename)

'''
@file.route('/show/<id>')
def show(id):
    photo=File.load(id)
    if photo is None:
        abort(404)
    url=photo.url(photo.filename)
    return render_template('file/show.html',url=url)
    '''