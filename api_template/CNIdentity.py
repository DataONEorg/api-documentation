import Exceptions
import Types



def registerAccount(session,person):
  """
  Create a new :term:`subject` in the DataONE system.

  Note that there should probably be a lot more metadata captured about the new user, and there should be a mechanism for specifying the default access control rules for the new account.


  :Version: 1.0, (2.0)
  :Use Cases:
    :doc:`UC16 </design/UseCases/16_uc>`
  :REST URL: ``POST /accounts``

  Parameters:
    session (Types.Session): |session| 
    person (Types.Person): Information about the Person to be registered with the account, including the real name and email address for the individual.  The Subject with the Person must match the subject of the X.509 certificate associated with the authenticated SSL session via client-side authentication, and must not have been registered previously. Transmitted as an UTF-8 encoded XML structure for the respective type as defined in the DataONE types schema, as a *File part* of the MIME multipart/mixed message.

  Returns:
    Types.Subject: The new subject in the DataONE system.  This may be a simple identifier.

  Raises:
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=4520)
    Exceptions.IdentifierNotUnique: The chosen identity already exists in the system (errorCode=409, detailCode=4521)
    Exceptions.InvalidCredentials: Raised if the supplied credentials are invalid, such as an invalid X.509 certificate. (errorCode=401, detailCode=4522)
    Exceptions.NotImplemented:  (errorCode=501, detailCode=4523)
    Exceptions.InvalidRequest:  (errorCode=400, detailCode=4524)
    Exceptions.NotAuthorized: The subject of the session does not match the subject of the person. (errorCode=401, detailCode=4525)
    Exceptions.InvalidToken:  (errorCode=401, detailCode=4526)

  .. include:: /apis/examples/cnidentity_registeraccount.txt

  """
  return None



def updateAccount(session,subject,person):
  """
  Update an existing :term:`subject` in the DataONE system. The target subject is determined from subject provided in the URL.

  The use calling this method must have write access to the account details.

  Note that there should be a policy for verifying the details that change via this method.


  :Version: 1.0, (2.0)
  :Use Cases:
    :doc:`UC16 </design/UseCases/16_uc>`
  :REST URL: ``PUT /accounts/{subject}``

  Parameters:
    session (Types.Session): |session| 
    subject (Types.Subject): The subject of the person being updated. Transmitted as part of the URL path and must be escaped accordingly.
    person (Types.Person): New information about the Person. The subject of the Person cannot be updated with this method and must match the subject of the X.509 certificate associated with the authenticated SSL session via client-side authentication. Transmitted as an UTF-8 encoded XML structure for the respective type as defined in the DataONE types schema, as a *File part* of the MIME multipart/mixed message.

  Returns:
    Types.Subject: The Subject in the DataONE system that was updated.

  Raises:
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=4530)
    Exceptions.InvalidCredentials: Raised if the supplied credentials are invalid, such as an invalid X.509 certificate. (errorCode=401, detailCode=4531)
    Exceptions.NotImplemented:  (errorCode=501, detailCode=4532)
    Exceptions.InvalidRequest:  (errorCode=400, detailCode=4533)
    Exceptions.NotAuthorized: Raised if the subject of the session does not match that of the person. (errorCode=401, detailCode=4534)
    Exceptions.NotFound: Raised if the account does not exist. (errorCode=404, detailCode=4535)
    Exceptions.InvalidToken:  (errorCode=401, detailCode=4536)

  .. include:: /apis/examples/cnidentity_updateaccount.txt

  """
  return None



def verifyAccount(session,subject):
  """
  Verify that the Person data associated with this Subject is a true representation of the real world person.

  This service can only be called by users who have an administrative role for the domain of users in question.

  A successful completion of this operation is indicated by returning a HTTP status of 200.

  An exeption MUST be returned if the account verification is not successful.


  :Version: 1.0, (2.0)
  :REST URL: ``PUT /accounts/verification/{subject}``

  Parameters:
    session (Types.Session): |session| 
    subject (Types.Subject): The Subject identifier of the Person to be verified.  After this service is called for a subject by an authorized user, the account is marked as verified by this user. Transmitted as part of the URL path and must be escaped accordingly.

  Returns:
    boolean: True if the account verification succeeds, otherwise false.

  Raises:
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=4540)
    Exceptions.NotAuthorized: This error is raised if the person attempting to validate the account is not authorized to verify accounts. (errorCode=401, detailCode=4541)
    Exceptions.NotImplemented:  (errorCode=501, detailCode=4542)
    Exceptions.InvalidToken:  (errorCode=401, detailCode=4543)
    Exceptions.InvalidRequest:  (errorCode=400, detailCode=4544)

  .. include:: /apis/examples/cnidentity_verifyaccount.txt

  """
  return None



