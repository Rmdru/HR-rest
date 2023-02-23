export default class Student {
    constructor() {
        this.deleteFunction();
        this.getStudentInfo();
        this.removeStudentInfo();
        this.removeStudentInfo();
        this.filterStudent();
    }

    deleteFunction() {
        if (document.querySelector("#students") != null) {
            // select all elements with the id "btnDelete"
            const deleteBtns = document.querySelectorAll(".students #btnDelete")

            // loop through each delete button
            deleteBtns.forEach((item) => {
                // add click event listener to each delete button
                item.addEventListener('click', (i) => {
                    // retrieve the unique id of the row to be deleted
                    const rowId = item.getAttribute('data-id')

                    // make a DELETE request to the server to delete the specified student
                    axios.delete('/students/' + rowId).then((response) => {
                        // reload the page after the student is successfully deleted
                        location.reload();
                    }, (error) => {
                        console.log(error);
                    });
                })
            })
        }
    }

    getStudentInfo() {
        if (document.querySelector("#students") != null) {
            // Select all edit modal buttons
            const editModalBtns = document.querySelectorAll(".students #btnEdit");

            // Loop through each button
            editModalBtns.forEach((item) => {
                // Add click event listener to each button
                item.addEventListener("click", () => {
                    const rowId = item.getAttribute("data-id");
                    // Make a GET request to retrieve the data for the selected student
                    axios.get("/students/" + rowId).then((response) => {
                        const student = response.data.student;
                        // check if the data is present in the response
                        if (student) {
                            // Get the modal element
                            const modal = document.getElementById("studentModal");

                            // Update the form action to include the ID
                            document.querySelector("#studentForm").action = `/students/${rowId}`;

                            // Get the form input elements
                            const nameInput = modal.querySelector("#inputName");
                            const emailInput = modal.querySelector("#inputEmail");
                            const studentNumberInput = modal.querySelector("#inputStudentNumber");

                            // Set the value of the input elements to the values from the response data
                            nameInput.value = student.name;
                            emailInput.value = student.email;
                            studentNumberInput.value = student.student_number;
                        } else {
                            console.error("No data found in the response");
                        }
                    });
                });
            });
        }
    }

    removeStudentInfo() {
        if (document.querySelector("#students") != null) {
            const creatBtn = document.querySelector('.students #btnCreate')

            if (creatBtn != null) {
                creatBtn.addEventListener('click', () => {
                    console.log('terst')
                    // Get the modal element
                    const modal = document.getElementById("studentModal");

                    // Get the form input elements
                    const nameInput = modal.querySelector("#inputName");
                    const emailInput = modal.querySelector("#inputEmail");
                    const studentNumberInput = modal.querySelector("#inputStudentNumber");

                    // Set the value of the input elements to the values from the response data
                    nameInput.value = '';
                    emailInput.value = '';
                    studentNumberInput.value = '';
                })
            }
        }
    }

    //Filter for students
    filterStudent() {
        if (document.querySelector("#students") != null) {
            const filterInput = document.querySelector("#filterAccordion input");

            var filterStudent = function () {
                //get filter input
                var input = document.getElementById("filterName").value;
                
                if (input == "") {
                    input = null;
                }

                //send request with axios
                axios.get("/students/filter/" + input).then((response) => {
                    const results = response.data;
                    // check if the data is present in the response
                    if (results) {
                        // Get the element
                        let el = document.querySelector(".table tbody");

                        //Create empty output var
                        let output = "";

                        //Show results in table
                        for (let i in results) {
                            output += "<tr>";
                                let id = results[i].id;
                                let name = results[i].name;
                                let email = results[i].email;
                                let studentNumber = results[i].student_number;

                                output += `<td>${name}</td>`;
                                output += `<td>${email}</td>`;
                                output += `<td>${studentNumber}</td>`;
                                output += `<td><a href="#" class="red" data-id="${id}" id="btnDelete">Verwijderen</a></td>`;
                                output += `<td><a href="#" class="blue" data-id="${id}" id="btnEdit" data-toggle="modal" data-target="#studentModal">Wijzigen</a></td>`;
                                output += `<td><a href="/students/${studentNumber}/aanwezigheid" class="blue">Aanwezigheid</a></td>`;
                            output += "</tr>";
                        }

                        el.innerHTML = output;
                    } else {
                        console.error("No data found in the response");
                    }
                });
            }

            //Event listeners
            if (filterInput != null) {
                filterInput.addEventListener('keyup', filterStudent, false);
                filterInput.addEventListener('change', filterStudent, false);
            }
        }
    }
}

