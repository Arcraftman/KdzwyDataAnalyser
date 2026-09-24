# DataAnalyser

独立的账无忧 Excel 财务数据看板项目。生成 22 张工作表的空白模板，在 Windows 桌面 Excel 中安装刷新宏，通过本机只读服务读取已授权账套，并可生成 DeepSeek 图表解读。项目运行不依赖 ReceiptUploader 包。

## Windows 安装

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
