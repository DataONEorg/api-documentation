import Exceptions
import Types



def get(session,id):
  """
  Retrieves the object identified by *id* from the node. If the object is not present on the node, then an :exc:`Exceptions.NotFound` error is raised, regardless of whether the object exists on another node in the DataONE system.

  v2.0: The supplied identifier may be a :term:`PID` or a :term:`SID`.


  :Version: 1.0, 2.0
  :Use Cases:
    :doc:`UC01 </design/UseCases/01_uc>`, :doc:`UC16 </design/UseCases/16_uc>`, :doc:`UC09 </design/UseCases/09_uc>`
  :REST URL: ``GET /object/{id}``

  Parameters:
    session (Types.Session): |session| 
    id (Types.Identifier): Identifier of the object to be retrieved. May be either a PID or a SID, the latter acting as if called using the HEAD PID. Transmitted as part of the URL path and must be escaped accordingly.

  Returns:
    Types.OctetStream: For science metadata objects, this will be the exact byte stream of the science metadata object as it was original ingested. Note that additional object types may in the future be returned by the get method.

  Raises:
    Exceptions.NotAuthorized:  (errorCode=401, detailCode=1000)
    Exceptions.NotImplemented:  (errorCode=501, detailCode=1001)
    Exceptions.NotFound: The object specified by the identifier is not present on this (or any) CN. The response body should contain a reference to :func:`CNRead.resolve`. (errorCode=404, detailCode=1020)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=1030)
    Exceptions.InvalidToken:  (errorCode=401, detailCode=1010)

  .. include:: /apis/examples/cn_get.txt

  """
  return None



def getSystemMetadata(session,id):
  """
  Returns the :term:`system metadata` that contains DataONE specific information about the object identified by *id*. Authoritative copies of system metadata are only available from the Coordinating Nodes.

  v2.0: The supplied identifier may be a :term:`PID` or a :term:`SID` and the returned :class:`v2_0.Types.SystemMetadata` structure has changed.


  :Version: 1.0, 2.0
  :Use Cases:
    :doc:`UC36 </design/UseCases/36_uc>`, :doc:`UC37 </design/UseCases/37_uc>`, :doc:`UC16 </design/UseCases/16_uc>`
  :REST URL: ``GET /meta/{id}``

  Parameters:
    session (Types.Session): |session| 
    id (Types.Identifier): Identifier for the object of interest. May be either a PID or a SID, the latter acts as if called with the HEAD PID. Transmitted as part of the URL path and must be escaped accordingly.

  Returns:
    Types.SystemMetadata: A system metadata document describing the object.

  Raises:
    Exceptions.InvalidToken:  (errorCode=401, detailCode=1050)
    Exceptions.NotImplemented:  (errorCode=501, detailCode=1041)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=1090)
    Exceptions.NotAuthorized: The principal identified by token does not have READ permission on the object. (errorCode=401, detailCode=1040)
    Exceptions.NotFound: There is no object identified by *pid* and so no system metadata can be returned. (errorCode=404, detailCode=1060)

  .. include:: /apis/examples/cn_getSystemMetadata.txt

  """
  return None



def describe(session,id):
  """
  This method provides a lighter weight mechanism than :func:`CNRead.getSystemMetadata` for a client to determine basic properties of the referenced object. The response should indicate properties that are typically returned in a HTTP HEAD request: the date late modified, the size of the object, the type of the object (the :attr:`SystemMetadata.formatId`).

  The principal indicated by *token* must have read privileges on the object, otherwise :exc:`Exceptions.NotAuthorized` is raised.

  If the object does not exist on the node servicing the request, then :exc:`Exceptions.NotFound` must be raised even if the object exists on another node in the DataONE system.

  Note that this method is likely to be called frequently and so efficiency should be taken into consideration during implementation.

  v2.0: The supplied identifier may be a :term:`PID` or a :term:`SID`.


  :Version: 1.0, 2.0
  :Use Cases:
    :doc:`UC16 </design/UseCases/16_uc>`
  :REST URL: ``HEAD /object/{id}``

  Parameters:
    session (Types.Session): |session| 
    id (Types.Identifier): Identifier for the object in question. May be either a PID or a SID, the latter acting as if called with the HEAD PID. Transmitted as part of the URL path and must be escaped accordingly.

  Returns:
    Types.DescribeResponse: A set of values providing a basic description of the object.

  Raises:
    Exceptions.NotImplemented:  (errorCode=501, detailCode=4930)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=4931)
    Exceptions.InvalidToken:  (errorCode=401, detailCode=4932)
    Exceptions.NotFound:  (errorCode=404, detailCode=4933)
    Exceptions.NotAuthorized:  (errorCode=401, detailCode=4934)

  .. include:: /apis/examples/describe.txt

  """
  return None



