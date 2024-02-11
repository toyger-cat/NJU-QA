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
from http import HTTPStatus
import dashscope

_ = load_dotenv(find_dotenv())

def call_with_messages():
    messages = [{'role': 'system', 'content': 'You are a helpful assistant.'},
                {'role': 'user', 'content': '如何做炒西红柿鸡蛋？'}]

    response = dashscope.Generation.call(
        dashscope.Generation.Models.qwen_turbo,
        messages=messages,
        result_format='message',  # set the result to be "message" format.
    )
    if response.status_code == HTTPStatus.OK:
        print(response)
    else:
        print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
            response.request_id, response.status_code,
            response.code, response.message
        ))


if __name__ == '__main__':
    call_with_messages()
