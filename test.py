from diff_match_patch import diff_unicode
from diff_match_patch import diff_str
from diff_match_patch import match_main_unicode

#print diff_unicode(u'abc', u'ab123c', counts_only=True, cleanup_semantic=False, checklines=True)
#print diff_str('abc', 'ab123c', 3)
match_threshold = 1.0
print match_main_unicode(u'abcdef', u'de', 3, match_distance=200, match_threshold=match_threshold)
