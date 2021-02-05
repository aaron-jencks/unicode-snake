REQUIREMENTS
============

Python 2.6
pygame 1.9 (to run the examples)

Two or more cores would be nice :)


CONTENTS
========

lib/multiproc.py        - The multiproc module; this stands alone; all other
                          files serve the examples

01_queues_pygame.py     - Queue example
02_pipes_pygame.py      - Pipe example
03_sockets_pygame.py    - Socket example

lib/modelpipe.py        - Model for Queue and Pipe examples
lib/viewpipe.py         - View for Queue and Pipe examples
lib/modelsocket.py      - Model for socket example
lib/viewsocket.py       - View for socket example
lib/spatialhash.py      - Collision detection for the examples
lib/vec2d.py            - 2D vector for the examples



DESCRIPTION
===========

Folks with multi-core CPUs will find their Python aspirations limited by the
speed and efficiency of a single core. This is due to the architecture of
Python's interpreter.

The multiprocessing module found in this distribution attempts to break this
barrier by providing a few classes to spawn child processes and let them
communicate. While these modules will work with any Python, some extra work has
been put into demonstrating their effectiveness with pygame.

This approach is aimed at hungry programs that need more than one CPU. In order
to accomplish this the program's functionality must be split into separate
processes which then collaborate by sending data via Queues, Pipes, or sockets.

It is likely useless to try this on a single-core processor because of the high
overhead of messaging. If you can make your program perform well on a single
core then you don't need the complexity of a multiprocess model.

Queues are the slowest connection. But they provide an optional throttle that
can prevent a process from flooding the connection so fast the receiver can't
keep up with it.

Pipes and sockets are a bit faster than Queues.

Of course, Pipes and Queues are confined to a single host whereas sockets can
communicate with processes over a network. One might even use multiprocessing
on multiple hosts collaborating via sockets.


HOW IT WORKS
============

Care must be taken so that the Runtime, QueueHandler, and message objects are
picklable. In addition, the main program needs to be importable (use the
common practice: if __name__ == "__main__": to shield main startup code).

The general steps to use the multiprocessing module are:

1. Subclass Runtime to implement your program logic.
2. Subclass QueueHandler to interpret your incoming messages.
3. Repeat steps 1 and 2 for as many processes as you need.
4. Construct the Runtime objects, and add their QueueHandler objects.
5. Set up the connections.
6. Construct the Master process and start it.

The procedure is only slightly different for sockets. Steps 5 and 6 are
reversed, and the server and client are started after the processes are forked.

Here's the general flow...

The Master creates the processes, starts each Runtime's run loop, and monitors
the processes. The Runtime's run loop drives the update() method, which is
intended to be overridden to provide program logic.

Each Runtime subclass handles its responsibilities and sends relevant data to
its collaborators via its named QueueHandlers.

Messages can be sent by any section of code that has visibility to a put()
method; this is a typical scoping problem. Each cycle of the run loop, the
QueueHandlers receive messages and route them to dedicated handler methods.

Though these examples provide no API support for the other features of Python's
multiprocessing module, they should be easy to integrate.

That is really all there is to it!
