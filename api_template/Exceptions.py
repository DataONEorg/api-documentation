
class AuthenticationTimeout(Exception):
    """
    The authentication request timed out.

    :errorCode: 408
    """

    def __init__(self, detailCode, description, traceInformation):
        """

        Args:
            detailCode (string): |exdetail|
            description (string): |exdescr|
            traceInformation (dictionary): |extrace|
        """
        pass


class IdentifierNotUnique(Exception):
    """
    The provided identifier conflicts with an existing identifier in the DataONE system.

    When serializing, the identifier in conflict should be rendered in traceInformation as the value of an identifier key.

    :errorCode: 409
    """

    def __init__(self, detailCode, description, pid, traceInformation):
        """

        Args:
            detailCode (string): |exdetail|
            description (string):  |exdescr|
            pid (Types.Identifier): The identifier value that is in conflict.
            traceInformation (dictionary): |extrace|
        """
        pass


class InsufficientResources(Exception):
    """
    There are insufficient resources at the node to support the requested operation.

    :errorCode: 413
    """

    def __init__(self, detailCode, description, traceInformation):
        """

        Args:
            detailCode (string): |exdetail|
            description (string): |exdescr|
            traceInformation (dictionary): |extrace|
        """
        pass


class InvalidCredentials(Exception):
    """
    Indicates that the credentials supplied (to :func:`CN_crud.login` for example) are invalid for some reason.

    :errorCode: 401
    """

    def __init__(self, detailCode, description, traceInformation):
        """

        Args:
            detailCode (string): |exdetail|
            description (string): |exdescr|
            traceInformation (dictionary): |extrace|
        """
        pass


class InvalidRequest(Exception):
    """
    The parameters provided in the call were invalid. The names and values of parameters should included in traceInformation.

    :errorCode: 400
    """

    def __init__(self, detailCode, description, traceInformation):
        """

        Args:
            detailCode (string): |exdetail|
            description (string): |exdescr|
            traceInformation (dictionary): |extrace|
        """
        pass

class InvalidSystemMetadata(Exception):
    """
    The supplied system metadata is invalid.

    This could be because some required field is not set, the metadata document is malformed, or the value of some field is not valid. The content of traceInformation should contain additional information about the error encountered (e.g. name of the field with bad value, if the document is malformed).

    :errorCode: 400
    """

    def __init__(self, detailCode, description, traceInformation):
        """

        Args:
            detailCode (string): |exdetail|
            description (string): |exdescr|
            traceInformation (dictionary): |extrace|
        """
        pass

class InvalidToken(Exception):
    """
    The supplied authentication token (Session) could not be verified as being valid.

    :errorCode: 401
    """

    def __init__(self, detailCode, description, traceInformation):
        """

        Args:
            detailCode (string): |exdetail|
            description (string): |exdescr|
            traceInformation (dictionary): |extrace|
        """
        pass

class NotAuthorized(Exception):
    """
    The supplied identity information is not authorized for the requested operation.

    :errorCode: 401
    """

    def __init__(self, detailCode, description, traceInformation):
        """

        Args:
            detailCode (string): |exdetail|
            description (string): |exdescr|
            traceInformation (dictionary): |extrace|
        """
        pass

class NotFound(Exception):
    """
    Used to indicate that an object is not present on the node where the exception was raised.

    The error message should include a reference to the :func:`CN_crud.resolve` method URL for the object.

    :errorCode: 404
    """

    def __init__(self, detailCode, description, pid, traceInformation):
        """

        Args:
            detailCode (string): |exdetail|
            description (string): |exdescr|
            pid (Types.Identifier): The identifier of the object that can not be located.
            traceInformation (dictionary): |extrace|
        """
        pass

class NotImplemented(Exception):
    """
    A method is not implemented, or alternatively, features of a particular method are not implemented.

    :errorCode: 501
    """

    def __init__(self, detailCode, description, traceInformation):
        """

        Args:
            detailCode (string): |exdetail|
            description (string): |exdescr|
            traceInformation (dictionary): |extrace|
        """
        pass

class ServiceFailure(Exception):
    """
    Some sort of system failure occurred that is preventing the requested operation from completing successfully.

    This error can be raised by any method in the DataONE API.

    :errorCode: 500
    """

    def __init__(self, detailCode, description, traceInformation):
        """

        Args:
            detailCode (string): |exdetail|
            description (string): |exdescr|
            traceInformation (dictionary): |extrace|
        """
        pass


class UnsupportedMetadataType(Exception):
    """
    The science metadata document submitted is not of a type that is recognized by the DataONE system.

    :errorCode: 400
    """

    def __init__(self, detailCode, description, traceInformation):
        """

        Args:
            detailCode (string): |exdetail|
            description (string): |exdescr|
            traceInformation (dictionary): |extrace|
        """
        pass

class UnsupportedType(Exception):
    """
    The information presented appears to be unsupported.

    This error might be encountered when attempting to register unrecognized science metadata for example.

    :errorCode: 400
    """

    def __init__(self, detailCode, description, traceInformation):
        """

        Args:
            detailCode (string): |exdetail|
            description (string): |exdescr|
            traceInformation (dictionary): |extrace|
        """
        pass

class SynchronizationFailed(Exception):
    """
    Sent to a Member Node from a Coordinating Node when an attempt to synchronize some object fails.

    :errorCode: 0
    """

    def __init__(self, detailCode, description, pid, traceInformation):
        """

        Args:
            detailCode (string): |exdetail|
            description (string): |exdescr|
            pid (Types.Identifier): Identifier of the object that could not be synchronized.
            traceInformation (dictionary): |extrace|
        """
        pass

class VersionMismatch(Exception):
    """
    The serialVersion of the system metadata being updated differs from the serialVersion supplied with the change request.

    :errorCode: 409
    """

    def __init__(self, detailCode, description, pid, traceInformation):
        """

        Args:
            detailCode (string): |exdetail|
            description (string): |exdescr|
            pid (Types.Identifier): Identifier of the system metadata for the object being updated.
            traceInformation (dictionary): |extrace|
        """
        pass
