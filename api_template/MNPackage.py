import Exceptions
import Types



def getPackage(session,packageType,id):
  """
  ``GET /packages/{packageType}/{pid}`` |br| Provides all of the content of a DataONE data package as defined by an OAI-ORE document in DataONE, in one of several possible package serialization formats.  The serialized package will contain all of the data described in the ORE aggregation. The default implementation will include packages in the BagIt format.  The packageType formats must be specified using the associated ObjectFormat formatId for that package serialization format.

  The {id} parameter must be the identifier of an ORE package object. If it is the identifier of one of the science metadata documents or data files contained within the package,  the Member Node should throw an InvalidRequest exception. Identifiers may be either PIDss or SIDs.

  This method is optional for Member Nodes.


  :Version: 1.2
  :REST URL: ``GET /packages/{packageType}/{pid}``

  Parameters:
    session (Types.Session): |session| 
    packageType (Types.ObjectFormatIdentifier): Indicates which package format will be used to serialize the package. All implementations must support a default BagIt package serialization, but are free to implement additional package serialization formats. Transmitted as part of the URL path and must be escaped accordingly.
    id (Types.Identifier): The identifier of the package or object in a package to be returned as a serialized package. Transmitted as part of the URL path and must be escaped accordingly.

  Returns:
    Types.OctetStream: Any return type is allowed, including application/octet-stream, but the format of the response should be specialized by the requested packageType.

  Raises:
    Exceptions.InvalidToken:  (errorCode=401, detailCode=2870)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=2871)
    Exceptions.NotAuthorized:  (errorCode=401, detailCode=2872)
    Exceptions.InvalidRequest:  (errorCode=400, detailCode=2873)
    Exceptions.NotImplemented:  (errorCode=501, detailCode=2874)
    Exceptions.NotFound: The specified pid does not exist. (errorCode=404, detailCode=2875)

  .. include:: /apis/examples/mnpackage_getpackage.txt

  """
  return None

