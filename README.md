Price Hike Backend

Price Hike is a simple backend system for a price comparison platform. It fetches product price data from predefined URLs and updates the latest prices in an Excel file. The backend is intentionally minimal and easy to maintain, using a single Python script and an Excel based database.

Project Files

backend.py
Contains the complete backend logic including product URLs price fetching parsing validation and Excel update operations.

database.xlsx
Acts as the database and stores product name source URL latest price and last updated time.

README
Project documentation.

Features

Fetches live price data from product URLs defined directly inside backend.py
Updates the latest prices in database.xlsx
Requires minimal setup and configuration
Can be executed multiple times to keep prices updated
Designed to support integration with a frontend price comparison website

Technology Stack

Programming Language Python
HTTP Requests Requests library
HTML Parsing BeautifulSoup
Excel Handling Pandas and OpenPyXL

How It Works

Product URLs are hard coded inside backend.py
The script sends HTTP requests to each URL
Price data is extracted from the response
The extracted prices are validated
The Excel file is updated with the latest price and timestamp
