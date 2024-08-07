# Web Scraping Script Documentation

# **Purpose**

### This Python script scrapes product details from two different e-commerce websites (Amazon and Flipkart) using BeautifulSoup and requests libraries.

### **Libraries Used**

- **`BeautifulSoup`**: For parsing HTML content
- **`requests`**: For making HTTP requests

### **Functions**

### **`amazon_scrap(url)`**

- **Purpose**: Scrapes product details from Amazon website.
- **Parameters**:
    - **`url`** (str): URL of the Amazon product page.
- **Steps**:
    1. Sends an HTTP GET request to the provided URL with specified headers.
    2. Parses the HTML content using BeautifulSoup.
    3. Extracts the product name, price, and sets the source as Amazon.
    4. Prints the product details.

### **`flipkart_scrap(url)`**

- **Purpose**: Scrapes product details from Flipkart website.
- **Parameters**:
    - **`url`** (str): URL of the Flipkart product page.
- **Steps**:
    1. Sends an HTTP GET request to the provided URL with specified headers.
    2. Parses the HTML content using BeautifulSoup.
    3. Extracts the product name, price, and sets the source as Flipkart.
    4. Prints the product details.

### **Execution**

- User is prompted to input URLs for Amazon and Flipkart products.
- The script then calls the respective scraping functions for each URL.
- Product details (name, price, source) are displayed for each website.