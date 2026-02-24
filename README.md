# LaTeX 公式在线计算系统

基于 DeepSeek API 的在线 LaTeX 公式求值工具。

## 功能特性

- 在线计算数学表达式
- 求解方程
- 求导、积分等数学运算
- 简洁美观的 Web 界面
- API Key 安全存储（后端管理）

## 技术栈

- **前端**：HTML + JavaScript
- **后端**：Python + Flask
- **AI 服务**：DeepSeek Chat API

## 项目结构

```
MyPrograms/
├── .env                     # 环境变量配置
├── backend/
│   ├── app.py              # Flask 后端主程序
│   ├── requirements.txt    # Python 依赖
│   └── static/
│       └── index.html      # 前端页面
└── README.md               # 本文档
```

## 快速开始

### 环境要求

- Python 3.8+
- DeepSeek API Key

### 1. 安装依赖

```bash
cd backend
pip install -r requirements.txt
```

### 2. 配置 API Key

编辑 `.env` 文件，配置您的 DeepSeek API：

```env
DEEPSEEK_API_KEY=your_api_key_here
DEEPSEEK_API_URL=https://api.deepseek.com
```

### 3. 启动服务

```bash
cd backend
python app.py
```

服务启动后访问：**http://127.0.0.1:5000**

### 4. 使用方法

1. 打开浏览器访问 http://127.0.0.1:5000
2. 在输入框中输入 LaTeX 公式
3. 点击"求值"按钮或按 `Ctrl+Enter` 提交
4. 查看计算结果

## 示例

| 输入 | 说明 |
|------|------|
| `2 + 3 * 4` | 计算表达式 |
| `x^2 + 2x + 1 = 0` | 解方程 |
| `derivative of x^3` | 求导数 |
| `integrate x^2` | 求积分 |
| `sqrt(16) + 2^3` | 复杂计算 |

## API 接口

### 求值接口

**端点**：`POST /api/evaluate`

**请求**：
```json
{
  "expression": "x^2 + 2x + 1 = 0"
}
```

**响应**：
```json
{
  "result": "x = -1"
}
```

**错误响应**：
```json
{
  "error": "错误信息"
}
```

## 常见问题

### Q: 启动失败，提示缺少模块

A: 确保已安装依赖，运行 `pip install -r requirements.txt`

### Q: API 请求超时

A: 检查网络连接，或稍后重试

### Q: 返回错误结果

A: DeepSeek 会尝试理解并计算公式，对于复杂数学问题可能需要更精确的描述

## 停止服务

按 `Ctrl+C` 停止后端服务。

## 注意事项

- API Key 存储在后端 `.env` 文件中，不会暴露给前端
- 请勿将 `.env` 文件提交到公共仓库
- 本项目仅供个人学习和使用

## 许可证

MIT License
