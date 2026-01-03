# GroceryLocatorHackRU25

A Flask web application that helps users find the cheapest grocery items at nearby stores by zipcode.

## Setup Instructions

### 1. Create a Virtual Environment

```bash
python3.11 -m venv venv
```

### 2. Activate the Virtual Environment

**On macOS/Linux:**
```bash
source venv/bin/activate
```

**On Windows:**
```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Note: `sqlite3` is included with Python and does not need to be installed separately.

### 4. Set Up the Database

First, create the database structure:
```bash
python database/makeDataBase.py
```

Then, populate it with data:
```bash
python database/fillDataBase.py
```

### 5. Run the Application

```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Dependencies

- pandas
- folium
- flask
- sqlite3 (built-in with Python)