def getSubjectInfo(session,subject):
  """
  Get the information about a Person (their equivalent identities, and the Groups to which they belong) or the Group (including members).


  :Version: 1.0, (2.0)
  :Use Cases:
    :doc:`UC12 </design/UseCases/12_uc>`
  :REST URL: ``GET /accounts/{subject}``

  Parameters:
    session (Types.Session): |session| 
    subject (Types.Subject): The Subject identifier of the Person or Group details to be returned.  Transmitted as part of the URL path and must be escaped accordingly.

  Returns:
    Types.SubjectInfo: The Person or Group details are contained in the returned SubjectList for the given Subject

  Raises:
    Exceptions.NotImplemented:  (errorCode=501, detailCode=4560)
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=4561)
    Exceptions.NotFound: Raised if the requested subject is not registered with the DataONE system (errorCode=404, detailCode=4564)
    Exceptions.NotAuthorized:  (errorCode=401, detailCode=4563)
    Exceptions.InvalidToken:  (errorCode=401, detailCode=4564)

  .. include:: /apis/examples/cnidentity_getsubjectinfo.txt

  """
  return None



def listSubjects(session,query,status,start,count):
  """
  List the subjects, including users, groups, and systems, that match search criteria.

  The list can be restricted to subjects whose identifier matches certain substrings, and the size of the resultset can be paged through.


  :Version: 1.0, (2.0)
  :REST URL: ``GET /accounts?query={query}[&status={status}&start={start}&count={count}]``

  Parameters:
    session (Types.Session): |session| 
    query (string): A query string criteria to be matched using a case-insensitive substring match against the identifier for the principal, the givenName or familyName of users, and the groupName of groups.  The function returns the union of all successful matches against these fields. Transmitted as a URL query parameter, and so must be escaped accordingly.
    status (string): When provided, the status field can limit the returned list of Subjects to only those with the given status. Currently the 'verified' status is supported. Transmitted as a URL query parameter, and so must be escaped accordingly.
    start (integer): The starting record number for the records to be returned (default = 0). Transmitted as a URL query parameter, and so must be escaped accordingly.
    count (integer): The maximum number of entries that should be returned in the response. The Member Node may return fewer and the caller should check the *total* in the response to determine if further pages may be retrieved (default = 100). Transmitted as a URL query parameter, and so must be escaped accordingly.

  Returns:
    Types.SubjectInfo: The list of people and groups that match the query.

  Raises:
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=2290)
    Exceptions.InvalidToken:  (errorCode=401, detailCode=2270)
    Exceptions.NotAuthorized:  (errorCode=401, detailCode=2260)
    Exceptions.NotImplemented:  (errorCode=501, detailCode=2261)
    Exceptions.InvalidRequest:  (errorCode=400, detailCode=2262)

  .. include:: /apis/examples/cnidentity_listsubjects.txt

  """
  return None



def mapIdentity(session,primarySubject,secondarySubject):
  """
  Create a new mapping between the two identities, asserting that they represent the same subject.

  Mapping identities with this method requires explicit authorization for the user given in the Session object. The caller must have made sure that the primary and secondary identities represent one and the same individual.

  Successful completion of the request is indicated by returning a HTTP status of 200.

  A failed request MUST be indicated by returning an appropriate exception and setting the response HTTP status accordingly.


  :Version: 1.0, (2.0)
  :REST URL: ``POST /accounts/map``

  Parameters:
    session (Types.Session): |session| 
    primarySubject (Types.Subject): The Subject identifier that will have a mapped identity to the other given subject.  Transmitted as a UTF-8 String as a *Param part* of the MIME multipart/mixed message.
    secondarySubject (Types.Subject): The Subject identifier that will have a mapped identity to the other given subject.  Transmitted as a UTF-8 String as a *Param part* of the MIME multipart/mixed message.

  Returns:
    boolean: True if the mapping was successfully initiated, false otherwise.

  Raises:
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=2390)
    Exceptions.InvalidToken:  (errorCode=401, detailCode=2370)
    Exceptions.NotAuthorized: The supplied principal does not have permission to map these two identities (errorCode=401, detailCode=2360)
    Exceptions.NotFound: The specified principal does not exist in the DataONE system (errorCode=404, detailCode=2340)
    Exceptions.NotImplemented:  (errorCode=501, detailCode=2361)
    Exceptions.InvalidRequest:  (errorCode=400, detailCode=2342)
    Exceptions.IdentifierNotUnique: The subject of the session and the provided subject are the same (errorCode=409, detailCode=2343)

  .. include:: /apis/examples/cnidentity_mapidentity.txt

  """
  return None



