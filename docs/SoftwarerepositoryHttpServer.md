# SoftwarerepositoryHttpServer

An external HTTP file server. This can represent the cisco.com website or a HTTP server in the user's datacenter. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_password_set** | **bool** |  | [optional] 
**location_link** | **str** | HTTP/HTTPS link to the image. Accepted formats are HTTP[s]://server-hostname/share/image or HTTP[s]://serverip/share/image.   | [optional] 
**password** | **str** | Password as configured on the HTTP[S] server for user authentication. It is generally required to authenticate user provided HTTP[S] based software repositories.   | [optional] 
**username** | **str** | Username as configured on the HTTP[S] server for user authentication. It is generally required to authenticate user provided HTTP[S] based software repositories.    | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


