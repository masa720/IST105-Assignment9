# IST105-Assignment9: Network Automation with Cisco DNA Center API

## Overview
This project is a Django web application for network automation using the Cisco DNA Center API. It supports API authentication, device inventory listing, interface details retrieval, and logs all interactions to MongoDB.

## Components
- Django (Web application)
- MongoDB (for logging)
- Docker (for MongoDB)
- Cisco DNA Center Sandbox API

## Directory Structure
```
assignment9/
  manage.py
  assignment9/           # Django project
  dna_center_cisco/      # Main app
    dnac_config.py       # DNA Center API credentials
    dnac_network.py      # API logic / CLI
    views.py             # Django views
    templates/dna_center_cisco/
      token.html         # Auth token display
      devices.html       # Device list
      interfaces.html    # Interface details
```

## Setup Instructions
### 1. Start MongoDB (Docker)
```sh
docker-compose up -d
```

### 2. Install Python Packages
```sh
cd assignment9
pip install -r requirements.txt
```

### 3. Create .env File
```
MONGODB_URI=mongodb://localhost:27017/
```

### 4. Django Migrations
```sh
python manage.py migrate
```

### 5. Start Django Server
```sh
python manage.py runserver 0.0.0.0:8000
```

### 6. Web Access
- Auth Token: http://localhost:8000/token/
- Device List: http://localhost:8000/devices/
- Interface Details: http://localhost:8000/interfaces/

### 7. Check MongoDB Logs
```sh
docker exec -it local-mongo mongosh
use automation_logs
db.logs.find().pretty()
```

## CLI Usage
```sh
cd assignment9
PYTHONPATH=. python dna_center_cisco/dnac_network.py
```

## Example requirements.txt
- Django
- requests
- pymongo
- python-dotenv

## Notes
- Uses Cisco DevNet Sandbox for DNA Center API.
- MongoDB and Django can run on separate EC2 instances or locally via Docker.
- Do not commit `.env` or `db.sqlite3` to Git.

---

## Author
- masaki
