export default class Teacher {
    teacher;
    constructor() {
        this.deleteFunction();
        this.getTeacherInfo();
        this.removeTeacherInfo();
        this.filterTeacher();
    }

    deleteFunction() {
        if (document.querySelector("#teachers") != null) {
            // select all elements with the id "btnDelete"
            const deleteBtns = document.querySelectorAll("#btnDelete")

            // loop through each delete button
            deleteBtns.forEach((item) => {
                // add click event listener to each delete button
                item.addEventListener('click', (i) => {
                    // retrieve the unique id of the row to be deleted
                    const rowId = item.getAttribute('data-id')

                    // make a DELETE request to the server to delete the specified teacher
                    axios.delete('/teacher/' + rowId).then((response) => {
                        // reload the page after the teacher is successfully deleted
                        location.reload();
                    }, (error) => {
                        console.log(error);
                    });
                })
            })
        }
    }

    getTeacherInfo() {
        if (document.querySelector("#teachers") != null) {
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
                            // const classInput = modal.querySelector("#inputClass");

                            // Set the value of the input elements to the values from the response data
                            nameInput.value = teacher.name;
                            emailInput.value = teacher.email;
                            // classInput.value = teacher.class;
                        } else {
                            console.error("No data found in the response");
                        }
                    });
                });
            });
        }
    }

    removeTeacherInfo() {
        if (document.querySelector("#teachers") != null) {
            const creatBtn = document.querySelector('#btnCreate');

            if (creatBtn != null) {
                creatBtn.addEventListener('click', () => {
                    console.log('terst')
                    // Get the modal element
                    const modal = document.getElementById("teacherModal");

                    // Get the form input elements
                    const nameInput = modal.querySelector("#inputName");
                    const emailInput = modal.querySelector("#inputEmail");
                    // const classInput = modal.querySelector("#inputClass");


                    // Set the value of the input elements to the values from the response data
                    nameInput.value = '';
                    emailInput.value = '';
                    // classInput.value = '';
                })
            }
        }
    }

    //Filter for teachers
    filterTeacher() {
        if (document.querySelector("#teachers") != null) {
            const filterInput = document.querySelector("#filterAccordion input");

            var filterTeacher = function () {
                //get filter input
                var input = document.getElementById("filterName").value;
                
                if (input == "") {
                    input = null;
                }

                //send request with axios
                axios.get("/teacher/filter/" + input).then((response) => {
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

                                output += `<td>${name}</td>`;
                                output += `<td>${email}</td>`;
                                output += `<td><a href="#" class="red" data-id="${id}" id="btnDelete">Verwijderen</a></td>`;
                                output += `<td><a href="#" class="blue" data-id="${id}" id="btnEdit" data-toggle="modal" data-target="#studentModal">Wijzigen</a></td>`;
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
                filterInput.addEventListener('keyup', filterTeacher, false);
                filterInput.addEventListener('change', filterTeacher, false);
            }
        }
    }
}