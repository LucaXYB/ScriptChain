# Django Interview Project

This repository contains the Django project for the interview, where we answer several questions related to Django ORM and performance optimization techniques.

## Project Structure

- **question1/**: Contains the implementation and explanation for the first interview question.

## Question 1: What is the difference between `select_related` and `prefetch_related`?

### Explanation

In Django ORM, both `select_related` and `prefetch_related` are used to optimize database queries by reducing the number of queries required to retrieve related objects. However, they operate in different ways and are suitable for different use cases:

- **`select_related`**: Performs a SQL JOIN and includes the fields of the related object in the SELECT statement. This method is suitable for one-to-one and many-to-one relationships.
- **`prefetch_related`**: Performs a separate lookup for each relationship and does the joining in Python. This method is suitable for one-to-many and many-to-many relationships.

### Implementation

In this project, we have implemented views to demonstrate the performance differences between `select_related` and `prefetch_related`. The results are displayed on a comparison page.

### Prerequisites

- **Python Version**: Ensure you have Python 3.x installed on your system. You can check your Python version with:

  ```bash
  python --version
  ```

1. **Clone the Repository**:
   - Open your terminal.
   - Run the following command to clone the repository to your local machine:

     ```bash
     git clone https://github.com/LucaXYB/ScriptChain_interview.git
     ```

   - Navigate to the project directory:

     ```bash
     cd ScriptChain_interview/django_project
     ```

2. **Set Up the Virtual Environment**:
   - Ensure you are in the project directory, then create a virtual environment:

     ```bash
     python3 -m venv myvenv
     ```

   - Activate the virtual environment:

     ```bash
     source myvenv/bin/activate  # On Windows use: myvenv\Scripts\activate
     ```

3. **Install Dependencies**:
   - Install all required dependencies from the `requirements.txt` file:

     ```bash
     pip install -r requirements.txt
     ```

4. **Run Migrations to Set Up the Database**:
   - Apply migrations to set up the database schema:

     ```bash
     python manage.py migrate
     ```

5. **Populate the Database with Test Data**:
   - Run the custom management command to populate the database with test data:

     ```bash
     python manage.py populate_test_data
     ```

6. **Start the Django Development Server**:
   - Run the following command to start the server:

     ```bash
     python manage.py runserver
     ```

   - The development server should now be running at `http://127.0.0.1:8000/`.

7. **View the Results**:
   - Access the following pages to see the results of the `select_related` and `prefetch_related` queries:
     - **`select_related` View**: [http://127.0.0.1:8000/question1/orders/](http://127.0.0.1:8000/question1/orders/)
     - **`prefetch_related` View**: [http://127.0.0.1:8000/question1/users/](http://127.0.0.1:8000/question1/users/)
     - **Comparison Page**: [http://127.0.0.1:8000/question1/compare/](http://127.0.0.1:8000/question1/compare/)

### Explore the Code

1. **Question 1 Code**:
   - The core logic for `question1` is located in the `question1/views.py` file.
   - The comparison results and details are displayed in `question1/templates/question1/compare_methods.html`.

2. **Models**:
   - The models for the `question1` app are located in `question1/models.py`.

### Conclusion

The comparison demonstrates that `select_related` is generally more efficient for simple relationships where a JOIN can be performed, while `prefetch_related` is better for complex relationships where multiple queries are necessary to avoid performance bottlenecks in SQL.

## Upcoming Questions

- **Question 2**: Explain Q objects in Django ORM and illustrate an example via code.
- **Question 3**: How would you set up your app using Django on AWS EC2 while also keeping your cost to a minimum?

Stay tuned for the implementations of these questions in their respective directories.
