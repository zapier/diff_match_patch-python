from diff_match_patch import diff_unicode
from diff_match_patch import diff_str
from diff_match_patch import match_main_unicode

#print diff_unicode(u'abc', u'ab123c', counts_only=True, cleanup_semantic=False, checklines=True)
#print diff_str('abc', 'ab123c', 3)
print match_main_unicode(u'abcdef', u'de', 3)
