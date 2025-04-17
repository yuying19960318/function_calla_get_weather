import requests ,json
import dashscope,os
from dotenv import load_dotenv
from function_weather import function_weather


class  function_qw:

    def __init__(self):
        load_dotenv("qw.env")
        dashscope.api_key = os.getenv("DASHSCOPE_API_KEY")
        print(f"Loaded API_KEY: {dashscope.api_key}")

    def qw_tools(self):
        tools = [
            {
                "type": "function",
                "function": {
                    "name": "get_weather",
                    "description": "获取指定城市的天气信息",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "city": {
                                "type": "string",
                                "description": "城市名称(英文)",
                            },
                        },
                        "required": ["city"],
                    },
                },
            }
        ]
        return tools

    def messages(self,question):
        messages= [
            {
                "role": "system","content": "你是一个翻译，请把下面的话翻译成英文",
                "role": "user","content": question,
            }
        ]
        print(messages)
        return messages
    def result(self,messages,qw_tools):

        response = dashscope.Generation.call(
            model="qwen-turbo",
            messages = messages,
            tools=qw_tools,
            result_format="message",
        )
        print(response)
        result = response.output.choices[0].message
        print(result)
        return result

    def get_toolscall(self,result):

        if "tool_calls" not in result:
            print(result.content)
            print("没有函数调用")
        elif result.tool_calls[0]["function"]["name"]=="get_weather":
            json_date=json.loads(result.tool_calls[0]["function"]["arguments"])
            city=json_date["city"]
            a = function_weather()
            b=a.get_weather(city)

            return b


