'''Script to generate the D1 API docs from the source contained in a 
spreadsheet.  This approach makes it much simpler to keep everything consistent,
although editing stuff in a spreadsheet can be a little cumbersome (OO Calc 
works much better than Excel for this).

This script was slapped together very quickly and is dependent on a certain 
layout of a source Excel 97 workbook.

Expected to be two worksheets:

:Functions: contains a list of modules (apis) and their methods

:Exceptions: contains a list of exceptions that can be raised by functions

'''

import os
import sys
import logging
import datetime
from optparse import OptionParser
import re
import xlrd
import xlwt
import textwrap
from functools import reduce

def generateTemplate(templateName):
  logging.info('Generating template %s' % templateName)


class docLoader(object):
  
  def __init__(self):
    self.sheetname = 'Sheet1'
    self.labelrow = 0
    self.startrow = 0
    self.endrow = 0
    self.data = {}
    self.colnames = {}
    self.textwrapper = textwrap.TextWrapper(width=80, drop_whitespace=True)


  def createWorksheet(self, workbook):
    '''Creates a template worksheet.
    '''
    pass
  

  def loadColIndex(self, sheet):
    '''
    Make sure the colname map is correct.
    '''
    logging.debug('Loading column indexes')
    rowvals = sheet.row_values(self.labelrow)
    ckeys = list(self.colnames.keys())
    for col in range(0,len(rowvals)):
      label = rowvals[col]
      if label in ckeys:
        self.colnames[label] = col
    logging.debug("Column index map = %s" % str(self.colnames))


  def _valToDetail(self, v):
    '''returns detail code given excel value
    '''
    try:
      v = str(int(v))
    except:
      v = str(v)
    return v


  def _getWorkingRowRange(self, sheet):
    '''
    Look for which rows contain the start and end markers
    '''
    colvals = sheet.col_values(self.colnames['Control'])
    self.startrow = colvals.index('START')
    self.endrow = colvals.index('END')      


  def _cleanParamName(self, v):
    v = v.replace("[","")
    v = v.replace("]","")
    v = v.strip()
    return v
  

  def _toTypeString(self, v):
    v = v.strip()
    if len(v) <= 0:
      return v
    if v[0] == v[0].lower():
      return v
    return ":class:`Types.%s`" % v
  
  
  def renderUseCase(self, uc):
    '''Generates a link to the specific use case.  Expects a format of UCxx
    '''
    uc = uc.lower()
    ucid = uc[2:]
    if len(ucid) > 1:
      res = ":doc:`UC%s </design/UseCases/%s_uc>`" % (ucid, ucid)
    else:
      res = None
    return res    
    
  
  def formatBlock(self, txt, indent, subsequent_indent=None, lastcr=True, doStrip=False):
    '''
    :param txt: Text to be formatted 
    :param indent: String to be used for initial indent
    :param subsequent_indent: String to be used for indenting lines after the 
      first one.  Defaults to the same as indent.
    :param lastcr: True if a trailing carriage return should be added to the 
      block.
    :param doStrip: True if white space should be stripped from the start and 
      end of each line in the source block (things work best if this isn't 
      necessary).  
    '''
    #split into multiple paras
    logging.debug(txt)
    td = txt.split("\n\n")
    res = []
    for t in td:
      res.append("%s%s" % (indent, t.rstrip()))
    return "\n\n".join(res)
 
    td = txt.split("\n\n")
    logging.debug(td)
    res = []
    self.textwrapper.initial_indent = indent
    if subsequent_indent is None:
      subsequent_indent = indent
    self.textwrapper.subsequent_indent = subsequent_indent
    for t in td:
      if doStrip:
        t = reduce(lambda x,y: "%s\n%s" % (x.strip(), y.strip()), t.split("\n"))
        twrapped = self.textwrapper.wrap(textwrap.dedent(t))
      if t.find('..') == 0:
        if subsequent_indent == indent:
          subsequent_indent = indent + " "*2
          self.textwrapper.subsequent_indent = subsequent_indent
      twrapped = self.textwrapper.wrap(t)
      twrapped = "\n".join(twrapped)
      logging.debug(twrapped)
      res.append(twrapped)
    
    if len(res) < 2:
      output = "%s" % res[0]
    else:
      output = "\n\n".join(res)
    if lastcr:
      return "%s\n" % output
    return output

  
  def loadContent(self, sheet):
    self.loadColIndex(sheet)
    self._getWorkingRowRange(sheet)
    self.data = {}
  
  
  def restTable(self, table, indent=0):
    '''Returns rows of a restructured text table.
    table = {'heading':[colname1, colname2, ...],
             'data':[{colname1: value,
                     colname2: value,
                     ... }, { }, ],
            }    
    '''
    colwidths = {}
    for head in table['heading']:
      colwidths[head] = len(head)
    for row in table['data']:
      for head in table['heading']:
        if len(row[head]) > colwidths[head]:
          colwidths[head] = len(row[head])
    #set the starting column numbers
    #colposn = [indent, ]
    #for i in xrange(1, len(table['heading'])):
    #  colposn[i] = colposn[i-1] + 2 + colwidths[table['heading'][i-1]]
    lstr = " "*indent
    heading = lstr
    for head in table['heading']:
      lstr = "%s%s" % (lstr, "="*(colwidths[head]+2) + " ")
      heading = "%s%s %s" % (heading, head, " "*(colwidths[head]+2 - len(head)))
    res = [lstr, heading, lstr]
    for row in table['data']:
      logging.debug(row)
      rstr = " "*indent
      for head in table['heading']:
        rstr = "%s%s %s" % (rstr, row[head], " "*(colwidths[head]+2 - len(row[head])))
      res.append(rstr)
    res.append(lstr)
    return res
    

  def restListTable(self, table, indent=0, withHeader=True, sortby=None):
    '''Uses the list form of REST table.  This is better for
    working with cells that have long descriptions for example.
    '''
    if sortby is not None:
      sortby = table['heading'][sortby]
      try:
        data = sorted(table['data'], key=lambda r: r[sortby] )
        table['data'] = data
      except Exception as e:
        logging.exception(e)
    sindent = " "*indent
    if withHeader:
      sstart = ".. list-table::"
      if 'title' in table:
        sstart = ".. list-table:: %s" % table['title']
      res = [self.formatBlock(sstart, 
                              sindent, " "*(indent+5), False),
                              ]
      if 'widths' in table:
        res.append("%s   :widths: %s" %  (sindent, table['widths']))
      res.append("%s   :header-rows: 1" % sindent)
      res.append('')
    else:
      res = []
    estr = "%s   * - " % sindent
    istr = "%s     - " % sindent
    if withHeader:
      res.append("%s%s" % (estr, self.formatBlock(table['heading'][0], "", " "*len(estr),False)))
      for i in range(1, len(table['heading'])):
        head = table['heading'][i]
        res.append("%s%s" % (istr, self.formatBlock(head, "", " "*len(istr), False)))
        
    for row in table['data']:
      txt = row[table['heading'][0]]
      rstr = "%s" % (self.formatBlock(txt, " "*len(estr), " "*len(estr), False))
      res.append("%s%s" % (estr, rstr[len(estr):]))
      for i in range(1, len(table['heading'])):
        head = table['heading'][i]
        rstr = "%s" % (self.formatBlock(row[head], " "*len(istr)," "*len(istr), False))
        res.append("%s%s" % (istr, rstr[len(istr):]))
    if withHeader:
      res.append('')
    return res
                 
  
  def generateText(self):
    '''Returns a dictionary with keys = module name and content = list of text rows 
    '''
    return {}


  def generatePython(self):
    '''Generates a Python source file stub.  Well, this is a place holder for 
    that if ever it eventuates.
    '''
    return {}