def resolve(session,id):
  """
  Returns a list of nodes (MNs or CNs) known to hold copies of the object identified by *id*. The object resolution process is intended to provide a simple mechanism for a client to discover from which node(s) a particular object may be retrieved. Details about method interfaces (i.e. REST URLs) exposed by a particular node can be determined by examining the response from the *node* collection. For convenience, the :func:`MNRead.get` URL is included in the response as is the base URL of the node REST services.

  Note also that the same functionality as *resolve()* can be implemented by retrieving a copy of the system metadata for the object and utilizing the node registry to discover the base URL from which the client can construct the *get()* URL. Resolve is provided for efficiency since the response size is much smaller.

  Resolve will return a HTTP status of 303 (see other) on success. The HTTP header "Location" MUST be set, and it's value SHOULD be the full get() URL for retrieving the object from the first location in the resolve response.

  v2.0: The supplied identifier may be a :term:`PID` or a :term:`SID`. If the identifier is a SID, then resolution is for the latest version of an object (i.e. the head of the obsolescence chain).


  :Version: 1.0, 2.0
  :Use Cases:
    :doc:`UC36 </design/UseCases/36_uc>`, :doc:`UC16 </design/UseCases/16_uc>`
  :REST URL: ``GET /resolve/{id}``

  Parameters:
    session (Types.Session): |session| 
    id (Types.Identifier): Identifier being resolved. May be either a PID or a SID, the latter acting as if called with the HEAD PID. Transmitted as part of the URL path and must be escaped accordingly.

  Returns:
    Types.ObjectLocationList: A list of nodes known to contain copies of the target object, plus the URLs known to resolve to the node get methods.

  Raises:
    Exceptions.InvalidToken:  (errorCode=401, detailCode=4130)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=4150)
    Exceptions.NotAuthorized:  (errorCode=401, detailCode=4120)
    Exceptions.NotFound: There is no object identified by the given identifier (errorCode=404, detailCode=4140)
    Exceptions.NotImplemented:  (errorCode=501, detailCode=4131)

  .. include:: /apis/examples/resolve.txt

  """
  return None



def getChecksum(session,pid):
  """
  Returns the checksum for the specified object as reported in the system metadata.

  Note that the signature of this method differs from :func:`MNRead.getChecksum` as that method takes an optional algorithm parameter.


  :Version: 1.0, (2.0)
  :Use Cases:
    :doc:`UC09 </design/UseCases/09_uc>`
  :REST URL: ``GET /checksum/{pid}``

  Parameters:
    session (Types.Session): |session| 
    pid (Types.Identifier): Identifier of the object for which checksum is being requested Transmitted as part of the URL path and must be escaped accordingly.

  Returns:
    Types.Checksum: The checksum of the specified object

  Raises:
    Exceptions.NotImplemented:  (errorCode=501, detailCode=1402)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=1410)
    Exceptions.NotFound:  (errorCode=404, detailCode=1420)
    Exceptions.NotAuthorized:  (errorCode=401, detailCode=1400)
    Exceptions.InvalidToken:  (errorCode=401, detailCode=1430)

  .. include:: /apis/examples/cnread_getchecksum.txt

  """
  return None



