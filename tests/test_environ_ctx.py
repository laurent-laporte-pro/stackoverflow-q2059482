# coding: utf-8
import os

from demo.environ_ctx import modified_environ


def setup_method(test_method):
    os.environ.pop('MODIFIED_ENVIRON', None)


def teardown_method(test_method):
    os.environ.pop('MODIFIED_ENVIRON', None)


def test_modified_environ__no_args():
    with modified_environ():
        pass


def test_modified_environ__inserted():
    with modified_environ(MODIFIED_ENVIRON="inserted"):
        assert os.environ['MODIFIED_ENVIRON'] == "inserted"
    assert 'MODIFIED_ENVIRON' not in os.environ


def test_modified_environ__updated():
    os.environ['MODIFIED_ENVIRON'] = "value"
    with modified_environ(MODIFIED_ENVIRON="updated"):
        assert os.environ['MODIFIED_ENVIRON'] == "updated"
    assert os.environ['MODIFIED_ENVIRON'] == "value"


def test_modified_environ__deleted():
    os.environ['MODIFIED_ENVIRON'] = "value"
    with modified_environ('MODIFIED_ENVIRON'):
        assert 'MODIFIED_ENVIRON' not in os.environ
    assert os.environ['MODIFIED_ENVIRON'] == "value"


def test_modified_environ__deleted_missing():
    with modified_environ('MODIFIED_ENVIRON'):
        assert 'MODIFIED_ENVIRON' not in os.environ
    assert os.environ['MODIFIED_ENVIRON'] == "value"
