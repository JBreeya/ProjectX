# Project X - Stock Information Web App 📈🌐

#### Objective:
The Stock Information Web App aims to provide users with real-time stock prices and support/resistance levels for selected companies on a specified date. Users can input a date, and the app fetches and displays relevant stock information.

#### Technologies Used:
- **Flask:** A micro web framework for Python, used for building the web application.
- **SQL Server:** A relational database management system for storing and retrieving stock-related data.
- **Yahoo Finance API:** Utilized via the `yfinance` library to fetch real-time stock prices.
- **HTML, CSS, JavaScript:** Front-end technologies for creating a user-friendly interface.

#### Key Features:

1. **Date Selection:**
   - Users can input a specific date using the date picker in the web interface. 🗓️

2. **Weekend Handling:**
   - The app checks if the selected date is a Saturday or Sunday and provides a message if the market is closed on weekends. 🚫📅

3. **Future Date Handling:**
   - If users select a future date, the app informs them that stock prices for that date are not available yet. ⏰🔮

4. **Email Notification:**
   - Users can click the "Mail" button to send an email containing stock information for the selected date to specified recipients. 📧📤

5. **Responsive Table:**
   - Display of stock information in a responsive table format, highlighting support and resistance levels. 📊👀

6. **Visual Indicators:**
   - Arrows indicating whether the stock price is below support or above resistance. ⬆️⬇️

7. **Dynamic Data Retrieval:**
   - Real-time fetching of stock prices and information from the Yahoo Finance API. 🔄📡

#### Usage Instructions:
1. Run the Flask application locally. 🚀
2. Open the web interface and select a date. 🌐
3. Click the "Run" button to fetch and display stock information. 📲
4. Optionally, click the "Mail" button to send an email with stock details. 📧🚀

#### Notes:
- Ensure the required libraries are installed (`flask`, `pyodbc`, `yfinance`, `pandas`) before running the application.
- The app provides valuable insights into stock trends and potential support/resistance levels, aiding users in making informed investment decisions. 📉💡
