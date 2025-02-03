# Number Classification API

## Overview
The Number Classification API is a FastAPI-based web service that takes a number as input and returns various mathematical properties along with a fun fact. The API is designed to be fast, publicly accessible, and compliant with the HNG12 Stage 1 backend task requirements.

## Features
- Determines if a number is **prime**
- Checks if a number is **perfect**
- Identifies if a number is an **Armstrong number**
- Classifies a number as **odd** or **even**
- Computes the **sum of its digits**
- Retrieves a **fun fact** from the [Numbers API](http://numbersapi.com)

## API Specification
### **Endpoint**
GET /api/classify-number?number=<integer>


### **Request Parameters**
| Parameter | Type   | Required | Description                 |
|-----------|--------|----------|-----------------------------|
| number    | int    | Yes      | The number to classify      |

### **Response Format**
#### **200 OK**
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}

```

git push -u origin main
#### **400 Bad Request (For Invalid Inputs)**
```json
{
    "number": "invalid",
    "error": true
}
```

## Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/number-classification-api.git
cd number-classification-api

```

### 2️⃣ Create & Activate a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate 

```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt

```

### 4️⃣ Run the API Locally
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

```