def listObjects(session,fromDate=None,toDate=None,formatId=None,identifier=None,start=0,count=1000,nodeId=None):
  """
  Retrieve the list of objects present on the CN that match the calling parameters. At a minimum, this method should be able to return a list of objects that match::

    fromDate < SystemMetadata.dateSysMetadataModified

  but is expected to also support date range (by also specifying *toDate*), and should also support slicing of the matching set of records by indicating the starting *index* of the response (where 0 is the index of the first item) and the *count* of elements to be returned.

  Note that date time precision is limited to one millisecond. If no timezone information is provided, the UTC will be assumed.

  Note that date time precision is limited to one millisecond. If no timezone information is provided, the UTC will be assumed.

  V2.0: Added filter on authoritativeMemberNode value.


  :Version: 1.0, (2.0)
  :Use Cases:
    :doc:`UC06 </design/UseCases/06_uc>`, :doc:`UC16 </design/UseCases/16_uc>`
  :REST URL: ``GET /object[?fromDate={fromDate}&toDate={toDate}&identifier={identifier}&formatId={formatId}&nodeId={nodeId}&start={start}&count={count}]``

  Parameters:
    session (Types.Session): |session| 
    fromDate (Types.DateTime): Entries with :attr:`SystemMetadata.dateSysMetadataModified` greater than or equal to (>=) *fromDate* must be returned.  Transmitted as a URL query parameter, and so must be escaped accordingly.
    toDate (Types.DateTime): Entries with :attr:`SystemMetadata.dateSysMetadataModified` less than (<) *toDate* must be returned. Transmitted as a URL query parameter, and so must be escaped accordingly.
    formatId (Types.ObjectFormatIdentifier): Restrict results to the specified object format. Transmitted as a URL query parameter, and so must be escaped accordingly.
    identifier (Types.Identifier): Restrict results to the specified identifier. May be either a PID or a SID. If the latter, will return results for each PID in the series. Transmitted as a URL query parameter, and so must be escaped accordingly.
    start (integer): The zero-based index of the first value, relative to the first record of the resultset that matches the parameters. Transmitted as a URL query parameter, and so must be escaped accordingly.
    count (integer): The maximum number of entries that should be returned in the response. The Member Node may return fewer and the caller should check the *total* in the response to determine if further pages may be retrieved. Transmitted as a URL query parameter, and so must be escaped accordingly.
    nodeId (Types.NodeReference): Restrict results to those with authoritativeMemberNode equal to nodeId. Transmitted as a URL query parameter, and so must be escaped accordingly.

  Returns:
    Types.ObjectList: The list of PIDs that match the query criteria. If none match, an empty list is returned.

  Raises:
    Exceptions.NotAuthorized:  (errorCode=401, detailCode=1520)
    Exceptions.InvalidRequest:  (errorCode=400, detailCode=1540)
    Exceptions.NotImplemented: Raised if some functionality requested is not implemented. In the case of an optional request parameter not being supported, the errorCode should be 400. If the requested format (through HTTP Accept headers) is not supported, then the standard HTTP 406 error code should be returned. (errorCode=501, detailCode=1560)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=1580)
    Exceptions.InvalidToken:  (errorCode=401, detailCode=1530)

  .. include:: /apis/examples/cnread_listobjects.txt

  """
  return None



def search(session,queryType,query):
  """
  Search the metadata catalog and return identifiers of metadata records that match the criteria.

  Search may be implemented by more than one type of search engine. The queryType parameter indicates which search engine should be targeted. The value and form of *query* is determined by the search engine.

  Currently supported search engines include: "solr"


  :Version: 1.0, (2.0)
  :Use Cases:
    :doc:`UC02 </design/UseCases/02_uc>`, :doc:`UC16 </design/UseCases/16_uc>`
  :REST URL: ``GET /search/{queryType}/{query}``

  Parameters:
    session (Types.Session): |session| 
    queryType (string): Indicates which search engine will be used to handle the query. Currently supported search engines include: "SOLR". Transmitted as part of the URL path and must be escaped accordingly.
    query (string): The remainder of the URL is passed verbatim to the respective search engine implementation. Hence it may contain additional path elements and query elements as determined by the functionality of the search engine. The caller is reponsible for providing a '?' to indicate the start of the query string portion of the URL, as well as proper URL escaping.   Transmitted as part of the URL path and must be escaped accordingly.

  Returns:
    Types.ObjectList: A list of objects that match the specified search criteria

  Raises:
    Exceptions.InvalidToken:  (errorCode=401, detailCode=4290)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=4310)
    Exceptions.NotAuthorized:  (errorCode=401, detailCode=4280)
    Exceptions.InvalidRequest:  (errorCode=400, detailCode=4300)
    Exceptions.NotImplemented:  (errorCode=501, detailCode=4281)

  .. include:: /apis/examples/cnread_search.txt

  """
  return None



