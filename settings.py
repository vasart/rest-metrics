# Please note that MONGO_HOST and MONGO_PORT could very well be left
# out as they already default to a bare bones local 'mongod' instance.
MONGO_HOST = '127.0.0.1'
MONGO_PORT = 27017

# Skip these if your db has no auth. But it really should.
MONGO_USERNAME = 'admin'
MONGO_PASSWORD = '*'

MONGO_DBNAME = 'admin'

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PUT']

# Hypermedia as the Engine of Application State
HATEOAS = False

DATE_FORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'

metrics = {
  'type': 'dict',
  'schema': {
    'timestamp': {
        'type': 'datetime',
	'required': True,
    },
    'agent': {
	'type': 'dict',
	'schema': {
	    'code_name': { 'type': 'string', 'minlength': 3, 'required': True, },
	    'full_name': { 'type': 'string', 'minlength': 8, 'required': True, },
	    'version_name': { 'type': 'string', 'minlength': 1, 'required': True, },
	    'version_code': { 'type': 'integer', 'required': True, },
	    'secret_key': { 'type': 'string', },
	    'install_guid': { 'type': 'string', 'minlength': 36, 'required': True, },
	},
	'required': True,
    },
    'metrics': {
	'allow_unknown': True,
	'type': 'dict',
	'required': True,
    }
  }
}

DOMAIN = {
    'metrics': metrics
}
