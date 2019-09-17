import Exceptions
import Types



def ping():
  """
  Low level "are you alive" operation. A valid ping response is indicated by a HTTP status of 200. A timestmap indicating the current system time (UTC) on the node MUST be returned in the HTTP Date header.

  The Member Node should perform some minimal internal functionality testing before answering. However, ping checks will be frequent (every few minutes) so the internal functionality test should not be high impact.

  Any status response other than 200 indicates that the node is offline for DataONE operations.

  Note that the timestamp returned in the Date header should follow the semantics as described in the HTTP specifications, http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.18

  The response body will be ignored by the caller expect in the case of an error, in which case the response body should contain the appropriate DataONE exception.


  :Version: 1.0, (2.0)
  :Use Cases:
    :doc:`UC10 </design/UseCases/10_uc>`
  :REST URL: ``GET /monitor/ping``

  Returns:
    null: Null body or Exception. The body of the message is ignored by the caller. The HTTP header *Date* MUST be set in the response.

  Raises:
    Exceptions.NotImplemented:  (errorCode=501, detailCode=2041)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=2042)
    Exceptions.InsufficientResources: A ping response may return InsufficientResources if for example the system is in a state where normal DataONE operations may be impeded by an unusually high load on the node. (errorCode=413, detailCode=2045)

  .. include:: /apis/examples/cn_ping.txt

  """
  return None



def create(session,pid,object,sysmeta):
  """
  Used internally within a Coordinating Node to add a new object to the object store.

  |cnprivate|

  v2.0: The structure of :class:`v2_0.Types.SystemMetadata` has changed from Version 1.


  :Version: 1.0, 2.0
  :Use Cases:
    :doc:`UC04 </design/UseCases/04_uc>`, :doc:`UC09 </design/UseCases/09_uc>`, :doc:`UC16 </design/UseCases/16_uc>`
  :REST URL: ``POST /object``

  Parameters:
    session (Types.Session): |session| 
    pid (Types.Identifier): The identifier that should be used in DataONE to identify and access the object. This is an Unicode string that follows the constraints on identifiers described in :doc:`/design/PIDs`. Transmitted as a UTF-8 String as a *Param part* of the MIME multipart/mixed message.
    object (bytes): The object (e.g. Science Metadata) bytes.
    sysmeta (Types.SystemMetadata): The complete system metadata document describing the object. Transmitted as an UTF-8 encoded XML structure for the respective type as defined in the DataONE types schema, as a *File part* of the MIME multipart/mixed message.

  Returns:
    Types.Identifier: The identifier that was used to insert the document into the system. This should be the same as the identifier provided as the *pid* parameter.

  Raises:
    Exceptions.NotAuthorized: The provided identity does not have permission to WRITE to the Member Node. (errorCode=401, detailCode=1100)
    Exceptions.IdentifierNotUnique: The requested identifier is already used by another object and therefore can not be used for this object. Clients should choose a new identifier that is unique and retry the operation or use :func:`CNCore.reserveIdentifier` to reserve one. (errorCode=409, detailCode=1120)
    Exceptions.UnsupportedType: The object store is unable to store the provided content. (errorCode=400, detailCode=4895)
    Exceptions.InsufficientResources: The CN object store is unable to execute the transfer because of resource limitations. (errorCode=413, detailCode=4897)
    Exceptions.InvalidSystemMetadata: The supplied system metadata is invalid. This could be because some required field is not set, the metadata document is malformed, or the value of some field is not valid. (errorCode=400, detailCode=4896)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=4893)
    Exceptions.InvalidToken:  (errorCode=401, detailCode=4894)
    Exceptions.NotImplemented:  (errorCode=501, detailCode=4890)
    Exceptions.InvalidRequest:  (errorCode=400, detailCode=4891)

  .. include:: /apis/examples/cncore_create.txt

  """
  return None



