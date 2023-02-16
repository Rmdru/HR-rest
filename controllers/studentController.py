from __main__ import jsonify, db, request, render_template, redirect, url_for, uuid
from models.userModel import User


class StudentController():
    __table_args__ = {'extend_existing': True}

    @staticmethod
    def get_all_students():
        students = User.query.all()
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
        password = request.form.get('password')
        student_number = int(request.form.get('student_number'))
        student_id = str(uuid.uuid4())

        new_student = User(id=student_id, name=name, email=email, password=password, studentNumber=student_number, role=1)

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


