import Exceptions
import Types



def query(session,queryEngine,query):
  """
  Submit a query against the specified *queryEngine* and return the response as formatted by the queryEngine.

  The :func:`MNQuery.query` operation may be implemented by more than one type of search engine and the *queryEngine* parameter indicates which search engine is targeted. The value and form of *query* is determined by the specific query engine.

  For example, the SOLR search engine will accept many of the standard parameters of SOLR, including field restrictions and faceting.

  This method is optional for Member Nodes, but if implemented, both getQueryEngineDescription and listQueryEngines must also be implemented.


  :Version: 1.1
  :Use Cases:
    :doc:`UC02 </design/UseCases/02_uc>`, :doc:`UC16 </design/UseCases/16_uc>`
  :REST URL: ``GET /query/{queryEngine}/{query}``

  Parameters:
    session (Types.Session): |session| 
    queryEngine (string): Indicates which search engine will be used to handle the query. Supported search engines can be determined through the MNQuery.listQueryEngines API call. Transmitted as part of the URL path and must be escaped accordingly.
    query (string): The remainder of the URL is passed verbatim to the respective search engine implementation. Hence it may contain additional path elements and query elements as determined by the functionality of the search engine. The caller is reponsible for providing a '?' to indicate the start of the query string portion of the URL, as well as proper URL escaping.   Transmitted as part of the URL path and must be escaped accordingly.

  Returns:
    Types.OctetStream: The structure of the response is determined by the chosen search engine and parameters provided to it.

  Raises:
    Exceptions.InvalidToken:  (errorCode=401, detailCode=2820)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=2821)
    Exceptions.NotAuthorized:  (errorCode=401, detailCode=2822)
    Exceptions.InvalidRequest:  (errorCode=400, detailCode=2823)
    Exceptions.NotImplemented:  (errorCode=501, detailCode=2824)
    Exceptions.NotFound: The specified queryEngine does not exist (errorCode=404, detailCode=2825)

  .. include:: /apis/examples/mnquery_query.txt

  """
  return None



def getQueryEngineDescription(session,queryEngine):
  """
  Provides metadata about the query service of the specified *queryEngine*. The metadata provides a brief description of the query engine, its version, its schema version, and an optional list of fields supported by the query engine.


  :Version: 1.1
  :REST URL: ``GET /query/{queryType}``

  Parameters:
    session (Types.Session): |session| 
    queryEngine (string): Indicates which query engine for which to provide descriptive metadata. Currently supported search engines can be determined through MNQuery.listQueryEngines. Transmitted as part of the URL path and must be escaped accordingly.

  Returns:
    Types.QueryEngineDescription: A list of fields that are supported by the search index and additional metadata.

  Raises:
    Exceptions.NotImplemented:  (errorCode=501, detailCode=2810)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=2811)
    Exceptions.InvalidToken:  (errorCode=401, detailCode=2812)
    Exceptions.NotAuthorized:  (errorCode=401, detailCode=2813)
    Exceptions.NotFound: The specified queryEngine does not exist (errorCode=404, detailCode=2814)

  .. include:: /apis/examples/mnquery_getqueryenginedescription.txt

  """
  return None



def listQueryEngines(session):
  """
  Returns a list of query engines, i.e. supported values for the *queryEngine* parameter of the *getQueryEngineDescription* and *query* operations.

  The list of search engines available may be influenced by the authentication status of the request.


  :Version: 1.1
  :REST URL: ``GET /query``

  Parameters:
    session (Types.Session): |session| 

  Returns:
    Types.QueryEngineList: A list of names of queryEngines available to the user identified by *session*. 

  Raises:
    Exceptions.NotImplemented:  (errorCode=501, detailCode=2800)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=2801)
    Exceptions.InvalidToken:  (errorCode=401, detailCode=2802)
    Exceptions.NotAuthorized:  (errorCode=401, detailCode=2803)

  .. include:: /apis/examples/mnquery_listqueryengines.txt

  """
  return None

