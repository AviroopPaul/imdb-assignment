# IMDb Assignment

## Overview

The IMDb Assignment is a Django-based web application that allows users to upload movie data via CSV files and view a list of movies with various filtering and sorting options. The application uses PostgreSQL as its database backend and leverages Django REST Framework for API functionalities.

## Features

- **CSV Upload:** Easily upload movie data through CSV files.
- **Movie Listing:** View a paginated list of movies with options to search, filter, and sort.
- **RESTful API:** Access movie data through a well-structured API.
- **Responsive Design:** User-friendly interface with basic styling.

## Prerequisites

Before setting up the project locally, ensure you have the following installed on your system:

- **Python 3.8 or higher:** [Download Python](https://www.python.org/downloads/)
- **PostgreSQL:** [Download PostgreSQL](https://www.postgresql.org/download/)
- **Git:** [Download Git](https://git-scm.com/downloads)

## Setup Instructions

Follow these steps to set up and run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/AviroopPaul/imdb_assignment.git
cd imdb_assignment
```

### 2. Create a Virtual Environment

It's recommended to use a virtual environment to manage project dependencies.

```bash
python3 -m venv venv
```

Activate the virtual environment:

- **On Windows:**

  ```bash
  venv\Scripts\activate
  ```

- **On macOS and Linux:**

  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies

Install the required Python packages using `pip`.

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

> **Note:** Ensure that a `requirements.txt` file exists in the project root. If not, create one with the necessary dependencies:

```bash
django==4.2.16
djangorestframework
django-filter
psycopg2-binary
pandas
numpy
```

### 4. Setup PostgreSQL Database

#### a. Install PostgreSQL

If PostgreSQL is not already installed, download and install it from the [official website](https://www.postgresql.org/download/).

#### b. Create a Database and User

1. **Access PostgreSQL Shell:**

   ```bash
   psql postgres
   ```

2. **Create a New Database:**

   ```sql
   CREATE DATABASE imdb_db;
   ```

3. **Create a New User:**

   ```sql
   CREATE USER imdb_user WITH PASSWORD 'your_password';
   ```

4. **Grant Privileges to the User:**

   ```sql
   GRANT ALL PRIVILEGES ON DATABASE imdb_db TO imdb_user;
   ```

5. **Exit the PostgreSQL Shell:**

   ```sql
   \q
   ```

#### c. Configure Environment Variables

The Django project uses environment variables to manage sensitive information like database credentials. You can set these variables in your shell or use a `.env` file with the help of `python-dotenv`.

1. **Install `python-dotenv`:**

   ```bash
   pip install python-dotenv
   ```

2. **Create a `.env` File in the Project Root:**

   ```bash
   touch .env
   ```

3. **Add the Following Lines to the `.env` File:**

   ```env
   DB_NAME=imdb_db
   DB_USER=imdb_user
   DB_PASSWORD=your_password
   ```

4. **Update `settings.py` to Load Environment Variables:**

   Ensure the `settings.py` file includes the following lines at the top:

   ```python
   from pathlib import Path
   import os
   from dotenv import load_dotenv

   load_dotenv()

   BASE_DIR = Path(__file__).resolve().parent.parent
   ```

### 5. Apply Migrations

Create the necessary database tables by running migrations.

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run the Development Server

Start the Django development server to run the application locally.

```bash
python manage.py runserver
```

Access the application by navigating to [http://localhost:8000](http://localhost:8000) in your web browser.

## Usage

### 1. Uploading Movies CSV

- Navigate to [http://localhost:8000/upload/](http://localhost:8000/upload/).
- Use the upload form to select and upload a CSV file containing movie data.
- Upon successful upload, a confirmation message will appear.

### 2. Viewing Movie List

- Navigate to [http://localhost:8000/movies/](http://localhost:8000/movies/).
- Browse through the list of movies with options to:
  - **Search:** Search movies by title or original title.
  - **Filter:** Filter movies by release date and original language.
  - **Sort:** Sort movies by release date, vote average, or budget in ascending or descending order.
  - **Pagination:** Navigate through different pages of movie listings.

## Project Structure

```
imdb_assignment/
├── imdb_assignment/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── imdb_app/
│   ├── migrations/
│   │   └── __init__.py
│   ├── static/
│   │   └── imdb_app/
│   │       ├── css/
│   │       │   └── styles.css
│   │       ├── js/
│   │       │   ├── movie_list.js
│   │       │   └── upload.js
│   ├── templates/
│   │   └── imdb_app/
│   │       ├── movie_list.html
│   │       └── upload.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   └── views.py
├── manage.py
├── requirements.txt
└── README.md
```

## API Endpoints

- **Upload CSV:** `POST /api/upload_csv/`
- **List Movies:** `GET /api/movies/`

### Example: Upload CSV

```bash
curl -X POST -F "file=@movies.csv" http://localhost:8000/api/upload_csv/
```

### Example: List Movies

```bash
curl http://localhost:8000/api/movies/
```

## Troubleshooting

- **Database Connection Issues:**
  - Ensure PostgreSQL is running.
  - Double-check the database credentials in the `.env` file.
  
- **Migrations Errors:**
  - Run `python manage.py makemigrations` and `python manage.py migrate` to apply migrations.
  
- **Static Files Not Loading:**
  - For development, ensure `DEBUG` is set to `True` in `settings.py`.
  - In production, ensure static files are correctly collected and served.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any questions or suggestions, feel free to contact [apavirooppaul10@gmail.com](mailto:apavirooppaul10@gmail.com).

# Quick Start Summary

1. **Clone Repository:**
   ```bash
   git clone https://github.com/AviroopPaul/imdb_assignment.git
   cd imdb_assignment
   ```
2. **Create and Activate Virtual Environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Setup PostgreSQL Database:**
   - Create database and user.
   - Update `.env` with `DB_NAME`, `DB_USER`, `DB_PASSWORD`.
5. **Apply Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
6. **Run Server:**
   ```bash
   python manage.py runserver
   ```
7. **Access Application:**
   - Upload Page: [http://localhost:8000/upload/](http://localhost:8000/upload/)
   - Movie List: [http://localhost:8000/movies/](http://localhost:8000/movies/)

# Acknowledgments

Thank you for using the IMDb Assignment project. Happy coding!

# License

This project is licensed under the MIT License.

# Contact

For any inquiries, please contact [apavirooppaul10@gmail.com](mailto:apavirooppaul10@gmail.com).

# Additional Notes

- Ensure environment variables are securely managed, especially in production environments.
- For production deployments, consider setting `DEBUG=False` and configuring allowed hosts and static files appropriately.

# Conclusion

This README should provide a comprehensive guide to setting up, configuring, and running the IMDb Assignment Django project locally. If you encounter any issues or have suggestions for improvements, feel free to reach out or contribute to the repository.