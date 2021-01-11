import pickle
import os
from os import path
filename = '/print_tree_record/thisisfilename.txt'
for i in range(0, 100):
    with open("example.p", "wb") as f:
        pickle.dump(i, f)
print(path.dirname(__file__))
print(os.listdir())
# with open(os.path.join(os.path.dirname(__file__),filename)) as f:
#     print(pickle.load(f))

with open(os.path.dirname(__file__)+filename, 'w') as f:
    pickle.dump('hoge', f)

# with open(r"print_tree_record/example.p", "rb") as f:
#     print(pickle.load(f))

pickle.dump('self.utree',
    open("example-hoge.p", 'wb'))

os.path.join(os.path.dirname(__file__),filename)