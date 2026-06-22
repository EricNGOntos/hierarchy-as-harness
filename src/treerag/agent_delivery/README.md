# TreeRAG 共享 agent_delivery

Gold / Flat / TreeRAG 共用 `src/realdata/agent_delivery/` 下的 compose、budget fill、Inspect judge 实现。
TreeRAG 入口为 `src/treerag/eval_arxiv_treerag.py`，通过 `PYTHONPATH=src/realdata` 加载共享代码。

本地 API 配置：

```bash
cp src/realdata/agent_delivery/llm_api.env.example src/realdata/agent_delivery/llm_api.env
# 或复制到本目录（二者等价，均被 .gitignore）
```
