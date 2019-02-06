from app import db, EmployeeData, Department
from sqlalchemy import and_

#db.session.add_all([Department('Computer Science'), Department('Electrical Engineering'), Department('Mechanical Engineering'), Department('Environmental Science')])
#db.session.commit()

#print(Department.query.all())

#db.session.add_all([EmployeeData('Cindy', 'Lou', 1), EmployeeData('Hena', 'Helmar', 2), EmployeeData('Steve', 'Blue', 3), EmployeeData('Jonathan', 'Stuard', 4)])
#db.session.commit()


#db.session.add(EmployeeData('Allen', 'Rose', 5))
#db.session.commit()

record = EmployeeData.query.filter(and_(EmployeeData.first_name == 'Allen', EmployeeData.last_name == 'Rose'))
record[0].department_id = 1
db.session.commit()

print(EmployeeData.query.all())
