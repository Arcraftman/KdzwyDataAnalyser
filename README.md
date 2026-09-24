# DataAnalyser

账无忧财务数据分析项目。仓库根目录包含 Electron 桌面客户端、Python 只读服务、独立的 C++ 迁移模块和旧 Excel 客户端。各部分职责见 [项目边界](docs/ARCHITECTURE.md)。

## Electron 桌面客户端

在 Windows 上安装 Node.js 22.12+（包含 npm）和 Python 3.10+，然后在本项目根目录运行：

```powershell
.\scripts\setup-local.ps1
npm install
npm run desktop
```

打开客户端后，点击“登录账无忧”，在弹出的登录窗口完成验证；返回客户端选择账套和月份，点击“刷新数据”。如果已有有效会话而本地服务未运行，点击“启动本地服务”。

当前桌面版显示财务总览、月度趋势及 11 张受管原始数据表。它通过本机 JSON 接口读取现有只读服务，不运行 VBA。预算和账龄人工录入、六张图表的 DeepSeek 解读、年度及研发专用报表尚未迁入桌面界面；这些功能仍在现有 Excel 客户端中。C++ 核心位于 `cpp/`，目前未接入桌面版。

会话和本地访问令牌仅保存在 `http_sessions/`、`runtime/`。Electron 渲染进程只接收已筛选的账套列表和报表数据；主进程只读取调用本地服务所需的访问令牌。

## Excel 客户端
### Windows 安装

在本目录打开 PowerShell：

```powershell
.\scripts\setup-local.ps1
.\.venv\Scripts\python.exe .\scripts\launch.py template
.\scripts\install-excel.ps1
```

Excel 需允许“信任对 VBA 工程对象模型的访问”才能安装宏；组织的宏运行策略仍适用。安装脚本生成 `excel/finance.xlsm`，不会覆盖已有文件。仅生成普通 `.xlsx` 时无需 Excel。

打开 `excel/finance.xlsm`，点击“登录账无忧”，在浏览器完成验证。登录后，填写控制台的 `company_数字` 和 `YYYY-MM`，点击“刷新财务数据”。可在看板中配置 DeepSeek API Key 并生成解读。账号密码不写入工作簿；会话、访问令牌和密钥都保存在本项目的 `http_sessions/` 与 `runtime/`，不进入 Git。

## 命令

```powershell
.\.venv\Scripts\python.exe .\scripts\launch.py template --output .\excel\finance-template.xlsx --overwrite
.\.venv\Scripts\python.exe .\scripts\launch.py login
.\.venv\Scripts\python.exe .\scripts\launch.py serve
.\.venv\Scripts\python.exe .\scripts\launch.py configure-deepseek
```

本机只读服务监听 `127.0.0.1:18768`。`config/finance_read_sources.json` 定义允许的财务读取接口；模板生成不会读取会计数据。工作簿刷新需要有效的账无忧登录会话。DeepSeek 使用自己的 API Key，仅发送看板汇总数值。

原 ReceiptUploader 的财务源码与入口已移除；本项目有自己的包、配置、命令、Excel 宏和运行目录。