def listFormats():
  """
  Returns a list of all object formats registered in the DataONE Object Format Vocabulary.

  v2.0: The structure of :class:`v2_0.Types.ObjectFormat` has changed.


  :Version: 1.0, 2.0
  :REST URL: ``GET /formats``

  Returns:
    Types.ObjectFormatList: The list of object formats registered in the DataONE Object Format Vocabulary

  Raises:
    Exceptions.NotImplemented: The service is not implemented. (errorCode=501, detailCode=4840)
    Exceptions.ServiceFailure: An error occurred when attempting to service the request. (errorCode=500, detailCode=4841)

  .. include:: /apis/examples/cn_listObjectFormats.txt

  """
  return None



def getFormat(formatId):
  """
  Returns the object format registered in the DataONE Object Format Vocabulary for the given format identifier.

  v2.0: The structure of :class:`v2_0.Types.ObjectFormat` has changed.


  :Version: 1.0, 2.0
  :REST URL: ``GET /formats/{formatId}``

  Parameters:
    formatId (Types.ObjectFormatIdentifier): Unique ObjectFormatIdentifier for the object format Transmitted as part of the URL path and must be escaped accordingly.

  Returns:
    Types.ObjectFormat: The object format registered in the DataONE Object Format Vocablulary

  Raises:
    Exceptions.NotImplemented: The service is not implemented. (errorCode=501, detailCode=4845)
    Exceptions.ServiceFailure: Unexpected exception from the service. (errorCode=500, detailCode=4846)
    Exceptions.NotFound: The format specified by *formatId* does not exist at this node. (errorCode=404, detailCode=4848)

  .. include:: /apis/examples/cn_getFormat.txt

  """
  return None



def getLogRecords(session,fromDate=None,toDate=None,event=None,idFilter=None,start=0,count=None):
  """
  Retrieves consolidated log information for the specified date range (fromDate < timestamp <= toDate) for the entire DataONE infrastructure

  Note that date time precision is limited to one millisecond. If no timezone information is provided, the UTC will be assumed.

  Note that full access to log records requires access through a priviledged account. A public user may be presented with an empty response.

  v2.0: The structure of :class:`v2_0.Types.Log` has changed.

  v2.0: The event parameter has changed from :class:`v1_0.Types.Event` to a plain *string*


  :Version: 1.0, 2.0
  :Use Cases:
    :doc:`UC16 </design/UseCases/16_uc>`
  :REST URL: ``GET /log?[fromDate={fromDate}][&toDate={toDate}][&event={event}][&idFilter={idFilter}][&start={start}][&count={count}]``

  Parameters:
    session (Types.Session): |session| 
    fromDate (Types.DateTime): Starting time for records in response, entries with timestamp greater than or equal to (>=) this value will be returned. Defaults to include all records. Transmitted as a URL query parameter, and so must be escaped accordingly.
    toDate (Types.DateTime): End time for records in response, entries with timestamp less than (<) this value will be returned. If not specified, then defaults to now. Transmitted as a URL query parameter, and so must be escaped accordingly.
    event (Types.Event, string): Return only log records for the specified type of event.  Default is all. Transmitted as a URL query parameter, and so must be escaped accordingly.
    idFilter (string): Return only log records for identifiers that start with the supplied identifier string. Support for this parameter is optional and MAY be ignored by the Coordinating Node implementation with no warning. Supports PID and SID values. Only PID values will be included in the returned entries. Transmitted as a URL query parameter, and so must be escaped accordingly.
    start (integer): The zero based index of the first log record to return. Default is 0. Transmitted as a URL query parameter, and so must be escaped accordingly.
    count (integer): The maximum number of log records that should be returned in the response. The Member Node may return fewer and the caller should check the *total* in the response to determine if further pages may be retrieved. Transmitted as a URL query parameter, and so must be escaped accordingly.

  Returns:
    Types.Log: 

  Raises:
    Exceptions.InvalidToken:  (errorCode=401, detailCode=1470)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=1490)
    Exceptions.NotAuthorized:  (errorCode=401, detailCode=1460)
    Exceptions.NotImplemented:  (errorCode=501, detailCode=1461)
    Exceptions.InvalidRequest:  (errorCode=400, detailCode=1480)
    Exceptions.InsufficientResources: The request could not be serviced due to a limitation of resources - too many requests, internal service timeout, or another similar failure. (errorCode=413, detailCode=1481)

  .. include:: /apis/examples/cncore_getlogrecords.txt

  """
  return None



