from __main__ import jsonify, db, request, render_template, redirect, url_for, uuid
from models.userModel import User


class TeacherController():

    @staticmethod
    def get_all_teachers():
        teachers = User.query.all()
        teachers_dict = [teacher.to_dict() for teacher in teachers]
        return teachers_dict

    @staticmethod
    def show_teacher(id):
        teacher = User.query.get(id)
        if not teacher:
            return jsonify({'message': 'Teacher not found'}), 404
        return jsonify({'teacher': teacher.to_dict()}), 200

    @staticmethod
    def create_teacher():
        name = request.form.get('name')
        email = request.form.get('email')
        teacher_id = str(uuid.uuid4())

        new_teacher = User(id=teacher_id, name=name, email=email, role=1)

        db.session.add(new_teacher)
        db.session.commit()

        return redirect(url_for('teachers_index'))

    @staticmethod
    def update_teacher(id):
        teacher = User.query.get(id)
        if not teacher:
            return jsonify({'message': 'Teacher not found'}), 404

        name = request.form.get('name')
        email = request.form.get('email')

        teacher.name = name
        teacher.email = email

        db.session.commit()

        return redirect(url_for('teachers_index'))

    @staticmethod
    def delete_teacher(id):
        teacher = User.query.get(id)
        if not teacher:
            return jsonify({'message': 'Teacher not found'}), 404
        db.session.delete(teacher)
        db.session.commit()
        return '', 204


def teacherController():
    return None