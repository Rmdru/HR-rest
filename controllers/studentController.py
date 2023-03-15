from __main__ import jsonify, db, request, render_template, redirect, url_for, uuid, flash
from models.userModel import User


class StudentController():

    @staticmethod
    def get_all_students():
        students = User.query.filter_by(role=1)
        students_dict = [student.to_dict() for student in students]
        return students_dict

    @staticmethod
    def show_student(id):
        student = User.query.get(id)
        if not student:
            return jsonify({'message': 'Student not found'}), 404
        return jsonify({'student': student.to_dict()}), 200

    @staticmethod
    def create_student():
        name = request.json.get('name')
        email = request.json.get('email')
        student_number = request.json.get('student_number')

        existing_student = User.query.filter((User.studentNumber == student_number) | (User.email == email)).first()
        if existing_student is not None:
            return jsonify({'message': 'Error: Dit studentnummer of email bestaat al.'})

        new_student = User(name=name, email=email, studentNumber=student_number, role=1)
        db.session.add(new_student)
        db.session.commit()

        return jsonify({'message': 'success'})

    @staticmethod
    def update_student(id):
        student = User.query.get(id)
        if not student:
            return jsonify({'message': 'Student not found'}), 404

        name = request.json.get('name')
        email = request.json.get('email')
        student_number = request.json.get('student_number')

        existing_student = User.query.filter((User.studentNumber == student_number) | (User.email == email)).filter(User.id != id).first()
        if existing_student is not None:
            return jsonify({'message': 'Error: Dit studentnummer of email bestaat al.'})

        student.name = name
        student.email = email
        student.studentNumber = student_number

        db.session.commit()

        return jsonify({'message': 'success'})
    
    @staticmethod
    def delete_student(id):
        student = User.query.get(id)
        if not student:
            return jsonify({'message': 'Student not found'}), 404
        db.session.delete(student)
        db.session.commit()
        return '', 204

    @staticmethod
    def filter_student(input):
        if input != "null":
            search = "%{}%".format(input)

            results = User.query.filter_by(role=1).filter(User.name.like(search))
        else:
            results = User.query.filter_by(role=1)

        if not results:
            return jsonify({'message': 'No results'}), 404
        results_dict = [result.to_dict() for result in results]
        return results_dict