def query(session,queryEngine,query):
  """
  Submit a query against the specified *queryEngine* and return the response as formatted by the queryEngine.

  The *query()* operation may be implemented by more than one type of search engine and the *queryEngine* parameter indicates which search engine is targeted. The value and form of *query* is determined by the specific query engine.

  For example, the solr search engine will accept many of the standard parameters of solr, including field restrictions and faceting.

  v1.1: This method was added.


  :Version: 1.1, (2.0)
  :Use Cases:
    :doc:`UC02 </design/UseCases/02_uc>`, :doc:`UC16 </design/UseCases/16_uc>`
  :REST URL: ``GET /query/{queryEngine}/{query}``

  Parameters:
    session (Types.Session): |session| 
    queryEngine (string): Indicates which search engine will be used to handle the query. Supported search engines can be determined through the CNRead.listQueryEngines API call. Transmitted as part of the URL path and must be escaped accordingly.
    query (string): The remainder of the URL is passed verbatim to the respective search engine implementation. Hence it may contain additional path elements and query elements as determined by the functionality of the search engine. The caller is reponsible for providing a '?' to indicate the start of the query string portion of the URL, as well as proper URL escaping.   Transmitted as part of the URL path and must be escaped accordingly.

  Returns:
    Types.OctetStream: The structure of the response is determined by the chosen search engine and parameters provided to it.

  Raises:
    Exceptions.InvalidToken:  (errorCode=401, detailCode=4320)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=4321)
    Exceptions.NotAuthorized:  (errorCode=401, detailCode=4322)
    Exceptions.InvalidRequest:  (errorCode=400, detailCode=4323)
    Exceptions.NotImplemented:  (errorCode=501, detailCode=4324)
    Exceptions.NotFound: The specified queryEngine does not exist (errorCode=404, detailCode=4325)

  .. include:: /apis/examples/cnread_query.txt

  """
  return None



def getQueryEngineDescription(session,queryEngine):
  """
  Provides metadata about the query service of the specified *queryEngine*. The metadata provides a brief description of the query engine, its version, its schema version, and an optional list of fields supported by the query engine.

  v1.1: This method was added.


  :Version: 1.1, (2.0)
  :REST URL: ``GET /query/{queryType}``

  Parameters:
    session (Types.Session): |session| 
    queryEngine (string): Indicates which query engine for which to provide descriptive metadata. Currently supported search engines can be determined through CNRead.listQueryEngines. Transmitted as part of the URL path and must be escaped accordingly.

  Returns:
    Types.QueryEngineDescription: A list of fields that are supported by the search index and additional metadata.

  Raises:
    Exceptions.NotImplemented:  (errorCode=501, detailCode=4410)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=4411)
    Exceptions.InvalidToken:  (errorCode=401, detailCode=4412)
    Exceptions.NotAuthorized:  (errorCode=401, detailCode=4413)
    Exceptions.NotFound: The specified queryEngine does not exist (errorCode=404, detailCode=4414)

  .. include:: /apis/examples/cnread_getqueryenginedescription.txt

  """
  return None



def listQueryEngines(session):
  """
  Returns a list of query engines, i.e. supported values for the *queryEngine* parameter of the *getQueryEngineDescription* and *query* operations.

  The list of search engines available may be influenced by the authentication status of the request.

  v1.1: This method was added.


  :Version: 1.1, (2.0)
  :REST URL: ``GET /query``

  Parameters:
    session (Types.Session): |session| 

  Returns:
    Types.QueryEngineList: A list of names of queryEngines available to the user identified by *session*. 

  Raises:
    Exceptions.NotImplemented:  (errorCode=501, detailCode=4420)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=4421)
    Exceptions.InvalidToken:  (errorCode=401, detailCode=4422)
    Exceptions.NotAuthorized:  (errorCode=401, detailCode=4423)

  .. include:: /apis/examples/cnread_listqueryengines.txt

  """
  return None



def synchronize(session,pid):
  """
  Indicates to the CN that a new or existing object identified by PID requires synchronization. Note that this operation is asynchronous, a successful return indicates that the synchronization task was successfully queued.

  This method may be called by any Member Node for new content or the authoritative Member Node for updates to existing content.

  The CN will schedule the synchronization task which will then be processed in the same way as content changes identified through the listObjects polling mechanism.

  v2.0: This method was added to the Version 2.0 API.


  :Version: 2.0
  :REST URL: ``POST /synchronize``

  Parameters:
    session (Types.Session): |session| 
    pid (Types.Identifier):  Transmitted as a UTF-8 String as a *Param part* of the MIME multipart/mixed message.

  Returns:
    boolean: True if the synchronization request was successfully queued, otherwise False

  Raises:
    Exceptions.NotImplemented:  (errorCode=501, detailCode=4960)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=4961)
    Exceptions.NotAuthorized:  (errorCode=401, detailCode=4962)
    Exceptions.InvalidToken:  (errorCode=401, detailCode=4963)

  .. include:: /apis/examples/cnread_synchronize.txt

  """
  return None

