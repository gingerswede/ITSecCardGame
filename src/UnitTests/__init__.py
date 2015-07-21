'''
copy of accepted answer on http://stackoverflow.com/questions/1732438/how-to-run-all-python-unit-tests-in-a-directory
'''
import unittest

testmodules = ['TestCard', 'TestDeck', 'TestPlayer']

suite = unittest.TestSuite()


for t in testmodules:
    try:
        mod = __import__(t, globals(), locals(), ['suite'])
        suitefn = getattr(mod, 'suite')
        suite.addTest(suitefn())
        
    except(ImportError, AttributeError):
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName(t))
        
unittest.TextTestRunner(verbosity=2).run(suite)