import sys;
from diff_match_patch import diff_str
from diff_match_patch import diff_unicode

print diff_str("abc", "ab123c", counts_only=False, cleanup_semantic=False, checklines=False)
print diff_unicode(u'abc', u'ab123c', counts_only=False, cleanup_semantic=False, checklines=False)
