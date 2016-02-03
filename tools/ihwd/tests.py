'''
A few tests for ihwd.

These tests are visual - need to look at output to see if it makes sense.
'''

import unittest
import logging
import ihwd

class TestIhwdFuncs(unittest.TestCase):
  
  def testFormatBlock(self):
    test = """There may be multiple representations of content (e.g. metadata as
    XML, RDF, or some other format).  May need to add another parameter to specify
    the format, or perhaps rely on HTTP content negotiation for this.

    Should there be a separate identifier for different representations of the
    same content?"""

    proc = ihwd.docLoader()
    testout = proc.formatBlock(test, "  ")
    print testout

  def testRestTable(self):
    data = {'heading': ['Function', 'Parameters'],
            'data': [{'Function':'get',
                     'Parameters':'(token, pid) -> bytes'},
                     {'Function':':func:`search`',
                      'Parameters':'``(token, query) ->`` :class:`Types.ObjectList`'}, ]}
    proc = ihwd.docLoader()
    testout = proc.restTable(data)
    print "\n".join(testout)
         
  def testRestListTable(self):
    data = {'heading': ['Function', 'Parameters'],
            'widths':"10 30",
            'title': 'Some table title that is really long and should wrap to multiple lines if this thing is actually working properly.',
            'data': [{'Function':'get',
                     'Parameters':'(token, pid) -> bytes'},
                     {'Function':':func:`search`',
                      'Parameters':'``(token, query) ->`` :class:`Types.ObjectList`'}, ]}
    proc = ihwd.docLoader()
    testout = proc.restListTable(data)
    print "\n".join(testout)


if __name__ == "__main__":
  logging.basicConfig(level=logging.DEBUG)
  unittest.main()

