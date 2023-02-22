from flask import render_template, jsonify
from controllers.lessonController import LessonController
from models.attendanceModel import Attendance


def setup_lesson_routes(app):
    # This route will redirect to the lessons index route
    @app.route("/lessen_overzicht")
    def lessons_index():
        lessons = LessonController.get_all_lessons()
        return render_template(
            "lessons/index.html", lessons=lessons
        )

    @app.route('/lessons/', methods=['POST'])
    def create_lesson():
        return LessonController.create_lesson()

    @app.route('/lessons/<id>', methods=['GET'])
    def show_lesson(id):
        return LessonController.show_lesson(id)

    @app.route('/lessons/<id>', methods=['POST'])
    def update_lesson(id):
        return LessonController.update_lesson(id)

    @app.route('/lessons/<id>', methods=['DELETE'])
    def delete_lesson(id):
        print(id)
        return LessonController.delete_lesson(id)

    @app.route('/lesson/<id>/aanwezigheid', methods=['GET'])
    def attendance_lesson(id):
        attendances = Attendance.query.filter(Attendance.lesson_id == id).all()
        attendance_dicts = [attendance.to_dict() for attendance in attendances]

        return render_template("/lessons/attendance/index.html", id=id, attendances=attendance_dicts)
