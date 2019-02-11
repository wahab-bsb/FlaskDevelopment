from app import db
from models import Departments, Employee

#db.create_all()
#db.session.commit()

#db.session.add_all(
#            [Departments('Computer Sciences'), Departments('Electrical Engineering'),Departments('Environmental Sciences'),
#            Departments('Mechanical Engineering'), Departments('Software Engineering')]
#        )
#db.session.commit()

print(Employee.query.all())
