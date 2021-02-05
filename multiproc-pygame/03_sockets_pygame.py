import sys
sys.path.insert(0, 'lib')

import multiproc
from modelsocket import ModelRuntime, ModelQueueHandler
from viewsocket import ViewRuntime, ViewQueueHandler

def main():
    model = ModelRuntime()
    view = ViewRuntime()
    multiproc.add_queue_handler(ModelQueueHandler(model), 'view')
    multiproc.add_queue_handler(ViewQueueHandler(view), 'model')
# Model and view must set up their own sockets after the processes fork.
#    multiproc.connect_pipes(model, view, 'view', 'model')
    master = multiproc.Master(view, model, sleep=2.0)
    master.run()

if __name__ == '__main__':
    main()
