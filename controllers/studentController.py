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
            return jsonify({'message': 'student not found'}), 404
        return jsonify({'student': student.to_dict()}), 200

    @staticmethod
    def create_student():
        name = request.form.get('name')
        date = request.form.get('date')
        start_time = request.form.get('start_time')
        end_time = request.form.get('end_time')
        leson_id = str(uuid.uuid4())

        new_student = User(id=leson_id, name=name, date=date, start_time=start_time, end_time=end_time)

        db.session.add(new_student)
        db.session.commit()

        return redirect(url_for('students_index'))

    @staticmethod
    def update_student(id):
        student = User.query.get(id)
        if not student:
            return jsonify({'message': 'student not found'}), 404

        name = request.form.get('name')
        date = request.form.get('date')
        start_time = request.form.get('start_time')
        end_time = request.form.get('end_time')

        student.name = name
        student.date = date
        student.start_time = start_time
        student.end_time = end_time

        db.session.commit()

        return redirect(url_for('students_index'))

    @staticmethod
    def delete_student(id):
        student = User.query.get(id)
        if not student:
            return jsonify({'message': 'student not found'}), 404
        db.session.delete(student)
        db.session.commit()
        return '', 204


