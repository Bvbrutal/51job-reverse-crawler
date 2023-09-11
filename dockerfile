# 使用 Python 3.8 作为基础镜像
FROM python:3.8

# 设置工作目录
WORKDIR /app

# 复制项目文件到容器
COPY . /app

# 安装项目依赖项
RUN pip install -r requirements.txt

# 容器启动时执行的命令
CMD ["python", "app.py"]
