# 3.8-slim-buster
FROM python@sha256:9a827faf80ac75c692525c67bc6cff0e6e4a4093e73ad2674d17584b0c645af8

COPY . /workspace
WORKDIR /workspace
RUN pip install -r requirements.txt
CMD ["bash", "test.sh"]
