## Chimera transmission structure

|DATA_SIZE|ACK_CODE|DATA|
- DATA_SIZE : contains the size in bytes of data transmitted for verification
- ACK_CODE : when Cataclysm requests data,  it sends a unique ACK code which is repeated back to identify the request the data belongs to
- DATA : data Cataclysm requested

## Cataclysm transmission structure
|DATA_SIZE|ACK_CODE|SET_GET|MODULE|DATA|
- SET_GET : Tells whether or not Cataclysm in communicating new values or requesting data from Chimera

MODULES: 
	0 : Test module