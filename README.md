# Diamond Price Prediction

This project predicts the price of diamonds based on features like carat, depth, table, cut, color, and clarity. It uses machine learning models to estimate the price, helping users get accurate diamond price predictions.

## Project Overview

The Diamond Price Prediction project utilizes Flask to create a web-based application where users can input diamond features, and the model predicts the price based on these inputs. This project also includes a machine learning pipeline built using `scikit-learn`, which was trained on real-world data.

### Key Features
- **Web Interface**: A simple, user-friendly interface to input diamond attributes.
- **Predictive Model**: Based on a trained machine learning model that uses features like carat, depth, cut, color, clarity, etc.
- **Interactive Results**: Displays predicted price of the diamond in a clear and responsive way.

## Technologies Used

- **Python**: The main programming language for building the application.
- **Flask**: Lightweight web framework used for serving the application.
- **Pandas**: For data manipulation and pre-processing.
- **NumPy**: For numerical operations.
- **Scikit-learn**: For building and using the machine learning model.
- **Seaborn**: For visualizing data and model results.

## Installation

### Prerequisites
- Python (recommended version: 3.8 or later)
- Anaconda (for managing the virtual environment)

### Steps to Set Up Locally

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/diamond-price-prediction.git
   cd diamond-price-prediction
   ```

2. **Create a Conda Environment:**
   Create a new virtual environment to manage dependencies.
   ```bash
   conda create -n diamond-price python=3.8
   conda activate diamond-price
   ```

3. **Install Dependencies:**
   Install all the required libraries.
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application:**
   Start the Flask application by running the following command:
   ```bash
   python application.py
   ```

5. **Access the Web Application:**
   Open your browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

## Usage

1. **Home Page**: The home page introduces the project and explains how to use the tool.
2. **Prediction Form**: The user can enter details about the diamond (e.g., carat, depth, table, etc.), and the model will predict the price.
3. **Result Page**: After submitting the form, the predicted price of the diamond will be displayed on this page.

## Project Structure

- **application.py**: Main Flask application file that runs the web app.
- **src/pipelines/prediction_pipeline.py**: Contains the data pipeline and machine learning model for price prediction.
- **templates/**: Contains HTML files for the frontend (e.g., `index.html`, `form.html`, `result.html`).
- **static/**: Contains static files like CSS, images, and JavaScript.
- **requirements.txt**: Lists the Python packages needed for the project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to contribute to this project. You can fork the repository, make your changes, and create a pull request.

---

### Contact

For any inquiries or issues, feel free to contact me at:
- **Email**: souravshukla@gmail.com
- **GitHub**: [@your-username](https://github.com/Mr-SRV-Shukla)
