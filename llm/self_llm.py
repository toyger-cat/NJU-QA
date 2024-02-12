"""
@file: self_llm.py
@time: 2024/2/12
@author: toyger-cat
@version: v1.0
@Contact: toyger-cat@outlook.com
@desc: 在 LangChain LLM 基础上封装的项目类
"""
from abc import ABC

from langchain.llms.base import LLM
from typing import Dict, Any, Mapping
from pydantic import Field


class SelfLLM(LLM):

    def __init__(self):
        super().__init__()

    url: str = None
    model_name: str = "qwen14_llm"
    request_timeout: float = None
    temperature: float = 0.1
    api_key: str = None
    model_kwargs: Dict[str, Any] = Field(default_factory=dict)

    @property
    def _default_params(self) -> Dict[str, Any]:
        normal_params = {
            "temperature": self.temperature,
            "request_timeout": self.request_timeout,
        }
        # print(type(self.model_kwargs))
        return {**normal_params}

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {**{"model_name": self.model_name}, **self._default_params}