def removeMapIdentity(session,subject):
  """
  Removes a previously asserted identity mapping from the Subject in the Session to the Subject given by the parameter. The reciprocol mapping entry is also removed.

  A successful request is indicated by returning a HTTP status of 200.

  A failed request MUST be indicated by returning an appropriate exception and setting the response HTTP status accordingly.


  :Version: 1.0, (2.0)
  :REST URL: ``DELETE /accounts/map/{subject}``

  Parameters:
    session (Types.Session): |session| 
    subject (Types.Subject): The Subject identifier to be used for equivalentIdentity. This Subject will not match the Subject named in the certificate. Transmitted as part of the URL path and must be escaped accordingly.

  Returns:
    boolean: True if the map was successfully created, false otherwise.

  Raises:
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=2390)
    Exceptions.InvalidToken:  (errorCode=401, detailCode=2370)
    Exceptions.NotAuthorized: The supplied principal does not have permission to map these two identities (errorCode=401, detailCode=2360)
    Exceptions.NotFound: The specified principal does not exist in the DataONE system, or the mapping between the subjects has no yet been initiated. (errorCode=404, detailCode=2340)
    Exceptions.NotImplemented:  (errorCode=501, detailCode=2361)

  .. include:: /apis/examples/cnidentity_removemapidentity.txt

  """
  return None



def requestMapIdentity(session,subject):
  """
  Request a new mapping between the authenticated identity in the session and the given identity, asserting that they represent the same subject.

  Mapping identities is a two-step process wherein a map request is made by a primary Subject and a subsequent (confirmation) map request is made by the secondary Subject. This ensures that mappings are performed only by those that have authority to do so.

  Successful completion of the request is indicated by returning a HTTP status of 200.

  A failed request MUST be indicated by returning an appropriate exception and setting the response HTTP status accordingly.


  :Version: 1.0, (2.0)
  :REST URL: ``POST /accounts/pendingmap``

  Parameters:
    session (Types.Session): |session| 
    subject (Types.Subject): The Subject identifier to be used for equivalentIdentity. This Subject will not match the Subject named in the certificate. Transmitted as a UTF-8 String as a *Param part* of the MIME multipart/mixed message.

  Returns:
    boolean: True if the mapping was successfully initiated, false otherwise.

  Raises:
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=2390)
    Exceptions.InvalidToken:  (errorCode=401, detailCode=2370)
    Exceptions.NotAuthorized: The supplied principal does not have permission to map these two identities (errorCode=401, detailCode=2360)
    Exceptions.NotFound: The specified principal does not exist in the DataONE system (errorCode=404, detailCode=2340)
    Exceptions.NotImplemented:  (errorCode=501, detailCode=2361)
    Exceptions.InvalidRequest:  (errorCode=400, detailCode=2342)
    Exceptions.IdentifierNotUnique: The subject of the session and the provided subject are the same (errorCode=409, detailCode=2343)

  .. include:: /apis/examples/cnidentity_requestmapidentity.txt

  """
  return None



def confirmMapIdentity(session,subject):
  """
  Confirms a previously initiated identity mapping. If subject A asserts that B is the same identity through :func:`CNIdentity.requestMapIdentity`, then this method is called by B to confirm that assertion.

  A successful request is indicated by returning a HTTP status of 200.

  A failed request MUST be indicated by returning an appropriate exception and setting the response HTTP status accordingly.


  :Version: 1.0, (2.0)
  :REST URL: ``PUT /accounts/pendingmap/{subject}``

  Parameters:
    session (Types.Session): |session| 
    subject (Types.Subject): The Subject identifier to be used for equivalentIdentity. This Subject will not match the Subject named in the certificate. Transmitted as part of the URL path and must be escaped accordingly.

  Returns:
    boolean: True if the map was successfully created, false otherwise.

  Raises:
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=2390)
    Exceptions.InvalidToken:  (errorCode=401, detailCode=2370)
    Exceptions.NotAuthorized: The supplied principal does not have permission to map these two identities (errorCode=401, detailCode=2360)
    Exceptions.NotFound: The specified principal does not exist in the DataONE system, or the mapping between the subjects has no yet been initiated. (errorCode=404, detailCode=2340)
    Exceptions.NotImplemented:  (errorCode=501, detailCode=2361)

  .. include:: /apis/examples/cnidentity_confirmmapidentity.txt

  """
  return None



