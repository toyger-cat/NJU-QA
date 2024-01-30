# NJU-QA

> 加载文件 -> 读取文本 -> 文本分割 -> 文本向量化 -> 问句向量化 -> 在文本向量中匹配出与问句向量最相似的 top k个 -> 匹配出的文本作为上下文和问题一起添加到 prompt中 -> 提交给 LLM生成回答

受项目[https://github.com/chatchat-space/Langchain-Chatchat](https://github.com/chatchat-space/Langchain-Chatchat)的启发，构建轻量化LLM+私域数据问答。

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
