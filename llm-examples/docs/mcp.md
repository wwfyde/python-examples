

- 支持MCP的客户端:
  - cursor
  - vscode -github copilot
  - claude

MCP 协议涉及三个核心角色：

• MCP Host（宿主）：用户操作 MCP 服务的平台，比如 AI 聊天工具或专业 IDE。
• MCP Server（服务端）：实际提供功能和数据支持的程序，比如访问文件、调用数据库、调用API。
• MCP Client（客户端）：连接 Host 与 Server，负责数据交互与通信。
简单来说，用户在 MCP Host 上发出指令，Host 通过 MCP Client 和 MCP Server 沟通，最终实现功能并返回结果给用户。