#===============================================================================

class ExceptionLoader(docLoader):
  
  def __init__(self):
    docLoader.__init__(self)
    self.sheetname = 'Exceptions'
    self.colnames = {'Control':0,
                     'Name':1,
                     'Description':2,
                     'Code':3,
                     'Params':4,
                     'ParamType':5,
                     'ParamDescr':6, 
                     'TODO': 7}
  
  def getNames(self):
    return [x['name'] for x in self.data['exceptions']]


  def getException(self, name):
    for exc in self.data['exceptions']:
      if name == exc['name']:
        return exc
    return None


  def getErrorCode(self, name):
    exc = self.getException(name)
    if exc is not None:
      return exc['code']
    return ''
  
  
  def newException(self, rowvals):
    res = {'name':rowvals[self.colnames['Name']],
           'description': [],
           'code': self._valToDetail(rowvals[self.colnames['Code']]),
           'params':[],
           'todo': []}
    res['description'].append(rowvals[self.colnames['Description']])
    param = {'name': rowvals[self.colnames['Params']],
             'type': rowvals[self.colnames['ParamType']],
             'descr': rowvals[self.colnames['ParamDescr']]}
    res['params'].append(param)
    v = rowvals[self.colnames['TODO']]
    if v != '':
      res['todo'].append(v)
    return res
    

  def loadContent(self, sheet):
    super(ExceptionLoader,self).loadContent(sheet)
    self.data = {'exceptions':[]}
    cexception = None
    for rowidx in range(self.startrow, self.endrow):
      rowvals = sheet.row_values(rowidx)
      logging.debug(str(rowvals))
      v = rowvals[self.colnames['Name']]
      if v != '':
        if not cexception is None:
          self.data['exceptions'].append(cexception)
        cexception = self.newException(rowvals)
      else:
        v = rowvals[self.colnames['Description']]
        if v != '':
          cexception['description'].append(v)
        v = rowvals[self.colnames['Params']]
        if v != '':
          param = {'name': v,
                   'type': rowvals[self.colnames['ParamType']],
                   'descr': rowvals[self.colnames['ParamDescr']]}
          cexception['params'].append(param)
        v = rowvals[self.colnames['TODO']]
        if v != '':
          cexception['todo'].append(v)
    self.data['exceptions'].append(cexception)
        
        
  def generateExceptionTable(self):
    def httpErrCodeURL(code):
      code = int(code)
      sc = code/100
      ssc = code % 100 + 1
      url = "http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.%d.%d" % (sc, ssc)
      return url      
    
    table = {'heading':['Exception','errorCode','Description'],
             'widths':'8 3 20',
             'title': 'Summary of exceptions defined in the DataONE APIs',
             'data': []}
    
    for exc in self.data['exceptions']:
      if int(exc['code']) < 100:
        #Local error codes
        ecstring = exc['code']
      else:
        ecstring = "`%s <%s>`_" % (exc['code'], httpErrCodeURL(exc['code']))
      row = {'Exception': ":exc:`Exceptions.%s`" % exc['name'],
             'errorCode': ecstring,
             'Description':'\n'.join(exc['description'])}
      table['data'].append(row)
    return self.restListTable(table)


  def renderException(self, exc):
    res = ['----', '']
    pnames = []
    for p in exc['params']:
      pnames.append(p['name'])
    res.append('.. exception:: %s(%s)\n' % (exc['name'], ', '.join(pnames)))
    for d in exc['description']:
      res.append(self.formatBlock(d, "   "))
    res.append('')
    res.append('   :errorCode: %s\n' % exc['code'])
    for param in exc['params']:
      res.append('   :param %s:' % self._cleanParamName(param['name']))
      res.append(self.formatBlock(param['descr'],'     '))
      res.append('')
      res.append('   :type %s: %s\n' % (self._cleanParamName(param['name']), 
                                        self._toTypeString(param['type'])))
    res.append('')      
    return res


  def generateText(self):
    res = ['..',
           '  WARNING: Content is generated automatically.  Manual edits will be lost.',
           '', '']
    #res += self.generateExceptionTable()
    for exception in self.data['exceptions']:
      res += self.renderException(exception)
    res.append('')
    return res    

  def generatePython(self):
    '''Generates a single module that implements the exceptions.
    '''
    pass
  

