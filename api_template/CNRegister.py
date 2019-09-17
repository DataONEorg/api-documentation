import Exceptions
import Types



def updateNodeCapabilities(session,nodeid,node):
  """
  For updating the capabilities of the specified node. Most information is replaced by information in the new node, however, the node identifier, nodeType, ping, syncrhonization.lastHarvested, and synchronization.lastCompleteHarvest are preserved from the existing entry.  Services in the old record not included in the new Node will be removed.

  Successful completion of this operation is indicated by a HTTP response status code of 200.

  Unsuccessful completion of this operation MUST be indicated by returning an appropriate exception.

  v2.0: The structure of :class:`v2_0.Types.Node` has changed.


  :Version: 1.0, 2.0
  :REST URL: ``PUT /node/{nodeid}``

  Parameters:
    session (Types.Session): |session| 
    nodeid (Types.NodeReference): The identifier of the existing node entry being updated. Transmitted as part of the URL path and must be escaped accordingly.
    node (Types.Node): An instance of :class`Types.Node` that contains the updated information.  Transmitted as an UTF-8 encoded XML structure for the respective type as defined in the DataONE types schema, as a *File part* of the MIME multipart/mixed message.

  Returns:
    boolean: True if operation is successful

  Raises:
    Exceptions.NotImplemented: The service is not implemented. (errorCode=501, detailCode=4820)
    Exceptions.NotAuthorized: The :term:`Subject` does not have authority to modify the node registration information. (errorCode=401, detailCode=4821)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=4822)
    Exceptions.InvalidRequest: The request was malformed. (errorCode=400, detailCode=4823)
    Exceptions.NotFound: The requested nodeid is not available in the registry. (errorCode=404, detailCode=4824)
    Exceptions.InvalidToken:  (errorCode=401, detailCode=4825)

  .. include:: /apis/examples/cnregister_updatenodecapabilities.txt

  """
  return None



def getNodeCapabilities(nodeid):
  """
  For retrieving the capabilities of the specified node if it is registered on the Coordinating Node being called.

  v2.0: The structure of :class:`v2_0.Types.Node` has changed.


  :Version: 1.0, 2.0
  :REST URL: ``GET /node/{nodeid}``

  Parameters:
    nodeid (Types.NodeReference): The identifier of the existing node entry being looked up. Transmitted as part of the URL path and must be escaped accordingly.

  Returns:
    Types.Node: An instance of :class`Types.Node` that contains the Node information. 

  Raises:
    Exceptions.NotImplemented: The service is not implemented. (errorCode=501, detailCode=4826)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=4827)
    Exceptions.InvalidRequest: The request was malformed. (errorCode=400, detailCode=4828)
    Exceptions.NotFound: The requested nodeid is not available in the registry. (errorCode=404, detailCode=4829)

  .. include:: /apis/examples/cnregister_getnodecapabilities.txt

  """
  return None



def register(session,node):
  """
  Register a new node in the system. If the node already exists, then a :exc:`IdentifierNotUnique` exception MUST be returned.

  v2.0: The structure of :class:`v2_0.Types.Node` has changed.


  :Version: 1.0, 2.0
  :REST URL: ``POST /node``

  Parameters:
    session (Types.Session): |session| 
    node (Types.Node): An instance of :class:`Types.Node` that fully describes the node being registered. Note that some attributes will be set by the Coordinating Node.  Transmitted as an UTF-8 encoded XML structure for the respective type as defined in the DataONE types schema, as a *File part* of the MIME multipart/mixed message.

  Returns:
    Types.NodeReference: The identifier of the new node entry if successful, otherwise an error is raised.

  Raises:
    Exceptions.NotImplemented:  (errorCode=501, detailCode=4840)
    Exceptions.NotAuthorized:  (errorCode=401, detailCode=4841)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=4842)
    Exceptions.InvalidRequest:  (errorCode=400, detailCode=4843)
    Exceptions.IdentifierNotUnique:  (errorCode=409, detailCode=4844)
    Exceptions.InvalidToken:  (errorCode=401, detailCode=4845)

  .. include:: /apis/examples/cnregister_register.txt

  """
  return None

