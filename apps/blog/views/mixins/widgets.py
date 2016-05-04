#!/usr/bin/env python
# -*- coding: utf-8 -*-


class WidgetsMixin(object):
    """
    Mixin containing public context data.
    """

    @property
    def public_context_data(self):
        """
        Public context data of widgets.
        TODO:数据放Redis，定时同步mysql 多个根目录, 标签, 友情链接
        """
        # w_categories = [{'title': '编程语言', 'url': 'http://127.0.0.1:8000/blog/', 'count': 2},
        #                 {'title': 'Linux', 'url': 'http://127.0.0.1:8000/blog/', 'count': 1},
        #                 {'title': 'Hadoop生态圈', 'url': 'http://127.0.0.1:8000/blog/', 'count': 0}]

        # w_tags = [{'title': 'Python', 'url': 'http://127.0.0.1:8000/blog/', 'count': 10},
        #           {'title': 'Leetcode', 'url': 'http://127.0.0.1:8000/blog/', 'count': 22},
        #           {'title': 'Java', 'url': 'http://127.0.0.1:8000/blog/', 'count': 5},
        #           {'title': 'Nginx', 'url': 'http://127.0.0.1:8000/blog/', 'count': 3},
        #           {'title': 'Linux', 'url': 'http://127.0.0.1:8000/blog/', 'count': 14}]

        return {}