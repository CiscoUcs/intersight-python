# IamSsoSessionAttributes

Session attributes required to maintain states of SP and IdP. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**idp_session_expiration** | **str** | SAML SessionNotOnOrAfter attribute sent by IdP in the assertion. IdP uses this to control for how long SP session maybe. SP does not issue SLO if the session is not valid.   | [optional] [readonly] 
**idp_session_index** | **str** | SAML SessionIndex attribute sent by IdP in the assertion. This has to be sent back to IdP in LogoutRequest.    | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


