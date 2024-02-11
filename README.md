# NJU-QA

## Reference

<https://github.com/chatchat-space/Langchain-Chatchat>

<https://github.com/datawhalechina/llm-universe>

email me: <toyger-cat@outlook.com>

## Outline

```bash
-project
    -readme.md 项目说明
    -requirements.txt 使用依赖包的版本
    -llm LLM调用封装
        -self_llm.py 自定义 LLM 基类
        -wenxin_llm.py 自定义百度文心 LLM
        -spark_llm.py 自定义讯飞星火 LLM
        -zhipuai_llm.py 自定义智谱AI LLM
        -call_llm.py 将各个 LLM 的原生接口封装在一起
        -test.ipynb 使用示例
    -embeddings embedding调用封装
        -zhipuai_embedding.py 自定义智谱AI embedding
        -call_embedding.py 调用 embedding 模型
    -data 源数据路径
    -database 数据库层封装
        -create_db.py 处理源数据及初始化数据库封装
    -qa_chain 应用层封装
        -qa_chain.py 封装检索问答链，返回一个检索问答链对象
        -chat_qa_chian.py：封装对话检索链，返回一个带有历史记录的对话检索链对象
        -get_vectordb.py 返回向量数据库对象
        -model_to_llm.py 调用模型
        -test.ipynb 使用示例
    -serve 服务层封装
        -run_gradio.py 启动 Gradio 界面
        -api.py 封装 FastAPI
        -run_api.sh 启动 API
        -test.ipynb 使用示例
```

## Task

- [ ] overload text_splitter
- [ ] define document_loaders
- [ ] specify embedding-models (consider retrain or customize keywords)
- [ ] UI based on streamlit

## tech

- [ ] Langchain
  - [ ] model: Qwen-14B-Chat(prefer use it locally)
  - [ ] database: pgvector
  - [ ] Embedding Models: piccolo-large-zh
    - [ ] also consider: Custom keyword adjustment Embedding model
  - [ ] streamlit UI

## data

- [ ] Use TXT / Markdown and other formatted files, and typeset them according to key points
