## Python PutHTTPServer

Implements the PUT HTTP command allowing files to be uploaded to the host machine.

**No authenciation is performed, so do not leave this on a public internet address.**

### Installation

Ensure `$PYTHONPATH` is set correctly. This is generally under
`${HOME}/.local/lib/<python-version/site-packages` but may differ in your environment.

    $ git clone https://github.com/davemulford/pyputhttp.git
    $ cd pyputhttp
    $ python setup.py install --user

### Usage

Syntax

    $ python -m PutHTTPServer <port>

Example

    $ python -m PutHTTPServer 8080