def reserveIdentifier(session,id):
  """
  Reserves the identifier that is unique and can not be used by any other sessions. Future calls to :func:`MNStorage.create` and :func:`MNStorage.update` that reference this ID must be made by the same :term:`principal` making the reservation, otherwise an error is raised on those methods.

  The requested identifier is transmitted in a MIME Multipart/form-data body with *id* as key, and the identifier string as value.

  v2.0: The identifier being reserved may be used as a :term:`PID` or :term:`SID`.


  :Version: 1.0, 2.0
  :Use Cases:
    :doc:`UC16 </design/UseCases/16_uc>`
  :REST URL: ``POST /reserve``

  Parameters:
    session (Types.Session): |session| 
    id (Types.Identifier): The identifier that is to be reserved. May be a PID or a SID value. Transmitted as a UTF-8 String as a *Param part* of the MIME multipart/mixed message.

  Returns:
    Types.Identifier: The identifier that was reserved

  Raises:
    Exceptions.InvalidToken:  (errorCode=401, detailCode=4190)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=4210)
    Exceptions.NotAuthorized: Supplied credentials does not have WRITE permission (errorCode=401, detailCode=4180)
    Exceptions.InvalidRequest: The identifier requested is not a valid format accepted by this service (errorCode=400, detailCode=4200)
    Exceptions.IdentifierNotUnique: The requested identifier can not be reserved because it already exists in the DataONE system or has already been reserved. (errorCode=409, detailCode=4210)
    Exceptions.NotImplemented:  (errorCode=501, detailCode=4191)

  .. include:: /apis/examples/cncore_reserveidentifier.txt

  """
  return None



def generateIdentifier(session,scheme,fragment=None):
  """
  Given a scheme and optional fragment, generates an identifier with that scheme and fragment that is unique. Returned identifier may be used as either a PID or a SID.

  The message body is encoded as MIME Multipart/form-data


  :Version: 1.0, (2.0)
  :Use Cases:
    :doc:`UC16 </design/UseCases/16_uc>`
  :REST URL: ``POST /generate``

  Parameters:
    session (Types.Session): |session| 
    scheme (string): The name of the identifier scheme to be used, drawn from a DataONE-specific vocabulary of identifier scheme names, including several common syntaxes such as DOI, ARK, LSID, UUID, and LSRN, among others. The first version of this method only supports the UUID scheme, and ignores the fragment parameter.  Transmitted as a UTF-8 String as a *Param part* of the MIME multipart/mixed message.
    fragment (string): The optional fragment to include in the generated Identifier. This parameter is optional and may not be present in the message body. Transmitted as a UTF-8 String as a *Param part* of the MIME multipart/mixed message.

  Returns:
    Types.Identifier: The identifier that was generated

  Raises:
    Exceptions.InvalidToken: The supplied authentication token is not a proper certificate, or missing required fields, or otherwise proves invalid. (errorCode=401, detailCode=4190)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=4210)
    Exceptions.NotAuthorized: Supplied credentials does not have WRITE permission (errorCode=401, detailCode=4180)
    Exceptions.InvalidRequest: The schme requested is not a valid schme accepted by this service (errorCode=400, detailCode=4200)
    Exceptions.NotImplemented:  (errorCode=501, detailCode=4191)

  .. include:: /apis/examples/cncore_generateidentifier.txt

  """
  return None



