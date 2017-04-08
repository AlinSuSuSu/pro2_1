from flask_wtf import FlaskForm
from wtforms import StringField,DateField,DateTimeField,SelectField,SubmitField
from wtforms.validators import Required,Regexp,ValidationError

from app.models import House,Owner

class OwnerForm(FlaskForm):
    ownername = StringField('业主名称',validators=[Required(message='不能为空')])
    house_houseid=SelectField("房屋编号",validators=[Required()])
    ownerdate=DateField("进户日期",validators=[Required()],format='%Y-%m-%d')
    submit=SubmitField("提交")
    def __init__(self,*args,**kwargs):
        super(OwnerForm, self).__init__(*args, **kwargs)
        qu=House.query.all()
        self.house_houseid.choices=[]
        a=0
        for q in qu:
            a =a+1
            self.house_houseid.choices.append((q.houseid,q.houseid))

    def validate_house_houseid(self,field):
        if Owner.query.filter_by(house_houseid = field.data).first():
            return ValidationError("该房子已有业主")