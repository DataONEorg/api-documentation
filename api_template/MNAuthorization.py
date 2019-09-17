import Exceptions
import Types



def isAuthorized(session,id,action):
  """
  Test if the user identified by the provided session has authorization for operation on the specified object.

  A successful operation is indicated by a return HTTP status of 200.

  Failure is indicated by an exception such as :exc:`NotAuthorized` being returned.

  The body of the response is arbitrary and SHOULD be ignored by the caller.

  If the action is not authorized, then a :exc:`NotAuthorized` exception MUST be raised.

  .. Note:: Should perhaps add convenience methods for "canRead()" and "canWrite()" to verify that a user is able to read / write an object.


  :Version: 1.0
  :Use Cases:
    :doc:`UC01 </design/UseCases/01_uc>`, :doc:`UC37 </design/UseCases/37_uc>`
  :REST URL: ``GET /isAuthorized/{id}?action={action}``

  Parameters:
    session (Types.Session): |session| 
    id (Types.Identifier): The identifer of the resource for which access is being checked. May be either a PID or a SID. Will use the HEAD PID when given a SID value. Transmitted as part of the URL path and must be escaped accordingly.
    action (Types.Permission): The type of operation which is being requested for the given pid. Transmitted as a URL query parameter, and so must be escaped accordingly.

  Returns:
    boolean: True if the operation is allowed

  Raises:
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=1760)
    Exceptions.NotImplemented:  (errorCode=501, detailCode=1780)
    Exceptions.NotFound:  (errorCode=404, detailCode=1800)
    Exceptions.NotAuthorized: This error is raised if the request comes from a black listed source (e.g. a temporary block may be imposed on a source that calls this method too many times within some time interval) (errorCode=401, detailCode=1820)
    Exceptions.InvalidToken:  (errorCode=401, detailCode=1840)
    Exceptions.InvalidRequest:  (errorCode=400, detailCode=1761)

  .. include:: /apis/examples/mnauthorization_isauthorized.txt

  """
  return None