def listChecksumAlgorithms():
  """
  Returns a list of checksum algorithms that are supported by DataONE.


  :Version: 1.0, (2.0)
  :REST URL: ``GET /checksum``

  Returns:
    Types.ChecksumAlgorithmList: A list of supported checksum algorithms. 

  Raises:
    Exceptions.NotImplemented: The service is not implemented. (errorCode=501, detailCode=4880)
    Exceptions.ServiceFailure: A problem occurred with the service that prevented it from returning the expected response. (errorCode=500, detailCode=4881)

  .. include:: /apis/examples/cncore_listchecksumalgorithms.txt

  """
  return None



def setObsoletedBy(session,pid,obsoletedByPid,serialVersion):
  """
  Updates the :attr:`Types.SystemMetadata.obsoletedBy` property for an object, indicating that the object specified by *pid* has been obsoleted by the identifier in *obsoletedByPid*.

  v2.0: Method implementation has changed to ensure that the obsolescence chain is consistent with use of any SID assigned to the object.

  |cnprivate|


  :Version: 1.0, 2.0
  :REST URL: ``PUT /obsoletedBy/{pid}``

  Parameters:
    session (Types.Session): |session| 
    pid (Types.Identifier): Identifier of the object system metadata being updated. Transmitted as part of the URL path and must be escaped accordingly.
    obsoletedByPid (Types.Identifier): Identifier of the object that obsoletes the object identified by *pid*.  Transmitted as a UTF-8 String as a *Param part* of the MIME multipart/mixed message.
    serialVersion (unsigned long): The serial version of the system metadata being updated. If the specified *serialVersion* does not match the current version at the Coordinating Nodes, then a :exc:`Exceptions.VersionMismatch` error is raised and no changes are made. Transmitted as a UTF-8 String as a *Param part* of the MIME multipart/mixed message.

  Returns:
    boolean: True if the operation succeeds, otherwise false.

  Raises:
    Exceptions.NotImplemented: The service endpoint has not yet been fully implemented (errorCode=501, detailCode=4940)
    Exceptions.ServiceFailure: A problem occurred with the service that prevented it from returning the expected response. (errorCode=500, detailCode=4941)
    Exceptions.InvalidRequest: The request was malformed and could not be processed. (errorCode=400, detailCode=4942)
    Exceptions.InvalidToken: The supplied session information could not be verified as a valid DataONE session. (errorCode=401, detailCode=4943)
    Exceptions.NotFound: The specified *pid* does not exist. (errorCode=404, detailCode=4944)
    Exceptions.NotAuthorized: The credentials provided with the request in the *session* do not have *write* privileges on *pid*. (errorCode=401, detailCode=4945)
    Exceptions.VersionMismatch: The provided *serialVersion* does not match the latest version that is held by the CN. The client should refresh it's copy, verify that the update is still necessary, and resubmit the request with the updated information. (errorCode=409, detailCode=4946)

  .. include:: /apis/examples/cncore_setobsoletedby.txt

  """
  return None



def delete(session,id):
  """
  Deletes an object from the entire DataONE system, including all nodes known to hold a copy of the object. The PID and/or SID of the object will continue to be shown as in use (preventing its reuse for other objects), however the object should not be resolvable (NotFound) or retrievable.

  The delete operation is used only by administrators in response to a request to remove an object from DataONE, perhaps because of legal requirements or the object has been identified as containing malicious content.

  |cnprivate|


  :Version: 1.0, (2.0)
  :Use Cases:
    :doc:`UC16 </design/UseCases/16_uc>`
  :REST URL: ``DELETE /object/{id}``

  Parameters:
    session (Types.Session): |session| 
    id (Types.Identifier): The identifier of the object to be deleted. May be either a PID or SID, the latter will operate on the HEAD PID. Transmitted as part of the URL path and must be escaped accordingly.

  Returns:
    Types.Identifier: The identifier of the object that was deleted.

  Raises:
    Exceptions.NotAuthorized:  (errorCode=401, detailCode=4960)
    Exceptions.NotFound: The delete operation failed because the object does not exist. (errorCode=404, detailCode=4961)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=4962)
    Exceptions.InvalidToken:  (errorCode=401, detailCode=4963)
    Exceptions.NotImplemented:  (errorCode=501, detailCode=4964)

  .. include:: /apis/examples/cncore_delete.txt

  """
  return None



