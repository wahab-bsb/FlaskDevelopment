from app import db, CustomerData

record1 = CustomerData('Emile', 'Rose', 23)
record2 = CustomerData('Bob', 'Mike', 20)
record3 = CustomerData('Sam', 'Jason', 30)
record4 = CustomerData('Micheal', 'Steven', 25)
record5 = CustomerData('Sarah', 'Micheal', 27)

db.session.add_all([record1, record2, record3, record4, record5])
db.session.commit()


records = CustomerData.query.all()
print(records)

print('----------------------------------------------')

recordQuery = CustomerData.query.filter_by(firstName='Emile', lastName='Rose')
print(recordQuery.all())

print('----------------------------------------------')

recordQuery.age = 24
db.session.commit()
recordQuery = CustomerData.query.filter_by(firstName='Emile', lastName='Rose')
print(recordQuery.all())

print('----------------------------------------------')

#db.session.delete(recordQueryw)
#db.session.commit()

#records = CustomerData.query.all()
#print(records)

print('----------------------------------------------')
