# Loan Eligibility Backend

This repository contains the backend data for the **Loan Eligibility** application, which uses the _Fuzzy Tsukamoto_ method to determine whether a person is eligible for a loan or not.

## Base URL

- https://kelayakan-pinjaman-backend.vercel.app
- Access Colab: [Here](https://colab.research.google.com/drive/1P2qeWxOnwBv67Jkw47Z5kVm2ykOqkxY_?usp=sharing)

## Endpoints

### 1. Loan Eligibility Prediction

- **URL:** `/predict`
- **Method:** `POST`
- **Request Body:**
  - `pendapatan`: `float`
  - `usia`: `int`
  - `tanggungan`: `int`
  - `pengeluaran`: `float`
  - `aset`: `float`

### 2. Dataset Information

- **URL:** `/dataset`
- **Method:** `GET`
- **Description:** Provides information about the dataset used.

### 3. Team Member Information

- **URL:** `/member`
- **Method:** `GET`
- **Description:** Provides information about the team members who worked on this project.

## Application Frontend

To access the frontend of this application, please visit: [Loan Eligibility Frontend](https://kelayakanpinjaman.vercel.app/)

## How to Run the Project

1. Clone this repository: `git clone https://github.com/username/kelayakan-pinjaman-backend.git`
2. Navigate to the project directory: `cd kelayakan-pinjaman-backend`
3. Install dependencies: `npm install`
4. Start the server: `npm start`

## Contribution

We highly appreciate contributions from anyone. To contribute, follow these steps:

1. Fork this repository.
2. Create a new feature branch: `git checkout -b your-feature`
3. Commit your changes: `git commit -m 'Add feature ABC'`
4. Push to the branch: `git push origin your-feature`
5. Submit a pull request.

## License

This project is licensed under the MIT License.
