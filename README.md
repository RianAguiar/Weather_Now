# 🌦️ Weather_Now  

A simple web application for checking the weather, working in Portuguese, built with **Django**, allowing users to search for a city and view current weather.

<p align="center">
  <img src="tarefas/static/img/image.png" width="350px" />
</p>
---

## 🐸 Features  
- 🐸 City search through an input field.  
- 🐸 Display of weather data: description, temperature, etc.  
- 🐸 Dynamic icons based on weather conditions (cloudy, clear sky, fog, rain, thunderstorms, etc).  
- 🐸 Responsive layout with clean design, gradients, and themed backgrounds.  
- 🇧🇷 Portuguese (pt-BR) language and Brazilian timezone support.  

---

## 🛠️ Technologies Used  
- **Django (Python)** — backend and template rendering.  
- **Custom HTML + CSS + Javascript** (gradients, smooth animations, responsive design).  
- **OpenWeather API** — for real-time weather data.  

---

## ✅ Requirements  
- Python 3.x  
- Django installed (`pip install django`)  

---

## 🚀 Installation & Usage  

1. Clone the repository:  
   ```bash
   git clone https://github.com/RianAguiar/Weather_Now.git

2. Navigate to the project directory:
   ```bash
   cd Weather_Now

3. VS Code Setup (Optional) For a better experience, install these extensions in your VSCode:

-**Django**: (For syntax highlighting, snippets, etc.)
-**SQLite Viewer**: (To inspect the database)

4. Install the request packages:
    ```bash
    py -3.11 -m pip install requests

5. Run database migrations (if needed):
    ```bash
    python manage.py migrate

6. Start the development server:
    ```bash
    python manage.py runserver

7. Open in your browser:
    ```bash
    👉 http://127.0.0.1:8000/ 
