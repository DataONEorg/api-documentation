import Exceptions
import Types



def echoCredentials(session):
  """
  ``GET /diag/subject`` |br| Echo the credentials used to make the call. This method can be used to verify the client certificate is valid and contains the expected information.

  v2.0: This method was added to the Version 2.0 API.


  :Version: 2.0
  :REST URL: ``GET /diag/subject``

  Parameters:
    session (Types.Session): |session| 

  Returns:
    Types.SubjectInfo: The subjects and groups parsed from the supplied session information.

  Raises:
    Exceptions.NotImplemented: The service is not implemented. (errorCode=501, detailCode=4965)
    Exceptions.ServiceFailure: An internal failure prevented a successful response. (errorCode=500, detailCode=4966)
    Exceptions.InvalidToken: The supplied session information could not be parsed. (errorCode=401, detailCode=4967)

  .. include:: /apis/examples/cndiagnostic_echocredentials.txt

  """
  return None



def echoSystemMetadata(session,sysmeta):
  """
  ``POST /diag/sysmeta`` |br| Parse and echo the provided system metadata

  On successful parsing, a copy of the system metadata is returned, otherwise an exception is returned indicating an error condition.

  v2.0: This operation is new to version 2.0.


  :Version: 2.0
  :REST URL: ``POST /diag/sysmeta``

  Parameters:
    session (Types.Session): |session| 
    sysmeta (Types.SystemMetadata): A SystemMetadata object to be examined. The object is parsed and error conditions reported by an exception response. On successful parsing, the SystemMetadata object is echoed back with a HTTP 200 status. Transmitted as an UTF-8 encoded XML structure for the respective type as defined in the DataONE types schema, as a *File part* of the MIME multipart/mixed message.

  Returns:
    Types.SystemMetadata: A copy of the supplied System Metadata.

  Raises:
    Exceptions.NotImplemented:  (errorCode=501, detailCode=4970)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=4971)
    Exceptions.NotAuthorized:  (errorCode=401, detailCode=4972)
    Exceptions.InvalidToken:  (errorCode=401, detailCode=4973)
    Exceptions.InvalidRequest:  (errorCode=400, detailCode=4974)
    Exceptions.IdentifierNotUnique:  (errorCode=409, detailCode=4975)
    Exceptions.InvalidSystemMetadata:  (errorCode=400, detailCode=4976)

  .. include:: /apis/examples/cndiagnostic_echosystemmetadata.txt

  """
  return None



def echoIndexedObject(session,queryEngine,sysmeta,object):
  """
  ``POST /diag/object`` |br| Parse and echo the provided science metadata or resource map document. The response is governed by the type of object provided in the request, and on success is one or more documents that are the result of parsing for indexing.

  Since DataONE supports multiple types of query engine, the query engine to be used for parsing is specified in the request.

  The servce may terminate the POST operation if the size of the object is beyond a reasonable size.

  v2.0: This operation is new to version 2.0.


  :Version: 2.0
  :REST URL: ``POST /diag/object``

  Parameters:
    session (Types.Session): |session| 
    queryEngine (string): A valid query engine name as reported by :func:`listQueryEngines` Transmitted as a UTF-8 String as a *Param part* of the MIME multipart/mixed message.
    sysmeta (Types.SystemMetadata): A SystemMetadata object that passes the echoSystemMetadata diagnostic. Transmitted as an UTF-8 encoded XML structure for the respective type as defined in the DataONE types schema, as a *File part* of the MIME multipart/mixed message.
    object (bytes): A document (e.g. science metadata or resource map) that is to be evalauted for indexing. 

  Returns:
    Types.OctetStream: A document representing the parsed object as it would be prior to being added to a search index. For the solr query engine for example, this would be the equivalent of a *<add><doc> .. </doc> .. </add>* structure with possibly multiple documents.

  Raises:
    Exceptions.NotImplemented: The service is not implemented. (errorCode=501, detailCode=4980)
    Exceptions.ServiceFailure: An internal failure prevented a successful response. (errorCode=500, detailCode=4981)
    Exceptions.NotAuthorized: The supplied credentials are not authorized for this operation. (errorCode=401, detailCode=4982)
    Exceptions.InvalidToken: The supplied session information could not be parsed. (errorCode=401, detailCode=4983)
    Exceptions.InvalidRequest: The structure of the request is invalid. (errorCode=400, detailCode=4984)
    Exceptions.InvalidSystemMetadata: The system metadata could not be parsed. (errorCode=400, detailCode=4985)
    Exceptions.UnsupportedType: The supplied object was not of a supported type. (errorCode=400, detailCode=4986)
    Exceptions.UnsupportedMetadataType: The provided metadata format is not supported by the query engine. (errorCode=400, detailCode=4987)
    Exceptions.InsufficientResources: Insufficient resources could be allocated to support the request. The provided object may be too large to process. (errorCode=413, detailCode=4988)

  .. include:: /apis/examples/cndiagnostic_echoindexedobject.txt

  """
  return None

