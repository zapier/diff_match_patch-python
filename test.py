import sys
import diff_match_patch

if sys.version_info[0] == 3:
    diff = diff_match_patch.diff
    diff_bytes = diff_match_patch.diff_bytes
    match_main = diff_match_patch.match_main
    match_main_bytes = diff_match_patch.match_main_bytes
else:
    diff = diff_match_patch.diff_unicode
    diff_bytes = diff_match_patch.diff_str
    match_main = diff_match_patch.match_main_unicode
    match_main_bytes = diff_match_patch.match_main_str

def test(text1, text2, diff_function):
    print(diff_function.__name__)
    print("-" * len(diff_function.__name__))

    print("<", repr(text1))
    print(">", repr(text2))
    print()

    print(diff_function(text1, text2, checklines=False, cleanup_semantic=True, as_patch=True))
    print()

    changes = diff_function(
        text1, text2,
        timelimit=15,
        checklines=False,
        cleanup_semantic=True,
        counts_only=False)

    for op, text in changes:
        print(op, repr(text))

    print("")

print(match_main(u'this is \u2192 test', u'is \u2192', 5, matchdistance=800, matchthreshold=0.25))
print(match_main_bytes(b'this is a test', b'is a', 3, matchdistance=800, matchthreshold=0.25))

test(u"this is a test", u"this program is not \u2192 a test", diff)
test(b"this is a test", b"this program is not ==> a test", diff_bytes)
