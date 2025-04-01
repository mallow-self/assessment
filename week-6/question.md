## Question 1:

Take the MCQ test to check your understanding of MRO, DataTables, django-ajax-datatable, django-storages, Django Class based Views, Mixins and Decorators.

---

## Question 2:

You've been tasked with building a Blog web application using Django. Here's a breakdown of the requirements:

### Model Design:

Create a model with fields for Title, Content, Image, Created at, Updated at, and Category (with options: Python, Django, PowerBI, Scrapy). Design the model using suitable field classes.

### Functionalities:

**List Page:**

Create a data table for the list page that displays all blog items. The table should have columns for Title, Content, and Category. Additionally, include action buttons for marking as completed, editing, and deleting.

**Detail Page:**

The Detail Page should display the blog title at the top, followed by the blog's image, content, and Category at the bottom. Additionally, it should include a button to navigate back to the list of blogs.

**Create Form:**

The Blog creation form will be accessible from the List Page within a modal pop-up. After creation, reload the datatable asynchronously. If errors occur during the creation process, display relevant error messages and retain the user's input for correction.

**Edit Form:**

Create a modal form with pre-populated values for editing a blog. After updating, asynchronously reload the data table. If any errors occur during the update, show relevant error messages and keep the user’s input for correction.

**Delete Process:**

When the user clicks the delete button, display a confirmation dialog using SweetAlert2. If the user confirms, proceed with the deletion based on their selection. After deletion, reload the data table asynchronously.

### Note:

- Utilize Conda for package management and Poetry for dependency management.
- Implement this Blog application using Class-Based Views (CBVs).
- Integrate Bootstrap Template for simplified styling.
- Implement DataTables using django-ajax-datatable.
- The images can be uploaded to the local file directory.  <subject to change after confirming with Poovarasu bro regarding the usage of django-storages>

### Output:

Please create a new branch in your repository and commit your code to that branch. Ensure to update the branch name in the comments of your code for reference.

---