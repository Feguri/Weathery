# Weathery
Weather application Tkinter

Welcome to Weathery, a weather application. 
It's my first ever project using Python and Tkinter for practicing purposes (worthy of sharing).

## Setup

1. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # macOS/Linux
   # .\.venv\Scripts\activate  # Windows
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. **OpenWeather API key**: obtain a free key from https://openweathermap.org/api and set it in the environment:
   ```bash
   export OPENWEATHER_API_KEY="your_key_here"  # macOS/Linux
   ```
   The app will fall back to a legacy key if this is not set, but it may not provide forecast data.

4. Run the application:
   ```bash
   ./.venv/bin/python main.py
   ```
