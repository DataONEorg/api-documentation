import Exceptions
import Types



def get(session,id):
  """
  Retrieve an object identified by *id* from the node. Supports both PIDs and SIDs. SID will return HEAD PID.

  The response MUST contain the bytes of the indicated object, and the checksum of the bytes retrieved SHOULD match the :attr:`SystemMetadata.checksum` recorded in the  :class:`Types.SystemMetadata` when calling with PID.

  If the object does not exist on the node servicing the request, then :exc:`Exceptions.NotFound` must be raised even if the object exists on another node in the DataONE system.

  Also implmented by Coordinating Nodes as :func:`CNRead.get`.


  :Version: 1.0
  :Use Cases:
    :doc:`UC01 </design/UseCases/01_uc>`, :doc:`UC06 </design/UseCases/06_uc>`, :doc:`UC16 </design/UseCases/16_uc>`
  :REST URL: ``GET /object/{id}``

  Parameters:
    session (Types.Session): |session| 
    id (Types.Identifier): The identifier for the object to be retrieved. May be a PID or a SID. Transmitted as part of the URL path and must be escaped accordingly.

  Returns:
    Types.OctetStream: Bytes of the specified object. 

  Raises:
    Exceptions.NotAuthorized: The provided identity does not have READ permission on the object. (errorCode=401, detailCode=1000)
    Exceptions.NotFound: The object specified by *id* does not exist at this node. The description should include a reference to the resolve method. (errorCode=404, detailCode=1020)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=1030)
    Exceptions.InvalidToken:  (errorCode=401, detailCode=1010)
    Exceptions.NotImplemented:  (errorCode=501, detailCode=1001)
    Exceptions.InsufficientResources: The node is unable to service the request due to insufficient resources such as CPU, memory, or bandwidth being over utilized. (errorCode=413, detailCode=1002)

  .. include:: /apis/examples/get.txt

  """
  return None



def getSystemMetadata(session,id):
  """
  Describes the object identified by *id* by returning the associated system metadata object.

  If the object does not exist on the node servicing the request, then :exc:`Exceptions.NotFound` MUST be raised even if the object exists on another node in the DataONE system.


  :Version: 1.0
  :Use Cases:
    :doc:`UC06 </design/UseCases/06_uc>`, :doc:`UC37 </design/UseCases/37_uc>`, :doc:`UC16 </design/UseCases/16_uc>`
  :REST URL: ``GET /meta/{id}``

  Parameters:
    session (Types.Session): |session| 
    id (Types.Identifier): Identifier for the science data or science metedata object of interest. May be either a PID or a SID. Transmitted as part of the URL path and must be escaped accordingly.

  Returns:
    Types.SystemMetadata: System metadata object describing the object.

  Raises:
    Exceptions.NotAuthorized:  (errorCode=401, detailCode=1040)
    Exceptions.NotImplemented:  (errorCode=501, detailCode=1041)
    Exceptions.NotFound: There is no data or science metadata identified by the given *id* on the node where the request was serviced. The error message should provide a hint to use the :func:`CNRead.resolve` mechanism. (errorCode=404, detailCode=1060)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=1090)
    Exceptions.InvalidToken:  (errorCode=401, detailCode=1050)

  .. include:: /apis/examples/getSystemMetadata.txt

  """
  return None



def describe(session,id):
  """
  This method provides a lighter weight mechanism than :func:`MNRead.getSystemMetadata` for a client to determine basic properties of the referenced object. The response should indicate properties that are typically returned in a HTTP HEAD request: the date late modified, the size of the object, the type of the object (the :attr:`SystemMetadata.formatId`).

  The principal indicated by *token* must have read privileges on the object, otherwise :exc:`Exceptions.NotAuthorized` is raised.

  If the object does not exist on the node servicing the request, then :exc:`Exceptions.NotFound` must be raised even if the object exists on another node in the DataONE system.

  Note that this method is likely to be called frequently and so efficiency should be taken into consideration during implementation.


  :Version: 1.0
  :Use Cases:
    :doc:`UC16 </design/UseCases/16_uc>`
  :REST URL: ``HEAD /object/{id}``

  Parameters:
    session (Types.Session): |session| 
    id (Types.Identifier): Identifier for the object in question. May be either a PID or a SID.  Transmitted as part of the URL path and must be escaped accordingly.

  Returns:
    Types.DescribeResponse: A set of values providing a basic description of the object.

  Raises:
    Exceptions.NotAuthorized:  (errorCode=401, detailCode=1360)
    Exceptions.NotFound:  (errorCode=404, detailCode=1380)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=1390)
    Exceptions.InvalidToken:  (errorCode=401, detailCode=1370)
    Exceptions.NotImplemented:  (errorCode=501, detailCode=1361)

  .. include:: /apis/examples/describe.txt

  """
  return None



