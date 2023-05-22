#!/usr/bin/env python3
'''
Parameterize and patch as decorators
'''

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD
GithubOrgClient = __import__("utils").GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test
    """
    @parameterized.expand([
        ("google"), ("abc")
    ])
    @patch('client.get_json', return_value={"payload": True})
    def test_org(self, org, mock_org):
        """
        Test
        """
        test_org = GithubOrgClient(org)
        res = test_org.org
        self.assertEqual(res, mock_org.return_value)
        mock_org.assert_called_once()

    def test_public_repos_url(self):
        """
        Test
        """
        with patch.object(GithubOrgClient,
                          'org',
                          new_callable=PropertyMock) as mck:
            mck.return_value = {"repos_url": "89"}
            test_org = GithubOrgClient('holberton')
            repo_url = test_org._public_repos_url
            self.assertEqual(repo_url, mck.return_value.get('repos_url'))
            mck.assert_called_once()

    @patch('client.get_json', return_value=[{'name': 'Holberton'},
                                            {'name': '89'},
                                            {'name': 'alx'}])
    def test_public_repos(self, mock_repo):
        """
        Test
        """
        with patch.object(GithubOrgClient,
                          '_public_repos_url',
                          new_callable=PropertyMock,
                          return_value="https://api.github.com/") as mck:

            test_c = GithubOrgClient('holberton')
            test_r = test_c.public_repos()
            for idx in range(3):
                self.assertIn(mock_repo.return_value[idx]['name'], test_r)
            mock_repo.assert_called_once()
            mck.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Test
        """
        inst = GithubOrgClient('holberton')
        lic = inst.has_license(repo, license_key)
        self.assertEqual(lic, expected)


def requests_get(*args, **kwargs):
    """
    mock request
    """
    class MockResponse:
        """
        mock
        """
        def __init__(self, json_data):
            self.json_data = json_data

        def json(self):
            return self.json_data
    ur = "https://api.github.com/orgs/google"
    if args[0] == ur:
        return MockResponse(TEST_PAYLOAD[0][0])
    if args[0] == TEST_PAYLOAD[0][0]["repos_url"]:
        return MockResponse(TEST_PAYLOAD[0][1])


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    [(TEST_PAYLOAD[0][0], TEST_PAYLOAD[0][1], TEST_PAYLOAD[0][2],
      TEST_PAYLOAD[0][3])]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    test
    """
    @classmethod
    def setUpClass(cls):
        """
        set up
        """
        cls.get_patcher = patch('utils.requests.get',
                                side_effect=requests_get)
        cls.get_patcher.start()
        cls.client = GithubOrgClient('google')

    @classmethod
    def tearDownClass(cls):
        """
        Tear down
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Test
        """
        self.assertEqual(self.client.public_repos(),
                         self.expected_repos)

    def test_public_repos_with_license(self):
        """
        Test
        """
        self.assertEqual(
            self.client.public_repos(license="apache-2.0"),
            self.apache2_repos)
