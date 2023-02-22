export default class Class_ {
    constructor() {
        this.deleteFunction();
        this.getClassInfo();
        this.removeClassInfo()
        this.removeClassInfo()
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

    getClassInfo() {
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
                        const modal = document.getElementById("classModal");

                        // Update the form action to include the ID
                        document.querySelector("#classForm").action = `/classes/${rowId}`;

                        // Get the form input elements
                        const nameInput = modal.querySelector("#inputName");

                        // Set the value of the input elements to the values from the response data
                        nameInput.value = class_.name;
                        dateInput.value = class_.date;
                    } else {
                        console.error("No data found in the response");
                    }
                });
            });
        });
    }

    removeClassInfo() {
        const creatBtn = document.querySelector('#btnCreate')

        if (creatBtn != null) {
            creatBtn.addEventListener('click', () => {
                console.log('terst')
                // Get the modal element
                const modal = document.getElementById("classModal");

                // Get the form input elements
                const nameInput = modal.querySelector("#inputName");

                // Set the value of the input elements to the values from the response data
                nameInput.value = '';
            })
        }
    }
}
