# curl

## Options

* -d
    
    (HTTP) Sends the specified data in a POST request to the HTTP server, in the same way that a browser does when a user has filled in an HTML form and presses the submit button.  This will cause curl to pass the data to the server using the content-type application/x-www-form-urlencoded.  Compare to -F, --form.

    --data-raw is almost the same but does not have a special interpretation of the @ character. To post data purely binary, you should instead use the --data-binary option.  To URL-en‐      
    code the value of a form field you may use --data-urlencode.

    If any of these options is used more than once on the same command line, the data pieces specified will be merged together with a separating &-symbol. Thus, using '-d name=daniel -d      skill=lousy' would generate a post chunk that looks like 'name=daniel&skill=lousy'.

    If  you  start the data with the letter @, the rest should be a file name to read the data from, or - if you want curl to read the data from stdin. Multiple files can also be specified. Posting data from a file named 'foobar' would thus be done with -d, --data @foobar. When --data is told to read from a file like that, carriage returns and newlines will be stripped out. If you don't want the @ character to have a special interpretation use --data-raw instead.

* -X 

    (HTTP)  Specifies  a  custom request method to use when communicating with the HTTP server.  The specified request method will be used instead of the method otherwise used (which defaults to GET). Read the HTTP 1.1 specification for details and explanations. Common additional HTTP requests include PUT and  DELETE,  but  related  technologies like WebDAV offers PROPFIND, COPY, MOVE and more.

* -k, --insecure
    
    (TLS) By default, every SSL connection curl makes is verified to be secure. This option allows curl to proceed and operate even for server connections otherwise considered insecure.

    The server connection is verified by making sure the server's certificate contains the right name and verifies successfully using the cert store.

    See this online resource for further details: https://curl.haxx.se/docs/sslcerts.html
    
    Resolves `curl: (60) SSL certificate problem`