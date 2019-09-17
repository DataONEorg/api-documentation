import Exceptions
import Types



def create(session,pid,object,sysmeta):
  """
  Called by a client to adds a new object to the Member Node.

  The *pid* must not exist in the DataONE system or should have been previously reserved using  :func:`CNCore.reserveIdentifier`. A new, unique :attr:`Types.SystemMetadata.seriesId` may be included.

  The caller MUST have authorization to write or create content on the Member Node.


  :Version: 1.0
  :Use Cases:
    :doc:`UC04 </design/UseCases/04_uc>`, :doc:`UC09 </design/UseCases/09_uc>`, :doc:`UC16 </design/UseCases/16_uc>`
  :REST URL: ``POST /object``

  Parameters:
    session (Types.Session): |session| 
    pid (Types.Identifier): The identifier that should be used in DataONE to identify and access the object. This is an Unicode string that follows the constraints on identifiers described in :doc:`/design/PIDs`. If the identifier is already in use, :exc:`Exceptions.IdentifierNotUnique` will be raised and the client SHOULD try again with a different, unique identifier.  Transmitted as a UTF-8 String as a *Param part* of the MIME multipart/mixed message.
    object (bytes): The data bytes that are to be added to the Member Node. 
    sysmeta (Types.SystemMetadata): The system metadata document that provides basic information about the object, including a reference to its identifier, access control information, etc. Attributes of the sysmeta that are the responsibility of the client MUST be set. Note that the obsoletes and obsoletedBy elements MUST not be set. It is the role of the update() method to ensure these are properly updated to ensure object lineage is as expected. Transmitted as an UTF-8 encoded XML structure for the respective type as defined in the DataONE types schema, as a *File part* of the MIME multipart/mixed message.

  Returns:
    Types.Identifier: The identifier that was used to insert the document into the system. 

  Raises:
    Exceptions.NotAuthorized: The provided identity does not have permission to WRITE to the Member Node. (errorCode=401, detailCode=1100)
    Exceptions.IdentifierNotUnique: The requested identifier is already used by another object and therefore can not be used for this object. Clients should choose a new identifier that is unique and retry the operation or use :func:`CNCore.reserveIdentifier` to reserve one. (errorCode=409, detailCode=1120)
    Exceptions.UnsupportedType: The MN can not deal with the content specified in the data package. (errorCode=400, detailCode=1140)
    Exceptions.InsufficientResources: The MN is unable to execute the transfer because it does not have sufficient storage space for example. (errorCode=413, detailCode=1160)
    Exceptions.InvalidSystemMetadata: The supplied system metadata is invalid. This could be because some required field is not set, the metadata document is malformed, or the value of some field is not valid. (errorCode=400, detailCode=1180)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=1190)
    Exceptions.InvalidToken:  (errorCode=401, detailCode=1110)
    Exceptions.NotImplemented:  (errorCode=501, detailCode=1101)
    Exceptions.InvalidRequest:  (errorCode=400, detailCode=1102)

  .. include:: /apis/examples/create.txt

  """
  return None



