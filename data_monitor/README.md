# AQUESA Data Monitor

## Overview
AQUESA Data Monitor is a web application for monitoring and analyzing data from AQUESA devices. It provides features for data visualization, duplicate detection, missing data identification, device status monitoring, and automated email reporting.

## Features
- Data visualization and analysis
- Duplicate data detection
- Missing data identification
- Device status monitoring
- Battery status tracking
- Automated email reporting

## Installation

### Prerequisites
- Python 3.10 or higher
- MongoDB

### Setup
1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv .venv
   ```
3. Activate the virtual environment:
   - Windows: `.venv\Scripts\activate`
   - Linux/Mac: `source .venv/bin/activate`
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Copy `.env.example` to `.env` and update the configuration values

## Running the Application

Start the application with:
```
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

This will start both the web interface and the email scheduler automatically.

## Deployment

### Render
This application is configured for deployment on Render using the `render.yaml` configuration file.

### Heroku
For Heroku deployment, use the provided `Procfile` and `runtime.txt`.

## Environment Variables

The following environment variables can be configured in the `.env` file:

### MongoDB Configuration
- `MONGO_URI`: MongoDB connection string
- `DB_NAME`: Database name
- `COLLECTION_NAME`: Collection name for raw data

### Email Configuration
- `EMAIL_ADDRESS`: Sender email address
- `EMAIL_PASSWORD`: Email password or app password
- `SMTP_SERVER`: SMTP server address
- `SMTP_PORT`: SMTP server port

### Application Settings
- `APP_HOST`: Host address (default: 0.0.0.0)
- `APP_PORT`: Port number (default: 8000)
- `DEBUG_MODE`: Enable debug mode (true/false)

## License
This project is proprietary software of Elementure.