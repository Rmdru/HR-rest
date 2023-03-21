export default class Class_ {
    constructor() {
        this.deleteFunction();
        this.getClassInfo();
        this.removeClassInfo()
        this.removeClassInfo()
        this.createClass()
        this.updateClass()
    }

    deleteFunction() {
        if (document.querySelector("#classes") != null) {
            // select all elements with the id "btnDelete"
            const deleteBtns = document.querySelectorAll("#btnDelete")

            // loop through each delete button
            deleteBtns.forEach((item) => {
                // add click event listener to each delete button
                item.addEventListener('click', (i) => {
                    // retrieve the unique id of the row to be deleted
                    const rowId = item.getAttribute('data-id')

                    // make a DELETE request to the server to delete the specified class
                    axios.delete('/classes/' + rowId).then((response) => {
                        // reload the page after the class is successfully deleted
                        location.reload();
                    }, (error) => {
                        console.log(error);
                    });
                })
            })
        }
    }

    getClassInfo() {
        if (document.querySelector("#classes") != null) {
            // Select all edit modal buttons
            const editModalBtns = document.querySelectorAll("#btnEdit");

            // Loop through each button
            editModalBtns.forEach((item) => {
                // Add click event listener to each button
                item.addEventListener("click", () => {
                    const rowId = item.getAttribute("data-id");
                    console.log(rowId)
                    // Make a GET request to retrieve the data for the selected class
                    axios.get("/classes/" + rowId).then((response) => {
                        const class_ = response.data.class;
                        // check if the data is present in the response
                        if (class_) {
                            // Get the modal element
                            const modal = document.getElementById("classModalUpdate");

                            // Update the form action to include the ID
                            document.querySelector("#classModalUpdate #classForm").action = `/classes/${rowId}`;

                            // Get the form input elements
                            const nameInput = modal.querySelector("#inputName");
                            const errorMessage = modal.querySelector(".error");

                            // Set the value of the input elements to the values from the response data
                            nameInput.value = class_.name;
                            dateInput.value = class_.date;
                            errorMessage.innerHTML = "";
                        } else {
                            console.error("No data found in the response");
                        }
                    });
                });
            });
        }
    }

    removeClassInfo() {
        if (document.querySelector("#classes") != null) {
            const creatBtn = document.querySelector('#btnCreate')

            if (creatBtn != null) {
                creatBtn.addEventListener('click', () => {
                    // Get the modal element
                    const modal = document.getElementById("classModal");

                    // Get the form input elements
                    const nameInput = modal.querySelector("#inputName");
                    const errorMessage = modal.querySelector(".error");

                    // Set the value of the input elements to the values from the response data
                    nameInput.value = '';
                    errorMessage.innerHTML = "";
                })
            }
        }
    }

    createClass() {
        if (document.getElementById("classModalCreate") != null) {
            const creatBtn = document.querySelector('#saveBtn');
            creatBtn.addEventListener('click', () => {
                // Get the modal element
                const modal = document.getElementById("classModalCreate");

                // Get the form input elements
                const nameInput = modal.querySelector("#inputName").value;

                let error = 0;

                if (nameInput == '') { 
                    error++;
                }

                if (error == 0) {
                    axios.post('/classes/', {
                        name: nameInput
                    })
                    .then((response) => {
                        const result = response.data;
                        if (result) {
                            if (result.message == 'Error: Deze klas bestaat al.') {
                                let output = '<div class="alert alert-danger" role="alert">Error: Deze klas bestaat al.</div>';
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

    updateClass() {
        if (document.getElementById("classModalUpdate") != null) {
            const creatBtn = document.querySelector('#classModalUpdate #saveBtn');
            creatBtn.addEventListener('click', () => {
                // Get the modal element
                const modal = document.getElementById("classModalUpdate");
               
                // Get the form element
                const classForm = document.querySelector("#classModalUpdate #classForm");

                // Get the ID from the form action attribute
                const rowId = classForm.getAttribute("action").split("/")[2];
   
                // Get the form input elements
                const nameInput = modal.querySelector("#inputName").value;
                
                let error = 0;

                if (nameInput == '') { 
                    error++;
                }

                if (error == 0) {
                    axios.post('/classes/' + rowId, {
                        name: nameInput
                    })
                    .then((response) => {
                        const result = response.data;
                        if (result) {
                            if (result.message == 'Error: Deze klas bestaat al.') {
                                let output = '<div class="alert alert-danger" role="alert">Error: Deze klas bestaat al.</div>';
                                document.querySelector('#classModalUpdate .error').innerHTML = output;
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

