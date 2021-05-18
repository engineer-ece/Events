```python
def lists(lst, m=0):
    print('  ' * (m-1) + '+-' * (m>0)+ lst.title )
    for l in lst.child:
       if type(l.child) is list:
           lists(l, m + 1)
       else:
           print('  ' * m + '+-' + l.title )
```
