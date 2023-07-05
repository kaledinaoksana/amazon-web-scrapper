<img src="logo.png" alt="drawing"/>

# Amazon Product Scraper 

The objective of this project is to create a Python application that scrapes product information from the Amazon website. The application will allow users to search for products, retrieve details such as price, ratings, reviews, and other relevant data, and save the information for further analysis.

## Steps

### 1. Environment

#### Install Python and required libraries

Create a virtual environment to manage dependencies.

`conda create -n env-amazon python=3.9 pandas numpy bs4 requests`

#### Usage

Activate environment: `conda activate env-amazon`

Run script: `python3 main.py`

Deactivate environment: `conda deactivate`

#### Installed extensions in VS Code

- Markdown Preview Github Styling
- Python Environment Manager

### 2. User Input

Provide a command-line interface or a simple graphical user interface (GUI) to accept user input for the product search.

### 3. Perform Web Scraping

Use the Requests library to send HTTP requests to the Amazon website and retrieve the HTML content of the search results page.
Use Beautiful Soup to parse the HTML content and extract relevant information such as product names, prices, ratings, and reviews.
Handle pagination to scrape multiple pages of search results if necessary.

### 4. Data Storage

Store the scraped data in a structured format, such as a CSV file, JSON file, or a database.
Include relevant attributes like product title, price, rating, review count, and any other information you find valuable.

### 5. Data Analysis and Visualization

Perform data analysis on the scraped data to identify trends, popular products, or other insights.
Use libraries like Pandas and Matplotlib to analyze and visualize the data in meaningful ways, such as price distributions, rating trends, or review sentiments.

### 6. Error Handling and Robustness

Implement error handling mechanisms to deal with common issues like network errors, data extraction failures, or anti-scraping measures taken by Amazon.
Consider incorporating retry mechanisms and user feedback prompts to handle potential errors gracefully.

### 7. User-Friendly Features

Enhance the application by adding user-friendly features such as progress indicators, clear error messages, and options for exporting data in different formats.

## 🛠 Skills

Scraping

## 👩🏻‍💻 Authors

[@kaledinaoksana](https://github.com/kaledinaoksana) Data Analyst

## 🔗 Links

 [![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/oksana-kaledina/)
