export default class Lesson {
    constructor() {
        this.deleteFunction();
        this.getLessonInfo();
        this.removeLessonInfo()
        this.initializeDatePicker();
        this.removeLessonInfo()
    }

    deleteFunction() {
        // select all elements with the id "btnDelete"
        const deleteBtns = document.querySelectorAll("#btnDelete")

        // loop through each delete button
        deleteBtns.forEach((item) => {
            // add click event listener to each delete button
            item.addEventListener('click', (i) => {
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

    getLessonInfo() {
        // Select all edit modal buttons
        const editModalBtns = document.querySelectorAll("#btnEdit");

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
                        const dateInput = modal.querySelector("#inputDate");
                        const startTimeInput = modal.querySelector("#inputStartTime");
                        const endTimeInput = modal.querySelector("#inputEndTime");

                        // Set the value of the input elements to the values from the response data
                        nameInput.value = lesson.name;
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

    removeLessonInfo() {
        const creatBtn = document.querySelector('#btnCreate')

        if (creatBtn != null) {
            creatBtn.addEventListener('click', () => {
                console.log('terst')
                // Get the modal element
                const modal = document.getElementById("lessonModal");

                // Get the form input elements
                const nameInput = modal.querySelector("#inputName");
                const dateInput = modal.querySelector("#inputDate");
                const startTimeInput = modal.querySelector("#inputStartTime");
                const endTimeInput = modal.querySelector("#inputEndTime");

                // Set the value of the input elements to the values from the response data
                nameInput.value = '';
                dateInput.value = '';
                startTimeInput.value = startTimeInput.options[0].value;
                endTimeInput.value = endTimeInput.options[0].value;
            })
        }
    }

    initializeDatePicker() {
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