#===============================================================================

class FunctionLoader(docLoader):
  '''Loads a list of modules, their functions, parameters, descriptions, 
  exceptions, and todo list from an XLS worksheet.
  data = {}:
    "modules" = {}:
      module_name: [function, ]
        function = {}:
          function_name:
            "description": [text, ]
            "version": text
            "rest": text
            "todo": [text, ]
            "exceptions": [exception, ]
            "rtype": text
            "rdescr": text
            "params": [params, ]
            "usecases": [usecases, ]
        "order" = [function_name, ]
    "order" = [module_name, ]
    
    todos = [text, ]
    exception = {}
      name
      detailCode
      descr
    params = {}:
      name
      type
      descr
    usecases = [text, ]
    
  '''
  
  def __init__(self, exceptions):
    docLoader.__init__(self)
    self.exceptions = exceptions
    self.sheetname = 'Functions'
    self.colnames = {'Control':0,
                     'Module':1,
                     'Function':2,
                     'Version': 3,
                     'Tier': 4,
                     'ImplStatus': 5,
                     'UseCases':6,
                     'REST':7,
                     'Description':8,
                     'RESTDescr':9,
                     'Params':10,
                     'ParamType':11,
                     'Xmit':12,
                     'ParamDescr':13,
                     'Return':14,
                     'ReturnDescr':15,
                     'Exceptions':16,
                     'detailCode':17,
                     'ExceptDescr':11,
                     'TODO': 19}
  

  def _addFunction(self, rvals):
    '''Initializes a new function description
    '''
    f = {'description':'',
         'version': '',
         'tier': '',
         'rest': '',
         'resteg': '',
         'todo':[],
         'exceptions':[],
         'rtype':'',
         'rdescr':'',
         'params':[],
         'usecases':[]}
    f['version'] = str(rvals[self.colnames['Version']]) 
    f['tier'] = str(rvals[self.colnames['Tier']]) 
    f['rest'] = str(rvals[self.colnames['REST']])
    f['resteg'] = str(rvals[self.colnames['RESTDescr']])
    f['description'] =  [str(rvals[self.colnames['Description']]), ]
    param = {'name': rvals[self.colnames['Params']],
             'type': rvals[self.colnames['ParamType']],
             'descr': rvals[self.colnames['ParamDescr']],
             'xmit': rvals[self.colnames['Xmit']], }
    if len(param['name']) > 0:
      f['params'] = [param, ]
    f['rtype'] = rvals[self.colnames['Return']]
    f['rdescr'] = rvals[self.colnames['ReturnDescr']]
    exc = {'name': rvals[self.colnames['Exceptions']],
           'detailCode': self._valToDetail(rvals[self.colnames['detailCode']]),
           'descr': rvals[self.colnames['ExceptDescr']]}
    f['exceptions'] = [exc, ]
    v = rvals[self.colnames['TODO']]
    if v != '':
      f['todo'].append(v)
    usecases = rvals[self.colnames['UseCases']]
    usecases = usecases.split(",")
    f['usecases'] = [uc.strip() for uc in usecases]
    return f
  
  
  def _loadRow(self, cf, rv):
    v = rv[self.colnames['Description']]
    if v != '':
      cf['description'].append(v)
    v = rv[self.colnames['Params']]
    if v != '':
      param = {'name': rv[self.colnames['Params']],
               'type': rv[self.colnames['ParamType']],
               'descr': rv[self.colnames['ParamDescr']],
               'xmit': rv[self.colnames['Xmit']],}
      cf['params'].append(param)
    v = rv[self.colnames['Exceptions']]
    if v != '':
      exc = {'name': rv[self.colnames['Exceptions']],
             'detailCode': self._valToDetail(rv[self.colnames['detailCode']]),
             'descr': rv[self.colnames['ExceptDescr']]}
      cf['exceptions'].append(exc)
    v = rv[self.colnames['TODO']]
    if v != '':
      cf['todo'].append(v)
    return cf
    
  
  def loadContent(self, sheet):
    '''
    Load function definitions from spreadsheet
    '''
    super(FunctionLoader, self).loadContent(sheet)    
    cmodule = None
    cfunction = None
    self.data['modules'] = {}
    self.data['order'] = []
    #iterate from rows between START and END
    for rowidx in range(self.startrow, self.endrow):
      rowvals = sheet.row_values(rowidx)
      logging.debug("ROW[%d] = %s" % (rowidx, str(rowvals)))
      if rowvals[self.colnames['Module']] != '' and \
         rowvals[self.colnames['Module']] != cmodule:
        cmodule = rowvals[self.colnames['Module']]
        if cmodule not in self.data['order']:
          self.data['order'].append(cmodule)
      if cmodule not in self.data['modules']:
        self.data['modules'][cmodule] = {'functions':{},
                                         'order': [] }
      if rowvals[self.colnames['Function']] != '' and \
         rowvals[self.colnames['Function']] != cfunction:
        cfunction = rowvals[self.colnames['Function']]
        self.data['modules'][cmodule]['order'].append(cfunction)
      if cfunction not in self.data['modules'][cmodule]['functions']:
        self.data['modules'][cmodule]['functions'][cfunction] = self._addFunction(rowvals)
      else:
        cf = self.data['modules'][cmodule]['functions'][cfunction]
        self.data['modules'][cmodule]['functions'][cfunction] = self._loadRow(cf, rowvals)


  def _functionToText(self, mname, fname):
    ppart = {'ssl':'Transmitted as part of the SSL handshake process.',
             'path':'Transmitted as part of the URL path and must be escaped accordingly.',
             'query':'Transmitted as a URL query parameter, and so must be escaped accordingly.',
             'param':'Transmitted as a UTF-8 String as a *Param part* of the MIME multipart/mixed message.',
             'file':'Transmitted as an UTF-8 encoded XML structure for the respective type as defined in the DataONE types schema, as a *File part* of the MIME multipart/mixed message.'}
    
    res = ['', ]
    func = self.data['modules'][mname]['functions'][fname]
    pnames = []
    for param in func['params']:
      pnames.append(param['name'])
    res.append(".. function:: %s(%s) -> %s" % (fname, ",".join(pnames), func['rtype']))
    res.append("")
    for row in func['description']:
      res.append(self.formatBlock(row, "   "))
      res.append("")
    
    res.append(self.formatBlock( ":Version: %s" % func['version'], "   " ))

    if len(func['usecases']) > 0:
      ucs = []
      for uc in func['usecases']:
        ucr = self.renderUseCase(uc)
        if ucr is not None:
          ucs.append(ucr.strip())
      if len(ucs) > 0:
        res.append(self.formatBlock(":Use Cases:", "   "))
        res.append(self.formatBlock(", ".join(ucs), "     "))
    if len(func['rest']) > 0:
      nodetype = "MN"
      if mname.find('CN') == 0:
        notetype = "CN"
      #rtext = ":REST URL: %s :ref:`%s.%s`" % (nodetype, mname, fname, )
      rtext = ":REST URL: ``%s``" % func['rest']
      res.append(self.formatBlock(rtext, "   "))
    else:
      rtext = ":REST URL: N/A"
      res.append(self.formatBlock(rtext, "   "))
    for param in func['params']:
      xmittype = param['xmit'].lower()
      #res.append("   :param %s: %s\n" % (self._cleanParamName(param['name']), param['descr']))
      if param['name'] == "object":
        res.append(self.formatBlock(":param %s: %s\n" % (self._cleanParamName(param['name']), \
                                    param['descr']), "   ", "     "))
      else:        
        res.append(self.formatBlock(":param %s: %s %s\n" % (self._cleanParamName(param['name']), \
                                    param['descr'], ppart[xmittype]), "   ", "     "))
      res.append("   :type %s: %s\n" % (self._cleanParamName(param['name']), self._toTypeString(param['type'])))
    res.append(self.formatBlock(":returns: %s\n" % func['rdescr'], "   ","     "))
    res.append("   :rtype: %s\n" % self._toTypeString(func['rtype']))
    for exc in func['exceptions']:
      ecode = self.exceptions.getErrorCode(exc['name'])
      if ecode == '':
        logging.warn("module %s func %s exception %s not in list of exceptions" % (mname, fname, exc['name']))
      res.append("   :raises Exceptions.%s: ``(errorCode=%s, detailCode=%s)``" % (exc['name'], ecode, exc['detailCode']))
      #res.append("     :errorCode: %s" % ecode)
      #res.append("     :detailCode: %s" % exc['detailCode'])
      res.append('')
      if exc['descr'] != '':
        res.append(self.formatBlock(exc['descr'],"     "))
        res.append('')
    if len(func['resteg']) > 0:
      res.append('')
      #include path is relative to the generated doc location, hence the ..
      #Example file should include necessary headings etc.
      res.append('.. include:: /apis/%s' % func['resteg'])
      res.append('')
    for todo in func['todo']:
      res.append(".. TODO::")
      res.append(self.formatBlock(todo,"    "))
    res += ['','',]
    return res
  

  def generateFunctionTable(self, mname, 
                            withHeader=True, 
                            title=None, 
                            funcmodule=False,
                            sortby=None):
    '''Generates a summary of functions in the module.
    sortby is the index of hte table column to sort by
    '''
    res = {'heading':['Tier', 'Version', 'REST','Function','Parameters'],
           'widths':'3 3 10 10 30',
           'title':'',
           'data':[]}
    if title is None:
      res['title'] = 'Functions defined in :mod:`%s`' % mname
    else:
      res['title'] = title
    for fname in self.data['modules'][mname]['order']:
      func = self.data['modules'][mname]['functions'][fname]
      params = []
      for param in func['params']:
        if param['type'] == '':
          logging.warn('%s.%s param %s has no type.' % (mname, fname, param['name']))
        else:
          if param['type'][0].islower():
            params.append("``%s``" % param['name'])
          else:
            params.append(':class:`%s<Types.%s>`' % (param['name'],param['type']))
      paramstr = ", ".join(params)
      rstr = ' '
      if func['rtype'] != '':
        if func['rtype'][0].islower():
          rstr = func['rtype']
        else:
          rstr = ":class:`Types.%s`" % func['rtype']
      entry = {'Tier':'',
               'Version': func['version'],
               'REST':'n/a',
               'Function':'',
               'Parameters': '(%s) ``->`` %s' % (paramstr, rstr)}
      if funcmodule:
        entry['Function'] = ":func:`%s.%s`" % (mname, fname)
      else:
        entry['Function'] = ":func:`%s`" % fname 

      if func['rest'] != '':
        #entry['REST'] = ":ref:`%s.%s`" % (mname, fname)
        entry['REST'] = "``%s``" % func['rest']

      if func['tier'] != '':
        entry['Tier'] = func['tier']

      res['data'].append(entry)
    return self.restListTable(res, withHeader=withHeader, sortby=sortby)


  def generateFunctionExceptionMatrix(self, exceptionList):
    '''Generates a table that provides a list of module, method, exception,
    error code, and detail code for each method.
    '''
    table = {'heading': ['Module', 'Method', 'Exception', 'Code', 'Detail'],
             'width': '10 10 10 10',
             'title': 'Cross reference of method by exception detail code',
             'data':[]}
    for module in self.data['order']:
      moddata = self.data['modules'][module]
      for i in range(0, len(moddata['order'])):
        func = moddata['functions'][moddata['order'][i]]
        modval = ":mod:`%s`" % module
        methodname = ':func:`%s <%s.%s>`' % (moddata['order'][i], module, moddata['order'][i])
        for exc in func['exceptions']:
          excentry = exceptionList.getException(exc['name'])
          logging.debug("Method name = %s" % methodname)
          logging.debug("exc = %s" % str(excentry))
          entry = {'Module': modval,
                   'Method': methodname,
                   'Exception': exc['name'],
                   'Code':excentry['code'],
                   'Detail': exc['detailCode'],
                  }
          logging.debug(str(entry))
          table['data'].append(entry)
    return self.restListTable(table)
            

  def generateModuleSummaryTable(self, withHeader=True):
    '''Generates a table that provides a list of modules, functions, and their 
    descriptions.
    Module Function Description
    '''
    table = {'heading':['Module','Function','Description'],
             'widths':'6 6 30',
             'title':'Overview of APIs and the functions they implement',
             'data':[]}
    for module in self.data['order']:
      moddata = self.data['modules'][module]
      for i in range(0, len(moddata['order'])):
        func = moddata['functions'][moddata['order'][i]]
        try:
          description = "\n".join(func['description'])
        except Exception as e:
          logging.exception(e)
          logging.error(str(func['description']))
          sys.exit()
        if len(func['usecases']) > 0:
          ucs = []
          for uc in func['usecases']:
            ucr = self.renderUseCase(uc)
            if not ucr is None:
              ucs.append(ucr)
          if len(ucs) > 0:
            descr = "Appears in functional use cases: %s" % ", ".join(ucs)
            description = "%s\n\n%s" % (description, descr)
        if i == 0:
          modval = ":mod:`%s`" % module
        else:
          modval = "\\"
        entry = {'Module': modval,
                 'Function': ':func:`%s.%s`' % (module, moddata['order'][i]),
                 'Description': description,}
        table['data'].append(entry)
    return self.restListTable(table, withHeader=withHeader)


  def generateRESTSummaryTable(self):
    '''Generates tables for CN and MN that lists the method, HTTP method, 
    url template and description for each REST endpoint
    '''
    logger = logging.getLogger('generateRESTSummaryTable')
    cntable = {'heading':['Path', 'Method', 'Description'],
               'widths':'10 10 30',
               'title':'REST URLs implemented on Coordinating Nodes.',
               'data':[]}
    mntable = {'heading':['Path', 'Method', 'Description'],
               'widths':'10 10 30',
               'title':'REST URLs implemented on Member Nodes.',
               'data':[]}
    logger.info("Order: %s" % str(self.data['order']))
    for module in self.data['order']:
      logger.info("Module: %s" % module)
      if module.startswith('CN'):
        moddata = self.data['modules'][module]
        for i in range(0,len(moddata['order'])):
          logger.info("Function: %s" % moddata['order'][i])
          func = moddata['functions'][moddata['order'][i]]
          entry = {'Method':':func:`%s.%s`' % (module, moddata['order'][i]),
                   'Path': '',
                   'Description':" ".join(func['description']),
                    }
          if func['rest'] != '':
            entry['Path'] = func['rest']
            cntable['data'].append(entry)
      else:
        moddata = self.data['modules'][module]
        for i in range(0,len(moddata['order'])):
          logger.info("Function: %s" % moddata['order'][i])
          func = moddata['functions'][moddata['order'][i]]
          entry = {'Method':':func:`%s.%s`' % (module, moddata['order'][i]),
                   'Path': '',
                   'Description':" ".join(func['description']),
                    }
          if func['rest'] != '':
            entry['Path'] = func['rest']
            mntable['data'].append(entry)
    res = self.restListTable(mntable)
    res.append("")
    res += self.restListTable(cntable)
    return res
          
    

  def generateText(self):
    res = {}
    res['module_summary'] = self.generateModuleSummaryTable()
    for module in self.data['order']:
      mdata = ['..','  Warning: this file is automatically generated.  Edits will be lost','','',]
      functable = self.generateFunctionTable(module)
      mdata += self.generateFunctionTable(module)
      mdata.append('')
      mdata.append('')
      for fname in self.data['modules'][module]['order']:
        mdata += self._functionToText(module, fname)
      res[module] = mdata
      #res["%s_methods" % module] = functable
    return res


  def generateComponentSummaryText(self):
    '''Generates two documents - for CN and one for MN that
    lists the methods in a table appropriate for inserting at the top
    of the document.
    '''
    res = {}
    for module in self.data['order']:
      #component,junk = module.split("_", 1)
      component = module[0:2]
      docname = "%s_function_table" % component
      if docname in res:
        functable = self.generateFunctionTable(module, 
                                               withHeader=False, 
                                               funcmodule=True)
      else:
        res[docname] = ['..','  Warning: this file is automatically generated.  Edits will be lost','','',]
        functable = self.generateFunctionTable(module, 
                                withHeader=True, 
                                title="Methods for %s component" % component,
                                funcmodule=True)
      res[docname] += functable
    for docname in list(res.keys()):
      res[docname].append('')
      res[docname].append('')
    return res


