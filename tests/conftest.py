from __future__ import absolute_import

import sys

import pytest


@pytest.yield_fixture
def in_tmpdir(tmpdir):
    with tmpdir.as_cwd():
        yield


@pytest.yield_fixture
def no_empty_path():
    # Some of our tests check things based on their pwd where things aren't
    # necessarily importable.  Let's make them not actually importable.
    empty_in_path = '' in sys.path
    if empty_in_path:  # pragma: no cover (depends on running conditions)
        # We're going to assume it is at the beginning
        sys.path.remove('')
        yield
        sys.path.insert(0, '')
    else:  # pragma: no cover (depend on running conditions)
        # noop
        yield
