
# Secure-A-Key: Security basics for End users 

This web application serves as an educational tool for teaching end users about the importance of secure online practices and how to avoid falling for common scams. Through interactive games and simulations, users can learn about creating strong passwords, the benefits of two-factor authentication, and identifying phishing emails.

## Features

- **Password Builder:** Allows users to create passwords and receive immediate feedback on their strength based on criteria such as length, inclusion of uppercase letters, numbers, and special characters.
- **Password Test:** Users can see how long it might take to crack their passwords based on their strength.
- **Two-Factor Authentication Simulator:** Demonstrates how two-factor authentication (2FA) adds an extra layer of security beyond just a password.
- **Phishing Mini Game:** Educates users on recognizing phishing attempts through simulated email analysis.

## Getting Started

These instructions will help you get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3
- Flask

### Installing

1. Clone the repository or download the project to your local machine.
2. Navigate to the project directory in a terminal.
3. Install the required Python packages:

for windows
```bash
python -m vevn .venv

pip install -r requirements.txt

.venv\Scripts\Activate.ps1
```
for linux
```bash
python -m venv .venv

pip install -r requirementx.txt

source .venv/bin/activate
```
4. Start the Flask server:

```bash
flask run
```

This will start a development server on `localhost:5000`.

### Usage

After launching the Flask application, navigate to `http://localhost:5000/` in your web browser. You will be greeted with the home page, from which you can access the various features of the application:

- To build and test passwords, use the **Password Builder** and **Password Test** features.
- To experience and understand two-factor authentication, proceed to the **Two-Factor Authentication Simulator**.
- To learn about identifying phishing emails, try out the **Phishing Mini Game**.

## License

This project is licensed under the MIT License - see the [LICENSE.md](#) file for details.
