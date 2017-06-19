import test2
total_tests = 0
tests_passed = 0
attribs = dir(test2)
for attrib in attribs:
	if attrib.startswith('test_'):
		f = getattr(test2, attrib)
		if f():
			tests_passed += 1
		total_tests += 1
print 'total tests =', total_tests
print 'tests passed =', tests_passed 
