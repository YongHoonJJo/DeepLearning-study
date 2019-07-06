#### Usefule code



##### Effective String Concat

```python
def method(str_lists):
  str_list = []
  for s in string_lists:
    str_list.append(s)
  return ''.join(str_list)
```

> <https://blog.leekchan.com/post/19062594439/python에서-효율적인-string-concatenation-방법>

<br>

##### change list into dict

```python
list_len = len(text_lists) 
payload = dict(zip(range(list_len), text_lists))
# { 0 : [], 1: [], ... }
```

> <https://hashcode.co.kr/questions/4786/파이썬-list에-있는-아이템을-dictionary로-변환>

<br>

