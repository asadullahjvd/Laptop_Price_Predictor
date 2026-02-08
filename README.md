# Laptop Price Predictor

## Overview
The Laptop Price Predictor is a machine learning-based project that predicts laptop prices based on various features. The goal is to provide users with an estimated price of a laptop based on its specifications, helping them make informed purchase decisions.

## Features
- **Predictive Modeling**: Utilizes machine learning algorithms to predict prices based on laptop specifications.
- **User-Friendly Interface**: A simple interface for users to input laptop details and receive price predictions.
- **Data Visualization**: Displays visual insights about laptop price distributions and model performance metrics.
- **Custom Prediction**: Users can input their laptop specifications to get a tailored price prediction.
- **Training Data**: Trained on a comprehensive dataset of laptop specifications and prices.

## Functionality
1. **Input Specifications**: Users can enter various specifications such as:
   - Brand
   - Model
   - Processor Type
   - RAM Size
   - Storage Type
   - Graphics Card
   - Display Size

2. **Price Prediction**: After entering the details, the application provides an estimated price based on the trained model.

3. **Model Training**: 
   - The model can be retrained on new data to improve its accuracy.
   - Evaluation metrics include RMSE (Root Mean Square Error) and R-squared values.

## Installation
To run the project locally, follow these steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/asadullahjvd/Laptop_Price_Predictor.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Laptop_Price_Predictor
   ```
3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python app.py
   ```

## Usage
- Input the laptop specifications in the form provided.
- Click on the ‘Predict Price’ button to see the estimated price.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for feature requests or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- Thanks to the contributors and the open-source community for providing datasets and libraries that made this project possible.