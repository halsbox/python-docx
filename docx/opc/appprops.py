# encoding: utf-8

"""
The :mod:`pptx.packaging` module coheres around the concerns of reading and
writing presentations to and from a .pptx file.
"""

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)
from lxml import etree


class AppProperties(object):
    """
    Corresponds to part named ``/docProps/app.xml``, containing the app
    document properties for this document package.
    """
    def __init__(self, element):
        self._element = element

    @property
    def template(self):
        return self._element.template_text

    @template.setter
    def template(self, value):
        self._element.template_text = value

    @property
    def total_time(self):
        return self._element.total_time_text

    @total_time.setter
    def total_time(self, value):
        self._element.total_time_text = value

    @property
    def pages(self):
        return self._element.pages_text

    @pages.setter
    def pages(self, value):
        self._element.pages_text = value

    @property
    def words(self):
        return self._element.words_text

    @words.setter
    def words(self, value):
        self._element.words_text = value

    @property
    def characters(self):
        return self._element.characters_text

    @characters.setter
    def characters(self, value):
        self._element.characters_text = value

    @property
    def lines(self):
        return self._element.lines_text

    @lines.setter
    def lines(self, value):
        self._element.lines_text = value

    @property
    def company(self):
        return self._element.company_text

    @company.setter
    def company(self, value):
        self._element.company_text = value

    @property
    def app_version(self):
        return self._element.app_version_text

    @app_version.setter
    def app_version(self, value):
        self._element.app_version_text = value

    @property
    def paragraphs(self):
        return self._element.paragraphs_text

    @paragraphs.setter
    def paragraphs(self, value):
        self._element.paragraphs_text = value
