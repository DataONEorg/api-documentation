import Exceptions
import Types



def ping():
  """
  ``GET /monitor/ping`` |br| Low level "are you alive" operation. A valid ping response is indicated by a HTTP status of 200. A timestmap indicating the current system time (UTC) on the node MUST be returned in the HTTP Date header.

  The Member Node should perform some minimal internal functionality testing before answering. However, ping checks will be frequent (every few minutes) so the internal functionality test should not be high impact.

  Any status response other than 200 indicates that the node is offline for DataONE operations.

  Note that the timestamp returned in the Date header should follow the semantics as described in the HTTP specifications, http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.18

  The response body will be ignored by the caller except in the case of an error, in which case the response body should contain the appropriate DataONE exception.


  :Version: 1.0
  :Use Cases:
    :doc:`UC10 </design/UseCases/10_uc>`
  :REST URL: ``GET /monitor/ping``

  Returns:
    null: Null body or Exception. The body of the message may be ignored by the caller. The HTTP header *Date* MUST be set in the response.

  Raises:
    Exceptions.NotImplemented: Ping is a required operation and so an operational member node should never return this exception unless under development. (errorCode=501, detailCode=2041)
    Exceptions.ServiceFailure: A ServiceFailure exception indicates that the node is not currently operational as a member node. A coordinating node or monitoring service may use this as an indication that the member node should be taken out of the pool of active nodes, though ping should be called on a regular basis to determine when the node might b ready to resume normal operations. (errorCode=500, detailCode=2042)
    Exceptions.InsufficientResources: A ping response may return InsufficientResources if for example the system is in a state where normal DataONE operations may be impeded by an unusually high load on the node. (errorCode=413, detailCode=2045)

  .. include:: /apis/examples/ping.txt

  """
  return None



def getLogRecords(session,fromDate=None,toDate=None,event=None,idFilter=None,start=0,count=1000):
  """
  ``GET /log?[fromDate={fromDate}][&toDate={toDate}][&event={event}][&idFilter={idFilter}][&start={start}][&count={count}]`` |br| Retrieve log information from the Member Node for the specified slice parameters. Log entries will only return PIDs.

  This method is used primarily by the log aggregator to generate aggregate statistics for nodes, objects, and the methods of access.

  The response MUST contain only records for which the requestor has permission to read.

  Note that date time precision is limited to one millisecond. If no timezone information is provided UTC will be assumed.

  Access control for this method MUST be configured to allow calling by Coordinating Nodes and MAY be configured to allow more general access.

  v2.0: The event parameter has changed from :class:`v1_0.Types.Event` to a plain *string*

  v2.0: The structure of :class:`v2_0.Types.Log` has changed.


  :Version: 1.0, 2.0
  :REST URL: ``GET /log?[fromDate={fromDate}][&toDate={toDate}][&event={event}][&idFilter={idFilter}][&start={start}][&count={count}]``

  Parameters:
    session (Types.Session): |session| 
    fromDate (Types.DateTime): Records with time stamp greater than or equal to (>=) this value will be returned. Transmitted as a URL query parameter, and so must be escaped accordingly.
    toDate (Types.DateTime): Records with a time stamp less than (<) this value will be returned. If not specified, then defaults to *now*. Transmitted as a URL query parameter, and so must be escaped accordingly.
    event (Types.Event, string): Return only log records for the specified type of event.  Default is *all*. Transmitted as a URL query parameter, and so must be escaped accordingly.
    idFilter (string): Return only log records for identifiers that start with the supplied identifier string. Support for this parameter is optional and MAY be ignored by the Member Node implementation with no warning. Accepts PIDs and SIDs Transmitted as a URL query parameter, and so must be escaped accordingly.
    start (integer): Optional zero based offset from the first record in the set of matching log records. Used to assist with paging the response. Transmitted as a URL query parameter, and so must be escaped accordingly.
    count (integer): The maximum number of log records that should be returned in the response. The Member Node may return fewer and the caller should check the *total* in the response to determine if further pages may be retrieved. Transmitted as a URL query parameter, and so must be escaped accordingly.

  Returns:
    Types.Log: 

  Raises:
    Exceptions.NotAuthorized: Raised if the user making the request is not authorized to access the log records. This is determined by the policy of the Member Node. (errorCode=401, detailCode=1460)
    Exceptions.InvalidRequest: The request parameters were malformed or an invalid date range was specified. (errorCode=400, detailCode=1480)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=1490)
    Exceptions.InvalidToken:  (errorCode=401, detailCode=1470)
    Exceptions.NotImplemented:  (errorCode=501, detailCode=1461)

  .. include:: /apis/examples/getLogRecords.txt

  """
  return None



def getCapabilities():
  """
  ``GET /  and  GET /node`` |br| Returns a document describing the capabilities of the Member Node.

  The response at the Member Node base URL is for convenience only. Clients of Member Nodes SHOULD use the /node URL to retrieve the node capabilities document.


  :Version: 1.0
  :REST URL: ``GET /  and  GET /node``

  Returns:
    Types.Node: The technical capabilities of the Member Node

  Raises:
    Exceptions.NotImplemented:  (errorCode=501, detailCode=2160)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=2162)

  .. include:: /apis/examples/mn_getCapabilities.txt

  """
  return None

