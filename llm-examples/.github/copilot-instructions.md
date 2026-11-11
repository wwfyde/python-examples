# Copilot Instructions for llm-examples

这是一个包含LLM、RAG和代理示例的代码库。本文档将帮助AI代理理解代码库的架构和开发最佳实践。

## 项目结构

主要组件:

- `agent-ui/`: Next.js构建的现代化Agent UI界面
- `api/`: FastAPI后端服务
- `examples/`: 各种LLM和Agent的示例代码
- `lib/`: 共享的工具库
- `prompts/`: 提示词模板
- `models/`: 数据模型定义

## 关键概念

### Agent UI (agent-ui/)

- 现代化的聊天界面,支持工具调用和推理步骤可视化
- 基于Next.js + TypeScript + Tailwind CSS构建
- 主要组件:
  - `src/components/chat/`: 聊天界面组件 
  - `src/types/os.ts`: 核心类型定义
  - `src/store.ts`: 全局状态管理

### API服务 (api/)

- 基于FastAPI构建的后端API
- `main.py`: 主要入口点,定义了图像标注等API接口
- 支持多种LLM提供商(OpenAI、千问等)

### 开发工作流

1. 依赖管理:
```bash
# Python项目
pip install -e .  # 安装开发依赖

# Agent UI
cd agent-ui
pnpm install
```

2. 运行服务:
```bash 
# 运行API服务
python -m api.main

# 运行Agent UI
cd agent-ui
pnpm dev
```

3. 测试:
- `examples/` 目录包含了各类功能的示例代码
- Jupyter notebooks 在 `notebooks/` 目录用于实验

## 集成要点

1. LLM集成:
- 支持的提供商定义在 `llm-providers/` 目录
- 每个提供商需实现标准接口

2. 代理开发:
- 主要框架代码在 `agents/` 目录
- 使用 Model Context Protocol (MCP) 进行代理间通信

3. UI定制:
- 页面组件定义在 `agent-ui/src/components`
- 使用 Tailwind CSS 进行样式定制
- 全局状态通过 Zustand 管理

## 代码约定

1. Python 代码:
- 使用 type hints
- 异步函数优先使用 async/await
- 配置通过环境变量或 config.yml 管理

2. TypeScript 代码:
- 严格类型检查
- 组件使用函数式编写
- 状态管理使用 Zustand

3. 文档:
- 重要函数需添加文档字符串
- 复杂逻辑需要注释说明
- API 接口需要添加 OpenAPI 文档

## 常见陷阱

1. 依赖管理:
- Python 项目使用 pyproject.toml 
- Node.js 项目使用 pnpm
- 注意版本兼容性

2. 环境配置:
- 需要正确配置 API keys
- 检查 config.yml 中的配置
- WebSocket 连接需要正确的URL

3. 调试提示:
- 使用 notebooks 调试 LLM 行为
- Agent UI 开发模式支持热重载
- API 服务支持自动重载