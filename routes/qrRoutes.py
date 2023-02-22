from __main__ import Flask, send_file, render_template, request, app
from flask_qrcode import QRcode
from models.lessonModel import Lesson
from controllers.attendanceController import AttendanceController

qrcode = QRcode(app)


def setup_qr_routes(app):
    @app.route("/check-in/<id>")
    def checkIn(id):
        return render_template("/checkin/qrcode.html", id=id)

    @app.route("/check-in/form/<id>")
    def checkInForm(id):
        lesson = Lesson.query.filter_by(id=id).first()
        if not lesson:
            return "Lesson not found"
        return render_template("/checkin/form.html", id=id, lesson=lesson)

    @app.route("/checkin-in/", methods=['POST'])
    def create_attendance():
        return AttendanceController.create_attendance()

    @app.route("/checkin-in/delete/<id>", methods=['POST'])
    def delete_attendance(id):
        print(id)
        return AttendanceController.delete_attendance(id)
