# werxs.ai Website

Werxs.ai website. Built in Python. Secured through Okta.

## Features

- **Secure Authentication with Okta:** Ensures secure access for both admin and future regular users by leveraging Okta's comprehensive authentication services.
- **Responsive Design with Bootstrap:** Delivers a seamless, mobile-friendly user experience across all devices, thanks to Bootstrap's responsive design capabilities.
- **Admin Dashboard:** Provides admin users with the tools needed to manage the platform effectively, including user permissions and content updates.
- **Data Upload Capability:** Allows users to securely upload training data bundles, which are then stored in AWS S3 for processing and analysis.

## Getting Started

This section will guide you through setting up the project locally on your machine.

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtualenv (optional but recommended for creating isolated Python environments)

### Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/werxs.ai/your-repo-name.git
    cd your-repo-name
    ```

2. **Set Up a Virtual Environment** (Optional)

    ```bash
    virtualenv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Environment Variables**

    Set up the necessary environment variables for Okta and AWS S3 integration. Refer to the `.env.example` file for the required variables.

5. **Run the Application**

    ```bash
    flask run
    ```

    Your application should now be running on `http://localhost:5000`.
