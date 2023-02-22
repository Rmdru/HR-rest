from __main__ import Flask, send_file, render_template, request, app, SocketIO, emit
from flask_qrcode import QRcode
import datetime
from models.lessonModel import Lesson
from models.attendanceModel import Attendance
from controllers.attendanceController import AttendanceController

qrcode = QRcode(app)


def setup_qr_routes(app):
    @app.route("/check-in/<id>")
    def checkIn(id):
        return render_template("lessons/checkin/qrcode.html", id=id)

    @app.route("/check-in/form/<id>")
    def checkInForm(id):
        lesson = Lesson.query.filter_by(id=id).first()
        if not lesson:
            return "Lesson not found"
        return render_template("lessons/checkin/form.html", id=id, lesson=lesson)

    @app.route("/checkin-in/", methods=['POST'])
    def create_attendance():
        return AttendanceController.create_attendance()

    @app.route("/attendances/<id>", methods=['DELETE'])
    def delete_attendance(id):
        return AttendanceController.delete_attendance(id)

    @app.route('/lesson/<id>/aanwezigheid', methods=['GET'])
    def attendance_lesson(id):
        # Start Flask-SocketIO only when this route is accessed
        socketio = SocketIO(app)

        @socketio.on('check-in')
        def handle_attendance(data):
            uuid = data['uuid']
            student_id = data['student_id']
            checkin_time = datetime.datetime.now().strftime('%H:%M:%S')
            question_answer = data['question_answer']
            mood = data['mood']
            emit('attendance', {'student_id': student_id,
                                'checkin_time': checkin_time,
                                'question_answer': question_answer,
                                'mood': mood,
                                'uuid': uuid}, broadcast=True)

        attendances = Attendance.query.filter(Attendance.lesson_id == id).all()
        attendance_dicts = [attendance.to_dict() for attendance in attendances]

        print(f"Rendering template for lesson id: {id}")
        return render_template("/lessons/attendance/index.html", id=id, attendances=attendance_dicts)
