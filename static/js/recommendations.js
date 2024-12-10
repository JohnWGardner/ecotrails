const editButtons = document.getElementsByClassName("btn-edit");
const recommendationText = document.getElementById("id_description");
const recommendationForm = document.getElementById("recommendationForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated recommendation's ID upon click.
* - Fetches the content of the corresponding recommendation.
* - Populates the `recommendationText` input/textarea with the recommendation's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_recommendation/{recommendationId}` endpoint.
*/
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let recommendationId = e.target.getAttribute("recommendation_id");
    let recommendationContent = document.getElementById(`recommendation${recommendationId}`).innerText;
    recommendationText.value = recommendationContent;
    submitButton.innerText = "Update";
    recommendationForm.setAttribute("action", `edit_recommendation/${recommendationId}`);
  });
}

/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated recommendation's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific recommendation.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    let recommendationId = e.target.getAttribute("recommendation_id");
    deleteConfirm.href = `delete_recommendation/${recommendationId}`;
    deleteModal.show();
  });
}