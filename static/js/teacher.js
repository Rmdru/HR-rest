export default class Teacher {
    teacher;
    constructor() {
        this.deleteFunction();
        this.getTeacherInfo();
        this.removeTeacherInfo()
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

                // make a DELETE request to the server to delete the specified teacher
                axios.delete('/teachers/' + rowId).then((response) => {
                    // reload the page after the teacher is successfully deleted
                    location.reload();
                }, (error) => {
                    console.log(error);
                });
            })
        })

    }

    getTeacherInfo() {
        // Select all edit modal buttons
        const editModalBtns = document.querySelectorAll("#btnEdit");

        // Loop through each button
        editModalBtns.forEach((item) => {
            // Add click event listener to each button
            item.addEventListener("click", () => {
                const rowId = item.getAttribute("data-id");
                console.log(rowId)
                // Make a GET request to retrieve the data for the selected teacher
                axios.get("/teachers/" + rowId).then((response) => {
                    const teacher = response.data.teacher;
                    // check if the data is present in the response
                    if (teacher) {
                        // Get the modal element
                        const modal = document.getElementById("teacherModal");

                        // Update the form action to include the ID
                        document.querySelector("#teacherForm").action = `/teachers/${rowId}`;

                        // Get the form input elements
                        const nameInput = modal.querySelector("#inputName");
                        const emailInput = modal.querySelector("#inputEmail");
                        const classInput = modal.querySelector("#inputDate");

                        // Set the value of the input elements to the values from the response data
                        nameInput.value = teacher.name;
                        emailInput.value = teacher.email;
                        classInput.value = teacher.class;
                    } else {
                        console.error("No data found in the response");
                    }
                });
            });
        });
    }

    removeTeacherInfo() {
        const creatBtn = document.querySelector('#btnCreate')

        if (creatBtn != null) {
            creatBtn.addEventListener('click', () => {
                console.log('terst')
                // Get the modal element
                const modal = document.getElementById("teacherModal");

                // Get the form input elements
                const nameInput = modal.querySelector("#inputName");
                const emailInput = modal.querySelector("#inputEmail");
                const classInput = modal.querySelector("#inputClass");


                // Set the value of the input elements to the values from the response data
                nameInput.value = '';
                emailInput.value = '';
                classInput.value = '';
            })
        }
    }
}

