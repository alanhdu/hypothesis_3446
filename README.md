# Reproducer for https://github.com/HypothesisWorks/hypothesis/issues/3446

Execute

```python
docker build -t foo . && docker run -it foo
```
