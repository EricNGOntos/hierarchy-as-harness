# TreeRAG 共享 agent_delivery

Gold / Flat / TreeRAG 共用 `src/realdata/agent_delivery/` 下的 compose、budget fill、Inspect judge 实现。
TreeRAG 入口为 `src/treerag/eval_arxiv_treerag.py`，通过 `PYTHONPATH=src/realdata` 加载共享代码。

本地 API 配置（勿提交）：

```bash
mkdir -p ~/.config/realdata_treerag
cp src/realdata/agent_delivery/llm_api.env.example ~/.config/realdata_treerag/llm_api.env
# 或复制到 src/realdata/agent_delivery/llm_api.env（均在 .gitignore）
```
