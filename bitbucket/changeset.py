# -*- coding: utf-8 -*-


URLS = {
    # Issues
    'GET_CHANGESETS': 'repositories/%(username)s/%(repo_slug)s/changesets/',
    'GET_CHANGESET': 'repositories/%(username)s/%(repo_slug)s/changesets/%(node_id)s/',
    'GET_PARTICIPANT': 'repositories/%(username)s/%(repo_slug)s/commit/%(sha1)s/',
    'GET_STATISTICS': 'repositories/%(username)s/%(repo_slug)s/changesets/%(node_id)s/diffstat',
    'GET_DIFF': 'repositories/%(username)s/%(repo_slug)s/changesets/%(node_id)s/diff',
    'GET_COMMENTS': 'repositories/%(username)s/%(repo_slug)s/changesets/%(node_id)s/comments',
    'DELETE_COMMENT': 'repositories/%(username)s/%(repo_slug)s/changesets/%(node_id)s/comments/%(comment_id)s',
    'CREATE_COMMENT': 'repositories/%(username)s/%(repo_slug)s/changesets/%(node_id)s/comments/',
    'UPDATE_COMMENT': 'repositories/%(username)s/%(repo_slug)s/changesets/%(node_id)s/comments/%(comment_id)s',
    'TOGGLE_COMMENT_SPAM_FLAG': 'repositories/%(username)s/%(repo_slug)s/changesets/%(node_id)s/comments/spam/%(comment_id)s',
}


class Changeset(object):
    """ This class provide changeset-related methods to Bitbucket objects."""

    def __init__(self, bitbucket, node_id=None):
        self.bitbucket = bitbucket
        self.bitbucket.URLS.update(URLS)
        self.node_id = node_id

    @property
    def node_id(self):
        """Your repository slug name."""
        return self._node_id

    @issue_id.setter
    def node_id(self, value):
        if value:
            self._node_id = value
        elif value is None:
            self._node_id = None

    @issue_id.deleter
    def node_id(self):
        del self._node_id

    def all(self, repo_slug=None, params=None):
        """ Get changesets from one of your repositories.
            Valid parameters are:
                limit:  an integer representing how many changesets to return
                        (15 by default)
                start:  the earliest node to start from (default is the tip)
        """
        repo_slug = repo_slug or self.bitbucket.repo_slug or ''
        url = self.bitbucket.url('GET_CHANGESETS', username=self.bitbucket.username, repo_slug=repo_slug)
        return self.bitbucket.dispatch('GET', url, auth=self.bitbucket.auth, params=params)

    def get(self, node_id, repo_slug=None):
        """ Get a changeset from one of your repositories.
        """
        repo_slug = repo_slug or self.bitbucket.repo_slug or ''
        url = self.bitbucket.url('GET_CHANGESET', username=self.bitbucket.username, repo_slug=repo_slug, node_id=node_id)
        return self.bitbucket.dispatch('GET', url, auth=self.bitbucket.auth)

