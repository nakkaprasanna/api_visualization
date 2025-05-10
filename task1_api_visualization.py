import requests
import matplotlib.pyplot as plt

API_KEY = "your_api_key"  # Replace with your OpenWeatherMap API key
city = "Mumbai"
url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

dates, temps = [], []
for entry in data['list']:
    dates.append(entry['dt_txt'])
    temps.append(entry['main']['temp'])

plt.figure(figsize=(10, 5))
plt.plot(dates[:10], temps[:10], marker='o')
plt.title(f"Temperature Forecast for {city}")
plt.xlabel("Date-Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
