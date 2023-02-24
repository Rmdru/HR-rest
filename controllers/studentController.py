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
        name = request.form.get('name')
        email = request.form.get('email')
        student_number = int(request.form.get('student_number'))

        new_student = User(name=name, email=email, studentNumber=student_number, role=1)

        if User.query.filter((User.studentNumber == student_number) | (User.email == email)).first() is not None:
            flash("Error: Dit studentnummer of email bestaat al.")
            return redirect(url_for('students_index'))

        db.session.add(new_student)
        db.session.commit()

        return redirect(url_for('students_index'))

    @staticmethod
    def update_student(id):
        student = User.query.get(id)
        if not student:
            return jsonify({'message': 'Student not found'}), 404

        name = request.form.get('name')
        email = request.form.get('email')
        student_number = request.form.get('student_number')

        student.name = name
        student.email = email
        student.student_number = student_number

        db.session.commit()

        return redirect(url_for('students_index'))

    @staticmethod
    def delete_student(id):
        student = User.query.get(id)
        if not student:
            return jsonify({'message': 'Student not found'}), 404
        db.session.delete(student)
        db.session.commit()
        return '', 204


