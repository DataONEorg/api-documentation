import Exceptions
import Types



def setReplicationStatus(session,pid,nodeRef,status,failure):
  """
  ``PUT /replicaNotifications/{pid}`` |br| Update the replication status of the system metadata, ensuring that the change is appropriate for the given state of system metadata.  For example, a MN can not change the status to *COMPLETED* unless the CN previously requested replication of the object and the replications status of the object (as indicated in the system metadata) is set to *QUEUED*.

  Successful completion of this operation is indicated by a HTTP response status code of 200.

  Unsuccessful completion of this operation MUST be indicated by returning an appropriate exception.

  The nodeRef, status, and failure parameters are transmitted as part of the HTTP request body encoded as a MIME Multipart/form-data encoded payload.

  This method can be only called by Coordinating Nodes and trusted Member Nodes.


  :Version: 1.0, (2.0)
  :Use Cases:
    :doc:`UC09 </design/UseCases/09_uc>`
  :REST URL: ``PUT /replicaNotifications/{pid}``

  Parameters:
    session (Types.Session): |session| 
    pid (Types.Identifier): Identifier of the object to be replicated between Member Nodes. Transmitted as part of the URL path and must be escaped accordingly.
    nodeRef (Types.NodeReference): Reference to the Node which made the setReplicationStatus call. If this is a Member Node, the checksum must be compared with that of the authoritative Member Node. If not, this step can be ignored as the call is not signifying a replication is complete. Transmitted as a UTF-8 String as a *Param part* of the MIME multipart/mixed message.
    status (Types.ReplicationStatus): Replication status. See system metadata schema for possible values.  Transmitted as a UTF-8 String as a *Param part* of the MIME multipart/mixed message.
    failure (Types.BaseException): A BaseException object or one of it's subclasses, or null.  If the status is set to 'failed', this exception object can provide more detail. Appropriate sub-classes include InsufficientResource, NotAuthorized, ServiceFailure, etc. Transmitted as an UTF-8 encoded XML structure for the respective type as defined in the DataONE types schema, as a *File part* of the MIME multipart/mixed message.

  Returns:
    boolean: True if the operation is allowed and expected, otherwise an exception should be raised.

  Raises:
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=4700)
    Exceptions.NotImplemented:  (errorCode=501, detailCode=4701)
    Exceptions.InvalidToken:  (errorCode=401, detailCode=4710)
    Exceptions.NotAuthorized:  (errorCode=401, detailCode=4720)
    Exceptions.InvalidRequest:  (errorCode=400, detailCode=4730)
    Exceptions.NotFound:  (errorCode=404, detailCode=4740)

  .. include:: /apis/examples/cnreplication_setreplicationstatus.txt

  """
  return None



def updateReplicationMetadata(session,pid,replicaMetadata,serialVersion):
  """
  ``PUT /replicaMetadata/{pid}`` |br| Replaces the replica with matching nodeRef in the system metadata of the specified object.  Adds a new replica if the nodeRef of passed in Replica is not already present.  Changes the date sys meta modified.

  Successful completion of the operation is indicated by returning a HTTP status of 200.

  Failure of the operation MUST be indicated by returning an appropriate exception.

  This method can be only called by Coordinating Nodes.


  :Version: 1.0, (2.0)
  :REST URL: ``PUT /replicaMetadata/{pid}``

  Parameters:
    session (Types.Session): |session| 
    pid (Types.Identifier):  Transmitted as part of the URL path and must be escaped accordingly.
    replicaMetadata (Types.Replica):  Transmitted as an UTF-8 encoded XML structure for the respective type as defined in the DataONE types schema, as a *File part* of the MIME multipart/mixed message.
    serialVersion (unsigned long): The serialVersion of the system metadata that is the intended target for the change.  Transmitted as a UTF-8 String as a *Param part* of the MIME multipart/mixed message.

  Returns:
    boolean: True on success

  Raises:
    Exceptions.NotImplemented:  (errorCode=501, detailCode=4850)
    Exceptions.NotAuthorized:  (errorCode=401, detailCode=4851)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=4852)
    Exceptions.InvalidRequest:  (errorCode=400, detailCode=4853)
    Exceptions.NotFound: The specified pid does not exist (errorCode=404, detailCode=4854)
    Exceptions.VersionMismatch: The serialVersion supplied with the request does not match the serialVersion of the target (errorCode=409, detailCode=4855)
    Exceptions.InvalidToken:  (errorCode=401, detailCode=4856)

  .. include:: /apis/examples/cnreplication_updatereplicationmetadata.txt

  """
  return None



