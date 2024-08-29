# Django Interview Project

This repository contains the Django project for the interview, where we answer several questions related to Django ORM and performance optimization techniques.

## Project Structure

- **question1/**: Contains the implementation and explanation for the first interview question.
- **question2/**: Contains the implementation and explanation for the second interview question.
- **question3/**: Contains the implementation and explanation for the third interview question. 

## Question 1: What is the difference between `select_related` and `prefetch_related`?

### Explanation

In Django ORM, both `select_related` and `prefetch_related` are used to optimize database queries by reducing the number of queries required to retrieve related objects. However, they operate in different ways and are suitable for different use cases:

- **`select_related`**: Performs a SQL JOIN and includes the fields of the related object in the SELECT statement. This method is suitable for one-to-one and many-to-one relationships.
- **`prefetch_related`**: Performs a separate lookup for each relationship and does the joining in Python. This method is suitable for one-to-many and many-to-many relationships.

### Implementation

In this project, we have implemented views to demonstrate the performance differences between `select_related` and `prefetch_related`. The results are displayed on a comparison page.

### How to Run

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

## Question 2: Explain Q objects in Django ORM and illustrate an example via code.

### Explanation

`Q` objects in Django ORM are used to encapsulate a collection of keyword arguments, allowing for complex queries with multiple conditions. They enable logical operators like `AND`, `OR`, and `NOT` within queries and can combine multiple conditions to create dynamic queries.

### Implementation

In this project, we have implemented various types of queries using `Q` objects, including `OR` queries, `AND` queries, `NOT` queries, combining multiple `Q` objects, and nested queries. The results of these queries are displayed on a web page, alongside a table that explains the definition, advantages, and disadvantages of `Q` objects.

### How to Run

1. **Clone the Repository**:
   - If you haven't already cloned the repository, follow the steps outlined in Question 1.

2. **Set Up the Virtual Environment and Install Dependencies**:
   - Ensure you have activated the virtual environment and installed the dependencies as mentioned in Question 1.

3. **Run Migrations to Set Up the Database**:
   - Apply migrations to set up the database schema for `question2`:

     ```bash
     python manage.py makemigrations question2
     python manage.py migrate
     ```

4. **Start the Django Development Server**:
   - Start the server:

     ```bash
     python manage.py runserver
     ```

5. **View the Results**:
   - Access the following page to see the results of the `Q` object queries:
     - **Q Object Queries View**: [http://127.0.0.1:8000/question2/q-object-queries/](http://127.0.0.1:8000/question2/q-object-queries/)

### Explore the Code

1. **Question 2 Code**:
   - The core logic for `question2` is located in the `question2/views.py` file.
   - The various `Q` object query results and details are displayed in `question2/templates/question2/q_object_queries.html`.

2. **Models**:
   - The models for the `question2` app are located in `question2/models.py`.


## Question 3: Django Project deployment on AWS EC2.

### Explanation

In this task, you will deploy a Django application on an AWS EC2 instance, utilizing the free tier to minimize costs. The deployment involves several steps, including setting up the EC2 instance, installing necessary dependencies, configuring Gunicorn as the application server, and using Nginx as the reverse proxy. This setup ensures that your Django application can handle incoming requests efficiently and securely.

### Implementation

### Part 1: Setting Up AWS EC2 Instance and Remote Connection

#### Step 1: Create an AWS EC2 Instance (Free Tier)

1. **Sign in to AWS Management Console**:
   - Go to the [AWS Management Console](https://aws.amazon.com/console/) and log in with your credentials.

2. **Navigate to EC2 Dashboard**:
   - In the AWS Management Console, search for "EC2" in the services search bar and select "EC2" to open the EC2 Dashboard.

3. **Launch a New Instance**:
   - Click on the "Launch Instance" button on the EC2 Dashboard to start creating a new EC2 instance.

4. **Choose Amazon Machine Image (AMI)**:
   - Under "Choose an Amazon Machine Image (AMI)", select the "Amazon Linux 2 AMI (HVM), SSD Volume Type" (which is free tier eligible).

5. **Select Instance Type**:
   - In the "Choose an Instance Type" section, select the `t2.micro` instance type, which is also free tier eligible. Click "Next: Configure Instance Details".

6. **Configure Instance Details**:
   - Leave the default settings and click "Next: Add Storage".

7. **Add Storage**:
   - The default storage configuration is typically sufficient. Click "Next: Add Tags".

8. **Add Tags**:
   - You can optionally add tags to help identify your instance. For example, you can add a tag with `Key` as `Name` and `Value` as `MyDjangoAppInstance`. Click "Next: Configure Security Group".

9. **Configure Security Group**:
   - **SSH**: By default, SSH (port 22) will be enabled. This allows you to connect to your instance remotely.
   - **HTTP**: Add a new rule to allow HTTP (port 80) traffic, which is necessary to serve your Django application.
   - **HTTPS (optional)**: If you plan to use HTTPS, you should also allow HTTPS (port 443).
   - Ensure the source is set to `0.0.0.0/0` to allow access from anywhere, or limit it to your IP address for added security.
   - Click "Review and Launch".

10. **Review and Launch**:
    - Review your settings, then click "Launch".
    - When prompted, create a new key pair or select an existing one. This key pair will be used to connect to your instance via SSH.
    - Download the `.pem` file and store it securely. You will need this to connect to your instance.

11. **Launch Instance**:
    - Click "Launch Instances". Your EC2 instance will start launching.

12. **View Instance**:
    - Click "View Instances" to go back to the EC2 Dashboard, where you can see your new instance starting up. Wait until the instance's "Instance State" changes to "running".

#### Step 2: Connect to Your EC2 Instance from Local Machine

1. **Move the `.pem` File to the `.ssh` Directory**:
   - Move the `.pem` file you downloaded to your local machine's `.ssh` directory for better security practices:
   
   ```bash
   mv ~/Downloads/your-key-pair.pem ~/.ssh/
   ```

2. **Set the Permissions for the Key Pair**: 
   - Set the correct permissions for the .pem file to make it secure   
   
   ```bash
   chmod 400 ~/.ssh/your-key-pair.pem
   ```

3. **Connect to the EC2 Instance**: 
   - Use the following SSH command to connect to your EC2 instance, replacing your-key-pair.pem with your key pair's name and ec2-user@your-ec2-public-ip with the public IP address of your instance:

   ```bash
   ssh -i ~/.ssh/your-key-pair.pem ec2-user@your-ec2-public-ip
   ```

4. **Verify the Connection**: 
   - Once connected, you should see a terminal prompt that indicates you're logged into the EC2 instance. You can now run commands on your remote instance.


### Part 2: Deploying the Django Project from GitHub to EC2 Instance

#### Step 1: Install Necessary Dependencies on the EC2 Instance

1. **Update the package list**:
   - After connecting to your EC2 instance, run the following command to update the package list:
   ```bash
   sudo yum update -y
   ```

2. **Install Git, Python, and pip**:
   - Install Git to clone your repository and install Python 3 and pip (Python's package installer):
   ```bash
   sudo yum install git -y
   sudo yum install python3 -y
   sudo yum install python3-pip -y
   ```
3. **Install virtualenv**:
   - Install virtualenv to create an isolated environment for your project:
   ```bash
   sudo pip3 install virtualenv
   ```

#### Step 2: Clone the Django Project from GitHub

1. **Navigate to the home directory**:
   - Ensure you're in the home directory of the EC2 instance:
   ```bash
   cd ~
   ```

2. **Clone the repository**:
   - Clone your GitHub repository to the EC2 instance using the following command:
   ```bash
   git clone https://github.com/LucaXYB/ScriptChain_interview.git
   ```

3. **Navigate to the project directory**:
   - After cloning, navigate to the Django project directory:
   ```bash
   cd ScriptChain_interview/django_project
   ```

#### Step 3: Set Up the Virtual Environment and Install Dependencies

1. **Create a virtual environment**:
   - Create a virtual environment within the project directory:
   ```bash
   python3 -m venv myvenv
   ```

2. **Activate the virtual environment**:
   - Activate the virtual environment:
   ```bash
   source myvenv/bin/activate
   ```

3. **Install project dependencies**:
   - Install the necessary dependencies from the requirements.txt file:
   ```bash
   pip install -r requirements.txt
   ```

#### Step4: Configure Gunicorn

1. **Create and edit the Gunicorn service file**:
   - Create a new systemd service file for Gunicorn:
   ```bash
   sudo nano /etc/systemd/system/gunicorn.service
   ```

2. **Add the following content to the service file**:
   - Ensure the paths are correct according to your project structure:
   ```bash
   [Unit]
   Description=gunicorn daemon for Django Project
   After=network.target

   [Service]
   User=ec2-user
   Group=nginx
   WorkingDirectory=/home/ec2-user/ScriptChain_interview/django_project
   ExecStart=/home/ec2-user/ScriptChain_interview/django_project/myvenv/bin/gunicorn --workers 3 --bind unix:/home/ec2-user/ScriptChain_interview/django_project/gunicorn.sock django_project.wsgi:application

   [Install]
   WantedBy=multi-user.target
   ```

3. **Save and exit**:
   - Save the file (Ctrl + O), then exit (Ctrl + X).

4. **Start and enable Gunicorn**:
   - Reload systemd to apply the changes, then start and enable Gunicorn:
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl start gunicorn
   sudo systemctl enable gunicorn
   ```

5. **Check Gunicorn status**:
   - Ensure Gunicorn is running:
   ```bash
   sudo systemctl status gunicorn
   ```
   - Confirm that the service is active and running.

#### Step 5: Configure Nginx

1. **Install Nginx**:
   - Install Nginx if it’s not already installed:
   ```bash
   sudo yum install nginx -y
   ```

2. **Create and edit the Nginx configuration file**:
   - Create a new Nginx configuration file for your Django project:
   ```bash
   sudo nano /etc/nginx/conf.d/django_project.conf
   ```

3. **Add the following content to the configuration file**:
   - Ensure the proxy_pass path matches the Gunicorn socket file location:
   ```bash
   server {
      listen 80;
      server_name your-ec2-public-ip;

      location / {
         proxy_pass http://unix:/home/ec2-user/ScriptChain_interview/django_project/gunicorn.sock;
         proxy_set_header Host $host;
         proxy_set_header X-Real-IP $remote_addr;
         proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
         proxy_set_header X-Forwarded-Proto $scheme;
      }

      location /static/ {
         alias /home/ec2-user/ScriptChain_interview/django_project/static/;
      }

      location /media/ {
         alias /home/ec2-user/ScriptChain_interview/django_project/media/;
      }
   }
   ```

4. **Save and exit**:
   - Save the file (Ctrl + O), then exit (Ctrl + X).

5. **Test the Nginx configuration**:
   - Ensure there are no syntax errors in the configuration:
   ```bash
   sudo nginx -t
   ```

6. **Start and enable Nginx**:
   - Start Nginx and enable it to start on boot:
   ```bash
   sudo systemctl start nginx
   sudo systemctl enable nginx
   ```

7. **Reload Nginx**:
   - Reload Nginx to apply the new configuration:
   ```bash
   sudo systemctl reload nginx
   ```

#### Step 6: Finalize and Test

1. **Open your browser**:
   - Visit your EC2 instance's public IP address in your browser:
   ```bash
   http://your-ec2-public-ip/
   ```
2. **Verify the Django application**:
   - You should see your Django application's homepage or whichever page you set as the default. This indicates that your project has been successfully deployed.
