import Exceptions
import Types



def view(session,theme,id):
  """
  Provides a formatted view of an object (science metadata, data, resource, or other) using the given named theme.

  The service :func:`CNView.view` operation will implement at least one {theme} named 'default' to provide a standard (possibly minimalistic) view of the content in HTML format. In addition, a CN may redirect a client to the view service of the authoritative Member Node for a PID if that node has implemented the :func:`MNView.view` service and implements a compatible theme.

  If the {theme} parameter is not recognized, the service must render the object using the default theme rather than throwing an error.  Note that the return type of Types.OctetStream requires that the consuming client has a priori knowledge of the theme being returned (like HTML). Response headers must include the correct mime-type of the view being returned.

  v2.0: This method was added to the Version 2.0 API.


  :Version: 2.0
  :REST URL: ``GET /views/{theme}/{id}``

  Parameters:
    session (Types.Session): |session| 
    theme (string): Indicates which themed view will be used to handle the query. All implementations must support a 'default' HTML theme, but are free to implement additional themes that return both HTML and non-HTML responses. Transmitted as part of the URL path and must be escaped accordingly.
    id (Types.Identifier): The identifier of the object to render in a view. May be a PID or a SID, the latter acting as if called with the HEAD PID. Transmitted as part of the URL path and must be escaped accordingly.

  Returns:
    Types.OctetStream: Any return type is allowed, including application/octet-stream, but the format of the response should be specialized by the requested theme.

  Raises:
    Exceptions.InvalidToken:  (errorCode=401, detailCode=2850)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=2851)
    Exceptions.NotAuthorized:  (errorCode=401, detailCode=2852)
    Exceptions.InvalidRequest:  (errorCode=400, detailCode=2853)
    Exceptions.NotImplemented:  (errorCode=501, detailCode=2854)
    Exceptions.NotFound: The specified pid does not exist. (errorCode=404, detailCode=2855)

  .. include:: /apis/examples/cnview_view.txt

  """
  return None



def listViews(session):
  """
  Provides a list of usable themes for rendering content in a view, including a required 'default' theme. The list of themes is provided as an OptionList, where the option key should be used as the theme name in calls to MNView.view, and the description provides a human readable description of what will be returned fo rthat theme.

  v2.0: This method was added to the Version 2.0 API.


  :Version: 2.0
  :REST URL: ``GET /views``

  Parameters:
    session (Types.Session): |session| 

  Returns:
    Types.OptionList: A list of available themes that can be used with the MNView.view service.

  Raises:
    Exceptions.InvalidToken:  (errorCode=401, detailCode=2860)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=2861)
    Exceptions.NotAuthorized:  (errorCode=401, detailCode=2862)
    Exceptions.InvalidRequest:  (errorCode=400, detailCode=2863)
    Exceptions.NotImplemented:  (errorCode=501, detailCode=2864)

  .. include:: /apis/examples/cnview_listviews.txt

  """
  return None

