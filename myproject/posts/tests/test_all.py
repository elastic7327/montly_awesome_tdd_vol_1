#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.test import TestCase
from posts.models import Post
from django.urls import reverse

import pytest

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
class TestPostsClass(TestCase):

    def test_smoke_test(self):
        # self.assertEqual(1, 2, 'Its Not Suppose to Equal!')
        assert 1 is 1, 'Shold be Equeal!!!'

    def test_post_model_create(self):
        Post.objects.create(
            title='Hello_Unit-test',
            body='ASDSADSADSADKJNASDJLASDKJA???ASDLKASDJKAJSDKDj')
        assert 1 == Post.objects.count(), 'Should be Equal!'

    def test_posts_get_view_request(self):
        url = reverse('post-lists')
        req = self.client.get(url, format='json')
        assert req.status_code == 200, f'{req.content}'
