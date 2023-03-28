export default class Lesson {
    constructor() {
        this.deleteFunction();
        this.getLessonInfo();
        this.removeLessonInfo()
        this.initializeDatePicker();
        this.createLesson();
        this.updateLesson();
    }

    deleteFunction() {
        if (document.querySelector("#lessons") != null) {
            // select all elements with the id "btnDelete"
            const deleteBtns = document.querySelectorAll(".lessons #btnDelete")

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
    }

    getLessonInfo() {
        if (document.querySelector("#lessons") != null) {

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
                            const modal = document.getElementById("lessonModalUpdate");

                            // Update the form action to include the ID
                            document.querySelector("#lessonModalUpdate #lessonForm").action = `/lessons/${rowId}`;

                            // Get the form input elements
                            const nameInput = modal.querySelector("#inputName");
                            const questionTextarea = modal.querySelector("#textareaQuestion");
                            const dateInput = modal.querySelector("#inputDate");
                            const startTimeInput = modal.querySelector("#inputStartTime");
                            const endTimeInput = modal.querySelector("#inputEndTime");
                            const errorMessage = modal.querySelector(".error");

                            // Set the value of the input elements to the values from the response data
                            nameInput.value = lesson.name;
                            questionTextarea.value = lesson.question;
                            dateInput.value = lesson.date;
                            startTimeInput.value = lesson.start_time;
                            endTimeInput.value = lesson.end_time;
                            errorMessage.innerHTML = "";
                        } else {
                            console.error("No data found in the response");
                        }
                    });
                });
            });
        }
    }

    removeLessonInfo() {
        if (document.querySelector("#lessons") != null) {

            const creatBtn = document.querySelector('.lessons #btnCreate')

            if (creatBtn != null) {
                creatBtn.addEventListener('click', () => {
                    // Get the modal element
                    const modal = document.getElementById("lessonModalCreate");

                    // Get the form input elements
                    const nameInput = modal.querySelector("#inputName");
                    const questionTextarea = modal.querySelector("#textareaQuestion");
                    const dateInput = modal.querySelector("#inputDate");
                    const startTimeInput = modal.querySelector("#inputStartTime");
                    const endTimeInput = modal.querySelector("#inputEndTime");
                    const errorMessage = modal.querySelector(".error");

                    // Set the value of the input elements to the values from the response data
                    nameInput.value = '';
                    questionTextarea.value = '';
                    dateInput.value = '';
                    startTimeInput.value = startTimeInput.options[0].value;
                    endTimeInput.value = endTimeInput.options[0].value;
                    errorMessage.innerHTML = '';
                })
            }
        }
    }

    initializeDatePicker() {
        if (document.querySelector("#lessons") != null) {
            const dateInputs = document.querySelectorAll('.datepicker');

            if (dateInputs != null) {
                dateInputs.forEach((input) => {
                    const picker = new Pikaday({
                        field: input,
                        format: 'DD/MM/YYYY',
                        minDate: new Date()
                    });
                });
            }
        }
    }

    createLesson() {
        if (document.getElementById("lessonModalCreate") != null) {
            const creatBtn = document.querySelector('#saveBtn');
            creatBtn.addEventListener('click', () => {
                // Get the modal element
                const modal = document.getElementById("lessonModalCreate");

                // Get the form input elements
                const nameInput = modal.querySelector("#inputName").value;
                const questionTextarea = modal.querySelector("#textareaQuestion").value;
                const dateInput = modal.querySelector("#inputDate").value;
                const startTimeInput = modal.querySelector("#inputStartTime").value;
                const endTimeInput = modal.querySelector("#inputEndTime").value;

                let error = 0;

                if (nameInput == '') { 
                    error++;
                }

                if (error == 0) {
                    axios.post('/lessons/', {
                        name: nameInput,
                        question: questionTextarea,
                        date: dateInput,
                        start_time: startTimeInput,
                        end_time: endTimeInput
                    })
                    .then((response) => {
                        const result = response.data;
                        if (result) {
                            if (result.message == 'Error: Deze les bestaat al.') {
                                let output = '<div class="alert alert-danger" role="alert">Error: Deze les bestaat al.</div>';
                                document.querySelector('.error').innerHTML = output;
                            } else {
                                location.reload();
                            }
                        }
                    })
                } else {
                    let output = '<div class="alert alert-danger" role="alert">Error: Zorg dat je alle velden goed invult.</div>';
                    document.querySelector('.error').innerHTML = output;
                }
            })
        }
    }

    updateLesson() {
        if (document.getElementById("lessonModalUpdate") != null) {
            const creatBtn = document.querySelector('#lessonModalUpdate #saveBtn');
            creatBtn.addEventListener('click', () => {
                // Get the modal element
                const modal = document.getElementById("lessonModalUpdate");
               
                // Get the form element
                const lessonForm = document.querySelector("#lessonModalUpdate #lessonForm");

                // Get the ID from the form action attribute
                const rowId = lessonForm.getAttribute("action").split("/")[2];
   
                // Get the form input elements
                const nameInput = modal.querySelector("#inputName").value;
                const questionTextarea = modal.querySelector("#textareaQuestion").value;
                const dateInput = modal.querySelector("#inputDate").value;
                const startTimeInput = modal.querySelector("#inputStartTime").value;
                const endTimeInput = modal.querySelector("#inputEndTime").value;
                
                let error = 0;

                if (nameInput == '') { 
                    error++;
                }

                if (error == 0) {
                    axios.post('/lessons/' + rowId, {
                        name: nameInput
                    })
                    .then((response) => {
                        const result = response.data;
                        if (result) {
                            if (result.message == 'Error: Deze les bestaat al.') {
                                let output = '<div class="alert alert-danger" role="alert">Error: Deze les bestaat al.</div>';
                                document.querySelector('#lessonModalUpdate .error').innerHTML = output;
                            } else {
                                location.reload();
                            }
                        }
                    })
                } else {
                    let output = '<div class="alert alert-danger" role="alert">Error: Zorg dat je alle velden goed invult.</div>';
                    document.querySelector('.error').innerHTML = output;
                }
            })
        }
    }
}