def archive(session,id):
  """
  Hides an object managed by DataONE from search operations, effectively preventing its discovery during normal operations.

  The operation does not delete the object bytes, but instead sets the :attr:`Types.SystemMetadata.archived` flag to True. This ensures that the object can still be resolved (and hence remain valid for existing citations and cross references), though will not appear in searches.

  Objects that are archived can not be updated through the :func:`MNStorage.update` operation.

  Archived objects can not be un-archived. This behavior may change in future versions of the DataONE API.

  The CN should ensure that all MNs holding a copy of the object are informed of the change so that they may update their information about the object.

  v2.0: The supplied identifier may be a :term:`PID` or a :term:`SID`.

  |cnprivate|


  :Version: 1.0, 2.0
  :REST URL: ``PUT /archive/{id}``

  Parameters:
    session (Types.Session): |session| 
    id (Types.Identifier): The identifier of the object to be archived. May be either a PID or a SID, the latter will act on the HEAD PID. Transmitted as part of the URL path and must be escaped accordingly.

  Returns:
    Types.Identifier: The identifier of the object that was archived.

  Raises:
    Exceptions.NotAuthorized:  (errorCode=401, detailCode=4970)
    Exceptions.NotFound: The archive operation failed because the object does not exist. (errorCode=404, detailCode=4971)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=4972)
    Exceptions.InvalidToken:  (errorCode=401, detailCode=4973)
    Exceptions.NotImplemented:  (errorCode=501, detailCode=4974)

  .. include:: /apis/examples/cncore_archive.txt

  """
  return None



def listNodes():
  """
  Returns a list of nodes that have been registered with the DataONE infrastructure.

  v2.0: The structure of :class:`v2_0.Types.Node` has changed.


  :Version: 1.0, 2.0
  :Use Cases:
    :doc:`UC39 </design/UseCases/39_uc>`
  :REST URL: ``GET /node``

  Returns:
    Types.NodeList: List of nodes from the registry

  Raises:
    Exceptions.NotImplemented:  (errorCode=501, detailCode=4800)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=4801)

  .. include:: /apis/examples/cn_node.txt

  """
  return None



def getCapabilities():
  """
  Returns a document describing the capabilities of the Coordinating Node.

  v2.0: The structure of :class:`v2_0.Types.Node` has changed.


  :Version: 1.0, 2.0
  :REST URL: ``GET /``

  Returns:
    Types.Node: The technical capabilities of the Coordinating Node

  Raises:
    Exceptions.NotImplemented:  (errorCode=501, detailCode=4802)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=4803)

  .. include:: /apis/examples/cncore_getcapabilities.txt

  """
  return None



def registerSystemMetadata(session,pid,sysmeta):
  """
  Provides a mechanism for adding system metadata independently of its associated object, such as when adding system metadata for data objects.

  This method is used internally by Coordinating Nodes.

  v2.0: The structure of :class:`v2_0.Types.SystemMetadata` has changed.


  :Version: 1.0, 2.0
  :REST URL: ``POST /meta``

  Parameters:
    session (Types.Session): |session| 
    pid (Types.Identifier):  Transmitted as a UTF-8 String as a *Param part* of the MIME multipart/mixed message.
    sysmeta (Types.SystemMetadata):  Transmitted as an UTF-8 encoded XML structure for the respective type as defined in the DataONE types schema, as a *File part* of the MIME multipart/mixed message.

  Returns:
    Types.Identifier: The pid that was updated.

  Raises:
    Exceptions.NotImplemented:  (errorCode=501, detailCode=4860)
    Exceptions.NotAuthorized:  (errorCode=401, detailCode=4861)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=4862)
    Exceptions.InvalidRequest:  (errorCode=400, detailCode=4863)
    Exceptions.InvalidSystemMetadata:  (errorCode=400, detailCode=4864)
    Exceptions.InvalidToken:  (errorCode=401, detailCode=4865)

  .. include:: /apis/examples/cncore_registersystemmetadata.txt

  """
  return None



