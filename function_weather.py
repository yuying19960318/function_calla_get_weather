import requests ,json
import dashscope,os
from dotenv import load_dotenv

class  function_weather:


    def get_weather(self,city):
        """
        使用 openweather API 获取指定城市的天气信息
        :city: 城市名称(英文)
        :return: 天气信息
        """
        print(city)
        openweather_api_key = os.getenv("OPENWEATHERMAP_API_KEY")
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={openweather_api_key}'
        response = requests.get(url)
        if not response.ok:
            print("请求失败")
            return ValueError("Failed to get weather data")
        response_json = response.json()
        kalvin_temp = response_json['main']['temp']
        result_temp = kalvin_temp - 273.15
        result_temp = round(result_temp, 2)
        print(f"当前{city}的温度为：{result_temp}°C")
        return f"该城市当前温度：{result_temp}°C"