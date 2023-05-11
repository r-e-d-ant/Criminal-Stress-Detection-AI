
## Stress Detection AI

This guide provides step-by-step instructions on how to run my Django project on different operating systems: Windows, macOS, and Linux. Follow the instructions relevant to your operating system.

** Prerequisites

Before getting started, ensure that you have the following prerequisites installed on your system:

Python 3.x: Download Python and follow the installation instructions.

# Setup

* Clone the project repository from repository-url or download and extract the project ZIP file.
* Open a terminal or command prompt and navigate to the project's root directory.
* Create a virtual environment for the project. Execute the following command:

```
python -m venv myenv # here myenv is virtual environment name, you can name it however u want
```
This command creates a virtual environment named "myenv" in the project directory.

* Activate the virtual environment:
- Windows:
```
myenv\Scripts\activate
```
- macOS/Linux:
source myenv/bin/activate

* Install project dependencies using pip:
```
pip install -r requirements.txt
```

# Running the Development Server

To run the Django development server and access the project in your web browser, follow the instructions below for your operating system.

- Windows
Open a terminal or command prompt.
Activate the virtual environment:

```
myenv\Scripts\activate
```

1. Navigate to the project's root directory.
2. Run the following command to start the development server:

```
python manage.py runserver
```

3. Open your web browser and visit http://localhost:8000 to access the project.

- macOS/Linux

Open a terminal.
Activate the virtual environment:

```
source myenv/bin/activate
```

1. Navigate to the project's root directory.
2. Run the following command to start the development server:

```
python manage.py runserver
```

3. Open your web browser and visit http://localhost:8000 to access the project.

# Additional Notes
Make sure the virtual environment is activated whenever you want to run the project.
If you encounter any issues, refer to the project's documentation or reach out for assistance.

# Citation

1. L. Rachakonda, A. K. Bapatla, S. P. Mohanty, and E. Kougianos, “SaYoPillow: Blockchain-Integrated Privacy-Assured IoMT Framework for Stress Management Considering Sleeping Habits”, IEEE Transactions on Consumer Electronics (TCE), Vol. 67, No. 1, Feb 2021, pp. 20-29.

2. L. Rachakonda, S. P. Mohanty, E. Kougianos, K. Karunakaran, and M. Ganapathiraju, “Smart-Pillow: An IoT based Device for Stress Detection Considering Sleeping Habits”, in Proceedings of the 4th IEEE International Symposium on Smart Electronic Systems (iSES), 2018, pp. 161--166.
