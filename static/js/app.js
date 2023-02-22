import Lesson from "./lesson.js";
import Student from "./student.js";
import Class_ from "./class.js";
import Teacher from "./teacher.js";
import Attendance from "./attendance.js";

document.addEventListener("DOMContentLoaded", () => {
    new Lesson();
    new Attendance();
  new Student();
  new Class_();
  new Teacher();