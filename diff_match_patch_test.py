import unittest
import sys;

from diff_match_patch import diff_str
from diff_match_patch import diff_unicode
from diff_match_patch import match_main_unicode

def diff_str_defaults(a, b):
  return diff_str(unicode(a), unicode(b), checklines=True, cleanup_semantic=False, counts_only=False, timelimit=0)

def diff_unicode_defaults(a, b):
  return diff_unicode(a, b, checklines=True, cleanup_semantic=False, counts_only=False, timelimit=0)

class DiffMatchPatchTest(unittest.TestCase):
  def testDiffString(self):
    # Perform a trivial diff.
    # Null case.
    self.assertEquals([], diff_str_defaults("", ""))

    # Equality.
    self.assertEquals([("=", "abc")], diff_str_defaults("abc", "abc"))

    # Simple insertion.
    self.assertEquals([("=", "ab"), ("+", "123"), ("=", "c")], diff_str_defaults("abc", "ab123c"))

  def testDiffUnicode(self):
    # Perform a trivial diff.
    # Null case.
    self.assertEquals([], diff_unicode_defaults(u'', u''))

    # Equality.
    self.assertEquals([("=", u'abc')], diff_unicode_defaults(u'abc', u'abc'))

    # Simple insertion.
    self.assertEquals([("=", u'ab'), ("+", u'123'), ("=", u'c')], diff_unicode_defaults(u'abc', u'ab123c'))

  def testMatchMainUnicode(self):
    self.assertEquals(0, match_main_unicode(u'abcdef', u'abcdef', 1000))

    self.assertEquals(-1, match_main_unicode(u'', u'abcdef', 1))

    self.assertEquals(3, match_main_unicode(u'abcdef', u'', 3))

    self.assertEquals(3, match_main_unicode(u'abcdef', u'de', 3))

    self.assertEquals(3, match_main_unicode(u'abcdef', u'defy', 4))

    self.assertEquals(0, match_main_unicode(u'abcdef', u'abcdefy', 0))

if __name__ == "__main__":
  unittest.main()
