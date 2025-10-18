# stage-zero
HNG Stage Zero Project
# 🧑‍💻 My Profile API Endpoint (`/me/`)

## 📄 Project Overview

This repository contains the backend code for the **User Profile Service** that exposes a dedicated endpoint to view profile data.

The service is built using **Python**, the **Django** framework, and **Django REST Framework (DRF)**.

***

## 🚀 Local Installation & Setup

Follow these steps to get the project up and running on your local machine.

### Prerequisites

* Python 3.8+
* pip (Python package installer)
* Virtual environment (recommended)

### Dependencies
* Django>=5.0,<5.1
* djangorestframework~=3.14

### Installation Steps

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```

2.  **Create and Activate Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    # venv\Scripts\activate  # On Windows
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Database Migration:**
    ```bash
    python manage.py migrate
    ```

5.  **Run the Server:**
    ```bash
    python manage.py runserver
    ```

The API will now be running at `http://127.0.0.1:8000/`.

***