#  def generatePlantUML(self):
#    '''Generates plantuml output that provides an overview of all methods and 
#    interfaces.
#    '''
#    res = ['@startuml /api/images/interface_overview_uml.png', ]
#    for module in self.data['order']:
#      pass
#      

#===============================================================================

def sourceModified(source, dest):
  '''Returns True if any part of source is newer than any files under 
  dest (recursive)
  '''
  def fmodTime(path):
    t = os.stat(path).st_mtime
    for root, dirs, files in os.walk(path):
      for f in files:
        ftime = os.stat(os.path.join(root,f)).st_mtime 
        if ftime > t:
          t = ftime
    return t
  
  return fmodTime(source) >= fmodTime(dest)


def generateDocs(fname, destpath):
  
  def _writeFile(filename, text):
    fdest = open(filename, 'w')
    fdest.write("\n".join(text))
    fdest.close()
  
  logging.info('Processing %s' % fname)
  book = xlrd.open_workbook(fname)
  exceptions = ExceptionLoader()
  exceptions.loadContent(book.sheet_by_name(exceptions.sheetname))
  functions = FunctionLoader(exceptions)
  functions.loadContent(book.sheet_by_name(functions.sheetname))
  
  #Render the exceptions
  logging.info("Generating exception list")
  fname = os.path.join(destpath, 'generated_exception_summary.txt')
  _writeFile(fname, exceptions.generateExceptionTable())
  
  fname = os.path.join(destpath, "generated_exceptions.txt")
  _writeFile(fname, exceptions.generateText())
  
  #Render the module, functions table
  fname = os.path.join(destpath, "generated_module_summary.txt")
  _writeFile(fname, functions.generateModuleSummaryTable())
  
  #Render the REST interface table
  fname = os.path.join(destpath, "generated_rest_summarytable.txt")
  _writeFile(fname, functions.generateRESTSummaryTable())
  
  #Render the method - exception cross reference
  fname = os.path.join(destpath, "generated_method_exception_xref.txt")
  _writeFile(fname, functions.generateFunctionExceptionMatrix(exceptions))
  
  text = functions.generateText()
  for k in list(text.keys()):
    logging.info('Generating module %s' % k)
    fname = os.path.join(destpath, "generated_%s.txt" % k)
    _writeFile(fname, text[k])
  
  text = functions.generateComponentSummaryText()
  for k in list(text.keys()):
    logging.info('Module summary doc %s' % k)
    fname = os.path.join(destpath, "generated_%s.txt" % k)
    _writeFile(fname, text[k])
 

#===============================================================================

if __name__ == '__main__':
  parser = OptionParser()
  parser.add_option("-v","--verbose",dest="loglevel",
                    help="1=DEBUG, 2=INFO, 3=WARN, 4=ERROR, 5=FATAL",
                    default=2, type="int")
  parser.add_option("-t","--template",dest="template",
                    help="Generate a template with NAME",
                    default = None, type="string")
  parser.add_option("-s","--source",dest="source",
                    help="Source workbook to process",
                    default = None, type="string")
  parser.add_option("-d","--destination", dest="destpath",
                    help="Output path where content will be written (must exist)",
                    default="generated", type="string")
  (options, args) = parser.parse_args()
  if options.loglevel < 1:
    options.loglevel = 1
  if options.loglevel > 5:
    options.loglevel = 5   
  
  logging.basicConfig(level=10*options.loglevel)
  if options.template is not None:
    generateTemplate(options.template)
  elif options.source is not None:
    generateDocs(options.source, options.destpath)
  else:
    parser.print_help()
  logging.info('Done.')
    