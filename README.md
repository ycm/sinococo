# sinococo

Accessing SinoCoCo:

```python
import database

db = database.load_database()
```

Querying characters:
```python
db["語"]                         # [('⿰言吾', <Node '⿰' with 2 children>)]
db["語"][0][1].glyph             # '⿰'
db["語"][0][1].children          # [<Node '言' with 0 children>, <Node '吾' with 0 children>]
db["語"][0][1].children[0].glyph # '言'
```
