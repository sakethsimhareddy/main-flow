# Main Flow

This repository contains various tasks and projects aimed at developing and demonstrating skills in Python, SQL, web development, and data analysis.

## Table of Contents

- [Overview](#overview)
- [Task Descriptions](#task-descriptions)
- [Setup and Installation](#setup-and-installation)
- [Running the Project](#running-the-project)
- [Project Structure](#project-structure)
- [Contributing](#contributing)

## Overview

Main Flow is a collection of tasks designed to help you learn and practice Python programming, web scraping, GUI development, data analysis, and full-stack web development.

## Task Descriptions

### Task 1: Basic Python Programming
- Simple Python scripts demonstrating fundamental concepts.

### Task 2: Data Analysis with CSV
- Reading CSV files, data analysis, and plotting data using Python libraries.

### Task 3: Web Scraping with Beautiful Soup
- Web scraping using Beautiful Soup.

### Task 4: Calculator Development
- Developing a fully functional calculator that operates in both GUI and command-line interface using Python and Tkinter.

### Task 5: Full-Stack Web Application
- Developing a React notes application with a back-end built using Java and Spring Boot.

### Task 6: Database Management Basics
- Learning basic database management concepts and SQL for data manipulation.
  
## Setup and Installation

### Prerequisites
- Python 3.x
- MySQL server
- Required Python libraries: mysql-connector-python, tkinter, pandas, matplotlib, BeautifulSoup, requests

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/sakethsimhareddy/main-flow.git
   cd main-flow
   ```

2. **Install Python libraries:**
   ```sh
   pip install mysql-connector-python pandas matplotlib beautifulsoup4 requests
   ```

3. **Set up MySQL:**
   - Create a database and user for the project.
   - Example:
     ```sql
     CREATE DATABASE CompanyDB;
     CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
     GRANT ALL PRIVILEGES ON CompanyDB.* TO 'username'@'localhost';
     USE CompanyDB;
     ```

## Running the Project

1. **Create the MySQL Table:**
   ```sql
   CREATE TABLE Employees (
       EmployeeID INT AUTO_INCREMENT PRIMARY KEY,
       FirstName VARCHAR(255) NOT NULL,
       LastName VARCHAR(255) NOT NULL,
       BirthDate DATE,
       Position VARCHAR(255)
   );
   ```

2. **Run the  application (Task):**
   ```sh
   python file_name.py
   ```

## Project Structure

- `task1.py`: Basic Python scripts.
- `task2.py`: Data analysis with CSV files.
- `task3.py`: Web scraping using Beautiful Soup.
- `task4.py`: Calculator development with GUI and CLI.
- `task5.py`: Full-stack web application with React and Spring Boot.
- `task6.py`: Database management basics.

## Contributing

Contributions are welcome! Please fork this repository and submit pull requests.
