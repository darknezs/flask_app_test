from flask import Flask,request,jsonify,render_template
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
import json
app = Flask(__name__)

DATABASE_URL = 'mysql+mysqldb://username:passwordไง@host/dbname'
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/students')
def get_students():
    db = next(get_db())
    students = db.query(Student).all()
    data = []
    for i in students:
        name = i.name
        id = i.id
        data.append({'id': id, 'name':name})
    return data


@app.post('/students')
def create_students():
    db = next(get_db())

    if 'name' not in request.json:
        return jsonify({'message':'name is require'}),400

    name = request.json['name']
    if not name:
        return jsonify({'message':'no val'}),400

    new_student = Student(name=name)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    data = []
    data.append({'id': new_student.id, 'name':new_student.name})
    return data

@app.put('/students')
def update_studens():
    db = next(get_db())

    if 'name' not in request.json or 'id' not in request.json:
        return jsonify({'message':'name or id is missing'}),400

    id = request.json['id']
    name = request.json['name']

    if not name or not id:
        return jsonify({'message':'name or id is missing'}),400

    std_to_update = db.query(Student).filter(Student.id == id).first()

    if not std_to_update:
        return jsonify({'message':'student not found'}),400

    std_to_update.name = name
    db.commit()
    db.refresh(std_to_update)
    return {
        "id" : std_to_update.id,
        "name" : std_to_update.name,
        "message" : "update succussfuly"
    }

@app.delete('/students')
def delete_student():
    db = next(get_db())

    if 'id' not in request.json:
        return jsonify({'message':'id is missing'}),400

    id = request.json['id']

    if not id:
        return jsonify({'message':'id is missing'}),400

    std_to_delete = db.query(Student).filter(Student.id == id).first()
    if not std_to_delete:
        return jsonify({'message':'studen not found'}),400

    db.delete(std_to_delete)
    db.commit()
    return jsonify({'message':f'{std_to_delete.name} is GONE'}),201

@app.get('/')
def indx():
    return 'im index page'
if __name__ == '__main__':
    app.run(debug=True, port=5454)
# db = SQLAlchemy(app)
