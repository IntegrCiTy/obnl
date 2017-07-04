# loads Protobuf messages (*_pb2.py)
import importlib
import os

if not __name__ == '__main__':

    PROTBUF_EXT = '_pb2.py'
    PACKAGE_SEPARATOR = '.'

    dir_path = os.path.dirname(os.path.realpath(__file__))
    only_protbuf_files = [f
                          for f in os.listdir(dir_path)
                          if os.path.isfile(os.path.join(dir_path, f)) and f.endswith(PROTBUF_EXT)
                          ]

    for opf in only_protbuf_files:
        importlib.import_module(os.path.splitext(__name__)[0] +
                                PACKAGE_SEPARATOR +
                                os.path.splitext(opf)[0])
        temp = importlib.machinery.SourceFileLoader(opf, os.path.join(dir_path, opf)).load_module()
        globals().update(temp.__dict__)
