import datetime
import pickle
import unittest2
from base import BackendTestMixin
from conf import SCM_TESTS
from vcs.nodes import FileNode

class PickleTestCaseMixin(BackendTestMixin):

    def _get_commits(self):
        commits = [
            {
                'message': 'Initial commit',
                'author': 'Joe Doe <joe.doe@example.com>',
                'date': datetime.datetime(2010, 1, 1, 20),
                'added': [
                    FileNode('foobar', content='Foobar'),
                    FileNode('foobar2', content='Foobar II'),
                    FileNode('foo/bar/baz', content='baz here!'),
                ],
            },
            {
                'message': 'Changes...',
                'author': 'Jane Doe <jane.doe@example.com>',
                'date': datetime.datetime(2010, 1, 1, 21),
                'added': [
                    FileNode('some/new.txt', content='news...'),
                ],
                'changed': [
                    FileNode('foobar', 'Foobar I'),
                ],
                'removed': [],
            },
        ]
        return commits

    def setUp(self):
        super(PickleTestCaseMixin, self).setUp()
        self.tip = self.repo.get_changeset()

    def test_pickle_file_node(self):
        node = self.tip.get_node('foobar')
        pickled_node = pickle.dumps(node)
        loaded_node = pickle.loads(pickled_node)
        self.assertEqual(loaded_node.content, node.content)


# For each backend create test case class
for alias in SCM_TESTS:
    attrs = {
        'backend_alias': alias,
    }
    cls_name = ''.join(('%s pickle test' % alias).title().split())
    bases = (PickleTestCaseMixin, unittest2.TestCase)
    globals()[cls_name] = type(cls_name, bases, attrs)

if __name__ == '__main__':
    unittest2.main()

