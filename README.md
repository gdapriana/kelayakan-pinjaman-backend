# Loan Eligibility Backend

## 🏦 Project Overview

This backend application determines loan eligibility using the Fuzzy Tsukamoto method. It provides intelligent loan assessment based on multiple financial parameters.

## 🚀 Project Demo

- **Backend Server:** [kelayakan-pinjaman-backend.vercel.app](https://kelayakan-pinjaman-backend.vercel.app)
- **Frontend Application:** [kelayakanpinjaman.vercel.app/](https://kelayakanpinjaman.vercel.app/)

## 📂 Project Structure

```
kelayakan-pinjaman-backend/
│
├── dataset/                 # Contains project datasets
├── resources/
│   ├── fuzzy.py             # Fuzzy Tsukamoto logic implementation
│   ├── member.py            # Project team information
│   └── preprocessing.py     # Data preprocessing utilities
└── app.py                   # Main application entry point
```

## 🔍 API Endpoints

### 1. Predict Loan Eligibility

- **URL:** `/predict`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "pendapatan": float,
    "usia": int,
    "tanggungan": int,
    "pengeluaran": float,
    "aset": float
  }
  ```

### 2. Dataset Information

- **URL:** `/dataset`
- **Method:** `GET`
- **Description:** Provides details about the dataset used for loan eligibility prediction

### 3. Team Members

- **URL:** `/member`
- **Method:** `GET`
- **Description:** Returns information about the project team

## 🧠 Methodology

The application uses the Fuzzy Tsukamoto method to assess loan eligibility. This approach allows for intelligent and nuanced decision-making by:

- Converting crisp input values to fuzzy input
- Applying fuzzy inference rules
- Defuzzifying results to determine loan eligibility

## 🛠️ Technologies Used

- Python
- Flask
- Fuzzy Logic
- Vercel (Deployment)

## 👥 Team

For detailed team information, please check the `/member` endpoint or contact the repository maintainers.

## 🤝 Contributing

Interested in contributing? Please read our contributing guidelines and feel free to submit pull requests.
