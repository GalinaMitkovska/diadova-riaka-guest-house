# Дядова ряка — Guest House

## About the Project

**Diadova Ryaka Guest House** is a Django web application for managing a guest house. The project provides information about the guest house, available rooms, additional services, bookings, and guest reviews.

The application is developed with Python and Django.

## Features

- Display information about the guest house.
- View available rooms and room types.
- View additional services.
- Create a booking.
- Cancel a booking according to the cancellation policy.
- Submit a review.

## Technologies

- Python
- Django
- SQLite
- HTML
- CSS

## Project Structure

- `core` — main pages and general information.
- `rooms` — room information and room types.
- `services` — additional services.
- `bookings` — bookings and related functionality.

## Installation and Setup

1. Clone the repository:

   ```bash
   git clone YOUR_GITHUB_REPOSITORY_URL
   ```

2. Navigate to the project directory:

   ```bash
   cd Diadova_riaka_guest_house
   ```

3. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment on Windows:

   ```bash
   venv\Scripts\activate
   ```

5. Install Django:

   ```bash
   pip install django
   ```

6. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

7. Start the development server:

   ```bash
   python manage.py runserver
   ```

8. Open the following address in your browser:

   `http://127.0.0.1:8000/`

## Author

Developed as a Django learning project.