def getChecksum(session,pid,checksumAlgorithm=None):
  """
  Returns a :class:`Types.Checksum` for the specified object using an accepted hashing algorithm. The result is used to determine if two instances referenced by a PID are identical, hence it is necessary that MNs can ensure that the returned checksum is valid for the referenced object either by computing it on the fly or by using a cached value that is certain to be correct.


  :Version: 1.0
  :REST URL: ``GET /checksum/{pid}[?checksumAlgorithm={checksumAlgorithm}]``

  Parameters:
    session (Types.Session): |session| 
    pid (Types.Identifier): The identifier of the object the operation is being performed on. Transmitted as part of the URL path and must be escaped accordingly.
    checksumAlgorithm (string): The name of an algorithm that will be used to compute a checksum of the bytes of the object. This value is drawn from a DataONE controlled list of values as indicted in the :class:`Types.SystemMetadata`. If not specified, then the system wide default checksum algorithm should be used. Transmitted as a URL query parameter, and so must be escaped accordingly.

  Returns:
    Types.Checksum: The checksum value originally computed for the specified object.

  Raises:
    Exceptions.NotAuthorized:  (errorCode=401, detailCode=1400)
    Exceptions.NotFound:  (errorCode=404, detailCode=1420)
    Exceptions.InvalidRequest: A supplied parameter was invalid, most likely an unsupported checksum algorithm was specified, in which case the error message should include an enumeration of supported checksum algorithms. (errorCode=400, detailCode=1402)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=1410)
    Exceptions.InvalidToken:  (errorCode=401, detailCode=1430)
    Exceptions.NotImplemented:  (errorCode=501, detailCode=1401)

  .. include:: /apis/examples/mnread_getchecksum.txt

  """
  return None



def listObjects(session,fromDate=None,toDate=None,formatId=None,identifier=None,replicaStatus=None,start=0,count=1000):
  """
  Retrieve the list of objects present on the MN that match the calling parameters. This method is required to support the process of :term:`Member Node synchronization`. At a minimum, this method MUST be able to return a list of objects that match::

    fromDate < SystemMetadata.dateSysMetadataModified

  but is expected to also support date range (by also specifying *toDate*), and should also support slicing of the matching set of records by indicating the starting *index* of the response (where 0 is the index of the first item) and the *count* of elements to be returned.

  Note that date time precision is limited to one millisecond. If no timezone information is provided, the UTC will be assumed.

  Note that date time precision is limited to one millisecond. If no timezone information is provided, the UTC will be assumed.


  :Version: 1.0
  :Use Cases:
    :doc:`UC06 </design/UseCases/06_uc>`, :doc:`UC16 </design/UseCases/16_uc>`
  :REST URL: ``GET /object[?fromDate={fromDate}&toDate={toDate}&identifier={identifier}&formatId={formatId}&replicaStatus={replicaStatus} &start={start}&count={count}]``

  Parameters:
    session (Types.Session): |session| 
    fromDate (Types.DateTime): Entries with :attr:`SystemMetadata.dateSysMetadataModified` greater than or equal to (>=) *fromDate* must be returned.  Transmitted as a URL query parameter, and so must be escaped accordingly.
    toDate (Types.DateTime): Entries with :attr:`SystemMetadata.dateSysMetadataModified` less than (<) *toDate* must be returned. Transmitted as a URL query parameter, and so must be escaped accordingly.
    formatId (Types.ObjectFormatIdentifier): Restrict results to the specified object format identifier. Transmitted as a URL query parameter, and so must be escaped accordingly.
    identifier (Types.Identifier): Restrict results to the specified identifier. May be a PID or a SID. In the case of the latter, returns a listing of all PIDs that share the given SID. Transmitted as a URL query parameter, and so must be escaped accordingly.
    replicaStatus (boolean): Indicates if replicated objects should be returned in the list (i.e. any entries present in the :attr:`SystemMetadata.replica`, objects that have been replicated to this node). If ``false``, then no objects that have been replicated should be returned. If ``true``, then any objects can be returned, regardless of replication status. The default value is ``true``. Transmitted as a URL query parameter, and so must be escaped accordingly.
    start (integer): The zero-based index of the first value, relative to the first record of the resultset that matches the parameters. Transmitted as a URL query parameter, and so must be escaped accordingly.
    count (integer): The maximum number of entries that should be returned in the response. The Member Node may return fewer and the caller should check the *total* in the response to determine if further pages may be retrieved. Transmitted as a URL query parameter, and so must be escaped accordingly.

  Returns:
    Types.ObjectList: The list of PIDs that match the query criteria. If none match, an empty list is returned.

  Raises:
    Exceptions.NotAuthorized:  (errorCode=401, detailCode=1520)
    Exceptions.InvalidRequest:  (errorCode=400, detailCode=1540)
    Exceptions.NotImplemented: Raised if some functionality requested is not implemented. In the case of an optional request parameter not being supported, the errorCode should be 400. If the requested format (through HTTP Accept headers) is not supported, then the standard HTTP 406 error code should be returned. (errorCode=501, detailCode=1560)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=1580)
    Exceptions.InvalidToken:  (errorCode=401, detailCode=1530)

  .. include:: /apis/examples/listObjects.txt

  """
  return None



