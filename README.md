# playwright test

本测试项目依赖于pytest，可参考以下中文文档

playwright 文档
https://pypi.org/project/playwright/
https://playwright.dev/python/docs/intro/

pytest-playwright 文档
https://pypi.org/project/pytest-playwright/

本项目参考了虫师 & Yusuke Iwaki 的项目
https://github.com/defnngj/playwright-pro
https://zenn.dev/yusukeiwaki/articles/cfda648dc170e5


## 1. 安装
### 1.1 clone 或 下载
```bash
# clone 项目
git clone https://github.com/tomoyachen/playwright-test.git
```

### 1.2 安装依赖
```bash
# 本地安装 poetry
pip install poetry

# 创建虚拟环境并安装依赖 (在项目根目录执行)
poetry install

# PlayWright 安装浏览器驱动
poetry run playwright install
```


## 2. 执行测试
## 2.1 PyCharm 执行
查看虚拟环境路径
```
poetry shell
```

PyCharm 配置运行环境
Preferences -> Project Interpreter -> Show All -> + (添加) -> Existing environment -> … (浏览) -> 选择刚才创建的虚拟环境目录

PyCharm 设置 Pytest 为 默认测试运行器
Preferences -> Tools -> Python Integrated Tools -> Testing -> pytest

PyCharm 执行 测试用例
配置成功后，符合命名规则的测试类与测试方法可以在行数列快速执行

## 2.2 命令行执行
命令：

pytest 用例路径 -参数 --参数


例：
```bash
例（虚拟环境）：
pytest testcase -s -v

例（本地环境）
poetry run pytest testcase --ignore=testcase/aaa/bbb -s -v
```

常用参数：
* -s 显示打印内容
* -v 显示详细执行过程
* --browser 指定浏览器 chromium, webkit, firefox（pytest-playwright）
* --headed 有头模式执行，不传此参数就是无头浏览器执行（pytest-playwright）

pytest.ini 文件中，addopts 可以配置默认附带参数


## 3. 配置信息

业务相关配置在 `config` 目录下的 yaml 文件中
* test 方法 或 fixture 方法中，使用 env fixture 来读取配置信息
* 其他代码中，使用Tools.get_config() 来读取配置信息

Pytest 配置 在pytest.ini 文件中

## 4. 预检查【扩展】
### 4.1 pre-commit

每次git commit都会自动检查，并且会自动修复一部分格式问题，通过检查才会提交成功
* 记得 git add . 来更新被检测文件

```bash
#第一次需要手动执行如下内容
pre-commit install #安装git hook脚本
pre-commit run --all-files #运行所配置的所有规则，使其起作用
```


## 5. 其他
### 5.1 Playwrigth 录制功能
```bash
# 快速启动录制工具
python -m playwright codegen

# 指定输出 py 文件、指定 baseUrl
python -m playwright codegen --target python -o testcase/sample.py https://www.baidu.com/

# 查看帮助
python -m playwright codegen --help
```

### 5.2 已知的编码问题
mac、linux 和 windows 系统下 对 pytest.int 文件中的中文解码方式不同。
mac、linux 使用 utf-8，windows 使用 ASCII
最简单的方式就是不使用中文