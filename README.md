# OpenCV 学习环境

## 整体架构

```
F:\OpenCV\                    ← 你的代码和项目文件放这里（你管）
F:\anaconda\envs\opencv\      ← Python 3.11 + OpenCV + NumPy（conda 管，隔离环境）
F:\python\                    ← 系统 Python 3.14（不动，保持原样）
```

两个 Python 互不影响。

---

## 环境信息

| 项目 | 详情 |
|------|------|
| Conda 环境名 | `opencv` |
| Python 版本 | 3.11.15 |
| OpenCV 版本 | 5.0.0 |
| NumPy 版本 | 2.4.6 |
| 环境路径 | `F:\anaconda\envs\opencv\` |
| 代码目录 | `F:\OpenCV\` |

---

## 方式一：VS Code（推荐日常使用）

### 首次配置（只需做一次，已完成）

1. Python 扩展 ✅ 已安装
2. 解释器配置 ✅ 已写 `F:\OpenCV\.vscode\settings.json`，指向 `opencv` 环境

### 第一次按 F5 时

会弹出两次选择框，按以下选择即可（只选一次，之后 VS Code 会记住）：

| 弹窗 | 选择 |
|------|------|
| "选择调试器" | **Python Debugger** |
| "选择调试配置" | **Python 文件** |

### 每次使用流程

1. 打开 VS Code
2. `文件` → `打开文件夹` → 选 `F:\OpenCV`
3. 确认右下角显示的是 `Python 3.11.15 ('opencv')`（通常自动选中）
4. 写 `.py` 代码，按 `F5` 运行

> 如果右下角解释器不对：`Ctrl+Shift+P` → `Python: Select Interpreter` → 选 `opencv` 环境

---

## 方式二：Anaconda Prompt（命令行）

### 每次使用流程

1. 开始菜单搜 **Anaconda Prompt**，打开
2. 每次打开后执行以下三步：

```
conda activate opencv
cd /d F:\OpenCV
python demo.py
```

3. 用完后：

```
conda deactivate
```

### 直接指定 OpenCV 环境运行

如果当前终端里的 `python` 不是 OpenCV 环境，也可以不用先激活环境，直接指定完整路径运行：

```powershell
& "F:\anaconda\envs\opencv\python.exe" .\demo.py
```

这样会强制使用 `F:\anaconda\envs\opencv\python.exe` 来运行当前目录下的 `demo.py`，生成结果仍然保存在 `F:\OpenCV\demo_output.jpg`。

---

## 验证环境是否正常

在 VS Code 终端或 Anaconda Prompt 中运行：

```
python -c "import cv2; print(cv2.__version__)"
```

输出 `5.0.0` 表示正常。

---

## 快速参考

| 命令 | 作用 |
|------|------|
| `conda activate opencv` | 激活 OpenCV 环境 |
| `conda deactivate` | 退出当前环境 |
| `conda list` | 查看已安装的包 |
| `conda info --envs` | 查看所有环境 |
| `python demo.py` | 运行代码 |
| `& "F:\anaconda\envs\opencv\python.exe" .\demo.py` | 直接用 OpenCV 环境运行代码 |

---

## 注意事项

- 系统 Python 3.14 不受任何影响，原有项目照常运行
- 所有 OpenCV 项目代码建议存放在 `F:\OpenCV\` 下
- 不要在 VS Code 和 Anaconda Prompt 之外随便 `pip install`，否则可能装到系统 Python 里
