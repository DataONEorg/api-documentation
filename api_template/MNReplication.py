import Exceptions
import Types



def replicate(session,sysmeta,sourceNode):
  """
  Called by a Coordinating Node to request that the Member Node create a copy of the specified object by retrieving it from another Member Nodeode and storing it locally so that it can be made accessible to the DataONE system.

  A successful operation is indicated by a HTTP status of 200 on the response.

  Failure of the operation MUST be indicated by returning an appropriate exception.

  Access control for this method MUST be configured to allow calling by Coordinating Nodes.


  :Version: 1.0
  :Use Cases:
    :doc:`UC09 </design/UseCases/09_uc>`
  :REST URL: ``POST /replicate``

  Parameters:
    session (Types.Session): |session| 
    sysmeta (Types.SystemMetadata): Copy of the CN held system metadata for the object. Transmitted as an UTF-8 encoded XML structure for the respective type as defined in the DataONE types schema, as a *File part* of the MIME multipart/mixed message.
    sourceNode (Types.NodeReference): A reference to node from which the content should be retrieved. The reference should be resolved by checking the CN node registry. Transmitted as a UTF-8 String as a *Param part* of the MIME multipart/mixed message.

  Returns:
    boolean: True if everything works OK, otherwise an error is returned.

  Raises:
    Exceptions.NotImplemented:  (errorCode=501, detailCode=2150)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=2151)
    Exceptions.NotAuthorized:  (errorCode=401, detailCode=2152)
    Exceptions.InvalidRequest:  (errorCode=400, detailCode=2153)
    Exceptions.InsufficientResources:  (errorCode=413, detailCode=2154)
    Exceptions.UnsupportedType:  (errorCode=400, detailCode=2155)
    Exceptions.InvalidToken:  (errorCode=401, detailCode=2156)

  .. include:: /apis/examples/replicate.txt

  """
  return None

