from __main__ import jsonify, db, request, render_template, redirect, url_for, uuid, flash
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
        name = request.json.get('name')
        question = request.json.get('question')
        date = request.json.get('date')
        start_time = request.json.get('start_time')
        end_time = request.json.get('end_time')

        existing_lesson = Lesson.query.filter((Lesson.name == name)).first()
        if existing_lesson is not None:
            return jsonify({'message': 'Error: Deze les bestaat al.'})

        new_lesson = Lesson(id=lesson_id, name=name, question=question, date=date, start_time=start_time, end_time=end_time)

        db.session.add(new_lesson)
        db.session.commit()

        return jsonify({'message': 'success'})

    @staticmethod
    def update_lesson(id):
        lesson = Lesson.query.get(id)
        if not lesson:
            return jsonify({'message': 'Lesson not found'}), 404

        name = request.json.get('name')
        question = request.json.get('question')
        date = request.json.get('date')
        start_time = request.json.get('start_time')
        end_time = request.json.get('end_time')

        existing_lesson = Lesson.query.filter((Lesson.name == name) | (Lesson.question == question) | (Lesson.date == date) | (Lesson.start_time == start_time) | (Lesson.end_time == end_time)).first()
        if existing_lesson is not None:
            return jsonify({'message': 'Error: Deze les bestaat al.'}) 

        lesson.name = name
        lesson.question = question
        lesson.date = date
        lesson.start_time = start_time
        lesson.end_time = end_time

        db.session.commit()

        return jsonify({'message': 'success'})

    @staticmethod
    def delete_lesson(id):
        lesson = Lesson.query.get(id)
        print(lesson)
        if not lesson:
            return jsonify({'message': 'Lesson not found'}), 404
        db.session.delete(lesson)
        db.session.commit()
        return '', 204