def update(session,pid,object,newPid,sysmeta):
  """
  This method is called by clients to update objects on Member Nodes.

  Updates an existing object by creating a new object identified by *newPid* on the Member Node which explicitly obsoletes the object identified by *pid* through appropriate changes to the SystemMetadata of *pid* and *newPid*.

  The Member Node sets :attr:`Types.SystemMetadata.obsoletedBy` on the object being obsoleted to the *pid* of the new object. It then updates :attr:`Types.SystemMetadata.dateSysMetadataModified` on both the new and old objects. The modified system metadata entries then become available in :func:`MNRead.listObjects`. This ensures that a Coordinating Node will pick up the changes when filtering on :attr:`Types.SystemMetadata.dateSysMetadataModified`.

  The update operation MUST fail with :exc:`Exceptions.InvalidRequest` on objects that have the :attr:`Types.SystemMetadata.archived` property set to true.

  A new, unique :attr:`Types.SystemMetadata.seriesId` may be included when beginning a series, or a series may be extended if the newPid obsoletes the existing pid.


  :Version: 1.0
  :Use Cases:
    :doc:`UC16 </design/UseCases/16_uc>`
  :REST URL: ``PUT /object/{pid}``

  Parameters:
    session (Types.Session): |session| 
    pid (Types.Identifier): The identifier of the object that is being updated. If this identifier does not exist in the system, an error is raised and the operation does not cause any changes to the objects or their metadata.  Transmitted as part of the URL path and must be escaped accordingly.
    object (bytes): The bytes of the data or science metadata object that will be deprecating the exsting object. 
    newPid (Types.Identifier): The identifier that will become the replacement identifier for the existing object after the update. This identifier must have been previously reserved.  Transmitted as a UTF-8 String as a *Param part* of the MIME multipart/mixed message.
    sysmeta (Types.SystemMetadata): A System Metadata document describing the new object. The :attr:`SystemMetadata.obsoletes` field must contain the identifier of the object being obsoleted. Other required client provided fields as described for :class:`Types.SystemMetadata` must be filled. Transmitted as an UTF-8 encoded XML structure for the respective type as defined in the DataONE types schema, as a *File part* of the MIME multipart/mixed message.

  Returns:
    Types.Identifier: The identifier of the document that is replacing the original, which should be the same as *newPid*.

  Raises:
    Exceptions.NotAuthorized:  (errorCode=401, detailCode=1200)
    Exceptions.IdentifierNotUnique: The requested identifier is already used by another object and therefore can not be used for this object.  Clients should choose a new identifier that is unique and retry the operation. (errorCode=409, detailCode=1220)
    Exceptions.UnsupportedType: The MN can not deal with the object provided. (errorCode=400, detailCode=1240)
    Exceptions.InsufficientResources: The MN is unable to execute the transfer because it does not have sufficient storage space for example. (errorCode=413, detailCode=1260)
    Exceptions.NotFound: The update operation failed because the object which was supposed to be updated in the system (indicated via the *obsoletedPid* parameter) is not present in the DataONE system, so update is an illegal operation. (errorCode=404, detailCode=1280)
    Exceptions.InvalidSystemMetadata: One or more required fields are not set, the metadata document is malformed or the value of some field is not valid. :attr:`SystemMetadata.obsoletes` is set by the client and does not match the *pid* of the object being obsoleted. :attr:`SystemMetadata.obsoletedBy` is set on the SystemMetadata of the new object provided by the client (a new object cannot be created in an obsoleted state). :attr:`SystemMetadata.obsoletedBy` is already set on the object being obsoleted (no branching is allowed in the obsolescence chain). (errorCode=400, detailCode=1300)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=1310)
    Exceptions.InvalidToken:  (errorCode=401, detailCode=1210)
    Exceptions.NotImplemented:  (errorCode=501, detailCode=1201)
    Exceptions.InvalidRequest: Raised when the request parameters are incorrect or the operation is not applicable to the current state of the object (e.g. an archived object can not be updated) (errorCode=400, detailCode=1202)

  .. include:: /apis/examples/mnstorage_update.txt

  """
  return None



def generateIdentifier(session,scheme,fragment=None):
  """
  Given a scheme and optional fragment, generates an identifier with that scheme and fragment that is unique. Maybe be used for generating either PIDs or SIDs.

  The message body is encoded as MIME Multipart/form-data


  :Version: 1.0
  :REST URL: ``POST /generate``

  Parameters:
    session (Types.Session): |session| 
    scheme (string): The name of the identifier scheme to be used, drawn from a DataONE-specific vocabulary of identifier scheme names, including several common syntaxes such as DOI, ARK, LSID, UUID, and LSRN, among others. The first version of this method only supports the UUID scheme, and ignores the fragment parameter.  Transmitted as a UTF-8 String as a *Param part* of the MIME multipart/mixed message.
    fragment (string): The optional fragment to include in the generated Identifier. This parameter is optional and may not be present in the message body. Transmitted as a UTF-8 String as a *Param part* of the MIME multipart/mixed message.

  Returns:
    Types.Identifier: The identifier that was generated

  Raises:
    Exceptions.InvalidToken: The supplied authentication token is not a proper certificate, or missing required fields, or otherwise proves invalid. (errorCode=401, detailCode=2190)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=2191)
    Exceptions.NotAuthorized: Supplied credentials does not have WRITE permission (errorCode=401, detailCode=2192)
    Exceptions.InvalidRequest: The scheme requested is not a valid scheme accepted by this service (errorCode=400, detailCode=2193)
    Exceptions.NotImplemented:  (errorCode=501, detailCode=2194)

  .. include:: /apis/examples/mnstorage_generateidentifier.txt

  """
  return None



