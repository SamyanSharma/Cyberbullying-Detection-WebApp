# Cyberbullying Detection WebApp

[![Project Status](https://img.shields.io/badge/Status-Active-success.svg)](https://github.com/Samyan1Sharma/Cyberbullying-Detection)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/Samyan1Sharma/Cyberbullying-Detection/blob/main/LICENSE)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)](https://github.com/Samyan1Sharma/Cyberbullying-Detection/blob/main/CONTRIBUTING.md)
![Framework](https://img.shields.io/badge/Framework-Flask-blue)
![Model](https://img.shields.io/badge/Model-LinearSVC-brightgreen)
![Python](https://img.shields.io/badge/Language-Python-blue)

A Flask based Web application that detects cyberbullying in text using a previously trained ML model (trained on [Cyberbullying Classification Dataset](https://www.kaggle.com/datasets/andrewmvd/cyberbullying-classification)).

## 📌 Overview
This Flask-based web application uses a pre-trained LinearSVC machine learning model with TF-IDF vectorization to detect cyberbullying in text input. Users can submit text, and the system analyzes it to predict whether it contains harmful or bullying content.

## 🚀 Features
- **Real-time text analysis**
- **User-friendly interface** with text input and results display
- **Six-category classification**:
  - 👴 Age-based
  - 🌍 Ethnicity-based
  - ⚧️ Gender-based
  - 🕌 Religion-based
  - 💢 Other cyberbullying
  - ✅ Not cyberbullying
- **Audit logging** of all predictions
- **Responsive design** for all devices
  
## 🛠 Prerequisites
- Python 3.7+
- Flask (pip install flask)
- Scikit-learn (pip install scikit-learn)

Other dependencies: pandas, numpy, joblib (for model loading)

```mermaid
graph TD
    A[Flask] --> B[LinearSVC Model]
    A --> C[Jinja2 Templates]
    B --> D[TF-IDF Vectorizer]
    D --> E[Text Preprocessing]
    A --> F[Prediction Logging]
```

![WebApp Interface](./WebApp_Interface.png)


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details..

## Acknowledgments
- Thanks to all contributors who have helped make this project possible
- Special thanks to the open-source community for their invaluable tools and libraries