def getPendingMapIdentity(session,subject):
  """
  Gets the SubjectInfo of a previously initiated identity mapping.

  A successful request is indicated by returning a HTTP status of 200.

  A failed request MUST be indicated by returning an appropriate exception and setting the response HTTP status accordingly.


  :Version: 1.0, (2.0)
  :REST URL: ``GET /accounts/pendingmap/{subject}``

  Parameters:
    session (Types.Session): |session| 
    subject (Types.Subject): The Subject identifier to be used for equivalentIdentity. This Subject will not match the Subject named in the certificate. Transmitted as part of the URL path and must be escaped accordingly.

  Returns:
    Types.SubjectInfo: The SubjectInfo

  Raises:
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=2390)
    Exceptions.NotAuthorized: The supplied principal does not have permission to get the SubjectInfo (errorCode=401, detailCode=2360)
    Exceptions.NotFound: The specified principal does not exist in the DataONE system, or the mapping between the subjects has no yet been initiated. (errorCode=404, detailCode=2340)
    Exceptions.NotImplemented:  (errorCode=501, detailCode=2361)
    Exceptions.InvalidToken:  (errorCode=401, detailCode=4961)

  .. include:: /apis/examples/cnidentity_getpendingmapidentity.txt

  """
  return None



def denyMapIdentity(session,subject):
  """
  Denies a previously initiated identity mapping. If subject A asserts that B is the same identity through :func:`CNIdentity.requestMapIdentity`, then this method is called by B to deny that assertion.

  A successful request is indicated by returning a HTTP status of 200.

  A failed request MUST be indicated by returning an appropriate exception and setting the response HTTP status accordingly.


  :Version: 1.0, (2.0)
  :REST URL: ``DELETE /accounts/pendingmap/{subject}``

  Parameters:
    session (Types.Session): |session| 
    subject (Types.Subject): The Subject identifier to be used for equivalentIdentity. This Subject will not match the Subject named in the certificate. Transmitted as part of the URL path and must be escaped accordingly.

  Returns:
    boolean: True if the map was successfully created, false otherwise.

  Raises:
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=2390)
    Exceptions.InvalidToken:  (errorCode=401, detailCode=2370)
    Exceptions.NotAuthorized: The supplied principal does not have permission to map these two identities (errorCode=401, detailCode=2360)
    Exceptions.NotFound: The specified principal does not exist in the DataONE system, or the mapping between the subjects has no yet been initiated. (errorCode=404, detailCode=2340)
    Exceptions.NotImplemented:  (errorCode=501, detailCode=2361)

  .. include:: /apis/examples/cnidentity_denymapidentity.txt

  """
  return None



def createGroup(session,group):
  """
  Create a group with the given name.

  Groups are lists of subjects that allow all members of the group to be referenced by listing solely the subject name of the group.  Group names must be unique within the DataONE system. Groups can only be modified by Subjects listed as rightsHolders.


  :Version: 1.0, (2.0)
  :REST URL: ``POST /groups``

  Parameters:
    session (Types.Session): |session| 
    group (Types.Group): The Group to be created. Transmitted as an UTF-8 encoded XML structure for the respective type as defined in the DataONE types schema, as a *File part* of the MIME multipart/mixed message.

  Returns:
    Types.Subject: The Subject of the group that was created.

  Raises:
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=2490)
    Exceptions.InvalidToken:  (errorCode=401, detailCode=2470)
    Exceptions.NotAuthorized: The supplied principal does not have permission to create a group (errorCode=401, detailCode=2460)
    Exceptions.NotImplemented:  (errorCode=501, detailCode=2461)
    Exceptions.IdentifierNotUnique: A group by this name already exists (errorCode=409, detailCode=2400)

  .. include:: /apis/examples/cnidentity_creategroup.txt

  """
  return None



def updateGroup(session,group):
  """
  Add members to the named group.

  Group members can be modified only by the original creator of the group, otherwise a NotAuthorized exception is thrown.  Group members are provided as a list of subjects that replace the group membership.

  Successful completion of this operation is indicated by a HTTP response status code of 200.

  Unsuccessful completion of this operation MUST be indicated by returning an appropriate exception.


  :Version: 1.0, (2.0)
  :REST URL: ``PUT /groups``

  Parameters:
    session (Types.Session): |session| 
    group (Types.Group): The new Group object that will replace the old Group. The Group.Subject must match the groupName and an update cannot modify this value. Transmitted as an UTF-8 encoded XML structure for the respective type as defined in the DataONE types schema, as a *File part* of the MIME multipart/mixed message.

  Returns:
    boolean: True if the group that was modified successfully, false otherwise

  Raises:
    Exceptions.ServiceFailure:  (errorCode=500, detailCode=2590)
    Exceptions.InvalidToken:  (errorCode=401, detailCode=2570)
    Exceptions.NotAuthorized: The supplied principal does not have permission to add to a group (errorCode=401, detailCode=2560)
    Exceptions.NotFound: The specified group does not exist in the DataONE system (errorCode=404, detailCode=2540)
    Exceptions.NotImplemented:  (errorCode=501, detailCode=2561)
    Exceptions.InvalidRequest:  (errorCode=400, detailCode=2542)

  .. include:: /apis/examples/cnidentity_updategroup.txt

  """
  return None