def delete(session,id):
  """
  Deletes an object managed by DataONE from the Member Node. Member Nodes MUST check that the caller (typically a Coordinating Node) is authorized to perform this function.

  The delete operation will be used primarily by Coordinating Nodes to help manage the number of replicas of an object that are present in the entire system.

  The operation removes the object from further interaction with DataONE services. The implementation may delete the object bytes, and in general should do so since a delete operation may be in response to a problem with the object (e.g. it contains malicious content, is innappropriate, or is the subject of a legal request).

  If the object does not exist on the node servicing the request, then an :exc:`Exceptions.NotFound` exception is raised. The message body of the exception SHOULD contain a hint as to the location of the :func:`CNRead.resolve` method.


  :Version: 1.0
  :Use Cases:
    :doc:`UC16 </design/UseCases/16_uc>`
  :REST URL: ``DELETE /object/{id}``

  Parameters:
    session (Types.Session): |session| 
    id (Types.Identifier): The identifier of the object to be deleted. May be either a PID or a SID. Will delete the HEAD PID when called with a SID. Transmitted as part of the URL path and must be escaped accordingly.

  Returns:
    Types.Identifier: The identifier of the object that was deleted.

  Raises:
    Exceptions.NotAuthorized:  (errorCode=401, detailCode=2900)
    Exceptions.NotFound: The delete operation failed because the object is not present on the node servicing the request. (errorCode=404, detailCode=2901)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=2902)
    Exceptions.InvalidToken:  (errorCode=401, detailCode=2903)
    Exceptions.NotImplemented:  (errorCode=501, detailCode=2904)

  .. include:: /apis/examples/mnstorage_delete.txt

  """
  return None



def archive(session,id):
  """
  Hides an object managed by DataONE from search operations, effectively preventing its discovery during normal operations.

  The operation does not delete the object bytes, but instead sets the :attr:`Types.SystemMetadata.archived` flag to True. This ensures that the object can still be resolved (and hence remain valid for existing citations and cross references), though will not appear in searches.

  Objects that are archived can not be updated through the :func:`MNStorage.update` operation.

  Archived objects can not be un-archived. This behavior may change in future versions of the DataONE API.

  Member Nodes MUST check that the caller is authorized to perform this function.

  If the object does not exist on the node servicing the request, then an :exc:`Exceptions.NotFound` exception is raised. The message body of the exception SHOULD contain a hint as to the location of the :func:`CNRead.resolve` method.


  :Version: 1.0
  :REST URL: ``PUT /archive/{id}``

  Parameters:
    session (Types.Session): |session| 
    id (Types.Identifier): The identifier of the object to be archived. May be either a PID or a SID. Will archive the HEAD PID when called with a SID. Transmitted as part of the URL path and must be escaped accordingly.

  Returns:
    Types.Identifier: The identifier of the object that was archived.

  Raises:
    Exceptions.NotAuthorized:  (errorCode=401, detailCode=2910)
    Exceptions.NotFound: The archive operation failed because the object is not present on the node servicing the request. (errorCode=404, detailCode=2911)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=2912)
    Exceptions.InvalidToken:  (errorCode=401, detailCode=2913)
    Exceptions.NotImplemented:  (errorCode=501, detailCode=2914)

  .. include:: /apis/examples/mnstorage_archive.txt

  """
  return None



def updateSystemMetadata(session,pid,sysmeta):
  """
  Provides a mechanism for updating system metadata for any objects held on the Member Node where that Member Node is the authoritative Member Node. Coordinating Node can call this method on the non-authoritative Member Node. However, this is not a normal operation and is for the special case - the authoritative Member Node doesn't exist any more. Coordinating Node calling the method on the non-authoriative Memember Node in the normal operation can cause an unexpected consequence.

  This method is typically used by Authoritative Member Node or rights holder[s] to ensure system metadata quality.


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

  .. include:: /apis/examples/mnstorage_updatesystemmetadata.txt

  """
  return None

