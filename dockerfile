# 使用一个基础镜像，例如python:3.9
FROM python:3.9

# 设置工作目录
WORKDIR /app

# 复制应用程序代码到容器中
COPY . /app

# 安装应用程序依赖
RUN pip install -r requirements.txt

# 暴露应用程序端口（Flask默认端口为5000）
EXPOSE 5000

# 启动应用程序
CMD ["python", "app.py"]