def updateSystemMetadata(session,pid,sysmeta):
  """
  Provides a mechanism for updating system metadata for any objects held in the federation.

  Usage of this method SHOULD be restricted to CNs for updating the system metadata in the underlying CN storage sub-system.

  v2.0: The structure of :class:`v2_0.Types.SystemMetadata` has changed.

  Note: the serial version and the replica list in the new system metadata will be ignored.


  :Version: 2.0
  :REST URL: ``PUT /meta``

  Parameters:
    session (Types.Session): |session| 
    pid (Types.Identifier):  Transmitted as a UTF-8 String as a *Param part* of the MIME multipart/mixed message.
    sysmeta (Types.SystemMetadata):  Transmitted as an UTF-8 encoded XML structure for the respective type as defined in the DataONE types schema, as a *File part* of the MIME multipart/mixed message.

  Returns:
    boolean: True if the update was successful.

  Raises:
    Exceptions.NotImplemented:  (errorCode=501, detailCode=4866)
    Exceptions.NotAuthorized:  (errorCode=401, detailCode=4867)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=4868)
    Exceptions.InvalidRequest:  (errorCode=400, detailCode=4869)
    Exceptions.InvalidSystemMetadata:  (errorCode=400, detailCode=4956)
    Exceptions.InvalidToken:  (errorCode=401, detailCode=4957)

  .. include:: /apis/examples/cncore_updatesystemmetadata.txt

  """
  return None



def hasReservation(session,subject,id):
  """
  Checks to determine if the supplied *subject* is the owner of the reservation of *id*.

  A positive response (that the *pid* is reserved and owned by *subject*) is indicated by a return of a HTTP status of 200.

  A negative response is indicated by an exception and the associated HTTP status code.

  v2.0: The identifier may be a :term:`PID` or :term:`SID`.


  :Version: 1.0, 2.0
  :REST URL: ``GET /reserve/{id}?subject={subject}``

  Parameters:
    session (Types.Session): |session| 
    subject (Types.Subject): The subject of the :term:`principal` (user) that made the reservation.  Transmitted as a URL query parameter, and so must be escaped accordingly.
    id (Types.Identifier): The identifier that is being checked for existing as a reserved identifier or is in use as an identifier for an existing object. May be either a PID or a SID. Transmitted as part of the URL path and must be escaped accordingly.

  Returns:
    boolean: True - subject has the reservation on the PID; False - the PID does not exist; False - the PID is already in use; False - the PID is reserved by somone else.

  Raises:
    Exceptions.NotImplemented: The method functionality is not implemented. (errorCode=501, detailCode=4920)
    Exceptions.ServiceFailure: An internal server error occurred. (errorCode=500, detailCode=4921)
    Exceptions.InvalidToken: The session information is invalid. (errorCode=401, detailCode=4922)
    Exceptions.NotFound: The PID does not exist as a reservation or an existing object and is not in use as an identifier. (errorCode=404, detailCode=4923)
    Exceptions.NotAuthorized: The PID is reserved but the owner is not the :term:`principal` identified by the *subjectInfo* OR the provide *session* does not have authority to access this service. (errorCode=401, detailCode=4924)
    Exceptions.InvalidRequest: The request was malformed and could not be processed (errorCode=400, detailCode=4925)

  .. include:: /apis/examples/cncore_hasreservation.txt

  """
  return None

