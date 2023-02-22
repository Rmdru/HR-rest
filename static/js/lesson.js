export default class Lesson {
    constructor() {
        this.deleteFunction();
        this.getLessonInfo();
        this.removeLessonInfo()
        this.initializeDatePicker();
    }

    deleteFunction() {

        if (document.querySelector(".lessons_index") != null) {
            // select all elements with the id "btnDelete"
            const deleteBtns = document.querySelectorAll(".lessons #btnDelete")

            // loop through each delete button
            deleteBtns.forEach((item) => {
                // add click event listener to each delete button
                item.addEventListener('click', (i) => {
                    console.log('testjoidjsfo')
                    // retrieve the unique id of the row to be deleted
                    const rowId = item.getAttribute('data-id')

                    // make a DELETE request to the server to delete the specified lesson
                    axios.delete('/lessons/' + rowId).then((response) => {
                        // reload the page after the lesson is successfully deleted
                        location.reload();
                    }, (error) => {
                        console.log(error);
                    });
                })
            })
        }
    }

    getLessonInfo() {
        if (document.querySelector(".lessons_index") != null) {

            // Select all edit modal buttons
            const editModalBtns = document.querySelectorAll(".lessons #btnEdit");

            // Loop through each button
            editModalBtns.forEach((item) => {
                // Add click event listener to each button
                item.addEventListener("click", () => {
                    const rowId = item.getAttribute("data-id");
                    console.log(rowId)
                    // Make a GET request to retrieve the data for the selected lesson
                    axios.get("/lessons/" + rowId).then((response) => {
                        const lesson = response.data.lesson;
                        // check if the data is present in the response
                        if (lesson) {
                            // Get the modal element
                            const modal = document.getElementById("lessonModal");

                            // Update the form action to include the ID
                            document.querySelector("#lessonForm").action = `/lessons/${rowId}`;

                            // Get the form input elements
                            const nameInput = modal.querySelector("#inputName");
                            const questionTextarea = modal.querySelector("#textareaQuestion");
                            const dateInput = modal.querySelector("#inputDate");
                            const startTimeInput = modal.querySelector("#inputStartTime");
                            const endTimeInput = modal.querySelector("#inputEndTime");

                            // Set the value of the input elements to the values from the response data
                            nameInput.value = lesson.name;
                            questionTextarea.value = lesson.question;
                            dateInput.value = lesson.date;
                            startTimeInput.value = lesson.start_time;
                            endTimeInput.value = lesson.end_time;
                        } else {
                            console.error("No data found in the response");
                        }
                    });
                });
            });
        }
    }

    removeLessonInfo() {
        if (document.querySelector(".lessons_index") != null) {

            const creatBtn = document.querySelector('.lessons #btnCreate')

            if (creatBtn != null) {
                creatBtn.addEventListener('click', () => {
                    // Get the modal element
                    const modal = document.getElementById("lessonModal");

                    // Get the form input elements
                    const nameInput = modal.querySelector("#inputName");
                    const questionTextarea = modal.querySelector("#textareaQuestion");
                    const dateInput = modal.querySelector("#inputDate");
                    const startTimeInput = modal.querySelector("#inputStartTime");
                    const endTimeInput = modal.querySelector("#inputEndTime");

                    // Set the value of the input elements to the values from the response data
                    nameInput.value = '';
                    questionTextarea.value = '';
                    dateInput.value = '';
                    startTimeInput.value = startTimeInput.options[0].value;
                    endTimeInput.value = endTimeInput.options[0].value;
                })
            }
        }
    }

    initializeDatePicker() {
        if (document.querySelector(".lessons_index") != null) {
            const dateInputs = document.querySelectorAll('.datepicker');

            if (dateInputs != null) {
                dateInputs.forEach((input) => {
                    const picker = new Pikaday({
                        field: input,
                        format: 'DD/MM/YYYY',
                        minDate: new Date(),
                        onSelect: function () {
                            console.log(input.value = this.toString());
                        }
                    });
                });
            }
        }
    }

}

