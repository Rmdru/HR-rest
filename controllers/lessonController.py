from __main__ import jsonify, db, request, render_template, redirect, url_for, uuid
from models.lessonModel import Lesson


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
        lesson_id = str(uuid.uuid4())
        name = request.form.get('name')
        question = request.form.get('question')
        date = request.form.get('date')
        start_time = request.form.get('start_time')
        end_time = request.form.get('end_time')

        new_lesson = Lesson(id=lesson_id, name=name, question=question, date=date, start_time=start_time, end_time=end_time)

        db.session.add(new_lesson)
        db.session.commit()

        return redirect(url_for('lessons_index'))

    @staticmethod
    def update_lesson(id):
        lesson = Lesson.query.get(id)
        if not lesson:
            return jsonify({'message': 'Lesson not found'}), 404

        print(request.form.get('question'), lesson.question)
        name = request.form.get('name')
        question = request.form.get('question')
        date = request.form.get('date')
        start_time = request.form.get('start_time')
        end_time = request.form.get('end_time')

        lesson.name = name
        lesson.question = question
        lesson.date = date
        lesson.start_time = start_time
        lesson.end_time = end_time

        db.session.commit()

        return redirect(url_for('lessons_index'))

    @staticmethod
    def delete_lesson(id):
        lesson = Lesson.query.get(id)
        print(lesson)
        if not lesson:
            return jsonify({'message': 'Lesson not found'}), 404
        db.session.delete(lesson)
        db.session.commit()
        return '', 204

    @staticmethod
    def filter_lessons(input):
        if input != "null":
            search = "%{}%".format(input)

            results = Lesson.query.filter(Lesson.name.like(search))
        else:
            results = Lesson.query.all()

        if not results:
            return jsonify({'message': 'No results'}), 404
        results_dict = [result.to_dict() for result in results]
        return results_dict