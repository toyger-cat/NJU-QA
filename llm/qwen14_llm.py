'''
@file: qwen14_llm.py
@time: 2024/2/11 23:22
@author: toyger-cat
@version: v1.0
@Contact: toyger-cat@outlook.com
@desc: 通过'messages调用'qwen14的API
'''

from dotenv import find_dotenv, load_dotenv
import os

_ = load_dotenv(find_dotenv())
wenxin_api_key = os.environ["DASHSCOPE_API_KEY"]
