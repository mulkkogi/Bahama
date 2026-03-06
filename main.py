python
def greet(name):
 return f"Hello, {name}!"
```
4. Добавьте файл `test_sample.py` со следующим содержимым:
```python
from main import greet
def test_greet():
 assert greet("world") == "Hello, world!"
