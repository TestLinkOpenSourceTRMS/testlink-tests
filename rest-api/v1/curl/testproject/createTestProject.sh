#!/bin/bash
# curl -i -X POST -u dev01:dev01 http://localhost/development/tlrepo/lib/api/rest/v1/testprojects
# -i include headers
# -X (HTTP) Specifies a custom request method to use when communicating with the HTTP server  
# -u user:password
# --data If you start the data with the letter @, the rest should be a file name to read the data from, 
#        or - if you want curl to read the data from stdin. 
#        The contents of the file must already be URL-encoded. 
#        Multiple files can also be specified. 
#        Posting data from a file named 'foobar' would thus be done with --data @foobar.
#
echo 'Testing TestLink REST API - POST /testprojects'
TURL="http://localhost/development/github/testlink-code";
TURL="$TURL/lib/api/rest/v2/testprojects"
# AUTH="restapi-leader:dev01"
AUTH="restapi-admin:fruta"

curl -i -H "Content-Type: application/json" -X POST --data "@../json/createTestProject.json" -u $AUTH $TURL