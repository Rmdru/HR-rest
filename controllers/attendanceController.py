from __main__ import jsonify, db, request, render_template, redirect, url_for, uuid
from models.attendanceModel import Attendance


class AttendanceController():

    @staticmethod
    def create_attendance():
        status = request.form.get('status')
        mood = request.form.get('mood')
        question_answer = request.form.get('question_answer')
        lesson_id = request.form.get('lesson_id')
        student_id = request.form.get('student_id')

        # Check if there is already an attendance for the same student in the same lesson
        existing_attendance = Attendance.query.filter_by(student_id=student_id, lesson_id=lesson_id).first()
        if existing_attendance is not None:
            # Return a 404 error response
            return render_template('/lessons/attendance/failed.html')

        # Create a new attendance object and add it to the database
        new_attendance = Attendance(status=status, mood=mood, question_answer=question_answer, lesson_id=lesson_id,
                                    student_id=student_id)

        db.session.add(new_attendance)
        db.session.commit()

        return render_template('/lessons/attendance/succes.html')

    @staticmethod
    def delete_attendance(student_number):
        attendance = Attendance.query.filter_by(student_id=student_number).first()
        if not attendance:
            return jsonify({'message': 'Attendance not found'}), 404
        db.session.delete(attendance)
        db.session.commit()
        return '', 204