def synchronizationFailed(session,message):
  """
  This is a callback method used by a CN to indicate to a MN that it cannot complete synchronization of the science metadata identified by *pid*. When called, the MN should take steps to record the problem description and notify an administrator or the data owner of the issue.

  A successful response is indicated by a HTTP status of 200. An unsuccessful call is indicated by a returned exception and associated HTTP status code.

  Access control for this method MUST be configured to allow calling by Coordinating Nodes and MAY be configured to allow more general access.


  :Version:
  :Use Cases:
    :doc:`UC06 </design/UseCases/06_uc>`
  :REST URL: ``POST /error``

  Parameters:
    session (Types.Session): |session| 
    message (Types.Exception): An instance of the :exc:`Exceptions.SynchronizationFailed` exception with body appropriately filled.  Transmitted as an UTF-8 encoded XML structure for the respective type as defined in the DataONE types schema, as a *File part* of the MIME multipart/mixed message.

  Returns:
    Types.Boolean: A successful response is indicated by a HTTP 200 status. An unsuccessful call is indicated by returing the appropriate exception.

  Raises:
    Exceptions.NotImplemented:  (errorCode=501, detailCode=2160)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=2161)
    Exceptions.NotAuthorized:  (errorCode=401, detailCode=2162)
    Exceptions.InvalidToken: Optionally raised by the receiving MN, depending on implementation. (errorCode=401, detailCode=2164)

  .. include:: /apis/examples/mnread_synchronizationfailed.txt

  """
  return None



def systemMetadataChanged(session,id,serialVersion,dateSysMetaLastModified):
  """
  Notifies the Member Node that the authoritative copy of system metadata on the Coordinating Nodes has changed.

  The Member Node SHOULD schedule an update to its information about the affected object by retrieving an authoritative copy from a Coordinating Node.

  Note that date time precision is limited to one millisecond.

  Access control for this method MUST be configured to allow calling by Coordinating Nodes.


  :Version: 1.0
  :REST URL: ``POST /dirtySystemMetadata``

  Parameters:
    session (Types.Session): |session| 
    id (Types.Identifier): Identifier of the object for which system metadata was changed. May be either a PID or a SID. Calling with SID is equivalent to calling with HEAD PID. Transmitted as a UTF-8 String as a *Param part* of the MIME multipart/mixed message.
    serialVersion (unsigned long): The serialVersion of the system metadata. Transmitted as a UTF-8 String as a *Param part* of the MIME multipart/mixed message.
    dateSysMetaLastModified (Types.DateTime): The time stamp for when the system metadata was changed. Transmitted as a UTF-8 String as a *Param part* of the MIME multipart/mixed message.

  Returns:
    boolean: True if notification was received OK, otherwise an error is returned.

  Raises:
    Exceptions.NotImplemented:  (errorCode=501, detailCode=1330)
    Exceptions.NotAuthorized:  (errorCode=401, detailCode=1331)
    Exceptions.InvalidToken:  (errorCode=401, detailCode=1332)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=1333)
    Exceptions.InvalidRequest:  (errorCode=400, detailCode=1334)

  .. include:: /apis/examples/mnread_systemmetadatachanged.txt

  """
  return None



def getReplica(session,pid):
  """
  Called by a target Member Node to fullfill the replication request originated by a Coordinating Node calling :func:`MNReplication.replicate`. This is a request to make a replica copy of the object, and differs from a call to GET /object in that it should be logged as a replication event rather than a read event on that object.

  If the object being retrieved is restricted access, then a Tier 2 or higher Member Node MUST make a call to :func:`CNReplication.isNodeAuthorized` to verify that the Subject of the caller is authorized to retrieve the content.

  A successful operation is indicated by a HTTP status of 200 on the response.

  Failure of the operation MUST be indicated by returning an appropriate exception.


  :Version: 1.0
  :Use Cases:
    :doc:`UC09 </design/UseCases/09_uc>`
  :REST URL: ``GET /replica/{pid}``

  Parameters:
    session (Types.Session): |session| 
    pid (Types.Identifier): The identifier of the object to get as a replica Transmitted as part of the URL path and must be escaped accordingly.

  Returns:
    Types.OctetStream: Bytes of the specified object.

  Raises:
    Exceptions.NotImplemented:  (errorCode=501, detailCode=2180)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=2181)
    Exceptions.NotAuthorized:  (errorCode=401, detailCode=2182)
    Exceptions.InvalidToken:  (errorCode=401, detailCode=2183)
    Exceptions.InsufficientResources: The node is unable to service the request due to insufficient resources such as CPU, memory, or bandwidth being over utilized. (errorCode=413, detailCode=2184)
    Exceptions.NotFound:  (errorCode=404, detailCode=2185)

  .. include:: /apis/examples/mnread_getreplica.txt

  """
  return None

