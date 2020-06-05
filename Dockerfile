FROM python:3.8-slim
RUN pip install --upgrade pip
RUN python3 -m pip install grpcio
RUN python3 -m pip install grpcio-tools
RUN mkdir /app
ARG project_dir=/app
COPY *.py $project_dir/
WORKDIR $project_dir
CMD ["python3", "echoServer.py"]
EXPOSE 50051
