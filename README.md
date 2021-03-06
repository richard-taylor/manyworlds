# manyworlds

This is a project inspired by Max Tegmark's book *Our Mathematical Universe*
and Justina Robson's sci-fi series *Quantum Gravity*.

The implementation here is Python 3, but should be considered only a reference
implementation of the protocols to be used between peers.

Can a network of peers *communicate effectively* without any central control?
Can mass *cheating* be avoided, or mitigated, when no one can be trusted
absolutely?

What is *trust* online anyway? Is trust a measure of the amount of information
two parties have shared? Most people trust their family most because they have
known them a long time. People trust friends they met face-to-face because just
seeing someone is exchanging a lot of information.

Internet systems normally force you to make binary choices about trust. It is
all or nothing. That isn't how the real world works. Can we do better and
introduce degrees of trust that are automatically created and monitored for us?

## Dependencies

* Python 3.2 (or later)
* python3-tk (for the GUI)

## Tests

Run the tests with the `bin/manyworlds_test.sh` script. They should all pass
if you have all the dependencies.

## Running

You can run a manyworlds peer with the `bin/manyworlds.sh` wrapper script. Try
it with the `--help` option to see what the parameters and default values are.

By default the logs and state information are written to `$HOME/.manyworlds`.
