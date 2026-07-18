# Email_Spam_Prediction



A simple **Streamlit** application that predicts whether an email is **spam** or **not spam** using a pre-trained machine learning model.

## Streamlit Preview - [Streamlit](https://emailspamprediction01.streamlit.app/)

## Overview

This project provides a small web interface for making spam predictions based on a few email-related features.  
Users enter values for several attributes, and the app returns a prediction using the saved model file.

## Features

- Clean Streamlit-based user interface
- Real-time spam prediction
- Simple input form for email features
- Uses a pre-trained model stored locally
- Easy to run on Windows or any Python-supported system

## Tech Stack

- **Python**
- **Streamlit**
- **Pandas**
- **Joblib**
- **Machine Learning model**: `email_spam_linear_model.joblib`

## Project Structure

```text
Email Spam Prediction/
├── Spam-Email_Prediction.py
├── email_spam_linear_model.joblib
└── README.md
```

## Input Fields

The app accepts the following inputs:

- **Email Length** — total length of the email
- **Number of Links** — count of links in the email
- **Number of Special Characters** — count of special characters
- **Capital Words** — number of capitalized words
- **Has Attachment** — indicates whether the email contains an attachment (`0` or `1`)

## Requirements

Install the following dependencies:

```bash
pip install streamlit pandas joblib
```

## Installation

1. Clone or download the project folder.
2. Open the project in **VS Code** or your preferred editor.
3. Ensure the model file is present in the same folder as the Python script.
4. Install the required Python packages.

## Running the Application

Run the Streamlit app from the project directory:

```bash
streamlit run Spam-Email_Prediction.py
```

After running the command, Streamlit will open the application in your browser.

## Usage

1. Enter the email feature values in the form.
2. Select whether the email has an attachment.
3. Click the **Predict** button.
4. The app displays the result as:
   - **Spam email**
   - **Not spam**

## Output

The prediction is shown with a score value returned by the model.

- A score of **0.5 or higher** is treated as **Spam**
- A score below **0.5** is treated as **Not spam**

## Notes

- The file `email_spam_linear_model.joblib` must remain in the same directory as `Spam-Email_Prediction.py`.
- All input values are expected to be numeric.
- The application is designed for educational and demonstration purposes.



Project developed for spam email prediction using machine learning.
