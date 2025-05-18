import gradio as gr
import os

# 环境变量安全调用示例
API_KEY = os.getenv("MY_KEY", "default_value")

def greet(name):
    return f"Hello {name}! Key:{API_KEY[:2]}***"

gr.Interface(greet, "text", "text").launch()