def setReplicationPolicy(session,id,policy,serialVersion):
  """
  ``PUT /replicaPolicies/{id}`` |br| Updates the replication policy entry for an object by updating the system metadata.

  Successful completion of the operation is indicated by returning a HTTP status of 200.

  Failure of the operation MUST be indicated by returning an appropriate exception.

  v2.0: The identifier may be a :term:`PID` or :term:`SID`.


  :Version: 1.0, 2.0
  :REST URL: ``PUT /replicaPolicies/{id}``

  Parameters:
    session (Types.Session): |session| 
    id (Types.Identifier): The identifier of the policy being updated. May be either a PID or a SID, the latter acting only on the HEAD PID. Transmitted as part of the URL path and must be escaped accordingly.
    policy (Types.ReplicationPolicy):  Transmitted as an UTF-8 encoded XML structure for the respective type as defined in the DataONE types schema, as a *File part* of the MIME multipart/mixed message.
    serialVersion (unsigned long): The serialVersion of the system metadata that is the intended target for the change. Transmitted as a UTF-8 String as a *Param part* of the MIME multipart/mixed message.

  Returns:
    boolean: True on success

  Raises:
    Exceptions.NotImplemented:  (errorCode=501, detailCode=4880)
    Exceptions.NotAuthorized:  (errorCode=401, detailCode=4881)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=4882)
    Exceptions.InvalidRequest:  (errorCode=400, detailCode=4883)
    Exceptions.NotFound:  (errorCode=404, detailCode=4884)
    Exceptions.InvalidToken:  (errorCode=401, detailCode=4885)
    Exceptions.VersionMismatch: The serialVersion supplied with the request does not match the serialVersion of the target (errorCode=409, detailCode=4886)

  .. include:: /apis/examples/cnreplication_setreplicationpolicy.txt

  """
  return None



def isNodeAuthorized(session,targetNodeSubject,pid):
  """
  ``GET /replicaAuthorizations/{pid}?targetNodeSubject={targetNodeSubject}`` |br| Verifies that a replication event was initiated by a CN by comparing the target node's identifiying subject with a known list of scheduled replication tasks.

  Successful completion of the operation is indicated by returning a HTTP status of 200.

  Failure of the operation MUST be indicated by returning an appropriate exception.


  :Version: 1.0, (2.0)
  :REST URL: ``GET /replicaAuthorizations/{pid}?targetNodeSubject={targetNodeSubject}``

  Parameters:
    session (Types.Session): |session| 
    targetNodeSubject (Types.Subject): The subject that identifies the target node, with a value extracted from the X.509 certificate passed in during the call to MNReplication.replicate(). Transmitted as a URL query parameter, and so must be escaped accordingly.
    pid (Types.Identifier): The identifier of the object to be replicated. Transmitted as part of the URL path and must be escaped accordingly.

  Returns:
    boolean: True on success

  Raises:
    Exceptions.NotImplemented: The method functionality is not implemented. (errorCode=501, detailCode=4870)
    Exceptions.NotAuthorized: Replication of PID is not authorized for the subject listed. (errorCode=401, detailCode=4871)
    Exceptions.ServiceFailure: An internal server error occurred. (errorCode=500, detailCode=4872)
    Exceptions.InvalidRequest: The replication request is invalid. (errorCode=400, detailCode=4873)
    Exceptions.NotFound: The PID does not exist as an existing object. (errorCode=404, detailCode=4874)
    Exceptions.InvalidToken: The session information is invalid. (errorCode=401, detailCode=4875)

  .. include:: /apis/examples/cnreplication_isnodeauthorized.txt

  """
  return None



def deleteReplicationMetadata(session,pid,nodeId,serialVersion):
  """
  ``PUT /removeReplicaMetadata/{pid}`` |br| Removes the replication information for the specified node from the object system metadata identified by *pid*.

  Removal of replication metadata is necessary if the Member Node goes offline permanently or for an extended period, or when it is deeemed prudent to migrate an object from one node to another to address resource management issues.

  This method can be only called by Coordinating Nodes.


  :Version: 1.0, (2.0)
  :REST URL: ``PUT /removeReplicaMetadata/{pid}``

  Parameters:
    session (Types.Session): |session| 
    pid (Types.Identifier): The identifier of the object whose replication metadata is being modified.  Transmitted as part of the URL path and must be escaped accordingly.
    nodeId (Types.NodeReference): The identifier of the node replication information that is being removed from the system metadata record. Transmitted as a UTF-8 String as a *Param part* of the MIME multipart/mixed message.
    serialVersion (unsigned long): The :attr:`Types.SystemMetadata.serialVersion` of the system metadata being updated. This MUST match the latest version of system metadata available for the object on the Coordinating Node. Transmitted as a UTF-8 String as a *Param part* of the MIME multipart/mixed message.

  Returns:
    boolean: True if the replication metadata was successfully deleted.

  Raises:
    Exceptions.NotImplemented: The method functionality if not fully implemented (errorCode=501, detailCode=4950)
    Exceptions.ServiceFailure: An internal server error occurred that prevented the operation from completing. (errorCode=500, detailCode=4951)
    Exceptions.InvalidRequest: The request parameters are malformed (errorCode=400, detailCode=4952)
    Exceptions.InvalidToken: The supplied session is invalid (errorCode=401, detailCode=4953)
    Exceptions.NotFound: The object identified by *pid* or the node reference specified by *nodeId* could not be located in the system metadata for the object. (errorCode=404, detailCode=4956)
    Exceptions.NotAuthorized: The subject identified by the *session* information does not have appropriate priviledges for modifiying the content or accessing the service. (errorCode=401, detailCode=4954)
    Exceptions.VersionMismatch: The *serialVersion* does not match the current :attr:`Types.SystemMetadata.serialVersion` value of the object system metadata. (errorCode=409, detailCode=4955)

  .. include:: /apis/examples/cnreplication_deletereplicationmetadata.txt

  """
  return None

