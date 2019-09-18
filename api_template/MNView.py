import Exceptions
import Types



def view(session,theme,id):
  """
  ``GET /views/{theme}/{pid}`` |br| Provides a formatted view of an object (science metadata, data, resource, or other) using the given named theme.

  If this service is implemented, the :func:`MNView.view` operation must implement at least one {theme} named 'default' to provide a standard (possibly minimalistic) view of the content in HTML format.

  If the {theme} parameter is not recognized, the service must render the object using the default theme rather than throwing an error.  Note that the return type of Types.OctetStream requires that the consuming client has a priori knowledge of the theme being returned (like HTML). Response headers must include the correct mime-type of the view being returned.

  This method is optional for Member Nodes, but if implemented,  MNView.listViews must also be implemented.


  :Version: 1.2
  :REST URL: ``GET /views/{theme}/{pid}``

  Parameters:
    session (Types.Session): |session| 
    theme (string): Indicates which themed view will be used to handle the query. All implementations must support a 'default' HTML theme, but are free to implement additional themes that return both HTML and non-HTML responses. Transmitted as part of the URL path and must be escaped accordingly.
    id (Types.Identifier): The identifier of the object to render in a view. May be either a PID or a SID. Transmitted as part of the URL path and must be escaped accordingly.

  Returns:
    Types.OctetStream: Any return type is allowed, including application/octet-stream, but the format of the response should be specialized by the requested theme.

  Raises:
    Exceptions.InvalidToken:  (errorCode=401, detailCode=2830)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=2831)
    Exceptions.NotAuthorized:  (errorCode=401, detailCode=2832)
    Exceptions.InvalidRequest:  (errorCode=400, detailCode=2833)
    Exceptions.NotImplemented:  (errorCode=501, detailCode=2834)
    Exceptions.NotFound: The specified pid does not exist. (errorCode=404, detailCode=2835)

  .. include:: /apis/examples/mnview_view.txt

  """
  return None



def listViews(session):
  """
  ``GET /views`` |br| Provides a list of usable themes for rendering content in a view, including a required 'default' theme. The list of themes is provided as an OptionList, where the option key should be used as the theme name in calls to MNView.view, and the description provides a human readable description of what will be returned fo rthat theme.

  This method is optional for Member Nodes, but if implemented,  MNView.view must also be implemented.


  :Version: 1.2
  :REST URL: ``GET /views``

  Parameters:
    session (Types.Session): |session| 

  Returns:
    Types.OptionList: A list of available themes that can be used with the MNView.view service.

  Raises:
    Exceptions.InvalidToken:  (errorCode=401, detailCode=2840)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=2841)
    Exceptions.NotAuthorized:  (errorCode=401, detailCode=2842)
    Exceptions.InvalidRequest:  (errorCode=400, detailCode=2843)
    Exceptions.NotImplemented:  (errorCode=501, detailCode=2844)

  .. include:: /apis/examples/mnview_listviews.txt

  """
  return None

