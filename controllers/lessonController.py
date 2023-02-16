from __main__ import jsonify, db, request, render_template, redirect, url_for, uuid
from models.lesson import Lesson


class LessonController():

    @staticmethod
    def get_all_lessons():
        lessons = Lesson.query.all()
        lessons_dict = [lesson.to_dict() for lesson in lessons]
        return lessons_dict

    @staticmethod
    def show_lesson(id):
        lesson = Lesson.query.get(id)
        if not lesson:
            return jsonify({'message': 'Lesson not found'}), 404
        return jsonify({'lesson': lesson.to_dict()}), 200

    @staticmethod
    def create_lesson():
        name = request.form.get('name')
        date = request.form.get('date')
        start_time = request.form.get('start_time')
        end_time = request.form.get('end_time')
        leson_id = str(uuid.uuid4())

        new_lesson = Lesson(id=leson_id, name=name, date=date, start_time=start_time, end_time=end_time)

        db.session.add(new_lesson)
        db.session.commit()

        return redirect(url_for('lessons_index'))

    @staticmethod
    def update_lesson(id):
        lesson = Lesson.query.get(id)
        if not lesson:
            return jsonify({'message': 'Lesson not found'}), 404

        name = request.form.get('name')
        date = request.form.get('date')
        start_time = request.form.get('start_time')
        end_time = request.form.get('end_time')

        lesson.name = name
        lesson.date = date
        lesson.start_time = start_time
        lesson.end_time = end_time

        db.session.commit()

        return redirect(url_for('lessons_index'))

    @staticmethod
    def delete_lesson(id):
        lesson = Lesson.query.get(id)
        if not lesson:
            return jsonify({'message': 'Lesson not found'}), 404
        db.session.delete(lesson)
        db.session.commit()
        return '', 204


