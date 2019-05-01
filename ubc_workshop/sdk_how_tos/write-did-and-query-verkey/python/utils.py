from os import environ
from pathlib import Path
from tempfile import gettempdir

PROTOCOL_VERSION = 2

def get_pool_genesis_txn_path(pool_name):
    path_temp = Path(gettempdir()).joinpath("indy")
    path = path_temp.joinpath("{}.txn".format(pool_name))
    save_pool_genesis_txn_file(path)
    return path

def pool_genesis_txn_data():
    with open('../../../genesis.txn', 'r') as myfile:
      data = myfile.read()
    return data

def save_pool_genesis_txn_file(path):
    data = pool_genesis_txn_data()
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(str(path), "w+") as f:
        f.writelines(data)
