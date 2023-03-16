from __main__ import jsonify, db, request, render_template, redirect, url_for, uuid, flash
from models.userModel import User


class TeacherController():

    @staticmethod
    def get_all_teachers():
        teachers = User.query.filter_by(role=0)
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

        new_teacher = User(id=teacher_id, name=name, email=email, role=2)

        if User.query.filter((User.email == email)).first() is not None:
            flash("Error: Een docent met deze email bestaat al.")
            return redirect(url_for('teachers_index'))

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
    
    @staticmethod
    def filter_teacher(input):
        if input != "null":
            search = "%{}%".format(input)

            results = User.query.filter_by(role=0).filter(User.name.like(search))
        else:
            results = User.query.filter_by(role=0)

        if not results:
            return jsonify({'message': 'No results'}), 404
        results_dict = [result.to_dict() for result in results]
        return results_dict


def teacherController():
    return None