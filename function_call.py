from function_qw import function_qw
from function_weather import function_weather
import gradio as gr

def function_call(question):
    # 实例化函数
    qw = function_qw()
    qw_tools = qw.qw_tools()    # 获取工具
    messages = qw.messages(question)   # 获取消息列表

    result = qw.result(messages,qw_tools)
    weather= qw.get_toolscall(result)
    return weather



iface = gr.Interface(
    fn=function_call,
    inputs=gr.Textbox(label='输入你的问题'),
    outputs=[
        gr.Textbox(label='AI建议'),  # 显示AI的天气建议
    ],
    title='天气小助手',
    description='想问问哪里的天气',
)

iface.launch()