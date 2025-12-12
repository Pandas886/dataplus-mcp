# Trino - Connectors

**Pages:** 45

---

## TPC-DS connector — Trino 478 Documentation

**URL:** https://trino.io/docs/current/connector/tpcds.html

**Contents:**
- TPC-DS connector#
- Configuration#
- TPC-DS schemas#
- Type mapping#
- SQL support#

The TPC-DS connector provides a set of schemas to support the TPC Benchmark™ DS (TPC-DS). TPC-DS is a database benchmark used to measure the performance of complex decision support databases.

This connector can be used to test the capabilities and query syntax of Trino without configuring access to an external data source. When you query a TPC-DS schema, the connector generates the data on the fly using a deterministic algorithm.

Use the Faker connector to create and query arbitrary data.

To configure the TPC-DS connector, create a catalog properties file etc/catalog/example.properties with the following contents:

The TPC-DS connector supplies several schemas:

Ignore the standard schema information_schema, which exists in every catalog, and is not directly provided by the TPC-DS connector.

Every TPC-DS schema provides the same set of tables. Some tables are identical in all schemas. The scale factor of the tables in a particular schema is determined from the schema name. For example, the schema sf1 corresponds to scale factor 1 and the schema sf300 corresponds to scale factor 300. Every unit in the scale factor corresponds to a gigabyte of data. For example, for scale factor 300, a total of 300 gigabytes are generated. The tiny schema is an alias for scale factor 0.01, which is a very small data set useful for testing.

Trino supports all data types used within the TPC-DS schemas so no mapping is required.

The connector provides globally available and read operation statements to access data and metadata in the TPC-DS dataset.

**Examples:**

Example 1 (unknown):
```unknown
connector.name=tpcds
```

Example 2 (unknown):
```unknown
connector.name=tpcds
```

Example 3 (unknown):
```unknown
SHOW SCHEMAS FROM example;
```

Example 4 (unknown):
```unknown
SHOW SCHEMAS FROM example;
```

---

## 404 - Connector removed — Trino 478 Documentation

**URL:** https://trino.io/docs/current/connector/removed.html

**Contents:**
- 404 - Connector removed#

The connector you are trying to learn more about has been removed in a prior Trino release. Refer to the list of connectors and release notes for details.

---

## ANALYZE — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/analyze.html

**Contents:**
- ANALYZE#
- Synopsis#
- Description#
- Examples#

Collects table and column statistics for a given table.

The optional WITH clause can be used to provide connector-specific properties. To list all available properties, run the following query:

Analyze table web to collect table and column statistics:

Analyze table stores in catalog hive and schema default:

Analyze partitions '1992-01-01', '1992-01-02' from a Hive partitioned table sales:

Analyze partitions with complex partition key (state and city columns) from a Hive partitioned table customers:

Analyze only columns department and product_id for partitions '1992-01-01', '1992-01-02' from a Hive partitioned table sales:

**Examples:**

Example 1 (unknown):
```unknown
ANALYZE table_name [ WITH ( property_name = expression [, ...] ) ]
```

Example 2 (unknown):
```unknown
ANALYZE table_name [ WITH ( property_name = expression [, ...] ) ]
```

Example 3 (unknown):
```unknown
SELECT * FROM system.metadata.analyze_properties
```

Example 4 (unknown):
```unknown
SELECT * FROM system.metadata.analyze_properties
```

---

## TPC-H connector — Trino 478 Documentation

**URL:** https://trino.io/docs/current/connector/tpch.html

**Contents:**
- TPC-H connector#
- Configuration#
- TPC-H schemas#
- Type mapping#
- SQL support#

The TPC-H connector provides a set of schemas to support the TPC Benchmark™ H (TPC-H). TPC-H is a database benchmark used to measure the performance of highly-complex decision support databases.

This connector can be used to test the capabilities and query syntax of Trino without configuring access to an external data source. When you query a TPC-H schema, the connector generates the data on the fly using a deterministic algorithm.

Use the Faker connector to create and query arbitrary data.

To configure the TPC-H connector, create a catalog properties file etc/catalog/example.properties with the following contents:

In the TPC-H specification, each column is assigned a prefix based on its corresponding table name, such as l_ for the lineitem table. By default, the TPC-H connector simplifies column names by excluding these prefixes with the default of tpch.column-naming to SIMPLIFIED. To use the long, standard column names, use the configuration in the catalog properties file:

The TPC-H connector supplies several schemas:

Ignore the standard schema information_schema, which exists in every catalog, and is not directly provided by the TPC-H connector.

Every TPC-H schema provides the same set of tables. Some tables are identical in all schemas. Other tables vary based on the scale factor, which is determined based on the schema name. For example, the schema sf1 corresponds to scale factor 1 and the schema sf300 corresponds to scale factor 300. The TPC-H connector provides an infinite number of schemas for any scale factor, not just the few common ones listed by SHOW SCHEMAS. The tiny schema is an alias for scale factor 0.01, which is a very small data set useful for testing.

Trino supports all data types used within the TPC-H schemas so no mapping is required.

The connector provides globally available and read operation statements to access data and metadata in the TPC-H dataset.

**Examples:**

Example 1 (unknown):
```unknown
connector.name=tpch
```

Example 2 (unknown):
```unknown
connector.name=tpch
```

Example 3 (unknown):
```unknown
tpch.column-naming=STANDARD
```

Example 4 (unknown):
```unknown
tpch.column-naming=STANDARD
```

---

## System connector — Trino 478 Documentation

**URL:** https://trino.io/docs/current/connector/system.html

**Contents:**
- System connector#
- Configuration#
- Using the System connector#
- System connector tables#
  - metadata.catalogs#
  - metadata.schema_properties#
  - metadata.table_properties#
  - metadata.materialized_views#
  - metadata.materialized_view_properties#
  - metadata.table_comments#

The System connector provides information and metrics about the currently running Trino cluster. It makes this available via normal SQL queries.

The System connector doesn’t need to be configured: it is automatically available via a catalog named system.

List the available system schemas:

List the tables in one of the schemas:

Query one of the tables:

Kill a running query:

The catalogs table contains the list of available catalogs.

The schema properties table contains the list of available properties that can be set when creating a new schema.

The table properties table contains the list of available properties that can be set when creating a new table.

The materialized views table contains the following information about all materialized views:

Name of the catalog containing the materialized view.

Name of the schema in catalog_name containing the materialized view.

Name of the materialized view.

Name of the catalog used for the storage table backing the materialized view.

Name of the schema in storage_catalog used for the storage table backing the materialized view.

Name of the storage table backing the materialized view.

Freshness of data in the storage table. Queries on the materialized view access the storage table if not STALE, otherwise the definition is used to access the underlying data in the source tables.

Date and time of the last refresh of the materialized view.

User supplied text about the materialized view.

SQL query that defines the data provided by the materialized view.

The materialized view properties table contains the list of available properties that can be set when creating a new materialized view.

The table comments table contains the list of table comment.

The nodes table contains the list of visible nodes in the Trino cluster along with their status.

The optimizer_rule_stats table contains the statistics for optimizer rule invocations during the query planning phase. The statistics are aggregated over all queries since the server start-up. The table contains information about invocation frequency, failure rates and performance for optimizer rules. For example, you can look at the multiplication of columns invocations and average_time to get an idea about which rules generally impact query planning times the most.

The queries table contains information about currently and recently running queries on the Trino cluster. From this table you can find out the original query SQL text, the identity of the user who ran the query, and performance information about the query, including how long the query was queued and analyzed.

The tasks table contains information about the tasks involved in a Trino query, including where they were executed, and how many rows and bytes each task processed.

The transactions table contains the list of currently open transactions and related metadata. This includes information such as the create time, idle time, initialization parameters, and accessed catalogs.

Kill the query identified by query_id. The query failure message includes the specified message. message is optional.

Trino supports all data types used within the System schemas so no mapping is required.

The connector provides globally available and read operation statements to access Trino system data and metadata.

**Examples:**

Example 1 (unknown):
```unknown
SHOW SCHEMAS FROM system;
```

Example 2 (unknown):
```unknown
SHOW SCHEMAS FROM system;
```

Example 3 (unknown):
```unknown
SHOW TABLES FROM system.runtime;
```

Example 4 (unknown):
```unknown
SHOW TABLES FROM system.runtime;
```

---

## Kafka connector — Trino 478 Documentation

**URL:** https://trino.io/docs/current/connector/kafka.html

**Contents:**
- Kafka connector#
- Requirements#
- Configuration#
  - Multiple Kafka clusters#
  - Log levels#
- Configuration properties#
  - kafka.default-schema#
  - kafka.nodes#
  - kafka.buffer-size#
  - kafka.timestamp-upper-bound-force-push-down-enabled#

This connector allows the use of Apache Kafka topics as tables in Trino. Each message is presented as a row in Trino.

Topics can be live. Rows appear as data arrives, and disappear as segments get dropped. This can result in strange behavior if accessing the same table multiple times in a single query (e.g., performing a self join).

The connector reads and writes message data from Kafka topics in parallel across workers to achieve a significant performance gain. The size of data sets for this parallelization is configurable and can therefore be adapted to your specific needs.

See the Kafka connector tutorial.

To connect to Kafka, you need:

Kafka broker version 3.3 or higher (with KRaft enabled).

Network access from the Trino coordinator and workers to the Kafka nodes. Port 9092 is the default port.

When using Protobuf decoder with the Confluent table description supplier, the following additional steps must be taken:

Copy the kafka-protobuf-provider and kafka-protobuf-types JAR files from Confluent for Confluent version 7.9.0 to the Kafka connector plugin directory (<install directory>/plugin/kafka) on all nodes in the cluster. The plugin directory depends on the Installation method.

By copying those JARs and using them, you agree to the terms of the Confluent Community License Agreement under which Confluent makes them available.

These steps are not required if you are not using Protobuf and Confluent table description supplier.

To configure the Kafka connector, create a catalog properties file etc/catalog/example.properties with the following content, replacing the properties as appropriate.

In some cases, such as when using specialized authentication methods, it is necessary to specify additional Kafka client properties in order to access your Kafka cluster. To do so, add the kafka.config.resources property to reference your Kafka config files. Note that configs can be overwritten if defined explicitly in kafka.properties:

You can have as many catalogs as you need, so if you have additional Kafka clusters, simply add another properties file to etc/catalog with a different name (making sure it ends in .properties). For example, if you name the property file sales.properties, Trino creates a catalog named sales using the configured connector.

Kafka consumer logging can be verbose and pollute Trino logs. To lower the log level, simply add the following to etc/log.properties:

The following configuration properties are available:

Default schema name for tables.

List of nodes in the Kafka cluster.

Kafka read buffer size.

kafka.hide-internal-columns

Controls whether internal columns are part of the table schema or not.

kafka.internal-column-prefix

Prefix for internal columns, defaults to _

kafka.messages-per-split

Number of messages that are processed by each Trino split; defaults to 100000.

kafka.protobuf-any-support-enabled

Enable support for encoding Protobuf any types to JSON by setting the property to true, defaults to false.

kafka.timestamp-upper-bound-force-push-down-enabled

Controls if upper bound timestamp pushdown is enabled for topics using CreateTime mode.

kafka.security-protocol

Security protocol for connection to Kafka cluster; defaults to PLAINTEXT.

kafka.ssl.keystore.location

Location of the keystore file.

kafka.ssl.keystore.password

Password for the keystore file.

kafka.ssl.keystore.type

File format of the keystore file; defaults to JKS.

kafka.ssl.truststore.location

Location of the truststore file.

kafka.ssl.truststore.password

Password for the truststore file.

kafka.ssl.truststore.type

File format of the truststore file; defaults to JKS.

kafka.ssl.key.password

Password for the private key in the keystore file.

kafka.ssl.endpoint-identification-algorithm

Endpoint identification algorithm used by clients to validate server host name; defaults to https.

kafka.config.resources

A comma-separated list of Kafka client configuration files. These files must exist on the machines running Trino. Only specify this if absolutely necessary to access Kafka. Example: /etc/kafka-configuration.properties

In addition, you must configure table schema and schema registry usage with the relevant properties.

Defines the schema which contains all tables that were defined without a qualifying schema name.

This property is optional; the default is default.

A comma separated list of hostname:port pairs for the Kafka data nodes.

This property is required; there is no default and at least one node must be defined.

Trino must still be able to connect to all nodes of the cluster even if only a subset is specified here, as segment files may be located only on a specific node.

Size of the internal data buffer for reading data from Kafka. The data buffer must be able to hold at least one message and ideally can hold many messages. There is one data buffer allocated per worker and data node.

This property is optional; the default is 64kb.

The upper bound predicate on _timestamp column is pushed down only for topics using LogAppendTime mode.

For topics using CreateTime mode, upper bound pushdown must be explicitly enabled via kafka.timestamp-upper-bound-force-push-down-enabled config property or timestamp_upper_bound_force_push_down_enabled session property.

This property is optional; the default is false.

In addition to the data columns defined in a table description file, the connector maintains a number of additional columns for each table. If these columns are hidden, they can still be used in queries but do not show up in DESCRIBE <table-name> or SELECT *.

This property is optional; the default is true.

Protocol used to communicate with brokers. Valid values are: PLAINTEXT, SSL.

This property is optional; default is PLAINTEXT.

Location of the keystore file used for connection to Kafka cluster.

This property is optional.

Password for the keystore file used for connection to Kafka cluster.

This property is optional, but required when kafka.ssl.keystore.location is given.

File format of the keystore file. Valid values are: JKS, PKCS12.

This property is optional; default is JKS.

Location of the truststore file used for connection to Kafka cluster.

This property is optional.

Password for the truststore file used for connection to Kafka cluster.

This property is optional, but required when kafka.ssl.truststore.location is given.

File format of the truststore file. Valid values are: JKS, PKCS12.

This property is optional; default is JKS.

Password for the private key in the keystore file used for connection to Kafka cluster.

This property is optional. This is required for clients only if two-way authentication is configured, i.e. ssl.client.auth=required.

The endpoint identification algorithm used by clients to validate server host name for connection to Kafka cluster. Kafka uses https as default. Use disabled to disable server host name validation.

This property is optional; default is https.

The internal column prefix is configurable by kafka.internal-column-prefix configuration property and defaults to _. A different prefix affects the internal column names in the following sections. For example, a value of internal_ changes the partition ID column name from _partition_id to internal_partition_id.

For each defined table, the connector maintains the following columns:

ID of the Kafka partition which contains this row.

Offset within the Kafka partition for this row.

Lowest offset in the segment (inclusive) which contains this row. This offset is partition specific.

Highest offset in the segment (exclusive) which contains this row. The offset is partition specific. This is the same value as _segment_start of the next segment (if it exists).

Running count for the current row within the segment. For an uncompacted topic, _segment_start + _segment_count is equal to _partition_offset.

True if the decoder could not decode the message for this row. When true, data columns mapped from the message should be treated as invalid.

Message bytes as a UTF-8 encoded string. This is only useful for a text topic.

Number of bytes in the message.

map(VARCHAR, array(VARBINARY))

Headers of the message where values with the same key are grouped as array.

True if the key decoder could not decode the key for this row. When true, data columns mapped from the key should be treated as invalid.

Key bytes as a UTF-8 encoded string. This is only useful for textual keys.

Number of bytes in the key.

For tables without a table definition file, the _key_corrupt and _message_corrupt columns will always be false.

The table schema for the messages can be supplied to the connector with a configuration file or a schema registry. It also provides a mechanism for the connector to discover tables.

You must configure the supplier with the kafka.table-description-supplier property, setting it to FILE or CONFLUENT. Each table description supplier has a separate set of configuration properties.

Refer to the following subsections for more detail. The FILE table description supplier is the default, and the value is case-insensitive.

In order to use the file-based table description supplier, the kafka.table-description-supplier must be set to FILE, which is the default.

In addition, you must set kafka.table-names and kafka.table-description-dir as described in the following sections:

Comma-separated list of all tables provided by this catalog. A table name can be unqualified (simple name), and is placed into the default schema (see below), or it can be qualified with a schema name (<schema-name>.<table-name>).

For each table defined here, a table description file (see below) may exist. If no table description file exists, the table name is used as the topic name on Kafka, and no data columns are mapped into the table. The table still contains all internal columns (see below).

This property is required; there is no default and at least one table must be defined.

References a folder within Trino deployment that holds one or more JSON files (must end with .json) which contain table description files.

This property is optional; the default is etc/kafka.

Kafka maintains topics only as byte messages and leaves it to producers and consumers to define how a message should be interpreted. For Trino, this data must be mapped into columns to allow queries against the data.

For textual topics that contain JSON data, it is entirely possible to not use any table definition files, but instead use the Trino JSON functions and operators to parse the _message column which contains the bytes mapped into a UTF-8 string. This is cumbersome and makes it difficult to write SQL queries. This only works when reading data.

A table definition file consists of a JSON definition for a table. The name of the file can be arbitrary but must end in .json. Place the file in the directory configured with the kafka.table-description-dir property. The table definition file must be accessible from all Trino nodes.

Trino table name defined by this file.

Schema containing the table. If omitted, the default schema name is used.

Kafka topic that is mapped.

Field definitions for data columns mapped to the message key.

Field definitions for data columns mapped to the message itself.

Starting with Kafka 0.8, each message in a topic can have an optional key. A table definition file contains sections for both key and message to map the data onto table columns.

Each of the key and message fields in the table definition is a JSON object that must contain two fields:

Selects the decoder for this group of fields.

A list of field definitions. Each field definition creates a new column in the Trino table.

Each field definition is a JSON object:

Name of the column in the Trino table.

Trino type of the column.

Selects the column decoder for this field. Defaults to the default decoder for this row data format and column type.

The path or URL where the Avro schema resides. Used only for Avro decoder.

Mapping information for the column. This is decoder specific, see below.

Sets a column-specific format hint to the column decoder.

Hides the column from DESCRIBE <table name> and SELECT *. Defaults to false.

Adds a column comment, which is shown with DESCRIBE <table name>.

There is no limit on field descriptions for either key or message.

The Confluent table description supplier uses the Confluent Schema Registry to discover table definitions. It is only tested to work with the Confluent Schema Registry.

The benefits of using the Confluent table description supplier over the file table description supplier are:

New tables can be defined without a cluster restart.

Schema updates are detected automatically.

There is no need to define tables manually.

Some Protobuf specific types like oneof and any are supported and mapped to JSON.

When using Protobuf decoder with the Confluent table description supplier, some additional steps are necessary. For details, refer to Requirements.

Set kafka.table-description-supplier to CONFLUENT to use the schema registry. You must also configure the additional properties in the following table:

Inserts are not supported, and the only data format supported is AVRO.

kafka.confluent-schema-registry-url

Comma-separated list of URL addresses for the Confluent schema registry. For example, http://schema-registry-1.example.org:8081,http://schema-registry-2.example.org:8081

kafka.confluent-schema-registry-client-cache-size

The maximum number of subjects that can be stored in the local cache. The cache stores the schemas locally by subjectId, and is provided by the Confluent CachingSchemaRegistry client.

kafka.empty-field-strategy

Avro allows empty struct fields, but this is not allowed in Trino. There are three strategies for handling empty struct fields:

IGNORE - Ignore structs with no fields. This propagates to parents. For example, an array of structs with no fields is ignored.

FAIL - Fail the query if a struct with no fields is defined.

MARK - Add a marker field named $empty_field_marker, which of type boolean with a null value. This may be desired if the struct represents a marker field.

This can also be modified via the empty_field_strategy session property.

kafka.confluent-subjects-cache-refresh-interval

The interval used for refreshing the list of subjects and the definition of the schema for the subject in the subject’s cache.

The subject naming strategy determines how a subject is resolved from the table name.

The default strategy is the TopicNameStrategy, where the key subject is defined as <topic-name>-key and the value subject is defined as <topic-name>-value. If other strategies are used there is no way to determine the subject name beforehand, so it must be specified manually in the table name.

To manually specify the key and value subjects, append to the topic name, for example: <topic name>&key-subject=<key subject>&value-subject=<value subject>. Both the key-subject and value-subject parameters are optional. If neither is specified, then the default TopicNameStrategy is used to resolve the subject name via the topic name. Note that a case-insensitive match must be done, as identifiers cannot contain upper case characters.

When using the Confluent table description supplier, the following Protobuf specific types are supported in addition to the normally supported types:

Protobuf schemas containing oneof fields are mapped to a JSON field in Trino.

For example, given the following Protobuf schema:

The corresponding Trino row is a JSON field test_oneof_column containing a JSON object with a single key. The value of the key matches the name of the oneof type that is present.

In the above example, if the Protobuf message has the test_oneof_column containing string_column set to a value Trino then the corresponding Trino row includes a column named test_oneof_column with the value JSON '{"string_column": "Trino"}'.

The Kafka connector supports the use of INSERT statements to write data to a Kafka topic. Table column data is mapped to Kafka messages as defined in the table definition file. There are five supported data formats for key and message encoding:

These data formats each have an encoder that maps column values into bytes to be sent to a Kafka topic.

Trino supports at-least-once delivery for Kafka producers. This means that messages are guaranteed to be sent to Kafka topics at least once. If a producer acknowledgement times out, or if the producer receives an error, it might retry sending the message. This could result in a duplicate message being sent to the Kafka topic.

The Kafka connector does not allow the user to define which partition will be used as the target for a message. If a message includes a key, the producer will use a hash algorithm to choose the target partition for the message. The same key will always be assigned the same partition.

Because Trino and Kafka each support types that the other does not, this connector maps some types when reading (decoding) or writing (encoding) data. Type mapping depends on the format (Raw, Avro, JSON, CSV).

Encoding is required to allow writing data; it defines how table columns in Trino map to Kafka keys and message data.

The Kafka connector contains the following encoders:

raw encoder - Table columns are mapped to a Kafka message as raw bytes.

CSV encoder - Kafka message is formatted as a comma-separated value.

JSON encoder - Table columns are mapped to JSON fields.

Avro encoder - Table columns are mapped to Avro fields based on an Avro schema.

Protobuf encoder - Table columns are mapped to Protobuf fields based on a Protobuf schema.

A table definition file must be defined for the encoder to work.

The raw encoder formats the table columns as raw bytes using the mapping information specified in the table definition file.

The following field attributes are supported:

dataFormat - Specifies the width of the column data type.

type - Trino data type.

mapping - start and optional end position of bytes to convert (specified as start or start:end).

The dataFormat attribute selects the number of bytes converted. If absent, BYTE is assumed. All values are signed.

SHORT - two bytes (big-endian)

INT - four bytes (big-endian)

LONG - eight bytes (big-endian)

FLOAT - four bytes (IEEE 754 format, big-endian)

DOUBLE - eight bytes (IEEE 754 format, big-endian)

The type attribute defines the Trino data type.

Different values of dataFormat are supported, depending on the Trino data type:

BYTE, SHORT, INT, LONG

BYTE, SHORT, INT, LONG

No other types are supported.

The mapping attribute specifies the range of bytes in a key or message used for encoding.

Both a start and end position must be defined for VARCHAR types. Otherwise, there is no way to know how many bytes the message contains. The raw format mapping information is static and cannot be dynamically changed to fit the variable width of some Trino data types.

If only a start position is given:

For fixed width types, the appropriate number of bytes are used for the specified dataFormat (see above).

If both a start and end position are given, then:

For fixed width types, the size must be equal to number of bytes used by specified dataFormat.

All bytes between start (inclusive) and end (exclusive) are used.

All mappings must include a start position for encoding to work.

The encoding for numeric data types (BIGINT, INTEGER, SMALLINT, TINYINT, REAL, DOUBLE) is straightforward. All numeric types use big-endian. Floating point types use IEEE 754 format.

Example raw field definition in a table definition file for a Kafka message:

Columns should be defined in the same order they are mapped. There can be no gaps or overlaps between column mappings. The width of the column as defined by the column mapping must be equivalent to the width of the dataFormat for all types except for variable width types.

Example insert query for the above table definition:

The raw encoder requires the field size to be known ahead of time, including for variable width data types like VARCHAR. It also disallows inserting values that do not match the width defined in the table definition file. This is done to ensure correctness, as otherwise longer values are truncated, and shorter values are read back incorrectly due to an undefined padding character.

The CSV encoder formats the values for each row as a line of comma-separated-values (CSV) using UTF-8 encoding. The CSV line is formatted with a comma , as the column delimiter.

The type and mapping attributes must be defined for each field:

type - Trino data type

mapping - The integer index of the column in the CSV line (the first column is 0, the second is 1, and so on)

dataFormat and formatHint are not supported and must be omitted.

The following Trino data types are supported by the CSV encoder:

No other types are supported.

Column values are converted to strings before they are formatted as a CSV line.

The following is an example CSV field definition in a table definition file for a Kafka message:

Example insert query for the above table definition:

The JSON encoder maps table columns to JSON fields defined in the table definition file according to RFC 4627.

For fields, the following attributes are supported:

type - Trino data type of column.

mapping - A slash-separated list of field names to select a field from the JSON object.

dataFormat - Name of formatter. Required for temporal types.

formatHint - Pattern to format temporal data. Only use with custom-date-time formatter.

The following Trino data types are supported by the JSON encoder:

TIMESTAMP WITH TIME ZONE

No other types are supported.

The following dataFormats are available for temporal data:

custom-date-time - Formats temporal data according to Joda Time pattern given by formatHint field.

milliseconds-since-epoch

All temporal data in Kafka supports milliseconds precision.

The following table defines which temporal data types are supported by dataFormats:

custom-date-time, iso8601

custom-date-time, iso8601, milliseconds-since-epoch, seconds-since-epoch

custom-date-time, iso8601

custom-date-time, iso8601, rfc2822, milliseconds-since-epoch, seconds-since-epoch

TIMESTAMP WITH TIME ZONE

custom-date-time, iso8601, rfc2822, milliseconds-since-epoch, seconds-since-epoch

The following is an example JSON field definition in a table definition file for a Kafka message:

The following shows an example insert query for the preceding table definition:

The Avro encoder serializes rows to Avro records as defined by the Avro schema. Trino does not support schemaless Avro encoding.

The Avro schema is encoded with the table column values in each Kafka message.

The dataSchema must be defined in the table definition file to use the Avro encoder. It points to the location of the Avro schema file for the key or message.

Avro schema files can be retrieved via HTTP or HTTPS from remote server with the syntax:

"dataSchema": "http://example.org/schema/avro_data.avsc"

Local files need to be available on all Trino nodes and use an absolute path in the syntax, for example:

"dataSchema": "/usr/local/schema/avro_data.avsc"

The following field attributes are supported:

name - Name of the column in the Trino table.

type - Trino data type of column.

mapping - A slash-separated list of field names to select a field from the Avro schema. If the field specified in mapping does not exist in the original Avro schema, then a write operation fails.

The following table lists supported Trino data types, which can be used in type for the equivalent Avro field type.

No other types are supported.

The following example shows an Avro field definition in a table definition file for a Kafka message:

In the following example, an Avro schema definition for the preceding table definition is shown:

The following is an example insert query for the preceding table definition:

VALUES (123456789, ‘example text’, FALSE);

The Protobuf encoder serializes rows to Protobuf DynamicMessages as defined by the Protobuf schema.

The Protobuf schema is encoded with the table column values in each Kafka message.

The dataSchema must be defined in the table definition file to use the Protobuf encoder. It points to the location of the proto file for the key or message.

Protobuf schema files can be retrieved via HTTP or HTTPS from a remote server with the syntax:

"dataSchema": "http://example.org/schema/schema.proto"

Local files need to be available on all Trino nodes and use an absolute path in the syntax, for example:

"dataSchema": "/usr/local/schema/schema.proto"

The following field attributes are supported:

name - Name of the column in the Trino table.

type - Trino type of column.

mapping - slash-separated list of field names to select a field from the Protobuf schema. If the field specified in mapping does not exist in the original Protobuf schema, then a write operation fails.

The following table lists supported Trino data types, which can be used in type for the equivalent Protobuf field type.

int32, uint32, sint32, fixed32, sfixed32

int64, uint64, sint64, fixed64, sfixed64

Protobuf type with repeated field

Timestamp, predefined in timestamp.proto

The following example shows a Protobuf field definition in a table definition file for a Kafka message:

In the following example, a Protobuf schema definition for the preceding table definition is shown:

The following is an example insert query for the preceding table definition:

For key and message, a decoder is used to map message and key data onto table columns.

The Kafka connector contains the following decoders:

raw - Kafka message is not interpreted; ranges of raw message bytes are mapped to table columns.

csv - Kafka message is interpreted as comma separated message, and fields are mapped to table columns.

json - Kafka message is parsed as JSON, and JSON fields are mapped to table columns.

avro - Kafka message is parsed based on an Avro schema, and Avro fields are mapped to table columns.

protobuf - Kafka message is parsed based on a Protobuf schema, and Protobuf fields are mapped to table columns.

If no table definition file exists for a table, the dummy decoder is used, which does not expose any columns.

The raw decoder supports reading of raw byte-based values from Kafka message or key, and converting it into Trino columns.

For fields, the following attributes are supported:

dataFormat - Selects the width of the data type converted.

type - Trino data type. See table later min this document for list of supported data types.

mapping - <start>[:<end>] - Start and end position of bytes to convert (optional).

The dataFormat attribute selects the number of bytes converted. If absent, BYTE is assumed. All values are signed.

Supported values are:

SHORT - two bytes (big-endian)

INT - four bytes (big-endian)

LONG - eight bytes (big-endian)

FLOAT - four bytes (IEEE 754 format)

DOUBLE - eight bytes (IEEE 754 format)

The type attribute defines the Trino data type on which the value is mapped.

Depending on the Trino type assigned to a column, different values of dataFormat can be used:

Allowed dataFormat values

BYTE, SHORT, INT, LONG

BYTE, SHORT, INT, LONG

No other types are supported.

The mapping attribute specifies the range of the bytes in a key or message used for decoding. It can be one or two numbers separated by a colon (<start>[:<end>]).

If only a start position is given:

For fixed width types, the column will use the appropriate number of bytes for the specified dataFormat (see above).

When VARCHAR value is decoded, all bytes from start position till the end of the message will be used.

If start and end position are given:

For fixed width types, the size must be equal to number of bytes used by specified dataFormat.

For VARCHAR all bytes between start (inclusive) and end (exclusive) are used.

If no mapping attribute is specified, it is equivalent to setting start position to 0 and leaving end position undefined.

The decoding scheme of numeric data types (BIGINT, INTEGER, SMALLINT, TINYINT, DOUBLE) is straightforward. A sequence of bytes is read from input message and decoded according to either:

big-endian encoding (for integer types)

IEEE 754 format for (for DOUBLE).

Length of decoded byte sequence is implied by the dataFormat.

For VARCHAR data type a sequence of bytes is interpreted according to UTF-8 encoding.

The CSV decoder converts the bytes representing a message or key into a string using UTF-8 encoding and then interprets the result as a CSV (comma-separated value) line.

For fields, the type and mapping attributes must be defined:

type - Trino data type. See the following table for a list of supported data types.

mapping - The index of the field in the CSV record.

The dataFormat and formatHint attributes are not supported and must be omitted.

Table below lists supported Trino types, which can be used in type and decoding scheme:

BIGINT, INTEGER, SMALLINT, TINYINT

Decoded using Java Long.parseLong()

Decoded using Java Double.parseDouble()

“true” character sequence maps to true; Other character sequences map to false

No other types are supported.

The JSON decoder converts the bytes representing a message or key into a JSON according to RFC 4627. Note that the message or key MUST convert into a JSON object, not an array or simple type.

For fields, the following attributes are supported:

type - Trino data type of column.

dataFormat - Field decoder to be used for column.

mapping - slash-separated list of field names to select a field from the JSON object.

formatHint - Only for custom-date-time.

The JSON decoder supports multiple field decoders, with _default being used for standard table columns and a number of decoders for date- and time-based types.

The following table lists Trino data types, which can be used as in type, and matching field decoders, which can be specified via dataFormat attribute.

Allowed dataFormat values

BIGINT, INTEGER, SMALLINT, TINYINT, DOUBLE, BOOLEAN, VARCHAR, VARCHAR(x)

Default field decoder (omitted dataFormat attribute)

custom-date-time, iso8601

custom-date-time, iso8601, milliseconds-since-epoch, seconds-since-epoch

custom-date-time, iso8601

custom-date-time, iso8601, rfc2822, milliseconds-since-epoch, seconds-since-epoch

TIMESTAMP WITH TIME ZONE

custom-date-time, iso8601, rfc2822, milliseconds-since-epoch seconds-since-epoch

No other types are supported.

This is the standard field decoder, supporting all the Trino physical data types. A field value is transformed under JSON conversion rules into boolean, long, double or string values. For non-date/time based columns, this decoder should be used.

To convert values from JSON objects into Trino DATE, TIME, TIME WITH TIME ZONE, TIMESTAMP or TIMESTAMP WITH TIME ZONE columns, special decoders must be selected using the dataFormat attribute of a field definition.

iso8601 - Text based, parses a text field as an ISO 8601 timestamp.

rfc2822 - Text based, parses a text field as an RFC 2822 timestamp.

specified via formatHint attribute. Format pattern should conform to https://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormat.html.

milliseconds-since-epoch - Number-based; interprets a text or number as number of milliseconds since the epoch.

seconds-since-epoch - Number-based; interprets a text or number as number of milliseconds since the epoch.

For TIMESTAMP WITH TIME ZONE and TIME WITH TIME ZONE data types, if timezone information is present in decoded value, it will be used as Trino value. Otherwise result time zone will be set to UTC.

The Avro decoder converts the bytes representing a message or key in Avro format based on a schema. The message must have the Avro schema embedded. Trino does not support schemaless Avro decoding.

For key/message, using avro decoder, the dataSchema must be defined. This should point to the location of a valid Avro schema file of the message which needs to be decoded. This location can be a remote web server (e.g.: dataSchema: 'http://example.org/schema/avro_data.avsc') or local file system(e.g.: dataSchema: '/usr/local/schema/avro_data.avsc'). The decoder fails if this location is not accessible from the Trino coordinator node.

For fields, the following attributes are supported:

name - Name of the column in the Trino table.

type - Trino data type of column.

mapping - A slash-separated list of field names to select a field from the Avro schema. If field specified in mapping does not exist in the original Avro schema, then a read operation returns NULL.

The following table lists the supported Trino types which can be used in type for the equivalent Avro field types:

Allowed Avro data type

No other types are supported.

The Avro decoder supports schema evolution feature with backward compatibility. With backward compatibility, a newer schema can be used to read Avro data created with an older schema. Any change in the Avro schema must also be reflected in Trino’s topic definition file. Newly added/renamed fields must have a default value in the Avro schema file.

The schema evolution behavior is as follows:

Column added in new schema: Data created with an older schema produces a default value when the table is using the new schema.

Column removed in new schema: Data created with an older schema no longer outputs the data from the column that was removed.

Column is renamed in the new schema: This is equivalent to removing the column and adding a new one, and data created with an older schema produces a default value when table is using the new schema.

Changing type of column in the new schema: If the type coercion is supported by Avro, then the conversion happens. An error is thrown for incompatible types.

The Protobuf decoder converts the bytes representing a message or key in Protobuf formatted message based on a schema.

For key/message, using the protobuf decoder, the dataSchema must be defined. It points to the location of a valid proto file of the message which needs to be decoded. This location can be a remote web server, dataSchema: 'http://example.org/schema/schema.proto', or local file, dataSchema: '/usr/local/schema/schema.proto'. The decoder fails if the location is not accessible from the coordinator.

For fields, the following attributes are supported:

name - Name of the column in the Trino table.

type - Trino data type of column.

mapping - slash-separated list of field names to select a field from the Protobuf schema. If field specified in mapping does not exist in the original proto file then a read operation returns NULL.

The following table lists the supported Trino types which can be used in type for the equivalent Protobuf field types:

Allowed Protobuf data type

int32, uint32, sint32, fixed32, sfixed32

int64, uint64, sint64, fixed64, sfixed64

Protobuf type with repeated field

Timestamp, predefined in timestamp.proto

oneof (Confluent table supplier only), Any

Message types with an Any field contain an arbitrary serialized message as bytes and a type URL to resolve that message’s type with a scheme of file://, http://, or https://. The connector reads the contents of the URL to create the type descriptor for the Any message and convert the message to JSON. This behavior is enabled by setting kafka.protobuf-any-support-enabled to true.

The descriptors for each distinct URL are cached for performance reasons and any modifications made to the type returned by the URL requires a restart of Trino.

For example, given the following Protobuf schema which defines MyMessage with three columns:

And a separate schema which uses an Any type which is a packed message of the above type and a valid URL:

The corresponding Trino column is named any_message of type JSON containing a JSON-serialized representation of the Protobuf message:

The Protobuf decoder supports the schema evolution feature with backward compatibility. With backward compatibility, a newer schema can be used to read Protobuf data created with an older schema. Any change in the Protobuf schema must also be reflected in the topic definition file.

The schema evolution behavior is as follows:

Column added in new schema: Data created with an older schema produces a default value when the table is using the new schema.

Column removed in new schema: Data created with an older schema no longer outputs the data from the column that was removed.

Column is renamed in the new schema: This is equivalent to removing the column and adding a new one, and data created with an older schema produces a default value when table is using the new schema.

Changing type of column in the new schema: If the type coercion is supported by Protobuf, then the conversion happens. An error is thrown for incompatible types.

Protobuf Timestamp has a nanosecond precision but Trino supports decoding/encoding at microsecond precision.

The connector provides read and write access to data and metadata in Trino tables populated by Kafka topics. See Row decoding for more information.

In addition to the globally available and read operation statements, the connector supports the following features:

INSERT, encoded to a specified data format. See also Kafka inserts.

**Examples:**

Example 1 (unknown):
```unknown
connector.name=kafka
kafka.table-names=table1,table2
kafka.nodes=host1:port,host2:port
kafka.config.resources=/etc/kafka-configuration.properties
```

Example 2 (unknown):
```unknown
connector.name=kafka
kafka.table-names=table1,table2
kafka.nodes=host1:port,host2:port
kafka.config.resources=/etc/kafka-configuration.properties
```

Example 3 (unknown):
```unknown
org.apache.kafka=WARN
```

Example 4 (unknown):
```unknown
org.apache.kafka=WARN
```

---

## OpenSearch connector — Trino 478 Documentation

**URL:** https://trino.io/docs/current/connector/opensearch.html

**Contents:**
- OpenSearch connector#
- Requirements#
- Configuration#
  - Authentication#
  - Connection security with TLS#
- Type mapping#
  - OpenSearch type to Trino type mapping#
  - Array types#
  - Date types#
  - Raw JSON transform#

The OpenSearch connector allows access to OpenSearch data from Trino. This document describes how to configure a catalog with the OpenSearch connector to run SQL queries against OpenSearch.

OpenSearch 1.1.0 or higher.

Network access from the Trino coordinator and workers to the OpenSearch nodes.

To configure the OpenSearch connector, create a catalog properties file etc/catalog/example.properties with the following content, replacing the properties as appropriate for your setup:

The following table details all general configuration properties:

The comma-separated list of host names of the OpenSearch cluster. This property is required.

Port to use to connect to OpenSearch.

opensearch.default-schema-name

The schema that contains all tables defined without a qualifying schema name.

opensearch.scroll-size

Sets the maximum number of hits that can be returned with each OpenSearch scroll request.

opensearch.scroll-timeout

Duration for OpenSearch to keep the search context alive for scroll requests.

opensearch.request-timeout

Timeout duration for all OpenSearch requests.

opensearch.connect-timeout

Timeout duration for all OpenSearch connection attempts.

opensearch.backoff-init-delay

The minimum duration between backpressure retry attempts for a single request to OpenSearch. Setting it too low can overwhelm an already struggling cluster.

opensearch.backoff-max-delay

The maximum duration between backpressure retry attempts for a single request.

opensearch.max-retry-time

The maximum duration across all retry attempts for a single request.

opensearch.node-refresh-interval

Duration between requests to refresh the list of available OpenSearch nodes.

opensearch.ignore-publish-address

Disable using the address published by the OpenSearch API to connect for queries. Some deployments map OpenSearch ports to a random public port and enabling this property can help in these cases.

opensearch.projection-pushdown-enabled

Read only projected fields from row columns while performing SELECT queries

The connection to OpenSearch can use AWS or password authentication.

To enable AWS authentication and authorization using IAM policies, the opensearch.security option must be set to AWS. Additionally, the following options must be configured:

opensearch.aws.region

AWS region of the OpenSearch endpoint. This option is required.

opensearch.aws.access-key

AWS access key to use to connect to the OpenSearch domain. If not set, the default AWS credentials provider chain is used.

opensearch.aws.secret-key

AWS secret key to use to connect to the OpenSearch domain. If not set, the default AWS credentials provider chain is used.

opensearch.aws.iam-role

Optional ARN of an IAM role to assume to connect to OpenSearch. Note that the configured IAM user must be able to assume this role.

opensearch.aws.external-id

Optional external ID to pass while assuming an AWS IAM role.

opensearch.aws.deployment-type

AWS OpenSearch deployment type. Possible values are PROVISIONED & SERVERLESS. This option is required.

To enable password authentication, the opensearch.security option must be set to PASSWORD. Additionally the following options must be configured:

Username to use to connect to OpenSearch.

opensearch.auth.password

Password to use to connect to OpenSearch.

The connector provides additional security options to connect to OpenSearch clusters with TLS enabled.

If your cluster uses globally-trusted certificates, you only need to enable TLS. If you require custom configuration for certificates, the connector supports key stores and trust stores in P12 (PKCS) or Java Key Store (JKS) format.

The available configuration values are listed in the following table:

opensearch.tls.enabled

Enable TLS security. Defaults to false.

opensearch.tls.keystore-path

The path to the P12 (PKCS) or JKS key store.

opensearch.tls.truststore-path

The path to P12 (PKCS) or JKS trust store.

opensearch.tls.keystore-password

The password for the key store specified by opensearch.tls.keystore-path.

opensearch.tls.truststore-password

The password for the trust store specified by opensearch.tls.truststore-path.

opensearch.tls.verify-hostnames

Flag to determine if the hostnames in the certificates must be verified. Defaults to true.

Because Trino and OpenSearch each support types that the other does not, the connector maps some types when reading data.

The connector maps OpenSearch types to the corresponding Trino types according to the following table:

For more information, see Date types.

No other types are supported.

Fields in OpenSearch can contain zero or more values, but there is no dedicated array type. To indicate a field contains an array, it can be annotated in a Trino-specific structure in the _meta section of the index mapping in OpenSearch.

For example, you can have an OpenSearch index that contains documents with the following structure:

The array fields of this structure can be defined by using the following command to add the field property definition to the _meta.trino property of the target index mapping with OpenSearch available at search.example.com:9200:

It is not allowed to use asRawJson and isArray flags simultaneously for the same column.

The OpenSearch connector supports only the default date type. All other OpenSearch date formats including built-in date formats and custom date formats are not supported. Dates with the format property are ignored.

Documents in OpenSearch can include more complex structures that are not represented in the mapping. For example, a single keyword field can have widely different content including a single keyword value, an array, or a multidimensional keyword array with any level of nesting.

The following command configures array_string_field mapping with OpenSearch available at search.example.com:9200:

All the following documents are legal for OpenSearch with array_string_field mapping:

See the OpenSearch array documentation for more details.

Further, OpenSearch supports types, such as k-NN vector, that are not supported in Trino. These and other types can cause parsing exceptions for users that use of these types in OpenSearch. To manage all of these scenarios, you can transform fields to raw JSON by annotating it in a Trino-specific structure in the _meta section of the OpenSearch index mapping. This indicates to Trino that the field, and all nested fields beneath, must be cast to a VARCHAR field that contains the raw JSON content. These fields can be defined by using the following command to add the field property definition to the _meta.trino property of the target index mapping.

The preceding configuration causes Trino to return the array_string_field field as a VARCHAR containing raw JSON. You can parse these fields with the built-in JSON functions.

It is not allowed to use asRawJson and isArray flags simultaneously for the same column.

The following hidden columns are available:

The OpenSearch document ID.

The document score returned by the OpenSearch query.

The source of the original document.

The connector provides globally available and read operation statements to access data and metadata in the OpenSearch catalog.

The connector provides support to query multiple tables using a concise wildcard table notation.

The connector provides specific table functions to access OpenSearch.

The raw_query function allows you to query the underlying database directly using the OpenSearch Query DSL syntax. The full DSL query is pushed down and processed in OpenSearch. This can be useful for accessing native features which are not available in Trino, or for improving query performance in situations where running a query natively may be faster.

The native query passed to the underlying data source is required to return a table as a result set. Only the data source performs validation or security checks for these queries using its own configuration. Trino does not perform these tasks. Only use passthrough queries to read data.

The raw_query function requires three parameters:

schema: The schema in the catalog that the query is to be executed on.

index: The index in OpenSearch to search.

query: The query to execute, written in OpenSearch Query DSL.

Once executed, the query returns a single row containing the resulting JSON payload returned by OpenSearch.

For example, query the example catalog and use the raw_query table function to search for documents in the orders index where the country name is ALGERIA as defined as a JSON-formatted query matcher and passed to the raw_query table function in the query parameter:

The query engine does not preserve the order of the results of this function. If the passed query contains an ORDER BY clause, the function result may not be ordered as expected.

The connector includes a number of performance improvements, detailed in the following sections.

The connector requests data from multiple nodes of the OpenSearch cluster for query processing in parallel.

The connector supports predicate push down for the following data types:

No other data types are supported for predicate push down.

**Examples:**

Example 1 (unknown):
```unknown
connector.name=opensearch
opensearch.host=search.example.com
opensearch.port=9200
opensearch.default-schema-name=default
```

Example 2 (unknown):
```unknown
connector.name=opensearch
opensearch.host=search.example.com
opensearch.port=9200
opensearch.default-schema-name=default
```

Example 3 (unknown):
```unknown
{
    "array_string_field": ["trino","the","lean","machine-ohs"],
    "long_field": 314159265359,
    "id_field": "564e6982-88ee-4498-aa98-df9e3f6b6109",
    "timestamp_field": "1987-09-17T06:22:48.000Z",
    "object_field": {
        "array_int_field": [86,75,309],
        "int_field": 2
    }
}
```

Example 4 (unknown):
```unknown
{
    "array_string_field": ["trino","the","lean","machine-ohs"],
    "long_field": 314159265359,
    "id_field": "564e6982-88ee-4498-aa98-df9e3f6b6109",
    "timestamp_field": "1987-09-17T06:22:48.000Z",
    "object_field": {
        "array_int_field": [86,75,309],
        "int_field": 2
    }
}
```

---

## Vertica connector — Trino 478 Documentation

**URL:** https://trino.io/docs/current/connector/vertica.html

**Contents:**
- Vertica connector#
- Requirements#
- Configuration#
  - General configuration properties#
  - Appending query metadata#
  - Domain compaction threshold#
  - Case insensitive matching#
- Type mapping#
  - Vertica to Trino type mapping#
  - Trino to Vertica type mapping#

The Vertica connector allows querying a Vertica database, also known as OpenText Analytics Database, as an external data source.

To connect to Vertica, you need:

Vertica 11.x or higher.

Network access from the coordinator and workers to the Vertica server. Port 5433 is the default port.

Create a catalog properties file in etc/catalog named example.properties to access the configured Vertica database in the example catalog. Replace example with your database name or some other descriptive name of the catalog. Configure the usage of the connector by specifying the name vertica and replace the connection properties as appropriate for your setup.

The connection-user and connection-password are typically required and determine the user credentials for the connection, often a service user. You can use secrets to avoid actual values in the catalog properties files.

The following table describes general catalog configuration properties for the connector:

case-insensitive-name-matching

Support case insensitive schema and table names. Defaults to false.

case-insensitive-name-matching.cache-ttl

Duration for which case insensitive schema and table names are cached. Defaults to 1m.

case-insensitive-name-matching.config-file

Path to a name mapping configuration file in JSON format that allows Trino to disambiguate between schemas and tables with similar names in different cases. Defaults to null.

case-insensitive-name-matching.config-file.refresh-period

Frequency with which Trino checks the name matching configuration file for changes. The duration value defaults to 0s (refresh disabled).

Duration for which metadata, including table and column statistics, is cached. Defaults to 0s (caching disabled).

metadata.cache-missing

Cache the fact that metadata, including table and column statistics, is not available. Defaults to false.

metadata.schemas.cache-ttl

Duration for which schema metadata is cached. Defaults to the value of metadata.cache-ttl.

metadata.tables.cache-ttl

Duration for which table metadata is cached. Defaults to the value of metadata.cache-ttl.

metadata.statistics.cache-ttl

Duration for which tables statistics are cached. Defaults to the value of metadata.cache-ttl.

metadata.cache-maximum-size

Maximum number of objects stored in the metadata cache. Defaults to 10000.

Maximum number of statements in a batched execution. Do not change this setting from the default. Non-default values may negatively impact performance. Defaults to 1000.

dynamic-filtering.enabled

Push down dynamic filters into JDBC queries. Defaults to true.

dynamic-filtering.wait-timeout

Maximum duration for which Trino waits for dynamic filters to be collected from the build side of joins before starting a JDBC query. Using a large timeout can potentially result in more detailed dynamic filters. However, it can also increase latency for some queries. Defaults to 20s.

The optional parameter query.comment-format allows you to configure a SQL comment that is sent to the datasource with each query. The format of this comment can contain any characters and the following metadata:

$QUERY_ID: The identifier of the query.

$USER: The name of the user who submits the query to Trino.

$SOURCE: The identifier of the client tool used to submit the query, for example trino-cli.

$TRACE_TOKEN: The trace token configured with the client tool.

The comment can provide more context about the query. This additional information is available in the logs of the datasource. To include environment variables from the Trino cluster with the comment , use the ${ENV:VARIABLE-NAME} syntax.

The following example sets a simple comment that identifies each query sent by Trino:

With this configuration, a query such as SELECT * FROM example_table; is sent to the datasource with the comment appended:

The following example improves on the preceding example by using metadata:

If Jane sent the query with the query identifier 20230622_180528_00000_bkizg, the following comment string is sent to the datasource:

Certain JDBC driver settings and logging configurations might cause the comment to be removed.

Pushing down a large list of predicates to the data source can compromise performance. Trino compacts large predicates into a simpler range predicate by default to ensure a balance between performance and predicate pushdown. If necessary, the threshold for this compaction can be increased to improve performance when the data source is capable of taking advantage of large predicates. Increasing this threshold may improve pushdown of large dynamic filters. The domain-compaction-threshold catalog configuration property or the domain_compaction_threshold catalog session property can be used to adjust the default value of 256 for this threshold.

When case-insensitive-name-matching is set to true, Trino is able to query non-lowercase schemas and tables by maintaining a mapping of the lowercase name to the actual name in the remote system. However, if two schemas and/or tables have names that differ only in case (such as “customers” and “Customers”) then Trino fails to query them due to ambiguity.

In these cases, use the case-insensitive-name-matching.config-file catalog configuration property to specify a configuration file that maps these remote schemas and tables to their respective Trino schemas and tables. Additionally, the JSON file must include both the schemas and tables properties, even if only as empty arrays.

Queries against one of the tables or schemes defined in the mapping attributes are run against the corresponding remote entity. For example, a query against tables in the case_insensitive_1 schema is forwarded to the CaseSensitiveName schema and a query against case_insensitive_2 is forwarded to the cASEsENSITIVEnAME schema.

At the table mapping level, a query on case_insensitive_1.table_1 as configured above is forwarded to CaseSensitiveName.tablex, and a query on case_insensitive_1.table_2 is forwarded to CaseSensitiveName.TABLEX.

By default, when a change is made to the mapping configuration file, Trino must be restarted to load the changes. Optionally, you can set the case-insensitive-name-matching.config-file.refresh-period to have Trino refresh the properties without requiring a restart:

Because Trino and Vertica each support types that the other does not, this connector modifies some types when reading or writing data. Data types may not map the same way in both directions between Trino and the data source. Refer to the following sections for type mapping in each direction.

The connector maps Vertica types to the corresponding Trino types according to the following table:

Vertica treats TINYINT, SMALLINT, INTEGER, and BIGINT as synonyms for the same 64-bit BIGINT data type

DOUBLE PRECISION (FLOAT)

Vertica treats FLOAT and REAL as the same 64-bit IEEE FLOAT

VARCHAR, LONG VARCHAR, VARCHAR(n), LONG VARCHAR(n)

VARBINARY, LONG VARBINARY, VARBINARY(n), LONG VARBINARY(n)

No other types are supported.

Unsupported Vertica types can be converted to VARCHAR with the vertica.unsupported_type_handling session property. The default value for this property is IGNORE.

The connector maps Trino types to the corresponding Vertica types according to the following table:

No other types are supported.

The following properties can be used to configure how data types from the connected data source are mapped to Trino data types and how the metadata is cached in Trino.

unsupported-type-handling

Configure how unsupported column data types are handled:

IGNORE, column is not accessible.

CONVERT_TO_VARCHAR, column is converted to unbounded VARCHAR.

The respective catalog session property is unsupported_type_handling.

jdbc-types-mapped-to-varchar

Allow forced mapping of comma separated lists of data types to convert to unbounded VARCHAR

The connector provides read and write access to data and metadata in Vertica. In addition to the globally available and read operation statements, the connector supports the following features:

ALTER TABLE excluding DROP COLUMN, see also ALTER TABLE RENAME TO limitation

The connector does not support renaming tables across multiple schemas. For example, the following statement is supported:

The following statement attempts to rename a table across schemas, and therefore is not supported:

The connector provides specific table functions to access Vertica.

The query function allows you to query the underlying database directly. It requires syntax native to the data source, because the full query is pushed down and processed in the data source. This can be useful for accessing native features or for improving query performance in situations where running a query natively may be faster.

The query table function is available in the system schema of any catalog that uses the Vertica connector, such as example. The following example passes myQuery to the data source. myQuery has to be a valid query for the data source, and is required to return a table as a result:

The query engine does not preserve the order of the results of this function. If the passed query contains an ORDER BY clause, the function result may not be ordered as expected.

The connector includes a number of performance features, detailed in the following sections.

The connector supports pushdown for a number of operations:

The join-pushdown.enabled catalog configuration property or join_pushdown_enabled catalog session property control whether the connector pushes down join operations. The property defaults to false, and enabling join pushdowns may negatively impact performance for some queries.

The cost-based optimizer can use table statistics from the Vertica database to improve query performance.

Support for table statistics is disabled by default. You can enable it with the catalog property statistics.enabled set to true. In addition, the connection-user configured in the catalog must have superuser permissions in Vertica to gather and populate statistics.

You can view statistics using SHOW STATS.

**Examples:**

Example 1 (unknown):
```unknown
connector.name=vertica
connection-url=jdbc:vertica://example.net:5433/test_db
connection-user=root
connection-password=secret
```

Example 2 (unknown):
```unknown
connector.name=vertica
connection-url=jdbc:vertica://example.net:5433/test_db
connection-user=root
connection-password=secret
```

Example 3 (unknown):
```unknown
query.comment-format=Query sent by Trino.
```

Example 4 (unknown):
```unknown
query.comment-format=Query sent by Trino.
```

---

## MySQL connector — Trino 478 Documentation

**URL:** https://trino.io/docs/current/connector/mysql.html

**Contents:**
- MySQL connector#
- Requirements#
- Configuration#
  - Connection security#
  - Data source authentication#
  - Multiple MySQL servers#
  - General configuration properties#
  - Appending query metadata#
  - Domain compaction threshold#
  - Case insensitive matching#

The MySQL connector allows querying and creating tables in an external MySQL instance. This can be used to join data between different systems like MySQL and Hive, or between two different MySQL instances.

To connect to MySQL, you need:

MySQL 5.7, 8.0 or higher.

Network access from the Trino coordinator and workers to MySQL. Port 3306 is the default port.

To configure the MySQL connector, create a catalog properties file in etc/catalog named, for example, example.properties, to mount the MySQL connector as the mysql catalog. Create the file with the following contents, replacing the connection properties as appropriate for your setup:

The connection-url defines the connection information and parameters to pass to the MySQL JDBC driver. The supported parameters for the URL are available in the MySQL Developer Guide.

For example, the following connection-url allows you to require encrypted connections to the MySQL server:

The connection-user and connection-password are typically required and determine the user credentials for the connection, often a service user. You can use secrets to avoid actual values in the catalog properties files.

If you have TLS configured with a globally-trusted certificate installed on your data source, you can enable TLS between your cluster and the data source by appending a parameter to the JDBC connection string set in the connection-url catalog configuration property.

For example, with version 8.0 of MySQL Connector/J, use the sslMode parameter to secure the connection with TLS. By default the parameter is set to PREFERRED which secures the connection if enabled by the server. You can also set this parameter to REQUIRED which causes the connection to fail if TLS is not established.

You can set the sslMode parameter in the catalog configuration file by appending it to the connection-url configuration property:

For more information on TLS configuration options, see the MySQL JDBC security documentation.

The connector can provide credentials for the data source connection in multiple ways:

inline, in the connector configuration file

in a separate properties file

as extra credentials set when connecting to Trino

You can use secrets to avoid storing sensitive values in the catalog properties files.

The following table describes configuration properties for connection credentials:

credential-provider.type

Type of the credential provider. Must be one of INLINE, FILE, or KEYSTORE; defaults to INLINE.

Connection user name.

Name of the extra credentials property, whose value to use as the user name. See extraCredentials in Parameter reference.

password-credential-name

Name of the extra credentials property, whose value to use as the password.

connection-credential-file

Location of the properties file where credentials are present. It must contain the connection-user and connection-password properties.

The location of the Java Keystore file, from which to read credentials.

File format of the keystore file, for example JKS or PEM.

Password for the key store.

keystore-user-credential-name

Name of the key store entity to use as the user name.

keystore-user-credential-password

Password for the user name key store entity.

keystore-password-credential-name

Name of the key store entity to use as the password.

keystore-password-credential-password

Password for the password key store entity.

You can have as many catalogs as you need, so if you have additional MySQL servers, simply add another properties file to etc/catalog with a different name, making sure it ends in .properties. For example, if you name the property file sales.properties, Trino creates a catalog named sales using the configured connector.

The following table describes general catalog configuration properties for the connector:

case-insensitive-name-matching

Support case insensitive schema and table names. Defaults to false.

case-insensitive-name-matching.cache-ttl

Duration for which case insensitive schema and table names are cached. Defaults to 1m.

case-insensitive-name-matching.config-file

Path to a name mapping configuration file in JSON format that allows Trino to disambiguate between schemas and tables with similar names in different cases. Defaults to null.

case-insensitive-name-matching.config-file.refresh-period

Frequency with which Trino checks the name matching configuration file for changes. The duration value defaults to 0s (refresh disabled).

Duration for which metadata, including table and column statistics, is cached. Defaults to 0s (caching disabled).

metadata.cache-missing

Cache the fact that metadata, including table and column statistics, is not available. Defaults to false.

metadata.schemas.cache-ttl

Duration for which schema metadata is cached. Defaults to the value of metadata.cache-ttl.

metadata.tables.cache-ttl

Duration for which table metadata is cached. Defaults to the value of metadata.cache-ttl.

metadata.statistics.cache-ttl

Duration for which tables statistics are cached. Defaults to the value of metadata.cache-ttl.

metadata.cache-maximum-size

Maximum number of objects stored in the metadata cache. Defaults to 10000.

Maximum number of statements in a batched execution. Do not change this setting from the default. Non-default values may negatively impact performance. Defaults to 1000.

dynamic-filtering.enabled

Push down dynamic filters into JDBC queries. Defaults to true.

dynamic-filtering.wait-timeout

Maximum duration for which Trino waits for dynamic filters to be collected from the build side of joins before starting a JDBC query. Using a large timeout can potentially result in more detailed dynamic filters. However, it can also increase latency for some queries. Defaults to 20s.

The optional parameter query.comment-format allows you to configure a SQL comment that is sent to the datasource with each query. The format of this comment can contain any characters and the following metadata:

$QUERY_ID: The identifier of the query.

$USER: The name of the user who submits the query to Trino.

$SOURCE: The identifier of the client tool used to submit the query, for example trino-cli.

$TRACE_TOKEN: The trace token configured with the client tool.

The comment can provide more context about the query. This additional information is available in the logs of the datasource. To include environment variables from the Trino cluster with the comment , use the ${ENV:VARIABLE-NAME} syntax.

The following example sets a simple comment that identifies each query sent by Trino:

With this configuration, a query such as SELECT * FROM example_table; is sent to the datasource with the comment appended:

The following example improves on the preceding example by using metadata:

If Jane sent the query with the query identifier 20230622_180528_00000_bkizg, the following comment string is sent to the datasource:

Certain JDBC driver settings and logging configurations might cause the comment to be removed.

Pushing down a large list of predicates to the data source can compromise performance. Trino compacts large predicates into a simpler range predicate by default to ensure a balance between performance and predicate pushdown. If necessary, the threshold for this compaction can be increased to improve performance when the data source is capable of taking advantage of large predicates. Increasing this threshold may improve pushdown of large dynamic filters. The domain-compaction-threshold catalog configuration property or the domain_compaction_threshold catalog session property can be used to adjust the default value of 256 for this threshold.

When case-insensitive-name-matching is set to true, Trino is able to query non-lowercase schemas and tables by maintaining a mapping of the lowercase name to the actual name in the remote system. However, if two schemas and/or tables have names that differ only in case (such as “customers” and “Customers”) then Trino fails to query them due to ambiguity.

In these cases, use the case-insensitive-name-matching.config-file catalog configuration property to specify a configuration file that maps these remote schemas and tables to their respective Trino schemas and tables. Additionally, the JSON file must include both the schemas and tables properties, even if only as empty arrays.

Queries against one of the tables or schemes defined in the mapping attributes are run against the corresponding remote entity. For example, a query against tables in the case_insensitive_1 schema is forwarded to the CaseSensitiveName schema and a query against case_insensitive_2 is forwarded to the cASEsENSITIVEnAME schema.

At the table mapping level, a query on case_insensitive_1.table_1 as configured above is forwarded to CaseSensitiveName.tablex, and a query on case_insensitive_1.table_2 is forwarded to CaseSensitiveName.TABLEX.

By default, when a change is made to the mapping configuration file, Trino must be restarted to load the changes. Optionally, you can set the case-insensitive-name-matching.config-file.refresh-period to have Trino refresh the properties without requiring a restart:

The connector supports Fault-tolerant execution of query processing. Read and write operations are both supported with any retry policy.

Table property usage example:

The following are supported MySQL table properties:

The primary key of the table, can choose multi columns as the table primary key. All key columns must be defined as NOT NULL.

Because Trino and MySQL each support types that the other does not, this connector modifies some types when reading or writing data. Data types may not map the same way in both directions between Trino and the data source. Refer to the following sections for type mapping in each direction.

The connector maps MySQL types to the corresponding Trino types following this table:

See MySQL DECIMAL type handling

BINARY, VARBINARY, TINYBLOB, BLOB, MEDIUMBLOB, LONGBLOB

TIMESTAMP(n) WITH TIME ZONE

No other types are supported.

The connector maps Trino types to the corresponding MySQL types following this table:

MySQL DECIMAL type handling

TIMESTAMP(n) WITH TIME ZONE

No other types are supported.

MySQL TIMESTAMP types are mapped to Trino TIMESTAMP WITH TIME ZONE. To preserve time instants, Trino sets the session time zone of the MySQL connection to match the JVM time zone. As a result, error messages similar to the following example occur when a timezone from the JVM does not exist on the MySQL server:

To avoid the errors, you must use a time zone that is known on both systems, or install the missing time zone on the MySQL server.

DECIMAL types with unspecified precision or scale are ignored unless the decimal-mapping configuration property or the decimal_mapping session property is set to allow_overflow. Then such types are mapped to a Trino DECIMAL with a default precision of 38 and default scale of 0. To change the scale of the resulting type, use the decimal-default-scale configuration property or the decimal_default_scale session property. The precision is always 38.

By default, values that require rounding or truncation to fit will cause a failure at runtime. This behavior is controlled via the decimal-rounding-mode configuration property or the decimal_rounding_mode session property, which can be set to UNNECESSARY (the default), UP, DOWN, CEILING, FLOOR, HALF_UP, HALF_DOWN, or HALF_EVEN (see RoundingMode).

The following properties can be used to configure how data types from the connected data source are mapped to Trino data types and how the metadata is cached in Trino.

unsupported-type-handling

Configure how unsupported column data types are handled:

IGNORE, column is not accessible.

CONVERT_TO_VARCHAR, column is converted to unbounded VARCHAR.

The respective catalog session property is unsupported_type_handling.

jdbc-types-mapped-to-varchar

Allow forced mapping of comma separated lists of data types to convert to unbounded VARCHAR

The MySQL connector provides a schema for every MySQL database. You can see the available MySQL databases by running SHOW SCHEMAS:

If you have a MySQL database named web, you can view the tables in this database by running SHOW TABLES:

You can see a list of the columns in the clicks table in the web database using either of the following:

Finally, you can access the clicks table in the web database:

If you used a different name for your catalog properties file, use that catalog name instead of example in the above examples.

The connector provides read access and write access to data and metadata in the MySQL database. In addition to the globally available and read operation statements, the connector supports the following features:

INSERT, see also Non-transactional INSERT

UPDATE, see also UPDATE limitation

DELETE, see also DELETE limitation

MERGE, see also Non-transactional MERGE

The connector supports adding rows using INSERT statements. By default, data insertion is performed by writing data to a temporary table. You can skip this step to improve performance and write directly to the target table. Set the insert.non-transactional-insert.enabled catalog property or the corresponding non_transactional_insert catalog session property to true.

Note that with this property enabled, data can be corrupted in rare cases where exceptions occur during the insert operation. With transactions disabled, no rollback can be performed.

Only UPDATE statements with constant assignments and predicates are supported. For example, the following statement is supported because the values assigned are constants:

Arithmetic expressions, function calls, and other non-constant UPDATE statements are not supported. For example, the following statement is not supported because arithmetic expressions cannot be used with the SET command:

All column values of a table row cannot be updated simultaneously. For a three column table, the following statement is not supported:

If a WHERE clause is specified, the DELETE operation only works if the predicate in the clause can be fully pushed down to the data source.

The connector supports adding, updating, and deleting rows using MERGE statements, if the merge.non-transactional-merge.enabled catalog property or the corresponding non_transactional_merge_enabled catalog session property is set to true. Merge is only supported for directly modifying target tables.

In rare cases, exceptions may occur during the merge operation, potentially resulting in a partial update.

Flush JDBC metadata caches. For example, the following system call flushes the metadata caches for all schemas in the example catalog

The execute procedure allows you to execute a query in the underlying data source directly. The query must use supported syntax of the connected data source. Use the procedure to access features which are not available in Trino or to execute queries that return no result set and therefore can not be used with the query or raw_query pass-through table function. Typical use cases are statements that create or alter objects, and require native feature such as constraints, default values, automatic identifier creation, or indexes. Queries can also invoke statements that insert, update, or delete data, and do not return any data as a result.

The query text is not parsed by Trino, only passed through, and therefore only subject to any security or access control of the underlying data source.

The following example sets the current database to the example_schema of the example catalog. Then it calls the procedure in that schema to drop the default value from your_column on your_table table using the standard SQL syntax in the parameter value assigned for query:

Verify that the specific database supports this syntax, and adapt as necessary based on the documentation for the specific connected database and database version.

The connector provides specific table functions to access MySQL.

The query function allows you to query the underlying database directly. It requires syntax native to MySQL, because the full query is pushed down and processed in MySQL. This can be useful for accessing native features which are not available in Trino or for improving query performance in situations where running a query natively may be faster.

The native query passed to the underlying data source is required to return a table as a result set. Only the data source performs validation or security checks for these queries using its own configuration. Trino does not perform these tasks. Only use passthrough queries to read data.

For example, query the example catalog and group and concatenate all employee IDs by manager ID:

The query engine does not preserve the order of the results of this function. If the passed query contains an ORDER BY clause, the function result may not be ordered as expected.

The connector includes a number of performance improvements, detailed in the following sections.

The MySQL connector can use table and column statistics for cost based optimizations, to improve query processing performance based on the actual data in the data source.

The statistics are collected by MySQL and retrieved by the connector.

The table-level statistics are based on MySQL’s INFORMATION_SCHEMA.TABLES table. The column-level statistics are based on MySQL’s index statistics INFORMATION_SCHEMA.STATISTICS table. The connector can return column-level statistics only when the column is the first column in some index.

MySQL database can automatically update its table and index statistics. In some cases, you may want to force statistics update, for example after creating new index, or after changing data in the table. You can do that by executing the following statement in MySQL Database.

MySQL and Trino may use statistics information in different ways. For this reason, the accuracy of table and column statistics returned by the MySQL connector might be lower than that of others connectors.

Improving statistics accuracy

You can improve statistics accuracy with histogram statistics (available since MySQL 8.0). To create histogram statistics execute the following statement in MySQL Database.

Refer to MySQL documentation for information about options, limitations and additional considerations.

The connector supports pushdown for a number of operations:

Aggregate pushdown for the following functions:

The connector performs pushdown where performance may be improved, but in order to preserve correctness an operation may not be pushed down. When pushdown of an operation may result in better performance but risks correctness, the connector prioritizes correctness.

The connector supports cost-based Join pushdown to make intelligent decisions about whether to push down a join operation to the data source.

When cost-based join pushdown is enabled, the connector only pushes down join operations if the available Table statistics suggest that doing so improves performance. Note that if no table statistics are available, join operation pushdown does not occur to avoid a potential decrease in query performance.

The following table describes catalog configuration properties for join pushdown:

join-pushdown.enabled

Enable join pushdown. Equivalent catalog session property is join_pushdown_enabled.

join-pushdown.strategy

Strategy used to evaluate whether join operations are pushed down. Set to AUTOMATIC to enable cost-based join pushdown, or EAGER to push down joins whenever possible. Note that EAGER can push down joins even when table statistics are unavailable, which may result in degraded query performance. Because of this, EAGER is only recommended for testing and troubleshooting purposes.

The connector does not support pushdown of any predicates on columns with textual types like CHAR or VARCHAR. This ensures correctness of results since the data source may compare strings case-insensitively.

In the following example, the predicate is not pushed down for either query since name is a column of type VARCHAR:

**Examples:**

Example 1 (unknown):
```unknown
connector.name=mysql
connection-url=jdbc:mysql://example.net:3306
connection-user=root
connection-password=secret
```

Example 2 (unknown):
```unknown
connector.name=mysql
connection-url=jdbc:mysql://example.net:3306
connection-user=root
connection-password=secret
```

Example 3 (unknown):
```unknown
connection-url=jdbc:mysql://example.net:3306?sslMode=REQUIRED
```

Example 4 (unknown):
```unknown
connection-url=jdbc:mysql://example.net:3306?sslMode=REQUIRED
```

---

## Cassandra connector — Trino 478 Documentation

**URL:** https://trino.io/docs/current/connector/cassandra.html

**Contents:**
- Cassandra connector#
- Requirements#
- Configuration#
  - Multiple Cassandra clusters#
- Configuration properties#
- Querying Cassandra tables#
- Type mapping#
  - Cassandra type to Trino type mapping#
  - Trino type to Cassandra type mapping#
- Partition key types#

The Cassandra connector allows querying data stored in Apache Cassandra.

To connect to Cassandra, you need:

Cassandra version 3.0 or higher.

Network access from the Trino coordinator and workers to Cassandra. Port 9042 is the default port.

To configure the Cassandra connector, create a catalog properties file etc/catalog/example.properties with the following contents, replacing host1,host2 with a comma-separated list of the Cassandra nodes, used to discovery the cluster topology:

You also need to set cassandra.native-protocol-port, if your Cassandra nodes are not using the default port 9042.

You can have as many catalogs as you need, so if you have additional Cassandra clusters, simply add another properties file to etc/catalog with a different name, making sure it ends in .properties. For example, if you name the property file sales.properties, Trino creates a catalog named sales using the configured connector.

The following configuration properties are available:

cassandra.contact-points

Comma-separated list of hosts in a Cassandra cluster. The Cassandra driver uses these contact points to discover cluster topology. At least one Cassandra host is required.

cassandra.native-protocol-port

The Cassandra server port running the native client protocol, defaults to 9042.

cassandra.consistency-level

Consistency levels in Cassandra refer to the level of consistency to be used for both read and write operations. More information about consistency levels can be found in the Cassandra consistency documentation. This property defaults to a consistency level of ONE. Possible values include ALL, EACH_QUORUM, QUORUM, LOCAL_QUORUM, ONE, TWO, THREE, LOCAL_ONE, ANY, SERIAL, LOCAL_SERIAL.

cassandra.allow-drop-table

Enables DROP TABLE operations. Defaults to false.

Configure authentication to Cassandra. Defaults to NONE. Set to PASSWORD for basic authentication, and configure cassandra.username and cassandra.password.

Username used for authentication to the Cassandra cluster. Requires cassandra.security=PASSWORD. This is a global setting used for all connections, regardless of the user connected to Trino.

Password used for authentication to the Cassandra cluster. Requires cassandra.security=PASSWORD. This is a global setting used for all connections, regardless of the user connected to Trino.

cassandra.protocol-version

It is possible to override the protocol version for older Cassandra clusters. By default, the value corresponds to the default protocol version used in the underlying Cassandra java driver. Possible values include V3, V4, V5, V6.

If authorization is enabled, cassandra.username must have enough permissions to perform SELECT queries on the system.size_estimates table.

The following advanced configuration properties are available:

Number of rows fetched at a time in a Cassandra query.

cassandra.partition-size-for-batch-select

Number of partitions batched together into a single select for a single partition key column table.

Number of keys per split when querying Cassandra.

cassandra.splits-per-node

Number of splits per node. By default, the values from the system.size_estimates table are used. Only override when connecting to Cassandra versions < 2.1.5, which lacks the system.size_estimates table.

Maximum number of statements to execute in one batch.

cassandra.client.read-timeout

Maximum time the Cassandra driver waits for an answer to a query from one Cassandra node. Note that the underlying Cassandra driver may retry a query against more than one node in the event of a read timeout. Increasing this may help with queries that use an index.

cassandra.client.connect-timeout

Maximum time the Cassandra driver waits to establish a connection to a Cassandra node. Increasing this may help with heavily loaded Cassandra clusters.

cassandra.client.so-linger

Number of seconds to linger on close if unsent data is queued. If set to zero, the socket will be closed immediately. When this option is non-zero, a socket lingers that many seconds for an acknowledgement that all data was written to a peer. This option can be used to avoid consuming sockets on a Cassandra server by immediately closing connections when they are no longer needed.

cassandra.retry-policy

Policy used to retry failed requests to Cassandra. This property defaults to DEFAULT. Using BACKOFF may help when queries fail with “not enough replicas”. The other possible values are DOWNGRADING_CONSISTENCY and FALLTHROUGH.

cassandra.load-policy.use-dc-aware

Set to true if the load balancing policy requires a local datacenter, defaults to true.

cassandra.load-policy.dc-aware.local-dc

The name of the datacenter considered “local”.

cassandra.load-policy.dc-aware.used-hosts-per-remote-dc

Uses the provided number of host per remote datacenter as failover for the local hosts for DefaultLoadBalancingPolicy.

cassandra.load-policy.dc-aware.allow-remote-dc-for-local

Set to true to allow to use hosts of remote datacenter for local consistency level.

cassandra.no-host-available-retry-timeout

Retry timeout for AllNodesFailedException, defaults to 1m.

cassandra.speculative-execution.limit

The number of speculative executions. This is disabled by default.

cassandra.speculative-execution.delay

The delay between each speculative execution, defaults to 500ms.

cassandra.tls.enabled

Whether TLS security is enabled, defaults to false.

cassandra.tls.keystore-path

Path to the PEM or JKS key store file.

cassandra.tls.truststore-path

Path to the PEM or JKS trust store file.

cassandra.tls.keystore-password

Password for the key store.

cassandra.tls.truststore-password

Password for the trust store.

The users table is an example Cassandra table from the Cassandra Getting Started guide. It can be created along with the example_keyspace keyspace using Cassandra’s cqlsh (CQL interactive terminal):

This table can be described in Trino:

This table can then be queried in Trino:

Because Trino and Cassandra each support types that the other does not, this connector modifies some types when reading or writing data. Data types may not map the same way in both directions between Trino and the data source. Refer to the following sections for type mapping in each direction.

The connector maps Cassandra types to the corresponding Trino types according to the following table:

US-ASCII character string

Arbitrary-precision integer

TIMESTAMP(3) WITH TIME ZONE

ROW with anonymous fields

No other types are supported.

The connector maps Trino types to the corresponding Cassandra types according to the following table:

TIMESTAMP(3) WITH TIME ZONE

No other types are supported.

Partition keys can only be of the following types:

Queries without filters containing the partition key result in fetching all partitions. This causes a full scan of the entire data set, and is therefore much slower compared to a similar query with a partition key as a filter.

IN list filters are only allowed on index (that is, partition key or clustering key) columns.

Range (< or > and BETWEEN) filters can be applied only to the partition keys.

The connector provides read and write access to data and metadata in the Cassandra database. In addition to the globally available and read operation statements, the connector supports the following features:

DELETE see SQL delete limitation

The execute procedure allows you to execute a query in the underlying data source directly. The query must use supported syntax of the connected data source. Use the procedure to access features which are not available in Trino or to execute queries that return no result set and therefore can not be used with the query or raw_query pass-through table function. Typical use cases are statements that create or alter objects, and require native feature such as constraints, default values, automatic identifier creation, or indexes. Queries can also invoke statements that insert, update, or delete data, and do not return any data as a result.

The query text is not parsed by Trino, only passed through, and therefore only subject to any security or access control of the underlying data source.

The following example sets the current database to the example_schema of the example catalog. Then it calls the procedure in that schema to drop the default value from your_column on your_table table using the standard SQL syntax in the parameter value assigned for query:

Verify that the specific database supports this syntax, and adapt as necessary based on the documentation for the specific connected database and database version.

The connector provides specific table functions to access Cassandra. .. _cassandra-query-function:

The query function allows you to query the underlying Cassandra directly. It requires syntax native to Cassandra, because the full query is pushed down and processed by Cassandra. This can be useful for accessing native features which are not available in Trino or for improving query performance in situations where running a query natively may be faster.

The query engine does not preserve the order of the results of this function. If the passed query contains an ORDER BY clause, the function result may not be ordered as expected.

As a simple example, to select an entire table:

By default, DROP TABLE operations are disabled on Cassandra catalogs. To enable DROP TABLE, set the cassandra.allow-drop-table catalog configuration property to true:

DELETE is only supported if the WHERE clause matches entire partitions.

**Examples:**

Example 1 (unknown):
```unknown
connector.name=cassandra
cassandra.contact-points=host1,host2
cassandra.load-policy.dc-aware.local-dc=datacenter1
```

Example 2 (unknown):
```unknown
connector.name=cassandra
cassandra.contact-points=host1,host2
cassandra.load-policy.dc-aware.local-dc=datacenter1
```

Example 3 (unknown):
```unknown
cqlsh> CREATE KEYSPACE example_keyspace
   ... WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };
cqlsh> USE example_keyspace;
cqlsh:example_keyspace> CREATE TABLE users (
              ...   user_id int PRIMARY KEY,
              ...   fname text,
              ...   lname text
              ... );
```

Example 4 (unknown):
```unknown
cqlsh> CREATE KEYSPACE example_keyspace
   ... WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };
cqlsh> USE example_keyspace;
cqlsh:example_keyspace> CREATE TABLE users (
              ...   user_id int PRIMARY KEY,
              ...   fname text,
              ...   lname text
              ... );
```

---

## Hudi connector — Trino 478 Documentation

**URL:** https://trino.io/docs/current/connector/hudi.html

**Contents:**
- Hudi connector#
- Requirements#
- General configuration#
- File system access configuration#
- SQL support#
  - Basic usage examples#
  - Schema and table management#
    - Metadata tables#
      - $timeline table#

The Hudi connector enables querying Hudi tables.

To use the Hudi connector, you need:

Hudi version 0.12.3 or higher.

Network access from the Trino coordinator and workers to the Hudi storage.

Access to a Hive metastore service (HMS).

Network access from the Trino coordinator to the HMS.

Data files stored in the Parquet file format on a supported file system.

To configure the Hudi connector, create a catalog properties file etc/catalog/example.properties that references the hudi connector.

You must configure a metastore for table metadata.

You must select and configure one of the supported file systems.

Replace the fs.x.enabled configuration property with the desired file system.

There are HMS configuration properties available for use with the Hudi connector. The connector recognizes Hudi tables synced to the metastore by the Hudi sync tool.

Additionally, following configuration properties can be set depending on the use-case:

List of column names that are hidden from the query output. It can be used to hide Hudi meta fields. By default, no fields are hidden.

hudi.parquet.use-column-names

Access Parquet columns using names from the file. If disabled, then columns are accessed using the index. Only applicable to Parquet file format.

hudi.split-generator-parallelism

Number of threads to generate splits from partitions.

hudi.split-loader-parallelism

Number of threads to run background split loader. A single background split loader is needed per query.

hudi.size-based-split-weights-enabled

Unlike uniform splitting, size-based splitting ensures that each batch of splits has enough data to process. By default, it is enabled to improve performance.

hudi.standard-split-weight-size

The split size corresponding to the standard weight (1.0) when size-based split weights are enabled.

hudi.minimum-assigned-split-weight

Minimum weight that a split can be assigned when size-based split weights are enabled.

hudi.max-splits-per-second

Rate at which splits are queued for processing. The queue is throttled if this rate limit is breached.

hudi.max-outstanding-splits

Maximum outstanding splits in a batch enqueued for processing.

hudi.per-transaction-metastore-cache-maximum-size

Maximum number of metastore data objects per transaction in the Hive metastore cache.

hudi.query-partition-filter-required

Set to true to force a query to use a partition column in the filter condition. The equivalent catalog session property is query_partition_filter_required. Enabling this property causes query failures if the partition column used in the filter condition doesn’t effectively reduce the number of data files read. Example: Complex filter expressions such as id = 1 OR part_key = '100' or CAST(part_key AS INTEGER) % 2 = 0 are not recognized as partition filters, and queries using such expressions fail if the property is set to true.

hudi.ignore-absent-partitions

Ignore partitions when the file system location does not exist rather than failing the query. This skips data that may be expected to be part of the table.

The connector supports accessing the following file systems:

Azure Storage file system support

Google Cloud Storage file system support

S3 file system support

HDFS file system support

You must enable and configure the specific file system access. Legacy support is not recommended and will be removed.

The connector provides read access to data in the Hudi table that has been synced to Hive metastore. The globally available and read operation statements are supported.

In the following example queries, stock_ticks_cow is the Hudi copy-on-write table referred to in the Hudi quickstart guide.

Hudi supports two types of tables depending on how the data is indexed and laid out on the file system. The following table displays a support matrix of tables types and query types for the connector:

Read-optimized queries

The connector exposes a metadata table for each Hudi table. The metadata table contains information about the internal structure of the Hudi table. You can query each metadata table by appending the metadata table name to the table name:

The $timeline table provides a detailed view of meta-data instants in the Hudi table. Instants are specific points in time.

You can retrieve the information about the timeline of the Hudi table test_table by using the following query:

The output of the query has the following columns:

Instant time is typically a timestamp when the actions performed.

Type of action performed on the table.

Current state of the instant.

**Examples:**

Example 1 (unknown):
```unknown
connector.name=hudi
hive.metastore.uri=thrift://example.net:9083
fs.x.enabled=true
```

Example 2 (unknown):
```unknown
connector.name=hudi
hive.metastore.uri=thrift://example.net:9083
fs.x.enabled=true
```

Example 3 (unknown):
```unknown
USE example.example_schema;

SELECT symbol, max(ts)
FROM stock_ticks_cow
GROUP BY symbol
HAVING symbol = 'GOOG';
```

Example 4 (unknown):
```unknown
USE example.example_schema;

SELECT symbol, max(ts)
FROM stock_ticks_cow
GROUP BY symbol
HAVING symbol = 'GOOG';
```

---

## Pinot connector — Trino 478 Documentation

**URL:** https://trino.io/docs/current/connector/pinot.html

**Contents:**
- Pinot connector#
- Requirements#
- Configuration#
- Configuration properties#
  - General configuration properties#
  - gRPC configuration properties#
- Querying Pinot tables#
- Dynamic tables#
- Type mapping#
  - Pinot type to Trino type mapping#

The Pinot connector allows Trino to query data stored in Apache Pinot™.

To connect to Pinot, you need:

Pinot 1.1.0 or higher.

Network access from the Trino coordinator and workers to the Pinot controller nodes. Port 8098 is the default port.

To configure the Pinot connector, create a catalog properties file e.g. etc/catalog/example.properties with at least the following contents:

Replace host1:8098,host2:8098 with a comma-separated list of Pinot controller nodes. This can be the ip or the FQDN, the url scheme (http://) is optional.

pinot.controller-urls

A comma separated list of controller hosts. If Pinot is deployed via Kubernetes this needs to point to the controller service endpoint. The Pinot broker and server must be accessible via DNS as Pinot returns hostnames and not IP addresses.

A host and port of broker. If broker URL exposed by Pinot controller API is not accessible, this property can be used to specify the broker endpoint. Enabling this property will disable broker discovery.

pinot.connection-timeout

Pinot connection timeout, default is 1m.

pinot.metadata-expiry

Pinot metadata expiration time, default is 2m.

pinot.controller.authentication.type

Pinot authentication method for controller requests. Allowed values are NONE and PASSWORD - defaults to NONE which is no authentication.

pinot.controller.authentication.user

Controller username for basic authentication method.

pinot.controller.authentication.password

Controller password for basic authentication method.

pinot.broker.authentication.type

Pinot authentication method for broker requests. Allowed values are NONE and PASSWORD - defaults to NONE which is no authentication.

pinot.broker.authentication.user

Broker username for basic authentication method.

pinot.broker.authentication.password

Broker password for basic authentication method.

pinot.max-rows-per-split-for-segment-queries

Fail query if Pinot server split returns more rows than configured, default to 2,147,483,646.

pinot.prefer-broker-queries

Pinot query plan prefers to query Pinot broker, default is false.

pinot.forbid-segment-queries

Forbid parallel querying and force all querying to happen via the broker, default is false.

pinot.segments-per-split

The number of segments processed in a split. Setting this higher reduces the number of requests made to Pinot. This is useful for smaller Pinot clusters, default is 1.

pinot.fetch-retry-count

Retry count for retriable Pinot data fetch calls, default is 2.

pinot.non-aggregate-limit-for-broker-queries

Max limit for non aggregate queries to the Pinot broker, default is 25,000.

pinot.max-rows-for-broker-queries

Max rows for a broker query can return, default is 50,000.

pinot.aggregation-pushdown.enabled

Push down aggregation queries, default is true.

pinot.count-distinct-pushdown.enabled

Push down count distinct queries to Pinot, default is true.

pinot.target-segment-page-size

Max allowed page size for segment query, default is 1MB.

Use Pinot Proxy for controller and broker requests, default is false.

If pinot.controller.authentication.type is set to PASSWORD then both pinot.controller.authentication.user and pinot.controller.authentication.password are required.

If pinot.broker.authentication.type is set to PASSWORD then both pinot.broker.authentication.user and pinot.broker.authentication.password are required.

If pinot.controller-urls uses https scheme then TLS is enabled for all connections including brokers.

Pinot gRPC port, default to 8090.

pinot.grpc.max-inbound-message-size

Max inbound message bytes when init gRPC client, default is 128MB.

pinot.grpc.use-plain-text

Use plain text for gRPC communication, default to true.

pinot.grpc.tls.keystore-type

TLS keystore type for gRPC connection, default is JKS.

pinot.grpc.tls.keystore-path

TLS keystore file location for gRPC connection, default is empty.

pinot.grpc.tls.keystore-password

TLS keystore password, default is empty.

pinot.grpc.tls.truststore-type

TLS truststore type for gRPC connection, default is JKS.

pinot.grpc.tls.truststore-path

TLS truststore file location for gRPC connection, default is empty.

pinot.grpc.tls.truststore-password

TLS truststore password, default is empty.

pinot.grpc.tls.ssl-provider

SSL provider, default is JDK.

Pinot Rest Proxy gRPC endpoint URI, default is null.

For more Apache Pinot TLS configurations, please also refer to Configuring TLS/SSL.

You can use secrets to avoid actual values in the catalog properties files.

The Pinot connector automatically exposes all tables in the default schema of the catalog. You can list all tables in the pinot catalog with the following query:

You can list columns in the flight_status table:

Queries written with SQL are fully supported and can include filters and limits:

To leverage Pinot’s fast aggregation, a Pinot query written in PQL can be used as the table name. Filters and limits in the outer query are pushed down to Pinot. Let’s look at an example query:

Filtering and limit processing is pushed down to Pinot.

The queries are routed to the broker and are more suitable to aggregate queries.

For SELECT queries without aggregates it is more performant to issue a regular SQL query. Processing is routed directly to the servers that store the data.

The above query is translated to the following Pinot PQL query:

Because Trino and Pinot each support types that the other does not, this connector maps some types when reading data.

The connector maps Pinot types to the corresponding Trino types according to the following table:

No other types are supported.

For Pinot DateTimeFields, if the FormatSpec is in days, then it is converted to a Trino DATE type. Pinot allows for LONG fields to have a FormatSpec of days as well, if the value is larger than Integer.MAX_VALUE then the conversion to Trino DATE fails.

If a Pinot TableSpec has nullHandlingEnabled set to true, then for numeric types the null value is encoded as MIN_VALUE for that type. For Pinot STRING type, the value null is interpreted as a NULL value.

The connector provides globally available and read operation statements to access data and metadata in Pinot.

The connector supports pushdown for a number of operations:

Aggregate pushdown for the following functions:

count(*) and count(distinct) variations of count()

Aggregate function pushdown is enabled by default, but can be disabled with the catalog property pinot.aggregation-pushdown.enabled or the catalog session property aggregation_pushdown_enabled.

A count(distinct) pushdown may cause Pinot to run a full table scan with significant performance impact. If you encounter this problem, you can disable it with the catalog property pinot.count-distinct-pushdown.enabled or the catalog session property count_distinct_pushdown_enabled.

The connector performs pushdown where performance may be improved, but in order to preserve correctness an operation may not be pushed down. When pushdown of an operation may result in better performance but risks correctness, the connector prioritizes correctness.

**Examples:**

Example 1 (unknown):
```unknown
connector.name=pinot
pinot.controller-urls=host1:8098,host2:8098
```

Example 2 (unknown):
```unknown
connector.name=pinot
pinot.controller-urls=host1:8098,host2:8098
```

Example 3 (unknown):
```unknown
SHOW TABLES FROM example.default;
```

Example 4 (unknown):
```unknown
SHOW TABLES FROM example.default;
```

---

## Elasticsearch connector — Trino 478 Documentation

**URL:** https://trino.io/docs/current/connector/elasticsearch.html

**Contents:**
- Elasticsearch connector#
- Requirements#
- Configuration#
  - Authentication#
  - Connection security with TLS#
- Type mapping#
  - Elasticsearch type to Trino type mapping#
  - Array types#
  - Date types#
  - Raw JSON transform#

The Elasticsearch connector allows access to Elasticsearch data from Trino. This document describes how to configure a catalog with the Elasticsearch connector to run SQL queries against Elasticsearch.

Elasticsearch 7.x or 8.x

Network access from the Trino coordinator and workers to the Elasticsearch nodes.

To configure the Elasticsearch connector, create a catalog properties file etc/catalog/example.properties with the following contents, replacing the properties as appropriate for your setup:

The following table details all general configuration properties:

The comma-separated list of host names for the Elasticsearch node to connect to. This property is required.

Port to use to connect to Elasticsearch.

elasticsearch.default-schema-name

The schema that contains all tables defined without a qualifying schema name.

elasticsearch.scroll-size

Sets the maximum number of hits that can be returned with each Elasticsearch scroll request.

elasticsearch.scroll-timeout

Duration for Elasticsearch to keep the search context alive for scroll requests.

elasticsearch.request-timeout

Timeout duration for all Elasticsearch requests.

elasticsearch.connect-timeout

Timeout duration for all Elasticsearch connection attempts.

elasticsearch.backoff-init-delay

The minimum duration between backpressure retry attempts for a single request to Elasticsearch. Setting it too low can overwhelm an already struggling cluster.

elasticsearch.backoff-max-delay

The maximum duration between backpressure retry attempts for a single request to Elasticsearch.

elasticsearch.max-retry-time

The maximum duration across all retry attempts for a single request to Elasticsearch.

elasticsearch.node-refresh-interval

Duration between requests to refresh the list of available Elasticsearch nodes.

elasticsearch.ignore-publish-address

Disable using the address published by the Elasticsearch API to connect for queries. Some deployments map Elasticsearch ports to a random public port and enabling this property can help in these cases.

The connection to Elasticsearch can use AWS or password authentication.

To enable AWS authentication and authorization using IAM policies, the elasticsearch.security option must be set to AWS. Additionally, the following options must be configured:

elasticsearch.aws.region

AWS region of the Elasticsearch endpoint. This option is required.

elasticsearch.aws.access-key

AWS access key to use to connect to the Elasticsearch domain. If not set, the default AWS credentials provider chain is used.

elasticsearch.aws.secret-key

AWS secret key to use to connect to the Elasticsearch domain. If not set, the default AWS credentials provider chain is used.

elasticsearch.aws.iam-role

Optional ARN of an IAM role to assume to connect to Elasticsearch. Note that the configured IAM user must be able to assume this role.

elasticsearch.aws.external-id

Optional external ID to pass while assuming an AWS IAM role.

To enable password authentication, the elasticsearch.security option must be set to PASSWORD. Additionally the following options must be configured:

elasticsearch.auth.user

Username to use to connect to Elasticsearch.

elasticsearch.auth.password

Password to use to connect to Elasticsearch.

The connector provides additional security options to connect to Elasticsearch clusters with TLS enabled.

If your cluster has globally-trusted certificates, you should only need to enable TLS. If you require custom configuration for certificates, the connector supports key stores and trust stores in P12 (PKCS) or Java Key Store (JKS) format.

The available configuration values are listed in the following table:

elasticsearch.tls.enabled

Enables TLS security.

elasticsearch.tls.keystore-path

The path to the P12 (PKCS) or JKS key store.

elasticsearch.tls.truststore-path

The path to P12 (PKCS) or JKS trust store.

elasticsearch.tls.keystore-password

The key password for the key store specified by elasticsearch.tls.keystore-path.

elasticsearch.tls.truststore-password

The key password for the trust store specified by elasticsearch.tls.truststore-path.

elasticsearch.tls.verify-hostnames

Flag to determine if the hostnames in the certificates must be verified. Defaults to true.

Because Trino and Elasticsearch each support types that the other does not, this connector maps some types when reading data.

The connector maps Elasticsearch types to the corresponding Trino types according to the following table:

For more information, see Date types.

No other types are supported.

Fields in Elasticsearch can contain zero or more values, but there is no dedicated array type. To indicate a field contains an array, it can be annotated in a Trino-specific structure in the _meta section of the index mapping.

For example, you can have an Elasticsearch index that contains documents with the following structure:

The array fields of this structure can be defined by using the following command to add the field property definition to the _meta.trino property of the target index mapping with Elasticsearch available at search.example.com:9200:

It is not allowed to use asRawJson and isArray flags simultaneously for the same column.

The Elasticsearch connector supports only the default date type. All other date formats including built-in date formats and custom date formats are not supported. Dates with the format property are ignored.

Documents in Elasticsearch can include more complex structures that are not represented in the mapping. For example, a single keyword field can have widely different content including a single keyword value, an array, or a multidimensional keyword array with any level of nesting.

The following command configures array_string_field mapping with Elasticsearch available at search.example.com:9200:

All the following documents are legal for Elasticsearch with array_string_field mapping:

See the Elasticsearch array documentation for more details.

Further, Elasticsearch supports types, such as dense_vector, that are not supported in Trino. These and other types can cause parsing exceptions for users that use of these types in Elasticsearch. To manage all of these scenarios, you can transform fields to raw JSON by annotating it in a Trino-specific structure in the _meta section of the index mapping. This indicates to Trino that the field, and all nested fields beneath, need to be cast to a VARCHAR field that contains the raw JSON content. These fields can be defined by using the following command to add the field property definition to the _meta.trino property of the target index mapping.

This preceding configuration causes Trino to return the array_string_field field as a VARCHAR containing raw JSON. You can parse these fields with the built-in JSON functions.

It is not allowed to use asRawJson and isArray flags simultaneously for the same column.

The following hidden columns are available:

The Elasticsearch document ID.

The document score returned by the Elasticsearch query.

The source of the original document.

Trino SQL queries can be combined with Elasticsearch queries by providing the full text query as part of the table name, separated by a colon. For example:

The connector provides globally available and read operation statements to access data and metadata in the Elasticsearch catalog.

The connector provides support to query multiple tables using a concise wildcard table notation.

The connector provides specific table functions to access Elasticsearch.

The raw_query function allows you to query the underlying database directly. This function requires Elastic Query DSL syntax. The full DSL query is pushed down and processed in Elasticsearch. This can be useful for accessing native features which are not available in Trino or for improving query performance in situations where running a query natively may be faster.

The native query passed to the underlying data source is required to return a table as a result set. Only the data source performs validation or security checks for these queries using its own configuration. Trino does not perform these tasks. Only use passthrough queries to read data.

The raw_query function requires three parameters:

schema: The schema in the catalog that the query is to be executed on.

index: The index in Elasticsearch to be searched.

query: The query to execute, written in Elastic Query DSL.

Once executed, the query returns a single row containing the resulting JSON payload returned by Elasticsearch.

For example, query the example catalog and use the raw_query table function to search for documents in the orders index where the country name is ALGERIA as defined as a JSON-formatted query matcher and passed to the raw_query table function in the query parameter:

The query engine does not preserve the order of the results of this function. If the passed query contains an ORDER BY clause, the function result may not be ordered as expected.

The connector includes a number of performance improvements, detailed in the following sections.

The connector requests data from multiple nodes of the Elasticsearch cluster for query processing in parallel.

The connector supports predicate push down for the following data types:

No other data types are supported for predicate push down.

**Examples:**

Example 1 (unknown):
```unknown
connector.name=elasticsearch
elasticsearch.host=localhost
elasticsearch.port=9200
elasticsearch.default-schema-name=default
```

Example 2 (unknown):
```unknown
connector.name=elasticsearch
elasticsearch.host=localhost
elasticsearch.port=9200
elasticsearch.default-schema-name=default
```

Example 3 (unknown):
```unknown
{
    "array_string_field": ["trino","the","lean","machine-ohs"],
    "long_field": 314159265359,
    "id_field": "564e6982-88ee-4498-aa98-df9e3f6b6109",
    "timestamp_field": "1987-09-17T06:22:48.000Z",
    "object_field": {
        "array_int_field": [86,75,309],
        "int_field": 2
    }
}
```

Example 4 (unknown):
```unknown
{
    "array_string_field": ["trino","the","lean","machine-ohs"],
    "long_field": 314159265359,
    "id_field": "564e6982-88ee-4498-aa98-df9e3f6b6109",
    "timestamp_field": "1987-09-17T06:22:48.000Z",
    "object_field": {
        "array_int_field": [86,75,309],
        "int_field": 2
    }
}
```

---

## Snowflake connector — Trino 478 Documentation

**URL:** https://trino.io/docs/current/connector/snowflake.html

**Contents:**
- Snowflake connector#
- Configuration#
  - Multiple Snowflake databases or accounts#
  - General configuration properties#
  - Appending query metadata#
  - Domain compaction threshold#
  - Case insensitive matching#
- Type mapping#
  - Snowflake type to Trino type mapping#
  - Trino type to Snowflake type mapping#

The Snowflake connector allows querying and creating tables in an external Snowflake account. This can be used to join data between different systems like Snowflake and Hive, or between two different Snowflake accounts.

To configure the Snowflake connector, create a catalog properties file in etc/catalog named, for example, example.properties, to mount the Snowflake connector as the snowflake catalog. Create the file with the following contents, replacing the connection properties as appropriate for your setup:

The Snowflake connector uses Apache Arrow as the serialization format when reading from Snowflake. Add the following required, additional JVM argument to the JVM config:

The Snowflake connector can only access a single database within a Snowflake account. Thus, if you have multiple Snowflake databases, or want to connect to multiple Snowflake accounts, you must configure multiple instances of the Snowflake connector.

The following table describes general catalog configuration properties for the connector:

case-insensitive-name-matching

Support case insensitive schema and table names. Defaults to false.

case-insensitive-name-matching.cache-ttl

Duration for which case insensitive schema and table names are cached. Defaults to 1m.

case-insensitive-name-matching.config-file

Path to a name mapping configuration file in JSON format that allows Trino to disambiguate between schemas and tables with similar names in different cases. Defaults to null.

case-insensitive-name-matching.config-file.refresh-period

Frequency with which Trino checks the name matching configuration file for changes. The duration value defaults to 0s (refresh disabled).

Duration for which metadata, including table and column statistics, is cached. Defaults to 0s (caching disabled).

metadata.cache-missing

Cache the fact that metadata, including table and column statistics, is not available. Defaults to false.

metadata.schemas.cache-ttl

Duration for which schema metadata is cached. Defaults to the value of metadata.cache-ttl.

metadata.tables.cache-ttl

Duration for which table metadata is cached. Defaults to the value of metadata.cache-ttl.

metadata.statistics.cache-ttl

Duration for which tables statistics are cached. Defaults to the value of metadata.cache-ttl.

metadata.cache-maximum-size

Maximum number of objects stored in the metadata cache. Defaults to 10000.

Maximum number of statements in a batched execution. Do not change this setting from the default. Non-default values may negatively impact performance. Defaults to 1000.

dynamic-filtering.enabled

Push down dynamic filters into JDBC queries. Defaults to true.

dynamic-filtering.wait-timeout

Maximum duration for which Trino waits for dynamic filters to be collected from the build side of joins before starting a JDBC query. Using a large timeout can potentially result in more detailed dynamic filters. However, it can also increase latency for some queries. Defaults to 20s.

The optional parameter query.comment-format allows you to configure a SQL comment that is sent to the datasource with each query. The format of this comment can contain any characters and the following metadata:

$QUERY_ID: The identifier of the query.

$USER: The name of the user who submits the query to Trino.

$SOURCE: The identifier of the client tool used to submit the query, for example trino-cli.

$TRACE_TOKEN: The trace token configured with the client tool.

The comment can provide more context about the query. This additional information is available in the logs of the datasource. To include environment variables from the Trino cluster with the comment , use the ${ENV:VARIABLE-NAME} syntax.

The following example sets a simple comment that identifies each query sent by Trino:

With this configuration, a query such as SELECT * FROM example_table; is sent to the datasource with the comment appended:

The following example improves on the preceding example by using metadata:

If Jane sent the query with the query identifier 20230622_180528_00000_bkizg, the following comment string is sent to the datasource:

Certain JDBC driver settings and logging configurations might cause the comment to be removed.

Pushing down a large list of predicates to the data source can compromise performance. Trino compacts large predicates into a simpler range predicate by default to ensure a balance between performance and predicate pushdown. If necessary, the threshold for this compaction can be increased to improve performance when the data source is capable of taking advantage of large predicates. Increasing this threshold may improve pushdown of large dynamic filters. The domain-compaction-threshold catalog configuration property or the domain_compaction_threshold catalog session property can be used to adjust the default value of 256 for this threshold.

When case-insensitive-name-matching is set to true, Trino is able to query non-lowercase schemas and tables by maintaining a mapping of the lowercase name to the actual name in the remote system. However, if two schemas and/or tables have names that differ only in case (such as “customers” and “Customers”) then Trino fails to query them due to ambiguity.

In these cases, use the case-insensitive-name-matching.config-file catalog configuration property to specify a configuration file that maps these remote schemas and tables to their respective Trino schemas and tables. Additionally, the JSON file must include both the schemas and tables properties, even if only as empty arrays.

Queries against one of the tables or schemes defined in the mapping attributes are run against the corresponding remote entity. For example, a query against tables in the case_insensitive_1 schema is forwarded to the CaseSensitiveName schema and a query against case_insensitive_2 is forwarded to the cASEsENSITIVEnAME schema.

At the table mapping level, a query on case_insensitive_1.table_1 as configured above is forwarded to CaseSensitiveName.tablex, and a query on case_insensitive_1.table_2 is forwarded to CaseSensitiveName.TABLEX.

By default, when a change is made to the mapping configuration file, Trino must be restarted to load the changes. Optionally, you can set the case-insensitive-name-matching.config-file.refresh-period to have Trino refresh the properties without requiring a restart:

Because Trino and Snowflake each support types that the other does not, this connector modifies some types when reading or writing data. Data types may not map the same way in both directions between Trino and the data source. Refer to the following sections for type mapping in each direction.

List of Snowflake data types.

The connector maps Snowflake types to the corresponding Trino types following this table:

INT, INTEGER, BIGINT, SMALLINT, TINYINT, BYTEINT

Synonymous with NUMBER(38,0). See Snowflake data types for fixed point numbers for more information.

FLOAT, FLOAT4, FLOAT8

The names FLOAT, FLOAT4, and FLOAT8 are for compatibility with other systems; Snowflake treats all three as 64-bit floating-point numbers. See Snowflake data types for floating point numbers for more information.

DOUBLE, DOUBLE PRECISION, REAL

Synonymous with FLOAT. See Snowflake data types for floating point numbers for more information.

Default precision and scale are (38,0).

Synonymous with NUMBER. See Snowflake data types for fixed point numbers for more information.

Synonymous with VARCHAR except default length is VARCHAR(1). See Snowflake String & Binary Data Types for more information.

Synonymous with VARCHAR. See Snowflake String & Binary Data Types for more information.

Synonymous with BINARY. See Snowflake String & Binary Data Types for more information.

TIMESTAMP with no time zone; time zone, if provided, is not stored. See Snowflake Date & Time Data Types for more information.

Alias for TIMESTAMP_NTZ. See Snowflake Date & Time Data Types for more information.

Alias for one of the TIMESTAMP variations (TIMESTAMP_NTZ by default). This connector always sets TIMESTAMP_NTZ as the variant.

TIMESTAMP WITH TIME ZONE

TIMESTAMP with time zone.

No other types are supported.

The connector maps Trino types to the corresponding Snowflake types following this table:

TIMESTAMP WITH TIME ZONE

No other types are supported.

The following properties can be used to configure how data types from the connected data source are mapped to Trino data types and how the metadata is cached in Trino.

unsupported-type-handling

Configure how unsupported column data types are handled:

IGNORE, column is not accessible.

CONVERT_TO_VARCHAR, column is converted to unbounded VARCHAR.

The respective catalog session property is unsupported_type_handling.

jdbc-types-mapped-to-varchar

Allow forced mapping of comma separated lists of data types to convert to unbounded VARCHAR

The connector provides read access and write access to data and metadata in a Snowflake database. In addition to the globally available and read operation statements, the connector supports the following features:

INSERT, see also Non-transactional INSERT

The connector supports adding rows using INSERT statements. By default, data insertion is performed by writing data to a temporary table. You can skip this step to improve performance and write directly to the target table. Set the insert.non-transactional-insert.enabled catalog property or the corresponding non_transactional_insert catalog session property to true.

Note that with this property enabled, data can be corrupted in rare cases where exceptions occur during the insert operation. With transactions disabled, no rollback can be performed.

Flush JDBC metadata caches. For example, the following system call flushes the metadata caches for all schemas in the example catalog

The execute procedure allows you to execute a query in the underlying data source directly. The query must use supported syntax of the connected data source. Use the procedure to access features which are not available in Trino or to execute queries that return no result set and therefore can not be used with the query or raw_query pass-through table function. Typical use cases are statements that create or alter objects, and require native feature such as constraints, default values, automatic identifier creation, or indexes. Queries can also invoke statements that insert, update, or delete data, and do not return any data as a result.

The query text is not parsed by Trino, only passed through, and therefore only subject to any security or access control of the underlying data source.

The following example sets the current database to the example_schema of the example catalog. Then it calls the procedure in that schema to drop the default value from your_column on your_table table using the standard SQL syntax in the parameter value assigned for query:

Verify that the specific database supports this syntax, and adapt as necessary based on the documentation for the specific connected database and database version.

The connector provides specific table functions to access Snowflake.

The query function allows you to query the underlying database directly. It requires syntax native to Snowflake, because the full query is pushed down and processed in Snowflake. This can be useful for accessing native features which are not available in Trino or for improving query performance in situations where running a query natively may be faster.

Find details about the SQL support of Snowflake that you can use in the query in the Snowflake SQL Command Reference, including PIVOT, lateral joins and other statements and functions.

The native query passed to the underlying data source is required to return a table as a result set. Only the data source performs validation or security checks for these queries using its own configuration. Trino does not perform these tasks. Only use passthrough queries to read data.

As a simple example, query the example catalog and select an entire table:

As a practical example, you can use the Snowflake SQL support for PIVOT to pivot on all distinct column values automatically with a dynamic pivot.

The query engine does not preserve the order of the results of this function. If the passed query contains an ORDER BY clause, the function result may not be ordered as expected.

The connector includes a number of performance improvements, detailed in the following sections.

The connector supports pushdown for a number of operations:

Aggregate pushdown for the following functions:

The connector performs pushdown where performance may be improved, but in order to preserve correctness an operation may not be pushed down. When pushdown of an operation may result in better performance but risks correctness, the connector prioritizes correctness.

**Examples:**

Example 1 (unknown):
```unknown
connector.name=snowflake
connection-url=jdbc:snowflake://<account>.snowflakecomputing.com
connection-user=root
connection-password=secret
snowflake.account=account
snowflake.database=database
snowflake.role=role
snowflake.warehouse=warehouse
```

Example 2 (unknown):
```unknown
connector.name=snowflake
connection-url=jdbc:snowflake://<account>.snowflakecomputing.com
connection-user=root
connection-password=secret
snowflake.account=account
snowflake.database=database
snowflake.role=role
snowflake.warehouse=warehouse
```

Example 3 (unknown):
```unknown
--add-opens=java.base/java.nio=ALL-UNNAMED
--sun-misc-unsafe-memory-access=allow
```

Example 4 (unknown):
```unknown
--add-opens=java.base/java.nio=ALL-UNNAMED
--sun-misc-unsafe-memory-access=allow
```

---

## Exasol connector — Trino 478 Documentation

**URL:** https://trino.io/docs/current/connector/exasol.html

**Contents:**
- Exasol connector#
- Requirements#
- Configuration#
  - Data source authentication#
  - General configuration properties#
  - Domain compaction threshold#
  - Case insensitive matching#
- Type mapping#
  - Exasol to Trino type mapping#
  - Mapping numeric types#

The Exasol connector allows querying an Exasol database.

To connect to Exasol, you need:

Exasol database version 8.34.0 or higher.

Network access from the Trino coordinator and workers to Exasol. Port 8563 is the default port.

To configure the Exasol connector as the example catalog, create a file named example.properties in etc/catalog. Include the following connection properties in the file:

The connection-url defines the connection information and parameters to pass to the JDBC driver. See the Exasol JDBC driver documentation for more information.

The connection-user and connection-password are typically required and determine the user credentials for the connection, often a service user. You can use secrets to avoid using actual values in catalog properties files.

If your Exasol database uses a self-signed TLS certificate you must specify the certificate’s fingerprint in the JDBC URL using parameter fingerprint, e.g.: jdbc:exa:exasol.example.com:8563;fingerprint=ABC123.

The connector can provide credentials for the data source connection in multiple ways:

inline, in the connector configuration file

in a separate properties file

as extra credentials set when connecting to Trino

You can use secrets to avoid storing sensitive values in the catalog properties files.

The following table describes configuration properties for connection credentials:

credential-provider.type

Type of the credential provider. Must be one of INLINE, FILE, or KEYSTORE; defaults to INLINE.

Connection user name.

Name of the extra credentials property, whose value to use as the user name. See extraCredentials in Parameter reference.

password-credential-name

Name of the extra credentials property, whose value to use as the password.

connection-credential-file

Location of the properties file where credentials are present. It must contain the connection-user and connection-password properties.

The location of the Java Keystore file, from which to read credentials.

File format of the keystore file, for example JKS or PEM.

Password for the key store.

keystore-user-credential-name

Name of the key store entity to use as the user name.

keystore-user-credential-password

Password for the user name key store entity.

keystore-password-credential-name

Name of the key store entity to use as the password.

keystore-password-credential-password

Password for the password key store entity.

The following table describes general catalog configuration properties for the connector:

case-insensitive-name-matching

Support case insensitive schema and table names. Defaults to false.

case-insensitive-name-matching.cache-ttl

Duration for which case insensitive schema and table names are cached. Defaults to 1m.

case-insensitive-name-matching.config-file

Path to a name mapping configuration file in JSON format that allows Trino to disambiguate between schemas and tables with similar names in different cases. Defaults to null.

case-insensitive-name-matching.config-file.refresh-period

Frequency with which Trino checks the name matching configuration file for changes. The duration value defaults to 0s (refresh disabled).

Duration for which metadata, including table and column statistics, is cached. Defaults to 0s (caching disabled).

metadata.cache-missing

Cache the fact that metadata, including table and column statistics, is not available. Defaults to false.

metadata.schemas.cache-ttl

Duration for which schema metadata is cached. Defaults to the value of metadata.cache-ttl.

metadata.tables.cache-ttl

Duration for which table metadata is cached. Defaults to the value of metadata.cache-ttl.

metadata.statistics.cache-ttl

Duration for which tables statistics are cached. Defaults to the value of metadata.cache-ttl.

metadata.cache-maximum-size

Maximum number of objects stored in the metadata cache. Defaults to 10000.

Maximum number of statements in a batched execution. Do not change this setting from the default. Non-default values may negatively impact performance. Defaults to 1000.

dynamic-filtering.enabled

Push down dynamic filters into JDBC queries. Defaults to true.

dynamic-filtering.wait-timeout

Maximum duration for which Trino waits for dynamic filters to be collected from the build side of joins before starting a JDBC query. Using a large timeout can potentially result in more detailed dynamic filters. However, it can also increase latency for some queries. Defaults to 20s.

Pushing down a large list of predicates to the data source can compromise performance. Trino compacts large predicates into a simpler range predicate by default to ensure a balance between performance and predicate pushdown. If necessary, the threshold for this compaction can be increased to improve performance when the data source is capable of taking advantage of large predicates. Increasing this threshold may improve pushdown of large dynamic filters. The domain-compaction-threshold catalog configuration property or the domain_compaction_threshold catalog session property can be used to adjust the default value of 256 for this threshold.

When case-insensitive-name-matching is set to true, Trino is able to query non-lowercase schemas and tables by maintaining a mapping of the lowercase name to the actual name in the remote system. However, if two schemas and/or tables have names that differ only in case (such as “customers” and “Customers”) then Trino fails to query them due to ambiguity.

In these cases, use the case-insensitive-name-matching.config-file catalog configuration property to specify a configuration file that maps these remote schemas and tables to their respective Trino schemas and tables. Additionally, the JSON file must include both the schemas and tables properties, even if only as empty arrays.

Queries against one of the tables or schemes defined in the mapping attributes are run against the corresponding remote entity. For example, a query against tables in the case_insensitive_1 schema is forwarded to the CaseSensitiveName schema and a query against case_insensitive_2 is forwarded to the cASEsENSITIVEnAME schema.

At the table mapping level, a query on case_insensitive_1.table_1 as configured above is forwarded to CaseSensitiveName.tablex, and a query on case_insensitive_1.table_2 is forwarded to CaseSensitiveName.TABLEX.

By default, when a change is made to the mapping configuration file, Trino must be restarted to load the changes. Optionally, you can set the case-insensitive-name-matching.config-file.refresh-period to have Trino refresh the properties without requiring a restart:

Because Trino and Exasol each support types that the other does not, this connector modifies some types when reading data. Data types may not map the same way in both directions between Trino and the data source. Refer to the following sections for type mapping in each direction.

Trino supports selecting Exasol database types. This table shows the Exasol to Trino data type mapping:

See Mapping numeric types

No other types are supported.

An Exasol DECIMAL(p, s) maps to Trino’s DECIMAL(p, s) and vice versa except in these conditions:

No precision is specified for the column (example: DECIMAL or DECIMAL(*)).

Scale (s) is greater than precision.

Precision (p) is greater than 36.

Trino’s VARCHAR(n) maps to VARCHAR(n) and vice versa if n is no greater than 2000000. Exasol does not support longer values. If no length is specified, the connector uses 2000000.

Trino’s CHAR(n) maps to CHAR(n) and vice versa if n is no greater than 2000. Exasol does not support longer values.

The following properties can be used to configure how data types from the connected data source are mapped to Trino data types and how the metadata is cached in Trino.

unsupported-type-handling

Configure how unsupported column data types are handled:

IGNORE, column is not accessible.

CONVERT_TO_VARCHAR, column is converted to unbounded VARCHAR.

The respective catalog session property is unsupported_type_handling.

jdbc-types-mapped-to-varchar

Allow forced mapping of comma separated lists of data types to convert to unbounded VARCHAR

The connector provides read access to data and metadata in Exasol. In addition to the globally available and read operation statements, the connector supports the following features:

Flush JDBC metadata caches. For example, the following system call flushes the metadata caches for all schemas in the example catalog

The execute procedure allows you to execute a query in the underlying data source directly. The query must use supported syntax of the connected data source. Use the procedure to access features which are not available in Trino or to execute queries that return no result set and therefore can not be used with the query or raw_query pass-through table function. Typical use cases are statements that create or alter objects, and require native feature such as constraints, default values, automatic identifier creation, or indexes. Queries can also invoke statements that insert, update, or delete data, and do not return any data as a result.

The query text is not parsed by Trino, only passed through, and therefore only subject to any security or access control of the underlying data source.

The following example sets the current database to the example_schema of the example catalog. Then it calls the procedure in that schema to drop the default value from your_column on your_table table using the standard SQL syntax in the parameter value assigned for query:

Verify that the specific database supports this syntax, and adapt as necessary based on the documentation for the specific connected database and database version.

The connector provides specific table functions to access Exasol.

The query function allows you to query the underlying database directly. It requires syntax native to Exasol, because the full query is pushed down and processed in Exasol. This can be useful for accessing native features which are not available in Trino or for improving query performance in situations where running a query natively may be faster.

The native query passed to the underlying data source is required to return a table as a result set. Only the data source performs validation or security checks for these queries using its own configuration. Trino does not perform these tasks. Only use passthrough queries to read data.

As a simple example, query the example catalog and select an entire table::

As a practical example, you can use the WINDOW clause from Exasol:

The query engine does not preserve the order of the results of this function. If the passed query contains an ORDER BY clause, the function result may not be ordered as expected.

The connector includes a number of performance improvements, detailed in the following sections.

The connector supports pushdown for a number of operations:

**Examples:**

Example 1 (unknown):
```unknown
connector.name=exasol
connection-url=jdbc:exa:exasol.example.com:8563
connection-user=user
connection-password=secret
```

Example 2 (unknown):
```unknown
connector.name=exasol
connection-url=jdbc:exa:exasol.example.com:8563
connection-user=user
connection-password=secret
```

Example 3 (unknown):
```unknown
{
  "schemas": [
    {
      "remoteSchema": "CaseSensitiveName",
      "mapping": "case_insensitive_1"
    },
    {
      "remoteSchema": "cASEsENSITIVEnAME",
      "mapping": "case_insensitive_2"
    }],
  "tables": [
    {
      "remoteSchema": "CaseSensitiveName",
      "remoteTable": "tablex",
      "mapping": "table_1"
    },
    {
      "remoteSchema": "CaseSensitiveName",
      "remoteTable": "TABLEX",
      "mapping": "table_2"
    }]
}
```

Example 4 (unknown):
```unknown
{
  "schemas": [
    {
      "remoteSchema": "CaseSensitiveName",
      "mapping": "case_insensitive_1"
    },
    {
      "remoteSchema": "cASEsENSITIVEnAME",
      "mapping": "case_insensitive_2"
    }],
  "tables": [
    {
      "remoteSchema": "CaseSensitiveName",
      "remoteTable": "tablex",
      "mapping": "table_1"
    },
    {
      "remoteSchema": "CaseSensitiveName",
      "remoteTable": "TABLEX",
      "mapping": "table_2"
    }]
}
```

---

## Redis connector — Trino 478 Documentation

**URL:** https://trino.io/docs/current/connector/redis.html

**Contents:**
- Redis connector#
- Requirements#
- Configuration#
  - Multiple Redis servers#
- Configuration properties#
  - redis.table-names#
  - redis.default-schema#
  - redis.nodes#
  - redis.scan-count#
  - redis.max-keys-per-fetch#

The Redis connector allows querying of live data stored in Redis. This can be used to join data between different systems like Redis and Hive.

Each Redis key/value pair is presented as a single row in Trino. Rows can be broken down into cells by using table definition files.

Currently, only Redis key of string and zset types are supported, only Redis value of string and hash types are supported.

Requirements for using the connector in a catalog to connect to a Redis data source are:

Redis 5.0.14 or higher (Redis Cluster is not supported)

Network access, by default on port 6379, from the Trino coordinator and workers to Redis.

To configure the Redis connector, create a catalog properties file etc/catalog/example.properties with the following content, replacing the properties as appropriate:

You can have as many catalogs as you need. If you have additional Redis servers, simply add another properties file to etc/catalog with a different name, making sure it ends in .properties.

The following configuration properties are available:

List of all tables provided by the catalog

Default schema name for tables

Location of the Redis server

Redis parameter for scanning of the keys

redis.max-keys-per-fetch

Get values associated with the specified number of keys in the redis command such as MGET(key…)

redis.key-prefix-schema-table

Redis keys have schema-name:table-name prefix

Delimiter separating schema_name and table_name if redis.key-prefix-schema-table is used

redis.table-description-dir

Directory containing table description files

redis.table-description-cache-ttl

The cache time for table description files

redis.hide-internal-columns

Controls whether internal columns are part of the table schema or not

Redis server username

Redis server password

Comma-separated list of all tables provided by this catalog. A table name can be unqualified (simple name) and is placed into the default schema (see below), or qualified with a schema name (<schema-name>.<table-name>).

For each table defined, a table description file (see below) may exist. If no table description file exists, the table only contains internal columns (see below).

This property is optional; the connector relies on the table description files specified in the redis.table-description-dir property.

Defines the schema which will contain all tables that were defined without a qualifying schema name.

This property is optional; the default is default.

The hostname:port pair for the Redis server.

This property is required; there is no default.

Redis Cluster is not supported.

The internal COUNT parameter for the Redis SCAN command when connector is using SCAN to find keys for the data. This parameter can be used to tune performance of the Redis connector.

This property is optional; the default is 100.

The internal number of keys for the Redis MGET command and Pipeline HGETALL command when connector is using these commands to find values of keys. This parameter can be used to tune performance of the Redis connector.

This property is optional; the default is 100.

If true, only keys prefixed with the schema-name:table-name are scanned for a table, and all other keys are filtered out. If false, all keys are scanned.

This property is optional; the default is false.

The character used for separating schema-name and table-name when redis.key-prefix-schema-table is true

This property is optional; the default is :.

References a folder within Trino deployment that holds one or more JSON files, which must end with .json and contain table description files.

Note that the table description files will only be used by the Trino coordinator node.

This property is optional; the default is etc/redis.

The Redis connector dynamically loads the table description files after waiting for the time specified by this property. Therefore, there is no need to update the redis.table-names property and restart the Trino service when adding, updating, or deleting a file end with .json to redis.table-description-dir folder.

This property is optional; the default is 5m.

In addition to the data columns defined in a table description file, the connector maintains a number of additional columns for each table. If these columns are hidden, they can still be used in queries, but they do not show up in DESCRIBE <table-name> or SELECT *.

This property is optional; the default is true.

The Redis database to query.

This property is optional; the default is 0.

The username for Redis server.

This property is optional; the default is null.

The password for password-protected Redis server.

This property is optional; the default is null.

For each defined table, the connector maintains the following columns:

Redis value corresponding to the key.

Number of bytes in the key.

Number of bytes in the value.

True if the decoder could not decode the key for this row. When true, data columns mapped from the key should be treated as invalid.

True if the decoder could not decode the message for this row. When true, data columns mapped from the value should be treated as invalid.

For tables without a table definition file, the _key_corrupt and _value_corrupt columns are false.

With the Redis connector it is possible to further reduce Redis key/value pairs into granular cells, provided the key/value string follows a particular format. This process defines new columns that can be further queried from Trino.

A table definition file consists of a JSON definition for a table. The name of the file can be arbitrary, but must end in .json.

Trino table name defined by this file.

Schema which will contain the table. If omitted, the default schema name is used.

Field definitions for data columns mapped to the value key.

Field definitions for data columns mapped to the value itself.

Please refer to the Kafka connector page for the description of the dataFormat as well as various available decoders.

In addition to the above Kafka types, the Redis connector supports hash type for the value field which represent data stored in the Redis hash.

Because Trino and Redis each support types that the other does not, this connector maps some types when reading data. Type mapping depends on the RAW, CSV, JSON, and AVRO file formats.

A decoder is used to map data to table columns.

The connector contains the following decoders:

raw: Message is not interpreted; ranges of raw message bytes are mapped to table columns.

csv: Message is interpreted as comma separated message, and fields are mapped to table columns.

json: Message is parsed as JSON, and JSON fields are mapped to table columns.

avro: Message is parsed based on an Avro schema, and Avro fields are mapped to table columns.

If no table definition file exists for a table, the dummy decoder is used, which does not expose any columns.

The raw decoder supports reading of raw byte-based values from message or key, and converting it into Trino columns.

For fields, the following attributes are supported:

dataFormat - Selects the width of the data type converted.

type - Trino data type. See the following table for a list of supported data types.

mapping - <start>[:<end>] - Start and end position of bytes to convert (optional).

The dataFormat attribute selects the number of bytes converted. If absent, BYTE is assumed. All values are signed.

Supported values are:

SHORT - two bytes (big-endian)

INT - four bytes (big-endian)

LONG - eight bytes (big-endian)

FLOAT - four bytes (IEEE 754 format)

DOUBLE - eight bytes (IEEE 754 format)

The type attribute defines the Trino data type on which the value is mapped.

Depending on the Trino type assigned to a column, different values of dataFormat can be used:

Allowed dataFormat values

BYTE, SHORT, INT, LONG

BYTE, SHORT, INT, LONG

No other types are supported.

The mapping attribute specifies the range of the bytes in a key or message used for decoding. It can be one or two numbers separated by a colon (<start>[:<end>]).

If only a start position is given:

For fixed width types, the column uses the appropriate number of bytes for the specified dataFormat (see above).

When the VARCHAR value is decoded, all bytes from the start position to the end of the message is used.

If start and end position are given:

For fixed width types, the size must be equal to the number of bytes used by specified dataFormat.

For the VARCHAR data type all bytes between start (inclusive) and end (exclusive) are used.

If no mapping attribute is specified, it is equivalent to setting the start position to 0 and leaving the end position undefined.

The decoding scheme of numeric data types (BIGINT, INTEGER, SMALLINT, TINYINT, DOUBLE) is straightforward. A sequence of bytes is read from input message and decoded according to either:

big-endian encoding (for integer types)

IEEE 754 format for (for DOUBLE).

The length of a decoded byte sequence is implied by the dataFormat.

For the VARCHAR data type, a sequence of bytes is interpreted according to UTF-8 encoding.

The CSV decoder converts the bytes representing a message or key into a string using UTF-8 encoding, and interprets the result as a link of comma-separated values.

For fields, the type and mapping attributes must be defined:

type - Trino data type. See the following table for a list of supported data types.

mapping - The index of the field in the CSV record.

The dataFormat and formatHint attributes are not supported and must be omitted.

BIGINT, INTEGER, SMALLINT, TINYINT

Decoded using Java Long.parseLong()

Decoded using Java Double.parseDouble()

“true” character sequence maps to true. Other character sequences map to false

No other types are supported.

The JSON decoder converts the bytes representing a message or key into Javascript Object Notation (JSON) according to RFC 4627. The message or key must convert into a JSON object, not an array or simple type.

For fields, the following attributes are supported:

type - Trino data type of column.

dataFormat - Field decoder to be used for column.

mapping - Slash-separated list of field names to select a field from the JSON object.

formatHint - Only for custom-date-time.

The JSON decoder supports multiple field decoders with _default being used for standard table columns and a number of decoders for date and time-based types.

The following table lists Trino data types, which can be used in type and matching field decoders, and specified via dataFormat attribute:

Allowed dataFormat values

BIGINT, INTEGER, SMALLINT, TINYINT, DOUBLE, BOOLEAN, VARCHAR, VARCHAR(x)

Default field decoder (omitted dataFormat attribute)

custom-date-time, iso8601

custom-date-time, iso8601, milliseconds-since-epoch, seconds-since-epoch

custom-date-time, iso8601

custom-date-time, iso8601, rfc2822, milliseconds-since-epoch, seconds-since-epoch

TIMESTAMP WITH TIME ZONE

custom-date-time, iso8601, rfc2822, milliseconds-since-epoch, seconds-since-epoch

No other types are supported.

This is the standard field decoder. It supports all the Trino physical data types. A field value is transformed under JSON conversion rules into boolean, long, double, or string values. This decoder should be used for columns that are not date or time based.

To convert values from JSON objects to Trino DATE, TIME, TIME WITH TIME ZONE, TIMESTAMP or TIMESTAMP WITH TIME ZONE columns, select special decoders using the dataFormat attribute of a field definition.

iso8601 - Text based, parses a text field as an ISO 8601 timestamp.

rfc2822 - Text based, parses a text field as an RFC 2822 timestamp.

custom-date-time - Text based, parses a text field according to Joda format pattern specified via formatHint attribute. The format pattern should conform to https://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormat.html.

milliseconds-since-epoch - Number-based, interprets a text or number as number of milliseconds since the epoch.

seconds-since-epoch - Number-based, interprets a text or number as number of milliseconds since the epoch.

For TIMESTAMP WITH TIME ZONE and TIME WITH TIME ZONE data types, if timezone information is present in decoded value, it is used as a Trino value. Otherwise, the result time zone is set to UTC.

The Avro decoder converts the bytes representing a message or key in Avro format based on a schema. The message must have the Avro schema embedded. Trino does not support schemaless Avro decoding.

The dataSchema must be defined for any key or message using Avro decoder. Avro decoder should point to the location of a valid Avro schema file of the message which must be decoded. This location can be a remote web server (e.g.: dataSchema: 'http://example.org/schema/avro_data.avsc') or local file system(e.g.: dataSchema: '/usr/local/schema/avro_data.avsc'). The decoder fails if this location is not accessible from the Trino cluster.

The following attributes are supported:

name - Name of the column in the Trino table.

type - Trino data type of column.

mapping - A slash-separated list of field names to select a field from the Avro schema. If the field specified in mapping does not exist in the original Avro schema, a read operation returns NULL.

The following table lists the supported Trino types that can be used in type for the equivalent Avro field types:

Allowed Avro data type

No other types are supported.

The Avro decoder supports schema evolution with backward compatibility. With backward compatibility, a newer schema can be used to read Avro data created with an older schema. Any change in the Avro schema must also be reflected in Trino’s topic definition file. Newly added or renamed fields must have a default value in the Avro schema file.

The schema evolution behavior is as follows:

Column added in new schema: Data created with an older schema produces a default value when the table is using the new schema.

Column removed in new schema: Data created with an older schema no longer outputs the data from the column that was removed.

Column is renamed in the new schema: This is equivalent to removing the column and adding a new one, and data created with an older schema produces a default value when the table is using the new schema.

Changing type of column in the new schema: If the type coercion is supported by Avro, then the conversion happens. An error is thrown for incompatible types.

The connector provides globally available and read operation statements to access data and metadata in Redis.

The connector includes a number of performance improvements, detailed in the following sections.

The connector performs pushdown where performance may be improved, but in order to preserve correctness an operation may not be pushed down. When pushdown of an operation may result in better performance but risks correctness, the connector prioritizes correctness.

The connector supports pushdown of keys of string type only, the zset type is not supported. Key pushdown is not supported when multiple key fields are defined in the table definition file.

The connector supports pushdown of equality predicates, such as IN or =. Inequality predicates, such as !=, and range predicates, such as >, <, or BETWEEN are not pushed down.

In the following example, the predicate of the first query is not pushed down since > is a range predicate. The other queries are pushed down:

**Examples:**

Example 1 (unknown):
```unknown
connector.name=redis
redis.table-names=schema1.table1,schema1.table2
redis.nodes=host:port
```

Example 2 (unknown):
```unknown
connector.name=redis
redis.table-names=schema1.table1,schema1.table2
redis.nodes=host:port
```

Example 3 (unknown):
```unknown
{
    "tableName": ...,
    "schemaName": ...,
    "key": {
        "dataFormat": ...,
        "fields": [
            ...
        ]
    },
    "value": {
        "dataFormat": ...,
        "fields": [
            ...
       ]
    }
}
```

Example 4 (unknown):
```unknown
{
    "tableName": ...,
    "schemaName": ...,
    "key": {
        "dataFormat": ...,
        "fields": [
            ...
        ]
    },
    "value": {
        "dataFormat": ...,
        "fields": [
            ...
       ]
    }
}
```

---

## Delta Lake connector — Trino 478 Documentation

**URL:** https://trino.io/docs/current/connector/delta-lake.html

**Contents:**
- Delta Lake connector#
- Requirements#
- General configuration#
- File system access configuration#
  - Delta Lake general configuration properties#
  - Catalog session properties#
  - Fault-tolerant execution support#
- Type mapping#
  - Delta Lake to Trino type mapping#
  - Trino to Delta Lake type mapping#

The Delta Lake connector allows querying data stored in the Delta Lake format, including Databricks Delta Lake. The connector can natively read the Delta Lake transaction log and thus detect when external systems change data.

To connect to Databricks Delta Lake, you need:

Tables written by Databricks Runtime 7.3 LTS, 9.1 LTS, 10.4 LTS, 11.3 LTS, 12.2 LTS, 13.3 LTS, 14.3 LTS, 15.4 LTS and 16.4 LTS are supported.

Deployments using AWS, HDFS, Azure Storage, and Google Cloud Storage (GCS) are fully supported.

Network access from the coordinator and workers to the Delta Lake storage.

Access to the Hive metastore service (HMS) of Delta Lake or a separate HMS, or a Glue metastore.

Network access to the HMS from the coordinator and workers. Port 9083 is the default port for the Thrift protocol used by the HMS.

Data files stored in the Parquet file format on a supported file system.

To configure the Delta Lake connector, create a catalog properties file etc/catalog/example.properties that references the delta_lake connector.

You must configure a metastore for metadata.

You must select and configure one of the supported file systems.

Replace the fs.x.enabled configuration property with the desired file system.

If you are using AWS Glue as your metastore, you must instead set hive.metastore to glue:

Each metastore type has specific configuration properties along with general metastore configuration properties.

The connector recognizes Delta Lake tables created in the metastore by the Databricks runtime. If non-Delta Lake tables are present in the metastore as well, they are not visible to the connector.

The connector supports accessing the following file systems:

Azure Storage file system support

Google Cloud Storage file system support

S3 file system support

HDFS file system support

You must enable and configure the specific file system access. Legacy support is not recommended and will be removed.

The following configuration properties are all using reasonable, tested default values. Typical usage does not require you to configure them.

delta.metadata.cache-ttl

Caching duration for Delta Lake tables metadata.

delta.metadata.cache-max-retained-size

Maximum retained size of Delta table metadata stored in cache. Must be specified in data size values such as 64MB. Default is calculated to 5% of the maximum memory allocated to the JVM.

delta.metadata.live-files.cache-size

Amount of memory allocated for caching information about files. Must be specified in data size values such as 64MB. Default is calculated to 10% of the maximum memory allocated to the JVM.

delta.metadata.live-files.cache-ttl

Caching duration for active files that correspond to the Delta Lake tables.

delta.compression-codec

The compression codec to be used when writing new data files. Possible values are:

The equivalent catalog session property is compression_codec.

delta.max-partitions-per-writer

Maximum number of partitions per writer.

delta.hide-non-delta-lake-tables

Hide information about tables that are not managed by Delta Lake. Hiding only applies to tables with the metadata managed in a Glue catalog, and does not apply to usage with a Hive metastore service.

delta.enable-non-concurrent-writes

Enable write support for all supported file systems. Specifically, take note of the warning about concurrency and checkpoints.

delta.default-checkpoint-writing-interval

Default integer count to write transaction log checkpoint entries. If the value is set to N, then checkpoints are written after every Nth statement performing table writes. The value can be overridden for a specific table with the checkpoint_interval table property.

delta.hive-catalog-name

Name of the catalog to which SELECT queries are redirected when a Hive table is detected.

delta.checkpoint-row-statistics-writing.enabled

Enable writing row statistics to checkpoint files.

delta.checkpoint-filtering.enabled

Enable pruning of data file entries as well as data file statistics columns which are irrelevant for the query when reading Delta Lake checkpoint files. Reading only the relevant active file data from the checkpoint, directly from the storage, instead of relying on the active files caching, likely results in decreased memory pressure on the coordinator. The equivalent catalog session property is checkpoint_filtering_enabled.

delta.dynamic-filtering.wait-timeout

Duration to wait for completion of dynamic filtering during split generation. The equivalent catalog session property is dynamic_filtering_wait_timeout.

delta.table-statistics-enabled

Enables Table statistics for performance improvements. The equivalent catalog session property is statistics_enabled.

delta.extended-statistics.enabled

Enable statistics collection with ANALYZE and use of extended statistics. The equivalent catalog session property is extended_statistics_enabled.

delta.extended-statistics.collect-on-write

Enable collection of extended statistics for write operations. The equivalent catalog session property is extended_statistics_collect_on_write.

delta.per-transaction-metastore-cache-maximum-size

Maximum number of metastore data objects per transaction in the Hive metastore cache.

delta.metastore.store-table-metadata

Store table comments and colum definitions in the metastore. The write permission is required to update the metastore.

delta.metastore.store-table-metadata-threads

Number of threads used for storing table metadata in metastore.

delta.delete-schema-locations-fallback

Whether schema locations are deleted when Trino can’t determine whether they contain external files.

delta.parquet.time-zone

Time zone for Parquet read and write.

delta.target-max-file-size

Target maximum size of written files; the actual size could be larger. The equivalent catalog session property is target_max_file_size.

delta.unique-table-location

Use randomized, unique table locations.

delta.register-table-procedure.enabled

Enable to allow users to call the register_table procedure.

delta.vacuum.min-retention

Minimum retention threshold for the files taken into account for removal by the VACUUM procedure. The equivalent catalog session property is vacuum_min_retention.

delta.deletion-vectors-enabled

Set to true for enabling deletion vectors by default when creating new tables.

delta.metadata.parallelism

Number of threads used for retrieving metadata. Currently, only table loading is parallelized.

delta.checkpoint-processing.parallelism

Number of threads used for retrieving checkpoint files of each table. Currently, only retrievals of V2 Checkpoint’s sidecar files are parallelized.

The following table describes catalog session properties supported by the Delta Lake connector:

parquet_max_read_block_size

The maximum block size used when reading Parquet files.

parquet_writer_block_size

The maximum block size created by the Parquet writer.

parquet_writer_page_size

The maximum page size created by the Parquet writer.

parquet_writer_page_value_count

The maximum value count of pages created by the Parquet writer.

parquet_writer_batch_size

Maximum number of rows processed by the Parquet writer in a batch.

projection_pushdown_enabled

Read only projected fields from row columns while performing SELECT queries.

The connector supports Fault-tolerant execution of query processing. Read and write operations are both supported with any retry policy.

Because Trino and Delta Lake each support types that the other does not, this connector modifies some types when reading or writing data. Data types might not map the same way in both directions between Trino and the data source. Refer to the following sections for type mapping in each direction.

See the Delta Transaction Log specification for more information about supported data types in the Delta Lake table format specification.

The connector maps Delta Lake types to the corresponding Trino types following this table:

TIMESTAMPNTZ (TIMESTAMP_NTZ)

TIMESTAMP(3) WITH TIME ZONE

No other types are supported.

The connector maps Trino types to the corresponding Delta Lake types following this table:

TIMESTAMPNTZ (TIMESTAMP_NTZ)

TIMESTAMP(3) WITH TIME ZONE

No other types are supported.

The connector supports the following Delta Lake table features:

Iceberg compatibility V1 & V2

Timestamp without time zone

Vacuum protocol check

No other features are supported.

The Delta Lake connector allows you to choose one of several means of providing authorization at the catalog level. You can select a different type of authorization check in different Delta Lake catalog files.

Enable authorization checks for the connector by setting the delta.security property in the catalog properties file. This property must be one of the security values in the following table:

ALLOW_ALL (default value)

No authorization checks are enforced.

The connector relies on system-level access control.

Operations that read data or metadata, such as SELECT are permitted. No operations that write data or metadata, such as CREATE TABLE, INSERT, or DELETE are allowed.

Authorization checks are enforced using a catalog-level access control configuration file whose path is specified in the security.config-file catalog configuration property. See Catalog-level access control files for information on the authorization configuration file.

The connector provides read and write access to data and metadata in Delta Lake. In addition to the globally available and read operation statements, the connector supports the following features:

Data management, see details for Delta Lake data management

Schema and table management, see details for Delta Lake schema and table management

The connector offers the ability to query historical data. This allows to query the table as it was when a previous snapshot of the table was taken, even if the data has since been modified or deleted.

The historical data of the table can be retrieved by specifying the version number corresponding to the version of the table to be retrieved:

A different approach of retrieving historical data is to specify a point in time in the past, such as a day or week ago. The latest snapshot of the table taken before or at the specified timestamp in the query is internally used for providing the previous state of the table:

The connector allows to create a new snapshot through Delta Lake’s replace table.

You can use a date to specify a point a time in the past for using a snapshot of a table in a query. Assuming that the session time zone is America/Los_Angeles the following queries are equivalent:

Use the $history metadata table to determine the snapshot ID of the table like in the following query:

Use the CALL statement to perform data manipulation or administrative tasks. Procedures are available in the system schema of each catalog. The following code snippet displays how to call the example_procedure in the examplecatalog catalog:

The connector can register existing Delta Lake tables into the metastore if delta.register-table-procedure.enabled is set to true for the catalog.

The system.register_table procedure allows the caller to register an existing Delta Lake table in the metastore, using its existing transaction logs and data files:

To prevent unauthorized users from accessing data, this procedure is disabled by default. The procedure is enabled only when delta.register-table-procedure.enabled is set to true.

The connector can remove existing Delta Lake tables from the metastore. Once unregistered, you can no longer query the table from Trino.

The procedure system.unregister_table allows the caller to unregister an existing Delta Lake table from the metastores without deleting the data:

system.flush_metadata_cache()

Flushes all metadata caches.

system.flush_metadata_cache(schema_name => ..., table_name => ...)

Flushes metadata cache entries of a specific table. Procedure requires passing named parameters.

The VACUUM procedure removes all old files that are not in the transaction log, as well as files that are not needed to read table snapshots newer than the current time minus the retention period defined by the retention period parameter.

Users with INSERT and DELETE permissions on a table can run VACUUM as follows:

All parameters are required and must be presented in the following order:

The delta.vacuum.min-retention configuration property provides a safety measure to ensure that files are retained as expected. The minimum value for this property is 0s. There is a minimum retention session property as well, vacuum_min_retention.

You can use the connector to INSERT, DELETE, UPDATE, and MERGE data in Delta Lake tables.

Write operations are supported for tables stored on the following systems:

Azure ADLS Gen2, Google Cloud Storage

Writes to the Azure ADLS Gen2 and Google Cloud Storage are enabled by default. Trino detects write collisions on these storage systems when writing from multiple Trino clusters, or from other query engines.

S3 and S3-compatible storage

Writes to Amazon S3 and S3-compatible storage must be enabled with the delta.enable-non-concurrent-writes property. Writes to S3 can safely be made from multiple Trino clusters; however, write collisions are not detected when writing concurrently from other Delta Lake engines. You must make sure that no concurrent data modifications are run to avoid data corruption.

The Schema and table management functionality includes support for:

ALTER TABLE, see details for Delta Lake ALTER TABLE

The connector supports creating schemas. You can create a schema with or without a specified location.

You can create a schema with the CREATE SCHEMA statement and the location schema property. Tables in this schema are located in a subdirectory under the schema location. Data files for tables in this schema using the default location are cleaned up if the table is dropped:

Optionally, the location can be omitted. Tables in this schema must have a location included when you create them. The data files for these tables are not removed if the table is dropped:

When Delta Lake tables exist in storage but not in the metastore, Trino can be used to register the tables:

The table schema is read from the transaction log instead. If the schema is changed by an external system, Trino automatically uses the new schema.

Using CREATE TABLE with an existing table content is disallowed, use the system.register_table procedure instead.

If the specified location does not already contain a Delta table, the connector automatically writes the initial transaction log entries and registers the table in the metastore. As a result, any Databricks engine can write to the table:

The Delta Lake connector also supports creating tables using the CREATE TABLE AS syntax.

The Delta Lake connector supports schema evolution, with safe column add, drop, and rename operations for non nested structures.

The connector supports the following ALTER TABLE statements.

The connector supports replacing an existing table as an atomic operation. Atomic table replacement creates a new snapshot with the new table definition as part of the table history.

To replace a table, use CREATE OR REPLACE TABLE or CREATE OR REPLACE TABLE AS.

In this example, a table example_table is replaced by a completely new definition and data from the source table:

The connector supports the following commands for use with ALTER TABLE EXECUTE.

The optimize command is used for rewriting the content of the specified table so that it is merged into fewer but larger files. If the table is partitioned, the data compaction acts separately on each partition selected for optimization. This operation improves read performance.

All files with a size below the optional file_size_threshold parameter (default value for the threshold is 100MB) are merged:

The following statement merges files in a table that are under 128 megabytes in size:

You can use a WHERE clause with the columns used to partition the table to filter which partitions are optimized:

You can use a more complex WHERE clause to narrow down the scope of the optimize procedure. The following example casts the timestamp values to dates, and uses a comparison to only optimize partitions with data from the year 2022 or newer:

Use a WHERE clause with metadata columns to filter which files are optimized.

The connector only supports the ALTER TABLE RENAME TO statement when met with one of the following conditions:

The table type is external.

The table is backed by a metastore that does not perform object storage operations, for example, AWS Glue.

The following table properties are available for use:

File system location URI for the table.

Set partition columns.

Set the checkpoint interval in number of table writes.

change_data_feed_enabled

Enables storing change data feed entries.

Column mapping mode. Possible values are:

deletion_vectors_enabled

Enables deletion vectors.

The following example uses all available table properties:

The connector supports read and write operations on shallow cloned tables. Trino does not support creating shallow clone tables. More information about shallow cloning is available in the Delta Lake documentation.

Shallow cloned tables let you test queries or experiment with changes to a table without duplicating data.

The connector exposes several metadata tables for each Delta Lake table. These metadata tables contain information about the internal structure of the Delta Lake table. You can query each metadata table by appending the metadata table name to the table name:

The $history table provides a log of the metadata changes performed on the Delta Lake table.

You can retrieve the changelog of the Delta Lake table test_table by using the following query:

The output of the query has the following history columns:

The version of the table corresponding to the operation

TIMESTAMP(3) WITH TIME ZONE

The time when the table version became active For tables with in-Commit timestamps enabled, this field returns value of inCommitTimestamp, Otherwise returns value of timestamp field that in the commitInfo

The identifier for the user which performed the operation

The username for the user which performed the operation

The name of the operation performed on the table

map(VARCHAR, VARCHAR)

Parameters of the operation

The ID of the cluster which ran the operation

The version of the table which was read in order to perform the operation

The level of isolation used to perform the operation

Whether or not the operation appended data

map(VARCHAR, VARCHAR)

Metrics of the operation

The $partitions table provides a detailed overview of the partitions of the Delta Lake table.

You can retrieve the information about the partitions of the Delta Lake table test_table by using the following query:

The output of the query has the following columns:

A row that contains the mapping of the partition column names to the partition column values.

The number of files mapped in the partition.

The size of all the files in the partition.

ROW(... ROW (min ..., max ... , null_count BIGINT))

Partition range and null counts.

The $properties table provides access to Delta Lake table configuration, table features and table properties. The table rows are key/value pairs.

You can retrieve the properties of the Delta table test_table by using the following query:

In addition to the defined columns, the Delta Lake connector automatically exposes metadata in a number of hidden columns in each table. You can use these columns in your SQL statements like any other column, e.g., they can be selected directly or used in conditional statements.

Full file system path name of the file for this row.

Date and time of the last modification of the file for this row.

Size of the file for this row.

The connector provides the following table functions:

Allows reading Change Data Feed (CDF) entries to expose row-level changes between two versions of a Delta Lake table. When the change_data_feed_enabled table property is set to true on a specific Delta Lake table, the connector records change events for all data changes on the table. This is how these changes can be read:

schema_name - type VARCHAR, required, name of the schema for which the function is called

table_name - type VARCHAR, required, name of the table for which the function is called

since_version - type BIGINT, optional, version from which changes are shown, exclusive

In addition to returning the columns present in the table, the function returns the following values for each change event:

Gives the type of change that occurred. Possible values are insert, delete, update_preimage and update_postimage.

Shows the table version for which the change occurred.

Represents the timestamp for the commit in which the specified change happened.

This is how it would be normally used:

The preceding sequence of SQL statements returns the following result:

The output shows what changes happen in which version. For example in version 3 two rows were modified, first one changed from ('url2', 'domain2', 2) into ('url2', 'domain4', 2) and the second from ('url6', 'domain2', 2) into ('url6', 'domain4', 2).

If since_version is not provided the function produces change events starting from when the table was created.

The preceding SQL statement returns the following result:

You can see changes that occurred at version 1 as three inserts. They are not visible in the previous statement when since_version value was set to 1.

The connector includes a number of performance improvements detailed in the following sections:

Support for write partitioning.

Use ANALYZE statements in Trino to populate data size and number of distinct values (NDV) extended table statistics in Delta Lake. The minimum value, maximum value, value count, and null value count statistics are computed on the fly out of the transaction log of the Delta Lake table. The cost-based optimizer then uses these statistics to improve query performance.

Extended statistics enable a broader set of optimizations, including join reordering. The controlling catalog property delta.table-statistics-enabled is enabled by default. The equivalent catalog session property is statistics_enabled.

Each ANALYZE statement updates the table statistics incrementally, so only the data changed since the last ANALYZE is counted. The table statistics are not automatically updated by write operations such as INSERT, UPDATE, and DELETE. You must manually run ANALYZE again to update the table statistics.

To collect statistics for a table, execute the following statement:

To recalculate from scratch the statistics for the table use additional parameter mode:

ANALYZE table_schema.table_name WITH(mode = ‘full_refresh’);

There are two modes available full_refresh and incremental. The procedure use incremental by default.

To gain the most benefit from cost-based optimizations, run periodic ANALYZE statements on every large table that is frequently queried.

The files_modified_after property is useful if you want to run the ANALYZE statement on a table that was previously analyzed. You can use it to limit the amount of data used to generate the table statistics:

As a result, only files newer than the specified time stamp are used in the analysis.

You can also specify a set or subset of columns to analyze using the columns property:

To run ANALYZE with columns more than once, the next ANALYZE must run on the same set or a subset of the original columns used.

To broaden the set of columns, drop the statistics and reanalyze the table.

You can disable extended statistics with the catalog configuration property delta.extended-statistics.enabled set to false. Alternatively, you can disable it for a session, with the catalog session property extended_statistics_enabled set to false.

If a table is changed with many delete and update operation, calling ANALYZE does not result in accurate statistics. To correct the statistics, you have to drop the extended statistics and analyze the table again.

Use the system.drop_extended_stats procedure in the catalog to drop the extended statistics for a specified table in a specified schema:

The Delta Lake connector is memory intensive and the amount of required memory grows with the size of Delta Lake transaction logs of any accessed tables. It is important to take that into account when provisioning the coordinator.

You must decrease memory usage by keeping the number of active data files in the table low by regularly running OPTIMIZE and VACUUM in Delta Lake.

When using the Delta Lake connector, you must monitor memory usage on the coordinator. Specifically, monitor JVM heap utilization using standard tools as part of routine operation of the cluster.

A good proxy for memory usage is the cache utilization of Delta Lake caches. It is exposed by the connector with the plugin.deltalake.transactionlog:name=<catalog-name>,type=transactionlogaccess JMX bean.

You can access it with any standard monitoring software with JMX support, or use the JMX connector with the following query:

Following is an example result:

In a healthy system, both datafilemetadatacachestats.hitrate and metadatacachestats.hitrate are close to 1.0.

Trino offers the possibility to transparently redirect operations on an existing table to the appropriate catalog based on the format of the table and catalog configuration.

In the context of connectors which depend on a metastore service (for example, Hive connector, Iceberg connector and Delta Lake connector), the metastore (Hive metastore service, AWS Glue Data Catalog) can be used to accustom tables with different table formats. Therefore, a metastore database can hold a variety of tables with different table formats.

As a concrete example, let’s use the following simple scenario which makes use of table redirection:

The output of the EXPLAIN statement points out the actual catalog which is handling the SELECT query over the table example_table.

The table redirection functionality works also when using fully qualified names for the tables:

Trino offers table redirection support for the following operations:

Table read operations

Table write operations

Table management operations

Trino does not offer view redirection support.

The connector supports redirection from Delta Lake tables to Hive tables with the delta.hive-catalog-name catalog configuration property.

The following table describes performance tuning catalog properties specific to the Delta Lake connector.

Performance tuning configuration properties are considered expert-level features. Altering these properties from their default values is likely to cause instability and performance degradation. It is strongly suggested that you use them only to address non-trivial performance issues, and that you keep a backup of the original values if you change them.

delta.domain-compaction-threshold

Minimum size of query predicates above which Trino compacts the predicates. Pushing a large list of predicates down to the data source can compromise performance. For optimization in that situation, Trino can compact the large predicates. If necessary, adjust the threshold to ensure a balance between performance and predicate pushdown.

delta.max-outstanding-splits

The target number of buffered splits for each table scan in a query, before the scheduler tries to pause.

delta.max-splits-per-second

Sets the maximum number of splits used per second to access underlying storage. Reduce this number if your limit is routinely exceeded, based on your filesystem limits. This is set to the absolute maximum value, which results in Trino maximizing the parallelization of data access by default. Attempting to set it higher results in Trino not being able to start.

Sets the largest data size for a single read section assigned to a worker after max-initial-splits have been processed. You can also use the corresponding catalog session property <catalog-name>.max_split_size.

delta.minimum-assigned-split-weight

A decimal value in the range (0, 1] used as a minimum for weights assigned to each split. A low value might improve performance on tables with small files. A higher value might improve performance for queries with highly skewed aggregations or joins.

delta.projection-pushdown-enabled

Read only projected fields from row columns while performing SELECT queries

delta.query-partition-filter-required

Set to true to force a query to use a partition filter. You can use the query_partition_filter_required catalog session property for temporary, catalog specific use.

The connector supports configuring and using file system caching.

The following table describes file system cache properties specific to the Delta Lake connector.

delta.fs.cache.disable-transaction-log-caching

Set to true to disable caching of the _delta_log directory of Delta Tables. This is useful in those cases when Delta Tables are destroyed and recreated, and the files inside the transaction log directory get overwritten and cannot be safely cached. Effective only when fs.cache.enabled=true.

**Examples:**

Example 1 (unknown):
```unknown
connector.name=delta_lake
hive.metastore.uri=thrift://example.net:9083
fs.x.enabled=true
```

Example 2 (unknown):
```unknown
connector.name=delta_lake
hive.metastore.uri=thrift://example.net:9083
fs.x.enabled=true
```

Example 3 (unknown):
```unknown
connector.name=delta_lake
hive.metastore=glue
```

Example 4 (unknown):
```unknown
connector.name=delta_lake
hive.metastore=glue
```

---

## Memory connector — Trino 478 Documentation

**URL:** https://trino.io/docs/current/connector/memory.html

**Contents:**
- Memory connector#
- Configuration#
- Examples#
- Type mapping#
- SQL support#
  - TRUNCATE and DROP TABLE#
- Dynamic filtering#
  - Delayed execution for dynamic filters#
- Limitations#

The Memory connector stores all data and metadata in RAM on workers and both are discarded when Trino restarts.

To configure the Memory connector, create a catalog properties file etc/catalog/example.properties with the following contents:

memory.max-data-per-node defines memory limit for pages stored in this connector per each node (default value is 128MB).

Create a table using the Memory connector:

Insert data into a table in the Memory connector:

Select from the Memory connector:

Trino supports all data types used within the Memory schemas so no mapping is required.

The connector provides read and write access to temporary data and metadata stored in memory. In addition to the globally available and read operation statements, the connector supports the following features:

User-defined function management

Upon execution of a TRUNCATE and a DROP TABLE operation, memory is not released immediately. It is instead released after the next write operation to the catalog.

The Memory connector supports the dynamic filtering optimization. Dynamic filters are pushed into local table scan on worker nodes for broadcast joins.

For the Memory connector, a table scan is delayed until the collection of dynamic filters. This can be disabled by using the configuration property memory.enable-lazy-dynamic-filtering in the catalog file.

When one worker fails/restarts, all data that was stored in its memory is lost. To prevent silent data loss the connector throws an error on any read access to such corrupted table.

When a query fails for any reason during writing to memory table, the table enters an undefined state. The table should be dropped and recreated manually. Reading attempts from the table may fail, or may return partial data.

When the coordinator fails/restarts, all metadata about tables is lost. The tables remain on the workers, but become inaccessible.

**Examples:**

Example 1 (unknown):
```unknown
connector.name=memory
memory.max-data-per-node=128MB
```

Example 2 (unknown):
```unknown
connector.name=memory
memory.max-data-per-node=128MB
```

Example 3 (unknown):
```unknown
CREATE TABLE example.default.nation AS
SELECT * from tpch.tiny.nation;
```

Example 4 (unknown):
```unknown
CREATE TABLE example.default.nation AS
SELECT * from tpch.tiny.nation;
```

---

## Thrift connector — Trino 478 Documentation

**URL:** https://trino.io/docs/current/connector/thrift.html

**Contents:**
- Thrift connector#
- Requirements#
- Configuration#
  - Multiple Thrift systems#
- Configuration properties#
  - trino.thrift.client.addresses#
  - trino-thrift.max-response-size#
  - trino-thrift.metadata-refresh-threads#
- TrinoThriftService implementation#
- Type mapping#

The Thrift connector makes it possible to integrate with external storage systems without a custom Trino connector implementation by using Apache Thrift on these servers. It is therefore generic and can provide access to any backend, as long as it exposes the expected API by using Thrift.

In order to use the Thrift connector with an external system, you need to implement the TrinoThriftService interface, found below. Next, you configure the Thrift connector to point to a set of machines, called Thrift servers, that implement the interface. As part of the interface implementation, the Thrift servers provide metadata, splits and data. The connector randomly chooses a server to talk to from the available instances for metadata calls, or for data calls unless the splits include a list of addresses. All requests are assumed to be idempotent and can be retried freely among any server.

To connect to your custom servers with the Thrift protocol, you need:

Network access from the Trino coordinator and workers to the Thrift servers.

A TrinoThriftService implementation for your system.

To configure the Thrift connector, create a catalog properties file etc/catalog/example.properties with the following content, replacing the properties as appropriate:

You can have as many catalogs as you need, so if you have additional Thrift systems to connect to, simply add another properties file to etc/catalog with a different name, making sure it ends in .properties.

The following configuration properties are available:

trino.thrift.client.addresses

Location of Thrift servers

trino-thrift.max-response-size

Maximum size of data returned from Thrift server

trino-thrift.metadata-refresh-threads

Number of refresh threads for metadata cache

trino.thrift.client.max-retries

Maximum number of retries for failed Thrift requests

trino.thrift.client.max-backoff-delay

Maximum interval between retry attempts

trino.thrift.client.min-backoff-delay

Minimum interval between retry attempts

trino.thrift.client.max-retry-time

Maximum duration across all attempts of a Thrift request

trino.thrift.client.backoff-scale-factor

Scale factor for exponential back off

trino.thrift.client.connect-timeout

trino.thrift.client.request-timeout

trino.thrift.client.socks-proxy

trino.thrift.client.max-frame-size

Maximum size of a raw Thrift response

trino.thrift.client.transport

Thrift transport type (UNFRAMED, FRAMED, HEADER)

trino.thrift.client.protocol

Thrift protocol type (BINARY, COMPACT, FB_COMPACT)

Comma-separated list of thrift servers in the form of host:port. For example:

This property is required; there is no default.

Maximum size of a data response that the connector accepts. This value is sent by the connector to the Thrift server when requesting data, allowing it to size the response appropriately.

This property is optional; the default is 16MB.

Number of refresh threads for metadata cache.

This property is optional; the default is 1.

The following IDL describes the TrinoThriftService that must be implemented:

The Thrift service defines data type support and mappings to Trino data types.

The connector provides globally available and read operation statements to access data and metadata in your Thrift service.

**Examples:**

Example 1 (unknown):
```unknown
connector.name=trino_thrift
trino.thrift.client.addresses=host:port,host:port
```

Example 2 (unknown):
```unknown
connector.name=trino_thrift
trino.thrift.client.addresses=host:port,host:port
```

Example 3 (unknown):
```unknown
trino.thrift.client.addresses=192.0.2.3:7777,192.0.2.4:7779
```

Example 4 (unknown):
```unknown
trino.thrift.client.addresses=192.0.2.3:7777,192.0.2.4:7779
```

---

## Lakehouse connector — Trino 478 Documentation

**URL:** https://trino.io/docs/current/connector/lakehouse.html

**Contents:**
- Lakehouse connector#
- General configuration#
- Configuration properties#
- File system access configuration#
- Examples#

The Lakehouse connector provides a unified way to interact with data stored in various table formats across different storage systems and metastore services. This single connector allows you to query and write data seamlessly, regardless of whether it’s in Iceberg, Delta Lake, or Hudi table formats, or traditional Hive tables.

This connector offers flexible connectivity to popular metastore services including AWS Glue and Hive Metastore. For data storage, it supports a wide range of options including cloud storage services such as AWS S3, S3-compatible storage, Google Cloud Storage (GCS), and Azure Blob Storage, as well as HDFS installations.

The connector combines the features of the Hive, Iceberg, Delta Lake, and Hudi connectors into a single connector. The configuration properties, session properties, table properties, and beahvior come from the underlying connectors. Please refer to the documentation for the underlying connectors for the table formats that you are using.

To configure the Lakehouse connector, create a catalog properties file etc/catalog/example.properties with the following content, replacing the properties as appropriate:

You must configure a AWS Glue or a Hive metastore. The hive.metastore property will also configure the Iceberg catalog. Do not specify iceberg.catalog.type.

You must select and configure one of the supported file systems.

The following configuration properties are available:

The default table type for newly created tables when the format table property is not specified. Possible values:

The connector supports accessing the following file systems:

Azure Storage file system support

Google Cloud Storage file system support

S3 file system support

HDFS file system support

You must enable and configure the specific file system access.

Create an Iceberg table:

**Examples:**

Example 1 (unknown):
```unknown
connector.name=lakehouse
```

Example 2 (unknown):
```unknown
connector.name=lakehouse
```

Example 3 (unknown):
```unknown
CREATE TABLE iceberg_table (
  c1 INTEGER,
  c2 DATE,
  c3 DOUBLE
)
WITH (
  type = 'ICEBERG'
  format = 'PARQUET',
  partitioning = ARRAY['c1', 'c2'],
  sorted_by = ARRAY['c3']
);
```

Example 4 (unknown):
```unknown
CREATE TABLE iceberg_table (
  c1 INTEGER,
  c2 DATE,
  c3 DOUBLE
)
WITH (
  type = 'ICEBERG'
  format = 'PARQUET',
  partitioning = ARRAY['c1', 'c2'],
  sorted_by = ARRAY['c3']
);
```

---

## Oracle connector — Trino 478 Documentation

**URL:** https://trino.io/docs/current/connector/oracle.html

**Contents:**
- Oracle connector#
- Requirements#
- Configuration#
  - Data source authentication#
  - Multiple Oracle servers#
  - General configuration properties#
  - Appending query metadata#
  - Domain compaction threshold#
  - Case insensitive matching#
  - Fault-tolerant execution support#

The Oracle connector allows querying and creating tables in an external Oracle database. Connectors let Trino join data provided by different databases, like Oracle and Hive, or different Oracle database instances.

To connect to Oracle, you need:

Network access from the Trino coordinator and workers to Oracle. Port 1521 is the default port.

To configure the Oracle connector as the example catalog, create a file named example.properties in etc/catalog. Include the following connection properties in the file:

The connection-url defines the connection information and parameters to pass to the JDBC driver. The Oracle connector uses the Oracle JDBC Thin driver, and the syntax of the URL may be different depending on your Oracle configuration. For example, the connection URL is different if you are connecting to an Oracle SID or an Oracle service name. See the Oracle Database JDBC driver documentation for more information.

The connection-user and connection-password are typically required and determine the user credentials for the connection, often a service user. You can use secrets to avoid actual values in the catalog properties files.

Oracle does not expose metadata comment via REMARKS column by default in JDBC driver. You can enable it using oracle.remarks-reporting.enabled config option. See Additional Oracle Performance Extensions for more details.

By default, the Oracle connector uses connection pooling for performance improvement. The below configuration shows the typical default values. To update them, change the properties in the catalog configuration file:

To disable connection pooling, update properties to include the following:

The connector can provide credentials for the data source connection in multiple ways:

inline, in the connector configuration file

in a separate properties file

as extra credentials set when connecting to Trino

You can use secrets to avoid storing sensitive values in the catalog properties files.

The following table describes configuration properties for connection credentials:

credential-provider.type

Type of the credential provider. Must be one of INLINE, FILE, or KEYSTORE; defaults to INLINE.

Connection user name.

Name of the extra credentials property, whose value to use as the user name. See extraCredentials in Parameter reference.

password-credential-name

Name of the extra credentials property, whose value to use as the password.

connection-credential-file

Location of the properties file where credentials are present. It must contain the connection-user and connection-password properties.

The location of the Java Keystore file, from which to read credentials.

File format of the keystore file, for example JKS or PEM.

Password for the key store.

keystore-user-credential-name

Name of the key store entity to use as the user name.

keystore-user-credential-password

Password for the user name key store entity.

keystore-password-credential-name

Name of the key store entity to use as the password.

keystore-password-credential-password

Password for the password key store entity.

If you want to connect to multiple Oracle servers, configure another instance of the Oracle connector as a separate catalog.

To add another Oracle catalog, create a new properties file. For example, if you name the property file sales.properties, Trino creates a catalog named sales.

The following table describes general catalog configuration properties for the connector:

case-insensitive-name-matching

Support case insensitive schema and table names. Defaults to false.

case-insensitive-name-matching.cache-ttl

Duration for which case insensitive schema and table names are cached. Defaults to 1m.

case-insensitive-name-matching.config-file

Path to a name mapping configuration file in JSON format that allows Trino to disambiguate between schemas and tables with similar names in different cases. Defaults to null.

case-insensitive-name-matching.config-file.refresh-period

Frequency with which Trino checks the name matching configuration file for changes. The duration value defaults to 0s (refresh disabled).

Duration for which metadata, including table and column statistics, is cached. Defaults to 0s (caching disabled).

metadata.cache-missing

Cache the fact that metadata, including table and column statistics, is not available. Defaults to false.

metadata.schemas.cache-ttl

Duration for which schema metadata is cached. Defaults to the value of metadata.cache-ttl.

metadata.tables.cache-ttl

Duration for which table metadata is cached. Defaults to the value of metadata.cache-ttl.

metadata.statistics.cache-ttl

Duration for which tables statistics are cached. Defaults to the value of metadata.cache-ttl.

metadata.cache-maximum-size

Maximum number of objects stored in the metadata cache. Defaults to 10000.

Maximum number of statements in a batched execution. Do not change this setting from the default. Non-default values may negatively impact performance. Defaults to 1000.

dynamic-filtering.enabled

Push down dynamic filters into JDBC queries. Defaults to true.

dynamic-filtering.wait-timeout

Maximum duration for which Trino waits for dynamic filters to be collected from the build side of joins before starting a JDBC query. Using a large timeout can potentially result in more detailed dynamic filters. However, it can also increase latency for some queries. Defaults to 20s.

The optional parameter query.comment-format allows you to configure a SQL comment that is sent to the datasource with each query. The format of this comment can contain any characters and the following metadata:

$QUERY_ID: The identifier of the query.

$USER: The name of the user who submits the query to Trino.

$SOURCE: The identifier of the client tool used to submit the query, for example trino-cli.

$TRACE_TOKEN: The trace token configured with the client tool.

The comment can provide more context about the query. This additional information is available in the logs of the datasource. To include environment variables from the Trino cluster with the comment , use the ${ENV:VARIABLE-NAME} syntax.

The following example sets a simple comment that identifies each query sent by Trino:

With this configuration, a query such as SELECT * FROM example_table; is sent to the datasource with the comment appended:

The following example improves on the preceding example by using metadata:

If Jane sent the query with the query identifier 20230622_180528_00000_bkizg, the following comment string is sent to the datasource:

Certain JDBC driver settings and logging configurations might cause the comment to be removed.

Pushing down a large list of predicates to the data source can compromise performance. Trino compacts large predicates into a simpler range predicate by default to ensure a balance between performance and predicate pushdown. If necessary, the threshold for this compaction can be increased to improve performance when the data source is capable of taking advantage of large predicates. Increasing this threshold may improve pushdown of large dynamic filters. The domain-compaction-threshold catalog configuration property or the domain_compaction_threshold catalog session property can be used to adjust the default value of 256 for this threshold.

When case-insensitive-name-matching is set to true, Trino is able to query non-lowercase schemas and tables by maintaining a mapping of the lowercase name to the actual name in the remote system. However, if two schemas and/or tables have names that differ only in case (such as “customers” and “Customers”) then Trino fails to query them due to ambiguity.

In these cases, use the case-insensitive-name-matching.config-file catalog configuration property to specify a configuration file that maps these remote schemas and tables to their respective Trino schemas and tables. Additionally, the JSON file must include both the schemas and tables properties, even if only as empty arrays.

Queries against one of the tables or schemes defined in the mapping attributes are run against the corresponding remote entity. For example, a query against tables in the case_insensitive_1 schema is forwarded to the CaseSensitiveName schema and a query against case_insensitive_2 is forwarded to the cASEsENSITIVEnAME schema.

At the table mapping level, a query on case_insensitive_1.table_1 as configured above is forwarded to CaseSensitiveName.tablex, and a query on case_insensitive_1.table_2 is forwarded to CaseSensitiveName.TABLEX.

By default, when a change is made to the mapping configuration file, Trino must be restarted to load the changes. Optionally, you can set the case-insensitive-name-matching.config-file.refresh-period to have Trino refresh the properties without requiring a restart:

The connector supports Fault-tolerant execution of query processing. Read and write operations are both supported with any retry policy.

The Oracle connector provides a schema for every Oracle database.

Run SHOW SCHEMAS to see the available Oracle databases:

If you used a different name for your catalog properties file, use that catalog name instead of example.

The Oracle user must have access to the table in order to access it from Trino. The user configuration, in the connection properties file, determines your privileges in these schemas.

If you have an Oracle database named web, run SHOW TABLES to see the tables it contains:

To see a list of the columns in the clicks table in the web database, run either of the following:

To access the clicks table in the web database, run the following:

Because Trino and Oracle each support types that the other does not, this connector modifies some types when reading or writing data. Data types may not map the same way in both directions between Trino and the data source. Refer to the following sections for type mapping in each direction.

Trino supports selecting Oracle database types. This table shows the Oracle to Trino data type mapping:

See Mapping numeric types

See Mapping numeric types

See Mapping datetime types

See Mapping datetime types

TIMESTAMP(p) WITH TIME ZONE

TIMESTAMP WITH TIME ZONE

See Mapping datetime types

No other types are supported.

Trino supports creating tables with the following types in an Oracle database. The table shows the mappings from Trino to Oracle data types:

For types not listed in the table below, Trino can’t perform the CREATE TABLE <table> AS SELECT operations. When data is inserted into existing tables, Oracle to Trino type mapping is used.

VARCHAR2(n CHAR) or NCLOB

See Mapping character types

CHAR(n CHAR) or NCLOB

See Mapping character types

See Mapping datetime types

See Mapping datetime types

TIMESTAMP WITH TIME ZONE

TIMESTAMP(3) WITH TIME ZONE

See Mapping datetime types

No other types are supported.

An Oracle NUMBER(p, s) maps to Trino’s DECIMAL(p, s) except in these conditions:

No precision is specified for the column (example: NUMBER or NUMBER(*)), unless oracle.number.default-scale is set.

Scale (s ) is greater than precision.

Precision (p ) is greater than 38.

Scale is negative and the difference between p and s is greater than 38, unless oracle.number.rounding-mode is set to a different value than UNNECESSARY.

If s is negative, NUMBER(p, s) maps to DECIMAL(p + s, 0).

For Oracle NUMBER (without precision and scale), you can change oracle.number.default-scale=s and map the column to DECIMAL(38, s).

Writing a timestamp with fractional second precision (p) greater than 9 rounds the fractional seconds to nine digits.

Oracle DATE type stores hours, minutes, and seconds, so it is mapped to Trino TIMESTAMP(0).

Due to date and time differences in the libraries used by Trino and the Oracle JDBC driver, attempting to insert or select a datetime value earlier than 1582-10-15 results in an incorrect date inserted.

Trino’s VARCHAR(n) maps to VARCHAR2(n CHAR) if n is no greater than 4000. A larger or unbounded VARCHAR maps to NCLOB.

Trino’s CHAR(n) maps to CHAR(n CHAR) if n is no greater than 2000. A larger CHAR maps to NCLOB.

Using CREATE TABLE AS to create an NCLOB column from a CHAR value removes the trailing spaces from the initial values for the column. Inserting CHAR values into existing NCLOB columns keeps the trailing spaces. For example:

Attempting to write a CHAR that doesn’t fit in the column’s actual size fails. This is also true for the equivalent VARCHAR types.

The following properties can be used to configure how data types from the connected data source are mapped to Trino data types and how the metadata is cached in Trino.

unsupported-type-handling

Configure how unsupported column data types are handled:

IGNORE, column is not accessible.

CONVERT_TO_VARCHAR, column is converted to unbounded VARCHAR.

The respective catalog session property is unsupported_type_handling.

jdbc-types-mapped-to-varchar

Allow forced mapping of comma separated lists of data types to convert to unbounded VARCHAR

Configuration property name

Session property name

oracle.number.default-scale

Default Trino DECIMAL scale for Oracle NUMBER (without precision and scale) date type. When not set then such column is treated as not supported.

oracle.number.rounding-mode

Rounding mode for the Oracle NUMBER data type. This is useful when Oracle NUMBER data type specifies higher scale than is supported in Trino. Possible values are:

UNNECESSARY - Rounding mode to assert that the requested operation has an exact result, hence no rounding is necessary.

CEILING - Rounding mode to round towards positive infinity.

FLOOR - Rounding mode to round towards negative infinity.

HALF_DOWN - Rounding mode to round towards nearest neighbor unless both neighbors are equidistant, in which case rounding down is used.

HALF_EVEN - Rounding mode to round towards the nearest neighbor unless both neighbors are equidistant, in which case rounding towards the even neighbor is performed.

HALF_UP - Rounding mode to round towards nearest neighbor unless both neighbors are equidistant, in which case rounding up is used

UP - Rounding mode to round towards zero.

DOWN - Rounding mode to round towards zero.

The connector provides read access and write access to data and metadata in Oracle. In addition to the globally available and read operation statements, the connector supports the following features:

INSERT, see also Non-transactional INSERT

UPDATE, see also UPDATE limitation

DELETE, see also DELETE limitation

ALTER TABLE, see also ALTER TABLE RENAME TO limitation

The connector supports adding rows using INSERT statements. By default, data insertion is performed by writing data to a temporary table. You can skip this step to improve performance and write directly to the target table. Set the insert.non-transactional-insert.enabled catalog property or the corresponding non_transactional_insert catalog session property to true.

Note that with this property enabled, data can be corrupted in rare cases where exceptions occur during the insert operation. With transactions disabled, no rollback can be performed.

Only UPDATE statements with constant assignments and predicates are supported. For example, the following statement is supported because the values assigned are constants:

Arithmetic expressions, function calls, and other non-constant UPDATE statements are not supported. For example, the following statement is not supported because arithmetic expressions cannot be used with the SET command:

All column values of a table row cannot be updated simultaneously. For a three column table, the following statement is not supported:

If a WHERE clause is specified, the DELETE operation only works if the predicate in the clause can be fully pushed down to the data source.

The connector does not support renaming tables across multiple schemas. For example, the following statement is supported:

The following statement attempts to rename a table across schemas, and therefore is not supported:

Flush JDBC metadata caches. For example, the following system call flushes the metadata caches for all schemas in the example catalog

The execute procedure allows you to execute a query in the underlying data source directly. The query must use supported syntax of the connected data source. Use the procedure to access features which are not available in Trino or to execute queries that return no result set and therefore can not be used with the query or raw_query pass-through table function. Typical use cases are statements that create or alter objects, and require native feature such as constraints, default values, automatic identifier creation, or indexes. Queries can also invoke statements that insert, update, or delete data, and do not return any data as a result.

The query text is not parsed by Trino, only passed through, and therefore only subject to any security or access control of the underlying data source.

The following example sets the current database to the example_schema of the example catalog. Then it calls the procedure in that schema to drop the default value from your_column on your_table table using the standard SQL syntax in the parameter value assigned for query:

Verify that the specific database supports this syntax, and adapt as necessary based on the documentation for the specific connected database and database version.

The connector provides specific table functions to access Oracle.

The query function allows you to query the underlying database directly. It requires syntax native to Oracle, because the full query is pushed down and processed in Oracle. This can be useful for accessing native features which are not available in Trino or for improving query performance in situations where running a query natively may be faster.

The native query passed to the underlying data source is required to return a table as a result set. Only the data source performs validation or security checks for these queries using its own configuration. Trino does not perform these tasks. Only use passthrough queries to read data.

As a simple example, query the example catalog and select an entire table:

As a practical example, you can use the MODEL clause from Oracle SQL:

The query engine does not preserve the order of the results of this function. If the passed query contains an ORDER BY clause, the function result may not be ordered as expected.

The connector includes a number of performance improvements, detailed in the following sections.

Based on performance reasons, Trino disables support for Oracle SYNONYM. To include SYNONYM, add the following configuration property:

The connector supports pushdown for a number of operations:

In addition, the connector supports Aggregation pushdown for the following functions:

count(), also count(distinct x)

Pushdown is only supported for DOUBLE type columns with the following functions:

stddev() and stddev_samp()

variance() and var_samp()

Pushdown is only supported for REAL or DOUBLE type column with the following functions:

The connector performs pushdown where performance may be improved, but in order to preserve correctness an operation may not be pushed down. When pushdown of an operation may result in better performance but risks correctness, the connector prioritizes correctness.

The join-pushdown.enabled catalog configuration property or join_pushdown_enabled catalog session property control whether the connector pushes down join operations. The property defaults to false, and enabling join pushdowns may negatively impact performance for some queries.

The connector does not support pushdown of any predicates on columns that use the CLOB, NCLOB, BLOB, or RAW(n) Oracle database types, or Trino data types that map to these Oracle database types.

In the following example, the predicate is not pushed down for either query since name is a column of type VARCHAR, which maps to NCLOB in Oracle:

In the following example, the predicate is pushed down for both queries since name is a column of type VARCHAR(25), which maps to VARCHAR2(25) in Oracle:

**Examples:**

Example 1 (unknown):
```unknown
connector.name=oracle
# The correct syntax of the connection-url varies by Oracle version and
# configuration. The following example URL connects to an Oracle SID named
# "orcl".
connection-url=jdbc:oracle:thin:@example.net:1521:orcl
connection-user=root
connection-password=secret
```

Example 2 (unknown):
```unknown
connector.name=oracle
# The correct syntax of the connection-url varies by Oracle version and
# configuration. The following example URL connects to an Oracle SID named
# "orcl".
connection-url=jdbc:oracle:thin:@example.net:1521:orcl
connection-user=root
connection-password=secret
```

Example 3 (unknown):
```unknown
oracle.connection-pool.max-size=30
oracle.connection-pool.min-size=1
oracle.connection-pool.inactive-timeout=20m
```

Example 4 (unknown):
```unknown
oracle.connection-pool.max-size=30
oracle.connection-pool.min-size=1
oracle.connection-pool.inactive-timeout=20m
```

---

## PostgreSQL connector — Trino 478 Documentation

**URL:** https://trino.io/docs/current/connector/postgresql.html

**Contents:**
- PostgreSQL connector#
- Requirements#
- Configuration#
  - Access to system tables#
  - Connection security#
  - Data source authentication#
  - Multiple PostgreSQL databases or servers#
  - General configuration properties#
  - Appending query metadata#
  - Domain compaction threshold#

The PostgreSQL connector allows querying and creating tables in an external PostgreSQL database. This can be used to join data between different systems like PostgreSQL and Hive, or between different PostgreSQL instances.

To connect to PostgreSQL, you need:

PostgreSQL 12.x or higher.

Network access from the Trino coordinator and workers to PostgreSQL. Port 5432 is the default port.

The connector can query a database on a PostgreSQL server. Create a catalog properties file that specifies the PostgreSQL connector by setting the connector.name to postgresql.

For example, to access a database as the example catalog, create the file etc/catalog/example.properties. Replace the connection properties as appropriate for your setup:

The connection-url defines the connection information and parameters to pass to the PostgreSQL JDBC driver. The parameters for the URL are available in the PostgreSQL JDBC driver documentation. Some parameters can have adverse effects on the connector behavior or not work with the connector.

The connection-user and connection-password are typically required and determine the user credentials for the connection, often a service user. You can use secrets to avoid actual values in the catalog properties files.

The PostgreSQL connector supports reading PostgreSQL catalog tables, such as pg_namespace. The functionality is turned off by default, and can be enabled using the postgresql.include-system-tables configuration property.

You can see more details in the pg_catalog schema in the example catalog, for example about the pg_namespace system table:

If you have TLS configured with a globally-trusted certificate installed on your data source, you can enable TLS between your cluster and the data source by appending a parameter to the JDBC connection string set in the connection-url catalog configuration property.

For example, with version 42 of the PostgreSQL JDBC driver, enable TLS by appending the ssl=true parameter to the connection-url configuration property:

For more information on TLS configuration options, see the PostgreSQL JDBC driver documentation.

The connector can provide credentials for the data source connection in multiple ways:

inline, in the connector configuration file

in a separate properties file

as extra credentials set when connecting to Trino

You can use secrets to avoid storing sensitive values in the catalog properties files.

The following table describes configuration properties for connection credentials:

credential-provider.type

Type of the credential provider. Must be one of INLINE, FILE, or KEYSTORE; defaults to INLINE.

Connection user name.

Name of the extra credentials property, whose value to use as the user name. See extraCredentials in Parameter reference.

password-credential-name

Name of the extra credentials property, whose value to use as the password.

connection-credential-file

Location of the properties file where credentials are present. It must contain the connection-user and connection-password properties.

The location of the Java Keystore file, from which to read credentials.

File format of the keystore file, for example JKS or PEM.

Password for the key store.

keystore-user-credential-name

Name of the key store entity to use as the user name.

keystore-user-credential-password

Password for the user name key store entity.

keystore-password-credential-name

Name of the key store entity to use as the password.

keystore-password-credential-password

Password for the password key store entity.

The PostgreSQL connector can only access a single database within a PostgreSQL server. Thus, if you have multiple PostgreSQL databases, or want to connect to multiple PostgreSQL servers, you must configure multiple instances of the PostgreSQL connector.

To add another catalog, simply add another properties file to etc/catalog with a different name, making sure it ends in .properties. For example, if you name the property file sales.properties, Trino creates a catalog named sales using the configured connector.

The following table describes general catalog configuration properties for the connector:

case-insensitive-name-matching

Support case insensitive schema and table names. Defaults to false.

case-insensitive-name-matching.cache-ttl

Duration for which case insensitive schema and table names are cached. Defaults to 1m.

case-insensitive-name-matching.config-file

Path to a name mapping configuration file in JSON format that allows Trino to disambiguate between schemas and tables with similar names in different cases. Defaults to null.

case-insensitive-name-matching.config-file.refresh-period

Frequency with which Trino checks the name matching configuration file for changes. The duration value defaults to 0s (refresh disabled).

Duration for which metadata, including table and column statistics, is cached. Defaults to 0s (caching disabled).

metadata.cache-missing

Cache the fact that metadata, including table and column statistics, is not available. Defaults to false.

metadata.schemas.cache-ttl

Duration for which schema metadata is cached. Defaults to the value of metadata.cache-ttl.

metadata.tables.cache-ttl

Duration for which table metadata is cached. Defaults to the value of metadata.cache-ttl.

metadata.statistics.cache-ttl

Duration for which tables statistics are cached. Defaults to the value of metadata.cache-ttl.

metadata.cache-maximum-size

Maximum number of objects stored in the metadata cache. Defaults to 10000.

Maximum number of statements in a batched execution. Do not change this setting from the default. Non-default values may negatively impact performance. Defaults to 1000.

dynamic-filtering.enabled

Push down dynamic filters into JDBC queries. Defaults to true.

dynamic-filtering.wait-timeout

Maximum duration for which Trino waits for dynamic filters to be collected from the build side of joins before starting a JDBC query. Using a large timeout can potentially result in more detailed dynamic filters. However, it can also increase latency for some queries. Defaults to 20s.

The optional parameter query.comment-format allows you to configure a SQL comment that is sent to the datasource with each query. The format of this comment can contain any characters and the following metadata:

$QUERY_ID: The identifier of the query.

$USER: The name of the user who submits the query to Trino.

$SOURCE: The identifier of the client tool used to submit the query, for example trino-cli.

$TRACE_TOKEN: The trace token configured with the client tool.

The comment can provide more context about the query. This additional information is available in the logs of the datasource. To include environment variables from the Trino cluster with the comment , use the ${ENV:VARIABLE-NAME} syntax.

The following example sets a simple comment that identifies each query sent by Trino:

With this configuration, a query such as SELECT * FROM example_table; is sent to the datasource with the comment appended:

The following example improves on the preceding example by using metadata:

If Jane sent the query with the query identifier 20230622_180528_00000_bkizg, the following comment string is sent to the datasource:

Certain JDBC driver settings and logging configurations might cause the comment to be removed.

Pushing down a large list of predicates to the data source can compromise performance. Trino compacts large predicates into a simpler range predicate by default to ensure a balance between performance and predicate pushdown. If necessary, the threshold for this compaction can be increased to improve performance when the data source is capable of taking advantage of large predicates. Increasing this threshold may improve pushdown of large dynamic filters. The domain-compaction-threshold catalog configuration property or the domain_compaction_threshold catalog session property can be used to adjust the default value of 256 for this threshold.

When case-insensitive-name-matching is set to true, Trino is able to query non-lowercase schemas and tables by maintaining a mapping of the lowercase name to the actual name in the remote system. However, if two schemas and/or tables have names that differ only in case (such as “customers” and “Customers”) then Trino fails to query them due to ambiguity.

In these cases, use the case-insensitive-name-matching.config-file catalog configuration property to specify a configuration file that maps these remote schemas and tables to their respective Trino schemas and tables. Additionally, the JSON file must include both the schemas and tables properties, even if only as empty arrays.

Queries against one of the tables or schemes defined in the mapping attributes are run against the corresponding remote entity. For example, a query against tables in the case_insensitive_1 schema is forwarded to the CaseSensitiveName schema and a query against case_insensitive_2 is forwarded to the cASEsENSITIVEnAME schema.

At the table mapping level, a query on case_insensitive_1.table_1 as configured above is forwarded to CaseSensitiveName.tablex, and a query on case_insensitive_1.table_2 is forwarded to CaseSensitiveName.TABLEX.

By default, when a change is made to the mapping configuration file, Trino must be restarted to load the changes. Optionally, you can set the case-insensitive-name-matching.config-file.refresh-period to have Trino refresh the properties without requiring a restart:

The connector supports Fault-tolerant execution of query processing. Read and write operations are both supported with any retry policy.

Because Trino and PostgreSQL each support types that the other does not, this connector modifies some types when reading or writing data. Data types may not map the same way in both directions between Trino and the data source. Refer to the following sections for type mapping in each direction.

The connector maps PostgreSQL types to the corresponding Trino types following this table:

DECIMAL(p, s) is an alias of NUMERIC(p, s). See Decimal type handling for more information.

TIMESTAMP(n) WITH TIME ZONE

MAP(VARCHAR, VARCHAR)

Disabled, ARRAY, or JSON

See Array type handling for more information.

GEOMETRY, GEOMETRY(GEOMETRY TYPE, SRID)

No other types are supported.

The connector maps Trino types to the corresponding PostgreSQL types following this table:

DECIMAL(p, s) is an alias of NUMERIC(p, s). See Decimal type handling for more information.

TIMESTAMP(n) WITH TIME ZONE

See Array type handling for more information.

No other types are supported.

DECIMAL types with unspecified precision or scale are ignored unless the decimal-mapping configuration property or the decimal_mapping session property is set to allow_overflow. Then such types are mapped to a Trino DECIMAL with a default precision of 38 and default scale of 0. To change the scale of the resulting type, use the decimal-default-scale configuration property or the decimal_default_scale session property. The precision is always 38.

By default, values that require rounding or truncation to fit will cause a failure at runtime. This behavior is controlled via the decimal-rounding-mode configuration property or the decimal_rounding_mode session property, which can be set to UNNECESSARY (the default), UP, DOWN, CEILING, FLOOR, HALF_UP, HALF_DOWN, or HALF_EVEN (see RoundingMode).

The PostgreSQL array implementation does not support fixed dimensions whereas Trino support only arrays with fixed dimensions. You can configure how the PostgreSQL connector handles arrays with the postgresql.array-mapping configuration property in your catalog file or the array_mapping session property. The following values are accepted for this property:

DISABLED (default): array columns are skipped.

AS_ARRAY: array columns are interpreted as Trino ARRAY type, for array columns with fixed dimensions.

AS_JSON: array columns are interpreted as Trino JSON type, with no constraint on dimensions.

The following properties can be used to configure how data types from the connected data source are mapped to Trino data types and how the metadata is cached in Trino.

unsupported-type-handling

Configure how unsupported column data types are handled:

IGNORE, column is not accessible.

CONVERT_TO_VARCHAR, column is converted to unbounded VARCHAR.

The respective catalog session property is unsupported_type_handling.

jdbc-types-mapped-to-varchar

Allow forced mapping of comma separated lists of data types to convert to unbounded VARCHAR

The PostgreSQL connector provides a schema for every PostgreSQL schema. You can see the available PostgreSQL schemas by running SHOW SCHEMAS:

If you have a PostgreSQL schema named web, you can view the tables in this schema by running SHOW TABLES:

You can see a list of the columns in the clicks table in the web database using either of the following:

Finally, you can access the clicks table in the web schema:

If you used a different name for your catalog properties file, use that catalog name instead of example in the above examples.

The connector provides read access and write access to data and metadata in PostgreSQL. In addition to the globally available and read operation statements, the connector supports the following features:

INSERT, see also Non-transactional INSERT

UPDATE, see also UPDATE limitation

DELETE, see also DELETE limitation

MERGE, see also Non-transactional MERGE

Schema and table management, see also:

ALTER TABLE RENAME TO limitation

ALTER SCHEMA limitation

The connector supports adding rows using INSERT statements. By default, data insertion is performed by writing data to a temporary table. You can skip this step to improve performance and write directly to the target table. Set the insert.non-transactional-insert.enabled catalog property or the corresponding non_transactional_insert catalog session property to true.

Note that with this property enabled, data can be corrupted in rare cases where exceptions occur during the insert operation. With transactions disabled, no rollback can be performed.

Only UPDATE statements with constant assignments and predicates are supported. For example, the following statement is supported because the values assigned are constants:

Arithmetic expressions, function calls, and other non-constant UPDATE statements are not supported. For example, the following statement is not supported because arithmetic expressions cannot be used with the SET command:

All column values of a table row cannot be updated simultaneously. For a three column table, the following statement is not supported:

If a WHERE clause is specified, the DELETE operation only works if the predicate in the clause can be fully pushed down to the data source.

The connector supports adding, updating, and deleting rows using MERGE statements, if the merge.non-transactional-merge.enabled catalog property or the corresponding non_transactional_merge_enabled catalog session property is set to true. Merge is only supported for directly modifying target tables.

In rare cases, exceptions may occur during the merge operation, potentially resulting in a partial update.

The connector does not support renaming tables across multiple schemas. For example, the following statement is supported:

The following statement attempts to rename a table across schemas, and therefore is not supported:

The connector supports renaming a schema with the ALTER SCHEMA RENAME statement. ALTER SCHEMA SET AUTHORIZATION is not supported.

Flush JDBC metadata caches. For example, the following system call flushes the metadata caches for all schemas in the example catalog

The execute procedure allows you to execute a query in the underlying data source directly. The query must use supported syntax of the connected data source. Use the procedure to access features which are not available in Trino or to execute queries that return no result set and therefore can not be used with the query or raw_query pass-through table function. Typical use cases are statements that create or alter objects, and require native feature such as constraints, default values, automatic identifier creation, or indexes. Queries can also invoke statements that insert, update, or delete data, and do not return any data as a result.

The query text is not parsed by Trino, only passed through, and therefore only subject to any security or access control of the underlying data source.

The following example sets the current database to the example_schema of the example catalog. Then it calls the procedure in that schema to drop the default value from your_column on your_table table using the standard SQL syntax in the parameter value assigned for query:

Verify that the specific database supports this syntax, and adapt as necessary based on the documentation for the specific connected database and database version.

The connector provides specific table functions to access PostgreSQL.

The query function allows you to query the underlying database directly. It requires syntax native to PostgreSQL, because the full query is pushed down and processed in PostgreSQL. This can be useful for accessing native features which are not available in Trino or for improving query performance in situations where running a query natively may be faster.

The native query passed to the underlying data source is required to return a table as a result set. Only the data source performs validation or security checks for these queries using its own configuration. Trino does not perform these tasks. Only use passthrough queries to read data.

As a simple example, query the example catalog and select an entire table:

As a practical example, you can leverage frame exclusion from PostgresQL when using window functions:

The query engine does not preserve the order of the results of this function. If the passed query contains an ORDER BY clause, the function result may not be ordered as expected.

The connector includes a number of performance improvements, detailed in the following sections.

The PostgreSQL connector can use table and column statistics for cost based optimizations, to improve query processing performance based on the actual data in the data source.

The statistics are collected by PostgreSQL and retrieved by the connector.

To collect statistics for a table, execute the following statement in PostgreSQL.

Refer to PostgreSQL documentation for additional ANALYZE options.

The connector supports pushdown for a number of operations:

Aggregate pushdown for the following functions:

The connector performs pushdown where performance may be improved, but in order to preserve correctness an operation may not be pushed down. When pushdown of an operation may result in better performance but risks correctness, the connector prioritizes correctness.

The connector supports cost-based Join pushdown to make intelligent decisions about whether to push down a join operation to the data source.

When cost-based join pushdown is enabled, the connector only pushes down join operations if the available Table statistics suggest that doing so improves performance. Note that if no table statistics are available, join operation pushdown does not occur to avoid a potential decrease in query performance.

The following table describes catalog configuration properties for join pushdown:

join-pushdown.enabled

Enable join pushdown. Equivalent catalog session property is join_pushdown_enabled.

join-pushdown.strategy

Strategy used to evaluate whether join operations are pushed down. Set to AUTOMATIC to enable cost-based join pushdown, or EAGER to push down joins whenever possible. Note that EAGER can push down joins even when table statistics are unavailable, which may result in degraded query performance. Because of this, EAGER is only recommended for testing and troubleshooting purposes.

Predicates are pushed down for most types, including UUID and temporal types, such as DATE.

The connector does not support pushdown of range predicates, such as >, <, or BETWEEN, on columns with character string types like CHAR or VARCHAR. Equality predicates, such as IN or =, and inequality predicates, such as != on columns with textual types are pushed down. This ensures correctness of results since the remote data source may sort strings differently than Trino.

In the following example, the predicate of the first query is not pushed down since name is a column of type VARCHAR and > is a range predicate. The other queries are pushed down.

There is experimental support to enable pushdown of range predicates on columns with character string types which can be enabled by setting the postgresql.experimental.enable-string-pushdown-with-collate catalog configuration property or the corresponding enable_string_pushdown_with_collate session property to true. Enabling this configuration will make the predicate of all the queries in the above example get pushed down.

**Examples:**

Example 1 (unknown):
```unknown
connector.name=postgresql
connection-url=jdbc:postgresql://example.net:5432/database
connection-user=root
connection-password=secret
```

Example 2 (unknown):
```unknown
connector.name=postgresql
connection-url=jdbc:postgresql://example.net:5432/database
connection-user=root
connection-password=secret
```

Example 3 (unknown):
```unknown
SHOW TABLES FROM example.pg_catalog;
SELECT * FROM example.pg_catalog.pg_namespace;
```

Example 4 (unknown):
```unknown
SHOW TABLES FROM example.pg_catalog;
SELECT * FROM example.pg_catalog.pg_namespace;
```

---

## ClickHouse connector — Trino 478 Documentation

**URL:** https://trino.io/docs/current/connector/clickhouse.html

**Contents:**
- ClickHouse connector#
- Requirements#
- Configuration#
  - Connection security#
  - Data source authentication#
  - Multiple ClickHouse servers#
  - General configuration properties#
  - Appending query metadata#
  - Domain compaction threshold#
  - Case insensitive matching#

The ClickHouse connector allows querying tables in an external ClickHouse server. This can be used to query data in the databases on that server, or combine it with other data from different catalogs accessing ClickHouse or any other supported data source.

To connect to a ClickHouse server, you need:

ClickHouse (version 25.3 or higher) or Altinity (version 22.8 or higher).

Network access from the Trino coordinator and workers to the ClickHouse server. Port 8123 is the default port.

The connector can query a ClickHouse server. Create a catalog properties file that specifies the ClickHouse connector by setting the connector.name to clickhouse.

For example, create the file etc/catalog/example.properties. Replace the connection properties as appropriate for your setup:

The connection-url defines the connection information and parameters to pass to the ClickHouse JDBC driver. The supported parameters for the URL are available in the ClickHouse JDBC driver configuration.

The connection-user and connection-password are typically required and determine the user credentials for the connection, often a service user. You can use secrets to avoid actual values in the catalog properties files.

If you have TLS configured with a globally-trusted certificate installed on your data source, you can enable TLS between your cluster and the data source by appending a parameter to the JDBC connection string set in the connection-url catalog configuration property.

For example, with version 2.6.4 of the ClickHouse JDBC driver, enable TLS by appending the ssl=true parameter to the connection-url configuration property:

For more information on TLS configuration options, see the Clickhouse JDBC driver documentation

The connector can provide credentials for the data source connection in multiple ways:

inline, in the connector configuration file

in a separate properties file

as extra credentials set when connecting to Trino

You can use secrets to avoid storing sensitive values in the catalog properties files.

The following table describes configuration properties for connection credentials:

credential-provider.type

Type of the credential provider. Must be one of INLINE, FILE, or KEYSTORE; defaults to INLINE.

Connection user name.

Name of the extra credentials property, whose value to use as the user name. See extraCredentials in Parameter reference.

password-credential-name

Name of the extra credentials property, whose value to use as the password.

connection-credential-file

Location of the properties file where credentials are present. It must contain the connection-user and connection-password properties.

The location of the Java Keystore file, from which to read credentials.

File format of the keystore file, for example JKS or PEM.

Password for the key store.

keystore-user-credential-name

Name of the key store entity to use as the user name.

keystore-user-credential-password

Password for the user name key store entity.

keystore-password-credential-name

Name of the key store entity to use as the password.

keystore-password-credential-password

Password for the password key store entity.

If you have multiple ClickHouse servers you need to configure one catalog for each server. To add another catalog:

Add another properties file to etc/catalog

Save it with a different name that ends in .properties

For example, if you name the property file sales.properties, Trino uses the configured connector to create a catalog named sales.

The following table describes general catalog configuration properties for the connector:

case-insensitive-name-matching

Support case insensitive schema and table names. Defaults to false.

case-insensitive-name-matching.cache-ttl

Duration for which case insensitive schema and table names are cached. Defaults to 1m.

case-insensitive-name-matching.config-file

Path to a name mapping configuration file in JSON format that allows Trino to disambiguate between schemas and tables with similar names in different cases. Defaults to null.

case-insensitive-name-matching.config-file.refresh-period

Frequency with which Trino checks the name matching configuration file for changes. The duration value defaults to 0s (refresh disabled).

Duration for which metadata, including table and column statistics, is cached. Defaults to 0s (caching disabled).

metadata.cache-missing

Cache the fact that metadata, including table and column statistics, is not available. Defaults to false.

metadata.schemas.cache-ttl

Duration for which schema metadata is cached. Defaults to the value of metadata.cache-ttl.

metadata.tables.cache-ttl

Duration for which table metadata is cached. Defaults to the value of metadata.cache-ttl.

metadata.statistics.cache-ttl

Duration for which tables statistics are cached. Defaults to the value of metadata.cache-ttl.

metadata.cache-maximum-size

Maximum number of objects stored in the metadata cache. Defaults to 10000.

Maximum number of statements in a batched execution. Do not change this setting from the default. Non-default values may negatively impact performance. Defaults to 1000.

dynamic-filtering.enabled

Push down dynamic filters into JDBC queries. Defaults to true.

dynamic-filtering.wait-timeout

Maximum duration for which Trino waits for dynamic filters to be collected from the build side of joins before starting a JDBC query. Using a large timeout can potentially result in more detailed dynamic filters. However, it can also increase latency for some queries. Defaults to 20s.

The optional parameter query.comment-format allows you to configure a SQL comment that is sent to the datasource with each query. The format of this comment can contain any characters and the following metadata:

$QUERY_ID: The identifier of the query.

$USER: The name of the user who submits the query to Trino.

$SOURCE: The identifier of the client tool used to submit the query, for example trino-cli.

$TRACE_TOKEN: The trace token configured with the client tool.

The comment can provide more context about the query. This additional information is available in the logs of the datasource. To include environment variables from the Trino cluster with the comment , use the ${ENV:VARIABLE-NAME} syntax.

The following example sets a simple comment that identifies each query sent by Trino:

With this configuration, a query such as SELECT * FROM example_table; is sent to the datasource with the comment appended:

The following example improves on the preceding example by using metadata:

If Jane sent the query with the query identifier 20230622_180528_00000_bkizg, the following comment string is sent to the datasource:

Certain JDBC driver settings and logging configurations might cause the comment to be removed.

Pushing down a large list of predicates to the data source can compromise performance. Trino compacts large predicates into a simpler range predicate by default to ensure a balance between performance and predicate pushdown. If necessary, the threshold for this compaction can be increased to improve performance when the data source is capable of taking advantage of large predicates. Increasing this threshold may improve pushdown of large dynamic filters. The domain-compaction-threshold catalog configuration property or the domain_compaction_threshold catalog session property can be used to adjust the default value of 1000 for this threshold.

When case-insensitive-name-matching is set to true, Trino is able to query non-lowercase schemas and tables by maintaining a mapping of the lowercase name to the actual name in the remote system. However, if two schemas and/or tables have names that differ only in case (such as “customers” and “Customers”) then Trino fails to query them due to ambiguity.

In these cases, use the case-insensitive-name-matching.config-file catalog configuration property to specify a configuration file that maps these remote schemas and tables to their respective Trino schemas and tables. Additionally, the JSON file must include both the schemas and tables properties, even if only as empty arrays.

Queries against one of the tables or schemes defined in the mapping attributes are run against the corresponding remote entity. For example, a query against tables in the case_insensitive_1 schema is forwarded to the CaseSensitiveName schema and a query against case_insensitive_2 is forwarded to the cASEsENSITIVEnAME schema.

At the table mapping level, a query on case_insensitive_1.table_1 as configured above is forwarded to CaseSensitiveName.tablex, and a query on case_insensitive_1.table_2 is forwarded to CaseSensitiveName.TABLEX.

By default, when a change is made to the mapping configuration file, Trino must be restarted to load the changes. Optionally, you can set the case-insensitive-name-matching.config-file.refresh-period to have Trino refresh the properties without requiring a restart:

The ClickHouse connector provides a schema for every ClickHouse database. Run SHOW SCHEMAS to see the available ClickHouse databases:

If you have a ClickHouse database named web, run SHOW TABLES to view the tables in this database:

Run DESCRIBE or SHOW COLUMNS to list the columns in the clicks table in the web databases:

Run SELECT to access the clicks table in the web database:

If you used a different name for your catalog properties file, use that catalog name instead of example in the above examples.

Table property usage example:

The following are supported ClickHouse table properties from https://clickhouse.tech/docs/en/engines/table-engines/mergetree-family/mergetree/

Name and parameters of the engine.

Array of columns or expressions to concatenate to create the sorting key. tuple() is used by default if order_by is not specified.

Array of columns or expressions to use as nested partition keys. Optional.

Array of columns or expressions to concatenate to create the primary key. Optional.

An expression to use for sampling. Optional.

Currently the connector only supports Log and MergeTree table engines in create table statement. ReplicatedMergeTree engine is not yet supported.

Because Trino and ClickHouse each support types that the other does not, this connector modifies some types when reading or writing data. Data types may not map the same way in both directions between Trino and the data source. Refer to the following sections for type mapping in each direction.

The connector maps ClickHouse types to the corresponding Trino types according to the following table:

TINYINT and INT1 are aliases of Int8

SMALLINT and INT2 are aliases of Int16

INT, INT4, and INTEGER are aliases of Int32

BIGINT is an alias of Int64

FLOAT is an alias of Float32

DOUBLE is an alias of Float64

Enabling clickhouse.map-string-as-varchar config property changes the mapping to VARCHAR

Enabling clickhouse.map-string-as-varchar config property changes the mapping to VARCHAR

TIMESTAMP(0) [WITH TIME ZONE]

No other types are supported.

The connector maps Trino types to the corresponding ClickHouse types according to the following table:

TINYINT and INT1 are aliases of Int8

SMALLINT and INT2 are aliases of Int16

INT, INT4, and INTEGER are aliases of Int32

BIGINT is an alias of Int64

FLOAT is an alias of Float32

DOUBLE is an alias of Float64

Enabling clickhouse.map-string-as-varchar config property changes the mapping to VARCHAR

No other types are supported.

The following properties can be used to configure how data types from the connected data source are mapped to Trino data types and how the metadata is cached in Trino.

unsupported-type-handling

Configure how unsupported column data types are handled:

IGNORE, column is not accessible.

CONVERT_TO_VARCHAR, column is converted to unbounded VARCHAR.

The respective catalog session property is unsupported_type_handling.

jdbc-types-mapped-to-varchar

Allow forced mapping of comma separated lists of data types to convert to unbounded VARCHAR

The connector provides read and write access to data and metadata in a ClickHouse catalog. In addition to the globally available and read operation statements, the connector supports the following features:

INSERT, see also Non-transactional INSERT

Schema and table management, see also:

ALTER SCHEMA limitation

The connector supports adding rows using INSERT statements. By default, data insertion is performed by writing data to a temporary table. You can skip this step to improve performance and write directly to the target table. Set the insert.non-transactional-insert.enabled catalog property or the corresponding non_transactional_insert catalog session property to true.

Note that with this property enabled, data can be corrupted in rare cases where exceptions occur during the insert operation. With transactions disabled, no rollback can be performed.

The connector supports renaming a schema with the ALTER SCHEMA RENAME statement. ALTER SCHEMA SET AUTHORIZATION is not supported.

Flush JDBC metadata caches. For example, the following system call flushes the metadata caches for all schemas in the example catalog

The execute procedure allows you to execute a query in the underlying data source directly. The query must use supported syntax of the connected data source. Use the procedure to access features which are not available in Trino or to execute queries that return no result set and therefore can not be used with the query or raw_query pass-through table function. Typical use cases are statements that create or alter objects, and require native feature such as constraints, default values, automatic identifier creation, or indexes. Queries can also invoke statements that insert, update, or delete data, and do not return any data as a result.

The query text is not parsed by Trino, only passed through, and therefore only subject to any security or access control of the underlying data source.

The following example sets the current database to the example_schema of the example catalog. Then it calls the procedure in that schema to drop the default value from your_column on your_table table using the standard SQL syntax in the parameter value assigned for query:

Verify that the specific database supports this syntax, and adapt as necessary based on the documentation for the specific connected database and database version.

The connector provides specific table functions to access ClickHouse.

The query function allows you to query the underlying database directly. It requires syntax native to ClickHouse, because the full query is pushed down and processed in ClickHouse. This can be useful for accessing native features which are not available in Trino or for improving query performance in situations where running a query natively may be faster.

The native query passed to the underlying data source is required to return a table as a result set. Only the data source performs validation or security checks for these queries using its own configuration. Trino does not perform these tasks. Only use passthrough queries to read data.

As a simple example, query the example catalog and select an entire table:

The query engine does not preserve the order of the results of this function. If the passed query contains an ORDER BY clause, the function result may not be ordered as expected.

The connector includes a number of performance improvements, detailed in the following sections.

The connector supports pushdown for a number of operations:

Aggregate pushdown for the following functions:

The connector performs pushdown where performance may be improved, but in order to preserve correctness an operation may not be pushed down. When pushdown of an operation may result in better performance but risks correctness, the connector prioritizes correctness.

The connector does not support pushdown of inequality predicates, such as !=, and range predicates such as >, or BETWEEN, on columns with character string types like CHAR or VARCHAR. Equality predicates, such as IN or =, on columns with character string types are pushed down. This ensures correctness of results since the remote data source may sort strings differently than Trino.

In the following example, the predicate of the first and second query is not pushed down since name is a column of type VARCHAR and > and != are range and inequality predicates respectively. The last query is pushed down.

**Examples:**

Example 1 (unknown):
```unknown
connector.name=clickhouse
connection-url=jdbc:clickhouse://host1:8123/
connection-user=exampleuser
connection-password=examplepassword
```

Example 2 (unknown):
```unknown
connector.name=clickhouse
connection-url=jdbc:clickhouse://host1:8123/
connection-user=exampleuser
connection-password=examplepassword
```

Example 3 (unknown):
```unknown
connection-url=jdbc:clickhouse://host1:8443/?ssl=true
```

Example 4 (unknown):
```unknown
connection-url=jdbc:clickhouse://host1:8443/?ssl=true
```

---

## Druid connector — Trino 478 Documentation

**URL:** https://trino.io/docs/current/connector/druid.html

**Contents:**
- Druid connector#
- Requirements#
- Configuration#
  - Data source authentication#
  - General configuration properties#
  - Appending query metadata#
  - Domain compaction threshold#
  - Case insensitive matching#
- Type mapping#
  - Druid type to Trino type mapping#

The Druid connector allows querying an Apache Druid database from Trino.

To connect to Druid, you need:

Druid version 0.18.0 or higher.

Network access from the Trino coordinator and workers to your Druid broker. Port 8082 is the default port.

Create a catalog properties file that specifies the Druid connector by setting the connector.name to druid and configuring the connection-url with the JDBC string to connect to Druid.

For example, to access a database as example, create the file etc/catalog/example.properties. Replace BROKER:8082 with the correct host and port of your Druid broker.

You can add authentication details to connect to a Druid deployment that is secured by basic authentication by updating the URL and adding credentials:

Now you can access your Druid database in Trino with the example catalog name from the properties file.

The connection-user and connection-password are typically required and determine the user credentials for the connection, often a service user. You can use secrets to avoid actual values in the catalog properties files.

The connector can provide credentials for the data source connection in multiple ways:

inline, in the connector configuration file

in a separate properties file

as extra credentials set when connecting to Trino

You can use secrets to avoid storing sensitive values in the catalog properties files.

The following table describes configuration properties for connection credentials:

credential-provider.type

Type of the credential provider. Must be one of INLINE, FILE, or KEYSTORE; defaults to INLINE.

Connection user name.

Name of the extra credentials property, whose value to use as the user name. See extraCredentials in Parameter reference.

password-credential-name

Name of the extra credentials property, whose value to use as the password.

connection-credential-file

Location of the properties file where credentials are present. It must contain the connection-user and connection-password properties.

The location of the Java Keystore file, from which to read credentials.

File format of the keystore file, for example JKS or PEM.

Password for the key store.

keystore-user-credential-name

Name of the key store entity to use as the user name.

keystore-user-credential-password

Password for the user name key store entity.

keystore-password-credential-name

Name of the key store entity to use as the password.

keystore-password-credential-password

Password for the password key store entity.

The following table describes general catalog configuration properties for the connector:

case-insensitive-name-matching

Support case insensitive schema and table names. Defaults to false.

case-insensitive-name-matching.cache-ttl

Duration for which case insensitive schema and table names are cached. Defaults to 1m.

case-insensitive-name-matching.config-file

Path to a name mapping configuration file in JSON format that allows Trino to disambiguate between schemas and tables with similar names in different cases. Defaults to null.

case-insensitive-name-matching.config-file.refresh-period

Frequency with which Trino checks the name matching configuration file for changes. The duration value defaults to 0s (refresh disabled).

Duration for which metadata, including table and column statistics, is cached. Defaults to 0s (caching disabled).

metadata.cache-missing

Cache the fact that metadata, including table and column statistics, is not available. Defaults to false.

metadata.schemas.cache-ttl

Duration for which schema metadata is cached. Defaults to the value of metadata.cache-ttl.

metadata.tables.cache-ttl

Duration for which table metadata is cached. Defaults to the value of metadata.cache-ttl.

metadata.statistics.cache-ttl

Duration for which tables statistics are cached. Defaults to the value of metadata.cache-ttl.

metadata.cache-maximum-size

Maximum number of objects stored in the metadata cache. Defaults to 10000.

Maximum number of statements in a batched execution. Do not change this setting from the default. Non-default values may negatively impact performance. Defaults to 1000.

dynamic-filtering.enabled

Push down dynamic filters into JDBC queries. Defaults to true.

dynamic-filtering.wait-timeout

Maximum duration for which Trino waits for dynamic filters to be collected from the build side of joins before starting a JDBC query. Using a large timeout can potentially result in more detailed dynamic filters. However, it can also increase latency for some queries. Defaults to 20s.

The optional parameter query.comment-format allows you to configure a SQL comment that is sent to the datasource with each query. The format of this comment can contain any characters and the following metadata:

$QUERY_ID: The identifier of the query.

$USER: The name of the user who submits the query to Trino.

$SOURCE: The identifier of the client tool used to submit the query, for example trino-cli.

$TRACE_TOKEN: The trace token configured with the client tool.

The comment can provide more context about the query. This additional information is available in the logs of the datasource. To include environment variables from the Trino cluster with the comment , use the ${ENV:VARIABLE-NAME} syntax.

The following example sets a simple comment that identifies each query sent by Trino:

With this configuration, a query such as SELECT * FROM example_table; is sent to the datasource with the comment appended:

The following example improves on the preceding example by using metadata:

If Jane sent the query with the query identifier 20230622_180528_00000_bkizg, the following comment string is sent to the datasource:

Certain JDBC driver settings and logging configurations might cause the comment to be removed.

Pushing down a large list of predicates to the data source can compromise performance. Trino compacts large predicates into a simpler range predicate by default to ensure a balance between performance and predicate pushdown. If necessary, the threshold for this compaction can be increased to improve performance when the data source is capable of taking advantage of large predicates. Increasing this threshold may improve pushdown of large dynamic filters. The domain-compaction-threshold catalog configuration property or the domain_compaction_threshold catalog session property can be used to adjust the default value of 256 for this threshold.

When case-insensitive-name-matching is set to true, Trino is able to query non-lowercase schemas and tables by maintaining a mapping of the lowercase name to the actual name in the remote system. However, if two schemas and/or tables have names that differ only in case (such as “customers” and “Customers”) then Trino fails to query them due to ambiguity.

In these cases, use the case-insensitive-name-matching.config-file catalog configuration property to specify a configuration file that maps these remote schemas and tables to their respective Trino schemas and tables. Additionally, the JSON file must include both the schemas and tables properties, even if only as empty arrays.

Queries against one of the tables or schemes defined in the mapping attributes are run against the corresponding remote entity. For example, a query against tables in the case_insensitive_1 schema is forwarded to the CaseSensitiveName schema and a query against case_insensitive_2 is forwarded to the cASEsENSITIVEnAME schema.

At the table mapping level, a query on case_insensitive_1.table_1 as configured above is forwarded to CaseSensitiveName.tablex, and a query on case_insensitive_1.table_2 is forwarded to CaseSensitiveName.TABLEX.

By default, when a change is made to the mapping configuration file, Trino must be restarted to load the changes. Optionally, you can set the case-insensitive-name-matching.config-file.refresh-period to have Trino refresh the properties without requiring a restart:

Because Trino and Druid each support types that the other does not, this connector modifies some types when reading data.

The connector maps Druid types to the corresponding Trino types according to the following table:

Except for the special _time column, which is mapped to TIMESTAMP.

Only applicable to the special _time column.

No other data types are supported.

Druid does not have a real NULL value for any data type. By default, Druid treats NULL as the default value for a data type. For example, LONG would be 0, DOUBLE would be 0.0, STRING would be an empty string '', and so forth.

The following properties can be used to configure how data types from the connected data source are mapped to Trino data types and how the metadata is cached in Trino.

unsupported-type-handling

Configure how unsupported column data types are handled:

IGNORE, column is not accessible.

CONVERT_TO_VARCHAR, column is converted to unbounded VARCHAR.

The respective catalog session property is unsupported_type_handling.

jdbc-types-mapped-to-varchar

Allow forced mapping of comma separated lists of data types to convert to unbounded VARCHAR

The connector provides read access to data and metadata in the Druid database. In addition to the globally available and read operation statements, the connector supports the following features:

Flush JDBC metadata caches. For example, the following system call flushes the metadata caches for all schemas in the example catalog

The execute procedure allows you to execute a query in the underlying data source directly. The query must use supported syntax of the connected data source. Use the procedure to access features which are not available in Trino or to execute queries that return no result set and therefore can not be used with the query or raw_query pass-through table function. Typical use cases are statements that create or alter objects, and require native feature such as constraints, default values, automatic identifier creation, or indexes. Queries can also invoke statements that insert, update, or delete data, and do not return any data as a result.

The query text is not parsed by Trino, only passed through, and therefore only subject to any security or access control of the underlying data source.

The following example sets the current database to the example_schema of the example catalog. Then it calls the procedure in that schema to drop the default value from your_column on your_table table using the standard SQL syntax in the parameter value assigned for query:

Verify that the specific database supports this syntax, and adapt as necessary based on the documentation for the specific connected database and database version.

The connector provides specific table functions to access Druid.

The query function allows you to query the underlying database directly. It requires syntax native to Druid, because the full query is pushed down and processed in Druid. This can be useful for accessing native features which are not available in Trino or for improving query performance in situations where running a query natively may be faster.

The native query passed to the underlying data source is required to return a table as a result set. Only the data source performs validation or security checks for these queries using its own configuration. Trino does not perform these tasks. Only use passthrough queries to read data.

As an example, query the example catalog and use STRING_TO_MV and MV_LENGTH from Druid SQL’s multi-value string functions to split and then count the number of comma-separated values in a column:

The query engine does not preserve the order of the results of this function. If the passed query contains an ORDER BY clause, the function result may not be ordered as expected.

**Examples:**

Example 1 (unknown):
```unknown
connector.name=druid
connection-url=jdbc:avatica:remote:url=http://BROKER:8082/druid/v2/sql/avatica/
```

Example 2 (unknown):
```unknown
connector.name=druid
connection-url=jdbc:avatica:remote:url=http://BROKER:8082/druid/v2/sql/avatica/
```

Example 3 (unknown):
```unknown
connection-url=jdbc:avatica:remote:url=http://BROKER:port/druid/v2/sql/avatica/;authentication=BASIC
connection-user=root
connection-password=secret
```

Example 4 (unknown):
```unknown
connection-url=jdbc:avatica:remote:url=http://BROKER:port/druid/v2/sql/avatica/;authentication=BASIC
connection-user=root
connection-password=secret
```

---

## Faker connector — Trino 478 Documentation

**URL:** https://trino.io/docs/current/connector/faker.html

**Contents:**
- Faker connector#
- Configuration#
  - Character types#
  - Non-character types#
  - Unsupported types#
  - Number of generated rows#
  - Null values#
- Type mapping#
- SQL support#
- Usage#

The Faker connector generates random data matching a defined structure. It uses the Datafaker library to make the generated data more realistic.

Use the connector to test and learn SQL queries without the need for a fixed, imported dataset, or to populate another data source with large and realistic test data. This allows testing the performance of applications processing data, including Trino itself, and application user interfaces accessing the data.

Create a catalog properties file that specifies the Faker connector by setting the connector.name to faker.

For example, to generate data in the generator catalog, create the file etc/catalog/generator.properties.

Create tables in the default schema, or create different schemas first. Tables in the catalog only exist as definition and do not hold actual data. Any query reading from tables returns random, but deterministic data. As a result, repeated invocation of a query returns identical data. See Usage for more examples.

Schemas, tables, and views in a catalog are not persisted, and are stored in the memory of the coordinator only. They need to be recreated every time after restarting the coordinator.

The following table details all general configuration properties:

faker.null-probability

Default probability of a value created as null for any column in any table that allows them. Defaults to 0.5.

Default number of rows in a table. Defaults to 1000.

Default locale for generating character-based data, specified as an IETF BCP 47 language tag string. Defaults to en.

faker.sequence-detection-enabled

If true, when creating a table using existing data, columns with the number of distinct values close to the number of rows are treated as sequences. Defaults to true.

faker.dictionary-detection-enabled

If true, when creating a table using existing data, columns with a low number of distinct values are treated as dictionaries, and get the allowed_values column property populated with random values. Defaults to true.

The following table details all supported schema properties. If they’re not set, values from corresponding configuration properties are used.

Default probability of a value created as null in any column that allows them, in any table of this schema.

Default number of rows in a table.

sequence_detection_enabled

If true, when creating a table using existing data, columns with the number of distinct values close to the number of rows are treated as sequences. Defaults to true.

dictionary_detection_enabled

If true, when creating a table using existing data, columns with a low number of distinct values are treated as dictionaries, and get the allowed_values column property populated with random values. Defaults to true.

The following table details all supported table properties. If they’re not set, values from corresponding schema properties are used.

Default probability of a value created as null in any column that allows null in the table.

Default number of rows in the table.

sequence_detection_enabled

If true, when creating a table using existing data, columns with the number of distinct values close to the number of rows are treated as sequences. Defaults to true.

dictionary_detection_enabled

If true, when creating a table using existing data, columns with a low number of distinct values are treated as dictionaries, and get the allowed_values column property populated with random values. Defaults to true.

The following table details all supported column properties.

Default probability of a value created as null in the column. Defaults to the null_probability table or schema property, if set, or the faker.null-probability configuration property.

Name of the Faker library generator used to generate data for the column. Only valid for columns of a character-based type. Defaults to a 3 to 40 word sentence from the Lorem provider.

Minimum generated value (inclusive). Cannot be set for character-based type columns.

Maximum generated value (inclusive). Cannot be set for character-based type columns.

List of allowed values. Cannot be set together with the min, or max properties.

If set, generate sequential values with this step. For date and time columns set this to a duration. Cannot be set for character-based type columns.

Faker supports the following character types:

Columns of those types use a generator producing the Lorem ipsum placeholder text. Unbounded columns return a random sentence with 3 to 40 words.

To have more control over the format of the generated data, use the generator column property. Some examples of valid generator expressions:

#{regexify '(a|b){2,3}'}

#{regexify '\\.\\*\\?\\+'}

#{bothify '????','false'}

#{Name.first_name} #{Name.first_name} #{Name.last_name}

#{number.number_between '1','10'}

See the Datafaker’s documentation for more information about the expression syntax and available providers.

Create a random output string with the provided input expression_string. The expression must use the syntax from Datafaker.

Use the random_string function from the default schema of the generator catalog to test a generator expression:

Faker supports the following non-character types:

INTERVAL DAY TO SECOND

INTERVAL YEAR TO MONTH

TIMESTAMP and TIMESTAMP(P)

TIMESTAMP WITH TIME ZONE and TIMESTAMP(P) WITH TIME ZONE

TIME WITH TIME ZONE and TIME(P) WITH TIME ZONE

You can not use generator expressions for non-character-based columns. To limit their data range, set the min and max column properties - see Usage.

Faker does not support the following data types:

Structural types ARRAY and MAP

HyperLogLog and all digest types

To generate data using these complex types, data from column of primitive types can be combined, like in the following example:

Running the queries returns data similar to the following result:

By default, the connector generates 1000 rows for every table. To control how many rows are generated for a table, use the LIMIT clause in the query. A default limit can be set using the default_limit table, or schema property or in the connector configuration file, using the faker.default-limit property. Use a limit value higher than the configured default to return more rows.

For columns without a NOT NULL constraint, null values are generated using the default probability of 50%. It can be modified using the null_probability property set for a column, table, or schema. The default value of 0.5 can be also modified in the catalog configuration file, by using the faker.null-probability property.

The Faker connector generates data itself, so no mapping is required.

The connector provides globally available and read operation statements to generate data.

To define the schema for generating data, it supports the following features:

CREATE TABLE AS, see also Using existing data statistics

Faker generates data when reading from a table created in a catalog using this connector. This makes it easy to fill an existing schema with random data, by copying only the schema into a Faker catalog, and inserting the data back into the original tables.

Using the catalog definition from Configuration you can proceed with the following steps.

Create a table with the same columns as in the table to populate with random data. Exclude all properties, because the Faker connector doesn’t support the same table properties as other connectors.

Insert random data into the original table, by selecting it from the generator catalog. Data generated by the Faker connector for columns of non-character types cover the whole range of that data type. Set the min and max column properties, to adjust the generated data as desired. The following example ensures that date of birth and age in years are related and realistic values.

Start with getting the complete definition of a table:

Modify the output of the previous query and add some column properties.

To generate even more realistic data, choose specific generators by setting the generator property on columns.

The Faker connector automatically sets the default_limit table property, and the min, max, and null_probability column properties, based on statistics collected by scanning existing data read by Trino from the data source. The connector uses these statistics to be able to generate data that is more similar to the original data set, without using any of that data:

Instead of using range, or other predicates, tables can be sampled, see TABLESAMPLE.

When the SELECT statement doesn’t contain a WHERE clause, a shorter notation can be used:

The Faker connector detects sequence columns, which are integer column with the number of distinct values almost equal to the number of rows in the table. For such columns, Faker sets the step column property to 1.

Sequence detection can be turned off using the sequence_detection_enabled table, or schema property or in the connector configuration file, using the faker.sequence-detection-enabled property.

The Faker connector detects dictionary columns, which are columns of non-character types with the number of distinct values lower or equal to 1000. For such columns, Faker generates a list of random values to choose from, and saves it in the allowed_values column property.

Dictionary detection can be turned off using the dictionary_detection_enabled table, or schema property or in the connector configuration file, using the faker.dictionary-detection-enabled property.

For example, copy the orders table from the TPC-H connector with statistics, using the following query:

Inspect the schema of the table created by the Faker connector:

The table schema should contain additional column and table properties.

**Examples:**

Example 1 (unknown):
```unknown
connector.name=faker
faker.null-probability=0.1
faker.default-limit=1000
faker.locale=pl
```

Example 2 (unknown):
```unknown
connector.name=faker
faker.null-probability=0.1
faker.default-limit=1000
faker.locale=pl
```

Example 3 (unknown):
```unknown
SELECT generator.default.random_string('#{Name.first_name}');
```

Example 4 (unknown):
```unknown
SELECT generator.default.random_string('#{Name.first_name}');
```

---

## Iceberg connector — Trino 478 Documentation

**URL:** https://trino.io/docs/current/connector/iceberg.html

**Contents:**
- Iceberg connector#
- Requirements#
- General configuration#
  - Fault-tolerant execution support#
- File system access configuration#
- Type mapping#
  - Iceberg to Trino type mapping#
  - Trino to Iceberg type mapping#
- Security#
  - Kerberos authentication#

Apache Iceberg is an open table format for huge analytic datasets. The Iceberg connector allows querying data stored in files written in Iceberg format, as defined in the Iceberg Table Spec. The connector supports Apache Iceberg table spec versions 1 and 2.

The table state is maintained in metadata files. All changes to table state create a new metadata file and replace the old metadata with an atomic swap. The table metadata file tracks the table schema, partitioning configuration, custom properties, and snapshots of the table contents.

Iceberg data files are stored in either Parquet, ORC, or Avro format, as determined by the format property in the table definition.

Iceberg is designed to improve on the known scalability limitations of Hive, which stores table metadata in a metastore that is backed by a relational database such as MySQL. It tracks partition locations in the metastore, but not individual data files. Trino queries using the Hive connector must first call the metastore to get partition locations, then call the underlying file system to list all data files inside each partition, and then read metadata from each data file.

Since Iceberg stores the paths to data files in the metadata files, it only consults the underlying file system for files that must be read.

To use Iceberg, you need:

Network access from the Trino coordinator and workers to the distributed object storage.

Access to a Hive metastore service (HMS), an AWS Glue catalog, a JDBC catalog, a REST catalog, a Nessie server, or a Snowflake catalog.

Data files stored in the file formats Parquet(default), ORC, or Avro on a supported file system.

To configure the Iceberg connector, create a catalog properties file etc/catalog/example.properties that references the iceberg connector.

The Hive metastore catalog is the default implementation.

You must select and configure one of the supported file systems.

Replace the fs.x.enabled configuration property with the desired file system.

Other metadata catalog types as listed in the requirements section of this topic are available. Each metastore type has specific configuration properties along with general metastore configuration properties.

The following configuration properties are independent of which catalog implementation is used:

Define the metastore type to use. Possible values are:

Define the data storage file format for Iceberg tables. Possible values are:

iceberg.compression-codec

The compression codec used when writing files. Possible values are:

iceberg.use-file-size-from-metadata

Read file sizes from metadata instead of file system. This property must only be used as a workaround for this issue. The problem was fixed in Iceberg version 0.11.0.

iceberg.max-partitions-per-writer

Maximum number of partitions handled per writer. The equivalent catalog session property is max_partitions_per_writer.

iceberg.target-max-file-size

Target maximum size of written files; the actual size may be larger.

iceberg.unique-table-location

Use randomized, unique table locations.

iceberg.dynamic-filtering.wait-timeout

Maximum duration to wait for completion of dynamic filters during split generation.

iceberg.delete-schema-locations-fallback

Whether schema locations are deleted when Trino can’t determine whether they contain external files.

iceberg.minimum-assigned-split-weight

A decimal value in the range (0, 1] used as a minimum for weights assigned to each split. A low value may improve performance on tables with small files. A higher value may improve performance for queries with highly skewed aggregations or joins.

iceberg.table-statistics-enabled

Enable Table statistics. The equivalent catalog session property is statistics_enabled for session specific use. Set to false to prevent statistics usage by the Cost-based optimizations to make better decisions about the query plan and therefore improve query processing performance. Setting to false is not recommended and does not disable statistics gathering.

iceberg.extended-statistics.enabled

Enable statistics collection with ANALYZE and use of extended statistics. The equivalent catalog session property is extended_statistics_enabled.

iceberg.extended-statistics.collect-on-write

Enable collection of extended statistics for write operations. The equivalent catalog session property is collect_extended_statistics_on_write.

iceberg.projection-pushdown-enabled

Enable projection pushdown

iceberg.hive-catalog-name

Catalog to redirect to when a Hive table is referenced.

iceberg.register-table-procedure.enabled

Enable to allow user to call register_table procedure.

iceberg.add-files-procedure.enabled

Enable to allow user to call add_files procedure.

iceberg.query-partition-filter-required

Set to true to force a query to use a partition filter for schemas specified with iceberg.query-partition-filter-required-schemas. Equivalent catalog session property is query_partition_filter_required.

iceberg.query-partition-filter-required-schemas

Specify the list of schemas for which Trino can enforce that queries use a filter on partition keys for source tables. Equivalent session property is query_partition_filter_required_schemas. The list is used if the iceberg.query-partition-filter-required configuration property or the query_partition_filter_required catalog session property is set to true.

iceberg.incremental-refresh-enabled

Set to false to force the materialized view refresh operation to always perform a full refresh. You can use the incremental_refresh_enabled catalog session property for temporary, catalog specific use. In the majority of cases, using incremental refresh, as compared to a full refresh, is beneficial since a much smaller subset of the source tables needs to be scanned. While incremental refresh may scan less data, it may result in the creation of more data files, since it uses the append operation to insert the new records.

iceberg.metadata-cache.enabled

Set to false to disable in-memory caching of metadata files on the coordinator. This cache is not used when fs.cache.enabled is set to true.

iceberg.object-store-layout.enabled

Set to true to enable Iceberg’s object store file layout. Enabling the object store file layout appends a deterministic hash directly after the data write path.

iceberg.expire-snapshots.min-retention

Minimal retention period for the expire_snapshot command. Equivalent session property is expire_snapshots_min_retention.

iceberg.remove-orphan-files.min-retention

Minimal retention period for the remove_orphan_files command. Equivalent session property is remove_orphan_files_min_retention.

iceberg.idle-writer-min-file-size

Minimum data written by a single partition writer before it can be considered as idle and can be closed by the engine. Equivalent session property is idle_writer_min_file_size.

iceberg.sorted-writing-enabled

Enable sorted writing to tables with a specified sort order. Equivalent session property is sorted_writing_enabled.

iceberg.sorted-writing.local-staging-path

A local directory that Trino can use for staging writes to sorted tables. The ${USER} placeholder can be used to use a different location for each user. When this property is not configured, the target storage will be used for staging while writing to sorted tables which can be inefficient when writing to object stores like S3. When fs.hadoop.enabled is not enabled, using this feature requires setup of local file system

iceberg.allowed-extra-properties

List of extra properties that are allowed to be set on Iceberg tables. Use * to allow all properties.

iceberg.split-manager-threads

Number of threads to use for generating splits.

Double the number of processors on the coordinator node.

iceberg.metadata.parallelism

Number of threads used for retrieving metadata. Currently, only table loading is parallelized.

iceberg.file-delete-threads

Number of threads to use for deleting files when running expire_snapshots procedure.

Double the number of processors on the coordinator node.

iceberg.bucket-execution

Enable bucket-aware execution. This allows the engine to use physical bucketing information to optimize queries by reducing data exchanges.

The connector supports Fault-tolerant execution of query processing. Read and write operations are both supported with any retry policy.

The connector supports accessing the following file systems:

Azure Storage file system support

Google Cloud Storage file system support

S3 file system support

HDFS file system support

You must enable and configure the specific file system access. Legacy support is not recommended and will be removed.

The connector reads and writes data into the supported data file formats Avro, ORC, and Parquet, following the Iceberg specification.

Because Trino and Iceberg each support types that the other does not, this connector modifies some types when reading or writing data. Data types may not map the same way in both directions between Trino and the data source. Refer to the following sections for type mapping in each direction.

The Iceberg specification includes supported data types and the mapping to the formating in the Avro, ORC, or Parquet files:

The connector maps Iceberg types to the corresponding Trino types according to the following table:

TIMESTAMP(6) WITH TIME ZONE

No other types are supported.

The connector maps Trino types to the corresponding Iceberg types according to the following table:

TIMESTAMP(6) WITH TIME ZONE

No other types are supported.

The Iceberg connector supports Kerberos authentication for the Hive metastore and HDFS and is configured using the same parameters as the Hive connector. Find more information in the HDFS file system support section.

The Iceberg connector allows you to choose one of several means of providing authorization at the catalog level.

You can enable authorization checks for the connector by setting the iceberg.security property in the catalog properties file. This property must be one of the following values:

No authorization checks are enforced.

The connector relies on system-level access control.

Operations that read data or metadata, such as SELECT are permitted. No operations that write data or metadata, such as CREATE TABLE, INSERT, or DELETE are allowed.

Authorization checks are enforced using a catalog-level access control configuration file whose path is specified in the security.config-file catalog configuration property. See Catalog-level access control files for information on the authorization configuration file.

This connector provides read access and write access to data and metadata in Iceberg. In addition to the globally available and read operation statements, the connector supports the following features:

Schema and table management and Partitioned tables

Materialized view management, see also Materialized views

The connector supports creating schemas. You can create a schema with or without a specified location.

You can create a schema with the CREATE SCHEMA statement and the location schema property. The tables in this schema, which have no explicit location set in CREATE TABLE statement, are located in a subdirectory under the directory corresponding to the schema location.

Create a schema on S3:

Create a schema on an S3-compatible object storage such as MinIO:

Create a schema on HDFS:

Optionally, on HDFS, the location can be omitted:

The Iceberg connector supports creating tables using the CREATE TABLE syntax. Optionally, specify the table properties supported by this connector:

When the location table property is omitted, the content of the table is stored in a subdirectory under the directory corresponding to the schema location.

The Iceberg connector supports creating tables using the CREATE TABLE AS with SELECT syntax:

Another flavor of creating tables with CREATE TABLE AS is with VALUES syntax:

Use the CALL statement to perform data manipulation or administrative tasks. Procedures are available in the system schema of each catalog. The following code snippet displays how to call the example_procedure in the examplecatalog catalog:

The connector can register existing Iceberg tables into the metastore if iceberg.register-table-procedure.enabled is set to true for the catalog.

The procedure system.register_table allows the caller to register an existing Iceberg table in the metastore, using its existing metadata and data files:

In addition, you can provide a file name to register a table with specific metadata. This may be used to register the table with some specific table state, or may be necessary if the connector cannot automatically figure out the metadata version to use:

To prevent unauthorized users from accessing data, this procedure is disabled by default. The procedure is enabled only when iceberg.register-table-procedure.enabled is set to true.

The connector can remove existing Iceberg tables from the metastore. Once unregistered, you can no longer query the table from Trino.

The procedure system.unregister_table allows the caller to unregister an existing Iceberg table from the metastores without deleting the data:

The connector can read from or write to Hive tables that have been migrated to Iceberg.

Use the procedure system.migrate to move a table from the Hive format to the Iceberg format, loaded with the source’s data files. Table schema, partitioning, properties, and location are copied from the source table. A bucketed Hive table will be migrated as a non-bucketed Iceberg table. The data files in the Hive table must use the Parquet, ORC, or Avro file format.

The procedure must be called for a specific catalog example with the relevant schema and table names supplied with the required parameters schema_name and table_name:

Migrate fails if any table partition uses an unsupported file format.

In addition, you can provide a recursive_directory argument to migrate a Hive table that contains subdirectories:

The default value is fail, which causes the migrate procedure to throw an exception if subdirectories are found. Set the value to true to migrate nested directories, or false to ignore them.

The connector can add files from tables or locations to an existing Iceberg table if iceberg.add-files-procedure.enabled is set to true for the catalog.

Use the procedure add_files_from_table to add existing files from a Hive table in the current catalog, or add_files to add existing files from a specified location, to an existing Iceberg table.

The data files must be the Parquet, ORC, or Avro file format.

The procedure adds the files to the target table, specified after ALTER TABLE, and loads them from the source table specified with the required parameters schema_name and table_name. The source table must be accessible in the same catalog as the target table and use the Hive format. The target table must use the Iceberg format. The catalog must use the Iceberg connector.

The following examples copy data from the Hive table hive_customer_orders in the legacy schema of the example catalog into the Iceberg table iceberg_customer_orders in the lakehouse schema of the example catalog:

Alternatively, you can set the current catalog and schema with a USE statement, and omit catalog and schema information:

Use a partition_filter argument to add files from specified partitions. The following example adds files from a partition where the region is ASIA and country is JAPAN:

In addition, you can provide a recursive_directory argument to migrate a Hive table that contains subdirectories:

The default value of recursive_directory is fail, which causes the procedure to throw an exception if subdirectories are found. Set the value to true to add files from nested directories, or false to ignore them.

The add_files procedure supports adding files, and therefore the contained data, to a target table, specified after ALTER TABLE. It loads the files from a object storage path specified with the required location parameter. The files must use the specified format, with ORC and PARQUET as valid values. The target Iceberg table must use the same format as the added files. The procedure does not validate file schemas for compatibility with the target Iceberg table. The location property is supported for partitioned tables.

The following examples copy ORC-format files from the location s3://my-bucket/a/path into the Iceberg table iceberg_customer_orders in the lakehouse schema of the example catalog:

Functions are available in the system schema of each catalog. Functions can be called in a SQL statement. For example, the following code snippet displays how to execute the system.bucket function in an Iceberg catalog:

This function exposes the Iceberg bucket transform so that users can determine what bucket a particular value falls into. The function takes two arguments: the partition value and the number of buckets.

The supported types for the 1st argument to this function are:

TIMESTAMP WITH TIME ZONE

For example, if we wanted to see what bucket number a particular string would be assigned, we can execute:

This function can be used in a WHERE clause to only operate on a particular bucket:

The Data management functionality includes support for INSERT, UPDATE, DELETE, TRUNCATE, and MERGE statements.

For partitioned tables, the Iceberg connector supports the deletion of entire partitions if the WHERE clause specifies filters only on the identity-transformed partitioning columns, that can match entire partitions. Given the table definition from Partitioned Tables section, the following SQL statement deletes all partitions for which country is US:

A partition delete is performed if the WHERE clause meets these conditions.

Tables using v2 of the Iceberg specification support deletion of individual rows by writing position delete files.

The Schema and table management functionality includes support for:

Iceberg supports schema evolution, with safe column add, drop, and rename operations, including in nested structures.

Iceberg supports updating column types only for widening operations:

DECIMAL(p,s) to DECIMAL(p2,s) when p2 > p (scale cannot change)

Partitioning can also be changed and the connector can still query data created before the partitioning change.

The connector supports the following commands for use with ALTER TABLE EXECUTE.

The optimize command is used for rewriting the content of the specified table so that it is merged into fewer but larger files. If the table is partitioned, the data compaction acts separately on each partition selected for optimization. This operation improves read performance.

All files with a size below the optional file_size_threshold parameter (default value for the threshold is 100MB) are merged in case any of the following conditions are met per partition:

more than one data file to merge is present

at least one data file, with delete files attached, is present

The following statement merges files in a table that are under 128 megabytes in size:

You can use a WHERE clause with the columns used to partition the table to filter which partitions are optimized:

You can use a more complex WHERE clause to narrow down the scope of the optimize procedure. The following example casts the timestamp values to dates, and uses a comparison to only optimize partitions with data from the year 2022 or newer:

Use a WHERE clause with metadata columns to filter which files are optimized.

Rewrites manifest files to cluster them by partitioning columns. This can be used to optimize scan planning when there are many small manifest files or when there are partition filters in read queries but the manifest files are not grouped by partitions. The iceberg table property commit.manifest.target-size-bytes controls the maximum size of manifest files produced by this procedure.

optimize_manifests can be run as follows:

The expire_snapshots command removes all snapshots and all related metadata and data files. Regularly expiring snapshots is recommended to delete data files that are no longer needed, and to keep the size of table metadata small. The procedure affects all snapshots that are older than the time period configured with the retention_threshold parameter.

expire_snapshots can be run as follows:

The value for retention_threshold must be higher than or equal to iceberg.expire-snapshots.min-retention in the catalog, otherwise the procedure fails with a similar message: Retention specified (1.00d) is shorter than the minimum retention configured in the system (7.00d). The default value for this property is 7d.

The remove_orphan_files command removes all files from a table’s data directory that are not linked from metadata files and that are older than the value of retention_threshold parameter. Deleting orphan files from time to time is recommended to keep size of a table’s data directory under control.

remove_orphan_files can be run as follows:

The value for retention_threshold must be higher than or equal to iceberg.remove-orphan-files.min-retention in the catalog otherwise the procedure fails with a similar message: Retention specified (1.00d) is shorter than the minimum retention configured in the system (7.00d). The default value for this property is 7d.

The output of the query has the following metrics:

processed_manifests_count

The count of manifest files read by remove_orphan_files.

The count of files belonging to snapshots that have not been expired.

The count of files scanned from the file system.

The count of files deleted by remove_orphan_files.

The drop_extended_stats command removes all extended statistics information from the table.

drop_extended_stats can be run as follows:

The connector supports modifying the properties on existing tables using ALTER TABLE SET PROPERTIES.

The following table properties can be updated after a table is created:

object_store_layout_enabled

For example, to update a table from v1 of the Iceberg specification to v2:

Or to set the column my_new_partition_column as a partition column on a table:

The current values of a table’s properties can be shown using SHOW CREATE TABLE.

Table properties supply or set metadata for the underlying tables. This is key for CREATE TABLE AS statements. Table properties are passed to the connector using a WITH clause.

Optionally specifies the format of table data files; either PARQUET, ORC, or AVRO. Defaults to the value of the iceberg.file-format catalog configuration property, which defaults to PARQUET.

Optionally specifies the compression-codec used for writing the table; either NONE, ZSTD, SNAPPY, LZ4, or GZIP. Defaults to the value of the iceberg.compression-codec catalog configuration property, which defaults to ZSTD.

Optionally specifies table partitioning. If a table is partitioned by columns c1 and c2, the partitioning property is partitioning = ARRAY['c1', 'c2'].

The sort order to be applied during writes to the content of each file written to the table. If the table files are sorted by columns c1 and c2, the sort order property is sorted_by = ARRAY['c1', 'c2']. The sort order applies to the contents written within each output file independently and not the entire dataset.

Optionally specifies the file system location URI for the table.

Optionally specifies the format version of the Iceberg specification to use for new tables; either 1 or 2. Defaults to 2. Version 2 is required for row level deletes.

Number of times to retry a commit before failing. Defaults to the value of the iceberg.max-commit-retry catalog configuration property, which defaults to 4.

orc_bloom_filter_columns

Comma-separated list of columns to use for ORC bloom filter. It improves the performance of queries using Equality and IN predicates when reading ORC files. Requires ORC format. Defaults to [].

The ORC bloom filters false positive probability. Requires ORC format. Defaults to 0.05.

parquet_bloom_filter_columns

Comma-separated list of columns to use for Parquet bloom filter. It improves the performance of queries using Equality and IN predicates when reading Parquet files. Requires Parquet format. Defaults to [].

object_store_layout_enabled

Whether Iceberg’s object store file layout is enabled. Defaults to false.

Optionally specifies the file system location URI for the table’s data files

Additional properties added to an Iceberg table. The properties are not used by Trino, and are available in the $properties metadata table. The properties are not included in the output of SHOW CREATE TABLE statements.

The table definition below specifies to use Parquet files, partitioning by columns c1 and c2, and a file system location of /var/example_tables/test_table:

The table definition below specifies to use ORC files with compression_codec SNAPPY, bloom filter index by columns c1 and c2, fpp is 0.05, and a file system location of /var/example_tables/test_table:

The table definition below specifies to use Avro files, partitioning by child1 field in parent column:

The connector exposes several metadata tables for each Iceberg table. These metadata tables contain information about the internal structure of the Iceberg table. You can query each metadata table by appending the metadata table name to the table name:

The $properties table provides access to general information about Iceberg table configuration and any additional metadata key/value pairs that the table is tagged with.

You can retrieve the properties of the current snapshot of the Iceberg table test_table by using the following query:

The $history table provides a log of the metadata changes performed on the Iceberg table.

You can retrieve the changelog of the Iceberg table test_table by using the following query:

The output of the query has the following columns:

TIMESTAMP(3) WITH TIME ZONE

The time when the snapshot became active.

The identifier of the snapshot.

The identifier of the parent snapshot.

Whether or not this snapshot is an ancestor of the current snapshot.

The $metadata_log_entries table provides a view of metadata log entries of the Iceberg table.

You can retrieve the information about the metadata log entries of the Iceberg table test_table by using the following query:

The output of the query has the following columns:

TIMESTAMP(3) WITH TIME ZONE

The time when the metadata was created.

The location of the metadata file.

The identifier of the latest snapshot when the metadata was updated.

The identifier of the latest schema when the metadata was updated.

latest_sequence_number

The data sequence number of the metadata file.

The $snapshots table provides a detailed view of snapshots of the Iceberg table. A snapshot consists of one or more file manifests, and the complete table contents are represented by the union of all the data files in those manifests.

You can retrieve the information about the snapshots of the Iceberg table test_table by using the following query:

The output of the query has the following columns:

TIMESTAMP(3) WITH TIME ZONE

The time when the snapshot became active.

The identifier for the snapshot.

The identifier for the parent snapshot.

The type of operation performed on the Iceberg table. The supported operation types in Iceberg are:

append when new data is appended.

replace when files are removed and replaced without changing the data in the table.

overwrite when new data is added to overwrite existing data.

delete when data is deleted from the table and no new data is added.

The list of Avro manifest files containing the detailed information about the snapshot changes.

map(VARCHAR, VARCHAR)

A summary of the changes made from the previous snapshot to the current snapshot.

The $manifests and $all_manifests tables provide a detailed overview of the manifests corresponding to the snapshots performed in the log of the Iceberg table. The $manifests table contains data for the current snapshot. The $all_manifests table contains data for all snapshots.

You can retrieve the information about the manifests of the Iceberg table test_table by using the following query:

The output of the query has the following columns:

The manifest file location.

The manifest file length.

The identifier for the partition specification used to write the manifest file.

The identifier of the snapshot during which this manifest entry has been added.

added_data_files_count

The number of data files with status ADDED in the manifest file.

The total number of rows in all data files with status ADDED in the manifest file.

existing_data_files_count

The number of data files with status EXISTING in the manifest file.

The total number of rows in all data files with status EXISTING in the manifest file.

deleted_data_files_count

The number of data files with status DELETED in the manifest file.

The total number of rows in all data files with status DELETED in the manifest file.

ARRAY(row(contains_null BOOLEAN, contains_nan BOOLEAN, lower_bound VARCHAR, upper_bound VARCHAR))

Partition range metadata.

The $partitions table provides a detailed overview of the partitions of the Iceberg table.

You can retrieve the information about the partitions of the Iceberg table test_table by using the following query:

The output of the query has the following columns:

A row that contains the mapping of the partition column names to the partition column values.

The number of records in the partition.

The number of files mapped in the partition.

The size of all the files in the partition.

ROW(... ROW (min ..., max ... , null_count BIGINT, nan_count BIGINT))

Partition range metadata.

The $files table provides a detailed overview of the data files in current snapshot of the Iceberg table.

To retrieve the information about the data files of the Iceberg table test_table, use the following query:

The output of the query has the following columns:

Type of content stored in the file. The supported content types in Iceberg are:

The data file location.

The format of the data file.

Spec ID used to track the file containing a row.

A row that contains the mapping of the partition column names to the partition column values.

The number of entries contained in the data file.

Mapping between the Iceberg column ID and its corresponding size in the file.

Mapping between the Iceberg column ID and its corresponding count of entries in the file.

Mapping between the Iceberg column ID and its corresponding count of NULL values in the file.

Mapping between the Iceberg column ID and its corresponding count of non-numerical values in the file.

Mapping between the Iceberg column ID and its corresponding lower bound in the file.

Mapping between the Iceberg column ID and its corresponding upper bound in the file.

Metadata about the encryption key used to encrypt this file, if applicable.

List of recommended split locations.

The set of field IDs used for equality comparison in equality delete files.

ID representing sort order for this file.

File metrics in human-readable form.

The $entries and $all_entries tables provide the table’s manifest entries for both data and delete files. The $entries table contains data for the current snapshot. The $all_entries table contains data for all snapshots.

To retrieve the information about the entries of the Iceberg table test_table, use the following query:

Abbreviated sample output:

The metadata tables include the following columns:

Numeric status indication to track additions and deletions. Deletes are informational only and not used in scans:

The snapshot ID of the reference.

Data sequence number of the file. Inherited when null and status is 1.

File sequence number indicating when the file was added. Inherited when null and status is 1.

Metadata including file path, file format, file size and other information.

JSON-formatted file metrics such as column size, value count, and others.

The $refs table provides information about Iceberg references including branches and tags.

You can retrieve the references of the Iceberg table test_table by using the following query:

The output of the query has the following columns:

Name of the reference.

Type of the reference, either BRANCH or TAG.

The snapshot ID of the reference.

max_reference_age_in_ms

The maximum age of the reference before it could be expired.

min_snapshots_to_keep

For branch only, the minimum number of snapshots to keep in a branch.

max_snapshot_age_in_ms

For branch only, the max snapshot age allowed in a branch. Older snapshots in the branch will be expired.

In addition to the defined columns, the Iceberg connector automatically exposes path metadata as a hidden column in each table:

$partition: Partition path for this row

$path: Full file system path name of the file for this row

$file_modified_time: Timestamp of the last modification of the file for this row

You can use these columns in your SQL statements like any other column. This can be selected directly, or used in conditional statements. For example, you can inspect the file path for each record:

Retrieve all records that belong to a specific file using "$path" filter:

Retrieve all records that belong to a specific file using "$file_modified_time" filter:

The connector exposes metadata tables in the system schema.

The iceberg_tables table allows listing only Iceberg tables from a given catalog. The SHOW TABLES statement, information_schema.tables, and jdbc.tables will all return all tables that exist in the underlying metastore, even if the table cannot be handled in any way by the iceberg connector. This can happen if other connectors like Hive or Delta Lake, use the same metastore, catalog, and schema to store its tables.

The table includes following columns:

The name of the schema the table is in.

The name of the table.

The following query lists Iceberg tables from all schemas in the example catalog.

The Iceberg connector supports dropping a table by using the DROP TABLE syntax. When the command succeeds, both the data of the Iceberg table and also the information related to the table in the metastore service are removed. Dropping tables that have their data/metadata stored in a different location than the table’s corresponding base directory on the object store is not supported.

The Iceberg connector supports setting comments on the following objects:

materialized view columns

The COMMENT option is supported on both the table and the table columns for the CREATE TABLE operation.

The COMMENT option is supported for adding table columns through the ALTER TABLE operations.

The connector supports the command COMMENT for setting comments on existing entities.

Iceberg supports partitioning by specifying transforms over the table columns. A partition is created for each unique tuple value produced by the transforms. Identity transforms are simply the column name. Other transforms are:

A partition is created for each year. The partition value is the integer difference in years between ts and January 1 1970.

A partition is created for each month of each year. The partition value is the integer difference in months between ts and January 1 1970.

A partition is created for each day of each year. The partition value is the integer difference in days between ts and January 1 1970.

A partition is created hour of each day. The partition value is a timestamp with the minutes and seconds set to zero.

The data is hashed into the specified number of buckets. The partition value is an integer hash of x, with a value between 0 and nbuckets - 1 inclusive.

The partition value is the first nchars characters of s.

In this example, the table is partitioned by the month of order_date, a hash of account_number (with 10 buckets), and country:

The connector supports sorted files as a performance improvement. Data is sorted during writes within each file based on the specified array of one or more columns.

Sorting is particularly beneficial when the sorted columns show a high cardinality and are used as a filter for selective reads.

The sort order is configured with the sorted_by table property. Specify an array of one or more columns to use for sorting when creating the table. The following example configures the order_date column of the orders table in the customers schema in the example catalog:

You can explicitly configure sort directions or null ordering in the following way:

Sorting can be combined with partitioning on the same column. For example:

You can disable sorted writing with the session property sorted_writing_enabled set to false.

Iceberg supports a snapshot model of data, where table snapshots are identified by a snapshot ID.

The connector provides a system table exposing snapshot information for every Iceberg table. Snapshots are identified by BIGINT snapshot IDs. For example, you can find the snapshot IDs for the customer_orders table by running the following query:

The connector supports replacing an existing table, as an atomic operation. Atomic table replacement creates a new snapshot with the new table definition as part of the table history.

To replace a table, use CREATE OR REPLACE TABLE or CREATE OR REPLACE TABLE AS.

Earlier snapshots of the table can be queried through Time travel queries.

In the following example, a table example_table can be replaced by a completely new definition and data from the source table:

The connector offers the ability to query historical data. This allows you to query the table as it was when a previous snapshot of the table was taken, even if the data has since been modified or deleted.

The historical data of the table can be retrieved by specifying the snapshot identifier corresponding to the version of the table to be retrieved:

A different approach of retrieving historical data is to specify a point in time in the past, such as a day or week ago. The latest snapshot of the table taken before or at the specified timestamp in the query is internally used for providing the previous state of the table:

The connector allows to create a new snapshot through Iceberg’s replace table.

You can use a date to specify a point a time in the past for using a snapshot of a table in a query. Assuming that the session time zone is Europe/Vienna the following queries are equivalent:

Iceberg supports named references of snapshots via branches and tags. Time travel can be performed to branches and tags in the table.

Use the $snapshots metadata table to determine the latest snapshot ID of the table like in the following query:

The table procedure rollback_to_snapshot allows the caller to roll back the state of the table to a previous snapshot id:

The Iceberg connector supports setting NOT NULL constraints on the table columns.

The NOT NULL constraint can be set on the columns, while creating tables by using the CREATE TABLE syntax:

When trying to insert/update data in the table, the query fails if trying to set NULL value on a column having the NOT NULL constraint.

The Iceberg connector supports Materialized view management. In the underlying system, each materialized view consists of a view definition and an Iceberg storage table. The storage table name is stored as a materialized view property. The data is stored in that storage table.

You can use the Table properties to control the created storage table and therefore the layout and performance. For example, you can use the following clause with CREATE MATERIALIZED VIEW to use the ORC format for the data files and partition the storage per day using the column event_date:

By default, the storage table is created in the same schema as the materialized view definition. The storage_schema materialized view property can be used to specify the schema where the storage table is created.

Creating a materialized view does not automatically populate it with data. You must run REFRESH MATERIALIZED VIEW to populate data in the materialized view.

Updating the data in the materialized view can be achieved using the REFRESH MATERIALIZED VIEW command. This operation may perform either an incremental or a full refresh, depending on the complexity of the materialized view definition and the snapshot history of the source tables. For a full refresh, the operation deletes the data from the storage table, and inserts the data that is the result of executing the materialized view query into the existing table. For incremental refresh, the existing data is not deleted from the storage table and only the delta records are processed from the source tables and appended into the storage table as needed. In both cases, data is replaced or appended atomically, so users can continue to query the materialized view while it is being refreshed. Refreshing a materialized view also stores the snapshot-ids of all Iceberg tables that are part of the materialized view’s query in the materialized view metadata. When the materialized view is queried, the snapshot-ids are used to check if the data in the storage table is up to date.

Materialized views that use non-Iceberg tables in the query show the default behavior around grace periods. If all tables are Iceberg tables, the connector can determine if the data has not changed and continue to use the data from the storage tables, even after the grace period expired.

Dropping a materialized view with DROP MATERIALIZED VIEW removes the definition and the storage table.

The connector supports the table functions described in the following sections.

Allows reading row-level changes between two versions of an Iceberg table. The following query shows an example of displaying the changes of the t1 table in the default schema in the current catalog. All changes between the start and end snapshots are returned.

The function takes the following required parameters:

Name of the schema for which the function is called.

Name of the table for which the function is called.

The identifier of the exclusive starting snapshot.

The identifier of the inclusive end snapshot.

Use the $snapshots metadata table to determine the snapshot IDs of the table.

The function returns the columns present in the table, and the following values for each change:

The type of change that occurred. Possible values are insert and delete.

The identifier of the snapshot in which the change occurred.

Timestamp when the snapshot became active.

Order number of the change, useful for sorting the results.

Retrieve the snapshot identifiers of the changes performed on the table:

Select the changes performed in the previously-mentioned INSERT statements:

The connector includes a number of performance improvements, detailed in the following sections.

The Iceberg connector can collect column statistics using ANALYZE statement. This can be disabled using iceberg.extended-statistics.enabled catalog configuration property, or the corresponding extended_statistics_enabled session property.

If your queries are complex and include joining large data sets, running ANALYZE on tables may improve query performance by collecting statistical information about the data:

This query collects statistics for all columns.

On wide tables, collecting statistics for all columns can be expensive. It is also typically unnecessary - statistics are only useful on specific columns, like join keys, predicates, or grouping keys. You can specify a subset of columns to analyzed with the optional columns property:

This query collects statistics for columns col_1 and col_2.

Note that if statistics were previously collected for all columns, they must be dropped using the drop_extended_stats command before re-analyzing.

Trino offers the possibility to transparently redirect operations on an existing table to the appropriate catalog based on the format of the table and catalog configuration.

In the context of connectors which depend on a metastore service (for example, Hive connector, Iceberg connector and Delta Lake connector), the metastore (Hive metastore service, AWS Glue Data Catalog) can be used to accustom tables with different table formats. Therefore, a metastore database can hold a variety of tables with different table formats.

As a concrete example, let’s use the following simple scenario which makes use of table redirection:

The output of the EXPLAIN statement points out the actual catalog which is handling the SELECT query over the table example_table.

The table redirection functionality works also when using fully qualified names for the tables:

Trino offers table redirection support for the following operations:

Table read operations

Table write operations

Table management operations

Trino does not offer view redirection support.

The connector supports redirection from Iceberg tables to Hive tables with the iceberg.hive-catalog-name catalog configuration property.

The connector supports configuring and using file system caching.

The Iceberg connector supports caching metadata in coordinator memory. This metadata caching is enabled by default and can be disabled by setting the iceberg.metadata-cache.enabled configuration property to false. When fs.cache.enabled is set to true, metadata is cached on local disks using the file system caching implementation. If fs.cache.enabled is enabled, metadata caching in coordinator memory is deactivated.

Additionally, you can use the following catalog configuration properties:

The maximum duration to keep files in the cache prior to eviction. The minimum value of 0s means that caching is effectively turned off. Defaults to 1h.

fs.memory-cache.max-size

The maximum total data size of the cache. When raising this value, keep in mind that the coordinator memory is used. Defaults to 200MB.

fs.memory-cache.max-content-length

The maximum file size that can be cached. Defaults to 15MB.

**Examples:**

Example 1 (unknown):
```unknown
connector.name=iceberg
hive.metastore.uri=thrift://example.net:9083
fs.x.enabled=true
```

Example 2 (unknown):
```unknown
connector.name=iceberg
hive.metastore.uri=thrift://example.net:9083
fs.x.enabled=true
```

Example 3 (unknown):
```unknown
CREATE SCHEMA example.example_s3_schema
WITH (location = 's3://my-bucket/a/path/');
```

Example 4 (unknown):
```unknown
CREATE SCHEMA example.example_s3_schema
WITH (location = 's3://my-bucket/a/path/');
```

---

## MongoDB connector — Trino 478 Documentation

**URL:** https://trino.io/docs/current/connector/mongodb.html

**Contents:**
- MongoDB connector#
- Requirements#
- Configuration#
  - Multiple MongoDB clusters#
- Configuration properties#
  - mongodb.connection-url#
  - mongodb.schema-collection#
  - mongodb.case-insensitive-name-matching#
  - mongodb.min-connections-per-host#
  - mongodb.connections-per-host#

The mongodb connector allows the use of MongoDB collections as tables in Trino.

To connect to MongoDB, you need:

MongoDB 4.2 or higher.

Network access from the Trino coordinator and workers to MongoDB. Port 27017 is the default port.

Write access to the schema information collection in MongoDB.

To configure the MongoDB connector, create a catalog properties file etc/catalog/example.properties with the following contents, replacing the properties as appropriate:

You can have as many catalogs as you need, so if you have additional MongoDB clusters, simply add another properties file to etc/catalog with a different name, making sure it ends in .properties). For example, if you name the property file sales.properties, Trino will create a catalog named sales using the configured connector.

The following configuration properties are available:

mongodb.connection-url

The connection url that the driver uses to connect to a MongoDB deployment

mongodb.schema-collection

A collection which contains schema information

mongodb.case-insensitive-name-matching

Match database and collection names case insensitively

mongodb.min-connections-per-host

The minimum size of the connection pool per host

mongodb.connections-per-host

The maximum size of the connection pool per host

mongodb.max-wait-time

The maximum wait time

mongodb.max-connection-idle-time

The maximum idle time of a pooled connection

mongodb.connection-timeout

The socket connect timeout

mongodb.socket-timeout

Use TLS/SSL for connections to mongod/mongos

mongodb.tls.keystore-path

Path to the or JKS key store

mongodb.tls.truststore-path

Path to the or JKS trust store

mongodb.tls.keystore-password

Password for the key store

mongodb.tls.truststore-password

Password for the trust store

mongodb.read-preference

mongodb.write-concern

mongodb.required-replica-set

The required replica set name

mongodb.cursor-batch-size

The number of elements to return in a batch

mongodb.allow-local-scheduling

Assign MongoDB splits to a specific worker

mongodb.dynamic-filtering.wait-timeout

Duration to wait for completion of dynamic filters during split generation

A connection string containing the protocol, credential, and host info for use in connecting to your MongoDB deployment.

For example, the connection string may use the format mongodb://<user>:<pass>@<host>:<port>/?<options> or mongodb+srv://<user>:<pass>@<host>/?<options>, depending on the protocol used. The user/pass credentials must be for a user with write access to the schema information collection.

See the MongoDB Connection URI for more information.

This property is required; there is no default. A connection URL must be provided to connect to a MongoDB deployment.

As MongoDB is a document database, there is no fixed schema information in the system. So a special collection in each MongoDB database should define the schema of all tables. Please refer the Table definition section for the details.

At startup, the connector tries to guess the data type of fields based on the type mapping.

The initial guess can be incorrect for your specific collection. In that case, you need to modify it manually. Please refer the Table definition section for the details.

Creating new tables using CREATE TABLE and CREATE TABLE AS SELECT automatically create an entry for you.

This property is optional; the default is _schema.

Match database and collection names case insensitively.

This property is optional; the default is false.

The minimum number of connections per host for this MongoClient instance. Those connections are kept in a pool when idle, and the pool ensures over time that it contains at least this minimum number.

This property is optional; the default is 0.

The maximum number of connections allowed per host for this MongoClient instance. Those connections are kept in a pool when idle. Once the pool is exhausted, any operation requiring a connection blocks waiting for an available connection.

This property is optional; the default is 100.

The maximum wait time in milliseconds, that a thread may wait for a connection to become available. A value of 0 means that it does not wait. A negative value means to wait indefinitely for a connection to become available.

This property is optional; the default is 120000.

The maximum idle time of a pooled connection in milliseconds. A value of 0 indicates no limit to the idle time. A pooled connection that has exceeded its idle time will be closed and replaced when necessary by a new connection.

This property is optional; the default is 0.

The connection timeout in milliseconds. A value of 0 means no timeout. It is used solely when establishing a new connection.

This property is optional; the default is 10000.

The socket timeout in milliseconds. It is used for I/O socket read and write operations.

This property is optional; the default is 0 and means no timeout.

This flag enables TLS connections to MongoDB servers.

This property is optional; the default is false.

The path to the PEM or JKS key store.

This property is optional.

The path to PEM or JKS trust store.

This property is optional.

The key password for the key store specified by mongodb.tls.keystore-path.

This property is optional.

The key password for the trust store specified by mongodb.tls.truststore-path.

This property is optional.

The read preference to use for queries, map-reduce, aggregation, and count. The available values are PRIMARY, PRIMARY_PREFERRED, SECONDARY, SECONDARY_PREFERRED and NEAREST.

This property is optional; the default is PRIMARY.

The write concern to use. The available values are ACKNOWLEDGED, JOURNALED, MAJORITY and UNACKNOWLEDGED.

This property is optional; the default is ACKNOWLEDGED.

The required replica set name. With this option set, the MongoClient instance performs the following actions:

This property is optional; no default value.

Limits the number of elements returned in one batch. A cursor typically fetches a batch of result objects and stores them locally. If batchSize is 0, Driver’s default are used. If batchSize is positive, it represents the size of each batch of objects retrieved. It can be adjusted to optimize performance and limit data transfer. If batchSize is negative, it limits the number of objects returned, that fit within the max batch size limit (usually 4MB), and the cursor is closed. For example if batchSize is -10, then the server returns a maximum of 10 documents, and as many as can fit in 4MB, then closes the cursor.

Do not use a batch size of 1.

This property is optional; the default is 0.

Set the value of this property to true if Trino and MongoDB share the same cluster, and specific MongoDB splits should be processed on the same worker and MongoDB node. Note that a shared deployment is not recommended, and enabling this property can lead to resource contention.

This property is optional, and defaults to false.

Duration to wait for completion of dynamic filters during split generation.

This property is optional; the default is 5s.

MongoDB maintains table definitions on the special collection where mongodb.schema-collection configuration value specifies.

The plugin cannot detect that a collection has been deleted. You must delete the entry by executing db.getCollection("_schema").remove( { table: deleted_table_name }) in the MongoDB Shell. You can also drop a collection in Trino by running DROP TABLE table_name.

A schema collection consists of a MongoDB document for a table.

The connector quotes the fields for a row type when auto-generating the schema; however, the auto-generated schema must be corrected manually in the collection to match the information in the tables.

Manually altered fields must be explicitly quoted, for example, row("UpperCase" varchar).

A list of field definitions. Each field definition creates a new column in the Trino table.

Each field definition:

Name of the column in the Trino table.

Trino type of the column.

Hides the column from DESCRIBE <table name> and SELECT *. Defaults to false.

There is no limit on field descriptions for either key or message.

MongoDB collection has the special field _id. The connector tries to follow the same rules for this special field, so there will be hidden field _id.

You can render the _id field to readable values with a cast to VARCHAR:

The first four bytes of each ObjectId represent an embedded timestamp of its creation time. Trino provides a couple of functions to take advantage of this MongoDB feature.

Extracts the TIMESTAMP WITH TIME ZONE from a given ObjectId:

Creates an ObjectId from a TIMESTAMP WITH TIME ZONE:

In MongoDB, you can filter all the documents created after 2021-08-07 17:51:36 with a query like this:

In Trino, the same can be achieved with this query:

The connector supports Fault-tolerant execution of query processing. Read and write operations are both supported with any retry policy.

Because Trino and MongoDB each support types that the other does not, this connector modifies some types when reading or writing data. Data types may not map the same way in both directions between Trino and the data source. Refer to the following sections for type mapping in each direction.

The connector maps MongoDB types to the corresponding Trino types following this table:

Map to ROW if the element type is not unique.

No other types are supported.

The connector maps Trino types to the corresponding MongoDB types following this table:

No other types are supported.

The connector provides read and write access to data and metadata in MongoDB. In addition to the globally available and read operation statements, the connector supports the following features:

The connector supports ALTER TABLE RENAME TO, ALTER TABLE ADD COLUMN and ALTER TABLE DROP COLUMN operations. Other uses of ALTER TABLE are not supported.

The connector provides specific table functions to access MongoDB.

The query function allows you to query the underlying MongoDB directly. It requires syntax native to MongoDB, because the full query is pushed down and processed by MongoDB. This can be useful for accessing native features which are not available in Trino or for improving query performance in situations where running a query natively may be faster.

For example, get all rows where regionkey field is 0:

**Examples:**

Example 1 (unknown):
```unknown
connector.name=mongodb
mongodb.connection-url=mongodb://user:[email protected]:27017/
```

Example 2 (unknown):
```unknown
connector.name=mongodb
mongodb.connection-url=mongodb://user:[email protected]:27017/
```

Example 3 (unknown):
```unknown
#. Connect in replica set mode, and discover all members of the set based on the given servers
#. Make sure that the set name reported by all members matches the required set name.
#. Refuse to service any requests, if authenticated user is not part of a replica set with the required name.
```

Example 4 (unknown):
```unknown
#. Connect in replica set mode, and discover all members of the set based on the given servers
#. Make sure that the set name reported by all members matches the required set name.
#. Refuse to service any requests, if authenticated user is not part of a replica set with the required name.
```

---

## MySQL event listener — Trino 478 Documentation

**URL:** https://trino.io/docs/current/admin/event-listeners-mysql.html

**Contents:**
- MySQL event listener#
- Rationale#
- Requirements#
- Configuration#
  - Configuration properties#

The MySQL event listener plugin allows streaming of query events to an external MySQL database. The query history in the database can then be accessed directly in MySQL or via Trino in a catalog using the MySQL connector.

This event listener is a first step to store the query history of your Trino cluster. The query events can provide CPU and memory usage metrics, what data is being accessed with resolution down to specific columns, and metadata about the query processing.

Running the capture system separate from Trino reduces the performance impact and avoids downtime for non-client-facing changes.

You need to perform the following steps:

Create a MySQL database.

Determine the JDBC connection URL for the database.

Ensure network access from the Trino coordinator to MySQL is available. Port 3306 is the default port.

To configure the MySQL event listener plugin, create an event listener properties file in etc named mysql-event-listener.properties with the following contents as an example:

The mysql-event-listener.db.url defines the connection to a MySQL database available at the domain example.net on port 3306. You can pass further parameters to the MySQL JDBC driver. The supported parameters for the URL are documented in the MySQL Developer Guide.

And set event-listener.config-files to etc/mysql-event-listener.properties in Config properties:

If another event listener is already configured, add the new value etc/mysql-event-listener.properties with a separating comma.

After this configuration and successful start of the Trino cluster, the table trino_queries is created in the MySQL database. From then on, any query processing event is captured by the event listener and a new row is inserted into the table. The table includes many columns, such as query identifier, query string, user, catalog, and others with information about the query processing.

mysql-event-listener.db.url

JDBC connection URL to the database including credentials

mysql-event-listener.terminate-on-initialization-failure

MySQL event listener initialization can fail if the database is unavailable. This boolean switch controls whether to throw an exception in such cases. Defaults to true.

**Examples:**

Example 1 (unknown):
```unknown
event-listener.name=mysql
mysql-event-listener.db.url=jdbc:mysql://example.net:3306
```

Example 2 (unknown):
```unknown
event-listener.name=mysql
mysql-event-listener.db.url=jdbc:mysql://example.net:3306
```

Example 3 (unknown):
```unknown
event-listener.config-files=etc/mysql-event-listener.properties
```

Example 4 (unknown):
```unknown
event-listener.config-files=etc/mysql-event-listener.properties
```

---

## BigQuery connector — Trino 478 Documentation

**URL:** https://trino.io/docs/current/connector/bigquery.html

**Contents:**
- BigQuery connector#
- BigQuery Storage API#
- Requirements#
- Configuration#
  - Multiple GCP projects#
  - Billing and data projects#
  - Arrow serialization support#
  - Reading from views#
  - Configuration properties#
  - Fault-tolerant execution support#

The BigQuery connector allows querying the data stored in BigQuery. This can be used to join data between different systems like BigQuery and Hive. The connector uses the BigQuery Storage API to read the data from the tables.

The Storage API streams data in parallel directly from BigQuery via gRPC without using Google Cloud Storage as an intermediary. It has a number of advantages over using the previous export-based read flow that should generally lead to better read performance:

It does not leave any temporary files in Google Cloud Storage. Rows are read directly from BigQuery servers using an Avro wire format.

The new API allows column filtering to only read the data you are interested in. Backed by a columnar datastore, it can efficiently stream data without reading all columns.

The API rebalances records between readers until they all complete. This means that all Map phases will finish nearly concurrently. See this blog article on how dynamic sharding is similarly used in Google Cloud Dataflow.

To connect to BigQuery, you need:

To enable the BigQuery Storage Read API.

Network access from your Trino coordinator and workers to the Google Cloud API service endpoint. This endpoint uses HTTPS, or port 443.

To configure BigQuery so that the Trino coordinator and workers have permissions in BigQuery.

To set up authentication. Your authentication options differ depending on whether you are using Dataproc/Google Compute Engine (GCE) or not.

On Dataproc/GCE the authentication is done from the machine’s role.

Outside Dataproc/GCE you have 3 options:

Use a service account JSON key and GOOGLE_APPLICATION_CREDENTIALS as described in the Google Cloud authentication getting started guide.

Set bigquery.credentials-key in the catalog properties file. It should contain the contents of the JSON file, encoded using base64.

Set bigquery.credentials-file in the catalog properties file. It should point to the location of the JSON file.

To configure the BigQuery connector, create a catalog properties file in etc/catalog named example.properties, to mount the BigQuery connector as the example catalog. Create the file with the following contents, replacing the connection properties as appropriate for your setup:

The BigQuery connector can only access a single GCP project. If you have data in multiple GCP projects, you must create several catalogs, each pointing to a different GCP project. For example, if you have two GCP projects, one for the sales and one for analytics, you can create two properties files in etc/catalog named sales.properties and analytics.properties, both having connector.name=bigquery but with different project-id. This will create the two catalogs, sales and analytics respectively.

The BigQuery connector determines the project ID to use based on the configuration settings. This behavior provides users with flexibility in selecting both the project to query and the project to bill for BigQuery operations. The following table explains how project IDs are resolved in different scenarios:

Configured properties

Only bigquery.credentials-key

The project ID from the credentials key is used for billing.

The project ID from the credentials key is used for querying data.

bigquery.credentials-key and bigquery.project-id

The project ID from the credentials key is used for billing.

bigquery.project-id is used for querying data.

bigquery.credentials-key and bigquery.parent-project-id

bigquery.parent-project-id is used for billing.

The project ID from the credentials key is used for querying data.

bigquery.credentials-key and bigquery.parent-project-id and bigquery.project-id

bigquery.parent-project-id is used for billing.

bigquery.project-id is used for querying data.

This is a feature which introduces support for using Apache Arrow as the serialization format when reading from BigQuery. Add the following required, additional JVM argument to the JVM config:

The connector has a preliminary support for reading from BigQuery views. Please note there are a few caveats:

Reading from views is disabled by default. In order to enable it, set the bigquery.views-enabled configuration property to true.

BigQuery views are not materialized by default, which means that the connector needs to materialize them before it can read them. This process affects the read performance.

The materialization process can also incur additional costs to your BigQuery bill.

By default, the materialized views are created in the same project and dataset. Those can be configured by the optional bigquery.view-materialization-project and bigquery.view-materialization-dataset properties, respectively. The service account must have write permission to the project and the dataset in order to materialize the view.

The project ID of the Google Cloud account used to store the data, see also Billing and data projects

Taken from the service account or from bigquery.parent-project-id, if set

bigquery.parent-project-id

The project ID Google Cloud Project to bill for the export, see also Billing and data projects

Taken from the service account

bigquery.views-enabled

Enables the connector to read from views and not only tables. Read this section before enabling this feature.

bigquery.view-expire-duration

Expire duration for the materialized view.

bigquery.view-materialization-project

The project where the materialized view is going to be created.

bigquery.view-materialization-dataset

The dataset where the materialized view is going to be created.

bigquery.skip-view-materialization

Use REST API to access views instead of Storage API. BigQuery BIGNUMERIC and TIMESTAMP types are unsupported.

bigquery.view-materialization-with-filter

Use filter conditions when materializing views.

bigquery.views-cache-ttl

Duration for which the materialization of a view will be cached and reused. Set to 0ms to disable the cache.

bigquery.metadata.cache-ttl

Duration for which metadata retrieved from BigQuery is cached and reused. Set to 0ms to disable the cache.

bigquery.max-read-rows-retries

The number of retries in case of retryable server issues.

bigquery.credentials-key

The base64 encoded credentials key.

None. See the requirements section

bigquery.credentials-file

The path to the JSON credentials file.

None. See the requirements section

bigquery.case-insensitive-name-matching

Match dataset and table names case-insensitively.

bigquery.case-insensitive-name-matching.cache-ttl

Duration for which case insensitive schema and table names are cached. Set to 0ms to disable the cache.

bigquery.query-results-cache.enabled

Enable query results cache.

bigquery.arrow-serialization.enabled

Enable using Apache Arrow serialization when reading data from BigQuery. Read this section before using this feature.

bigquery.arrow-serialization.max-allocation

The maximum amount of memory the Apache Arrow buffer allocator is allowed to use.

bigquery.max-parallelism

The max number of partitions to split the data into. Reduce this number if the default parallelism (number of workers x 3) is too high.

bigquery.channel-pool.initial-size

The initial size of the connection pool, also known as a channel pool, used for gRPC communication.

bigquery.channel-pool.min-size

The minimum number of connections in the connection pool, also known as a channel pool, used for gRPC communication.

bigquery.channel-pool.max-size

The maximum number of connections in the connection pool, also known as a channel pool, used for gRPC communication.

bigquery.channel-pool.min-rpc-per-channel

Threshold to start scaling down the channel pool. When the average of outstanding RPCs in a single minute drop below this threshold, channels are removed from the pool.

bigquery.channel-pool.max-rpc-per-channel

Threshold to start scaling up the channel pool. When the average of outstanding RPCs in a single minute surpass this threshold, channels are added to the pool.

The maximum number of retry attempts to perform for the RPC calls. If this value is set to 0, the value from bigquery.rpc-timeout is used. Retry is deactivated when both bigquery.rpc-retries and bigquery.rpc-timeout are 0. If this value is positive, and the number of attempts exceeds bigquery.rpc-retries limit, retries stop even if the total retry time is still lower than bigquery.rpc-timeout.

Timeout duration on when the retries for the RPC call should be given up completely. The higher the timeout, the more retries can be attempted. If this value is 0s, then bigquery.rpc-retries is used to determine retries. Retry is deactivated when bigquery.rpc-retries and bigquery.rpc-timeout are both 0. If this value is positive, and the retry duration has reached the timeout value, retries stop even if the number of attempts is lower than the bigquery.rpc-retries value.

bigquery.rpc-retry-delay

The delay duration before the first retry attempt for RPC calls.

bigquery.rpc-retry-delay-multiplier

Controls the change in delay before the next retry. The retry delay of the previous call is multiplied by the bigquery.rpc-retry-delay-multiplier to calculate the retry delay for the next RPC call.

bigquery.rpc-proxy.enabled

Use a proxy for communication with BigQuery.

bigquery.rpc-proxy.uri

Proxy URI to use if connecting through a proxy.

bigquery.rpc-proxy.username

Proxy username to use if connecting through a proxy.

bigquery.rpc-proxy.password

Proxy password to use if connecting through a proxy.

bigquery.rpc-proxy.keystore-path

Keystore containing client certificates to present to proxy if connecting through a proxy. Only required if proxy uses mutual TLS.

bigquery.rpc-proxy.keystore-password

Password of the keystore specified by bigquery.rpc-proxy.keystore-path.

bigquery.rpc-proxy.truststore-path

Truststore containing certificates of the proxy server if connecting through a proxy.

bigquery.rpc-proxy.truststore-password

Password of the truststore specified by bigquery.rpc-proxy.truststore-path.

The connector supports Fault-tolerant execution of query processing. Read and write operations are both supported with any retry policy.

Because Trino and BigQuery each support types that the other does not, this connector modifies some types when reading or writing data. Data types may not map the same way in both directions between Trino and the data source. Refer to the following sections for type mapping in each direction.

The connector maps BigQuery types to the corresponding Trino types according to the following table:

INT, SMALLINT, INTEGER, BIGINT, TINYINT, and BYTEINT are aliases for INT64 in BigQuery.

The default precision and scale of NUMERIC is (38, 9).

Precision > 38 is not supported. The default precision and scale of BIGNUMERIC is (77, 38).

TIMESTAMP(6) WITH TIME ZONE

In Well-known text (WKT) format

No other types are supported.

The connector maps Trino types to the corresponding BigQuery types according to the following table:

INT, SMALLINT, INTEGER, BIGINT, TINYINT, and BYTEINT are aliases for INT64 in BigQuery.

The default precision and scale of NUMERIC is (38, 9).

No other types are supported.

For each Trino table which maps to BigQuery view there exists a system table which exposes BigQuery view definition. Given a BigQuery view example_view you can send query SELECT * example_view$view_definition to see the SQL which defines view in BigQuery.

In addition to the defined columns, the BigQuery connector exposes partition information in a number of hidden columns:

$partition_date: Equivalent to _PARTITIONDATE pseudo-column in BigQuery

$partition_time: Equivalent to _PARTITIONTIME pseudo-column in BigQuery

You can use these columns in your SQL statements like any other column. They can be selected directly, or used in conditional statements. For example, you can inspect the partition date and time for each record:

Retrieve all records stored in the partition _PARTITIONDATE = '2022-04-07':

Two special partitions __NULL__ and __UNPARTITIONED__ are not supported.

The connector provides read and write access to data and metadata in the BigQuery database. In addition to the globally available and read operation statements, the connector supports the following features:

If a WHERE clause is specified, the DELETE operation only works if the predicate in the clause can be fully pushed down to the data source.

The connector provides support to query multiple tables using a concise wildcard table notation.

The execute procedure allows you to execute a query in the underlying data source directly. The query must use supported syntax of the connected data source. Use the procedure to access features which are not available in Trino or to execute queries that return no result set and therefore can not be used with the query or raw_query pass-through table function. Typical use cases are statements that create or alter objects, and require native feature such as constraints, default values, automatic identifier creation, or indexes. Queries can also invoke statements that insert, update, or delete data, and do not return any data as a result.

The query text is not parsed by Trino, only passed through, and therefore only subject to any security or access control of the underlying data source.

The following example sets the current database to the example_schema of the example catalog. Then it calls the procedure in that schema to drop the default value from your_column on your_table table using the standard SQL syntax in the parameter value assigned for query:

Verify that the specific database supports this syntax, and adapt as necessary based on the documentation for the specific connected database and database version.

The connector provides specific table functions to access BigQuery.

The query function allows you to query the underlying BigQuery directly. It requires syntax native to BigQuery, because the full query is pushed down and processed by BigQuery. This can be useful for accessing native features which are not available in Trino or for improving query performance in situations where running a query natively may be faster.

The native query passed to the underlying data source is required to return a table as a result set. Only the data source performs validation or security checks for these queries using its own configuration. Trino does not perform these tasks. Only use passthrough queries to read data.

For example, query the example catalog and group and concatenate all employee IDs by manager ID:

The query engine does not preserve the order of the results of this function. If the passed query contains an ORDER BY clause, the function result may not be ordered as expected.

The connector includes a number of performance improvements, detailed in the following sections.

The connector supports pushdown for a number of operations:

Limit pushdown for access to tables and other objects when using the REST API to reduce CPU consumption in BigQuery and performance overall. Pushdown is not supported by the Storage API, used for the more common Trino-managed tables, and therefore not used for access with it.

See the BigQuery pricing documentation.

**Examples:**

Example 1 (unknown):
```unknown
connector.name=bigquery
bigquery.project-id=<your Google Cloud Platform project id>
```

Example 2 (unknown):
```unknown
connector.name=bigquery
bigquery.project-id=<your Google Cloud Platform project id>
```

Example 3 (unknown):
```unknown
--add-opens=java.base/java.nio=ALL-UNNAMED
--sun-misc-unsafe-memory-access=allow
```

Example 4 (unknown):
```unknown
--add-opens=java.base/java.nio=ALL-UNNAMED
--sun-misc-unsafe-memory-access=allow
```

---

## Google Sheets connector — Trino 478 Documentation

**URL:** https://trino.io/docs/current/connector/googlesheets.html

**Contents:**
- Google Sheets connector#
- Configuration#
- Configuration properties#
- Credentials#
- Metadata sheet#
- Querying sheets#
- Writing to sheets#
- API usage limits#
- Type mapping#
  - Google Sheets type to Trino type mapping#

The Google Sheets connector allows reading and writing Google Sheets spreadsheets as tables in Trino.

Create etc/catalog/example.properties to mount the Google Sheets connector as the example catalog, with the following contents:

The following configuration properties are available:

gsheets.credentials-path

Path to the Google API JSON key file

gsheets.credentials-key

The base64 encoded credentials key

gsheets.delegated-user-email

User email to impersonate the service account with domain-wide delegation enabled

gsheets.metadata-sheet-id

Sheet ID of the spreadsheet, that contains the table mapping

gsheets.max-data-cache-size

Maximum number of spreadsheets to cache, defaults to 1000

gsheets.data-cache-ttl

How long to cache spreadsheet data or metadata, defaults to 5m

gsheets.connection-timeout

Timeout when connection to Google Sheets API, defaults to 20s

Timeout when reading from Google Sheets API, defaults to 20s

gsheets.write-timeout

Timeout when writing to Google Sheets API, defaults to 20s

The connector requires credentials in order to access the Google Sheets API.

Open the Google Sheets API page and click the Enable button. This takes you to the API manager page.

Select a project using the drop-down menu at the top of the page. Create a new project, if you do not already have one.

Choose Credentials in the left panel.

Click Manage service accounts, then create a service account for the connector. On the Create key step, create and download a key in JSON format.

The key file needs to be available on the Trino coordinator and workers. Set the gsheets.credentials-path configuration property to point to this file. The exact name of the file does not matter – it can be named anything.

Alternatively, set the gsheets.credentials-key configuration property. It should contain the contents of the JSON file, encoded using base64.

Optionally, set the gsheets.delegated-user-email property to impersonate a user. This allows you to share Google Sheets with this email instead of the service account.

The metadata sheet is used to map table names to sheet IDs. Create a new metadata sheet. The first row must be a header row containing the following columns in this order:

See this example sheet as a reference.

The metadata sheet must be shared with the service account user, the one for which the key credentials file was created. Click the Share button to share the sheet with the email address of the service account.

Set the gsheets.metadata-sheet-id configuration property to the ID of this sheet.

The service account user must have access to the sheet in order for Trino to query it. Click the Share button to share the sheet with the email address of the service account.

The sheet needs to be mapped to a Trino table name. Specify a table name (column A) and the sheet ID (column B) in the metadata sheet. To refer to a specific range in the sheet, add the range after the sheet ID, separated with #. If a range is not provided, the connector loads only 10,000 rows by default from the first tab in the sheet.

The first row of the provided sheet range is used as the header and will determine the column names of the Trino table. For more details on sheet range syntax see the google sheets docs.

The same way sheets can be queried, they can also be written by appending data to existing sheets. In this case the service account user must also have Editor permissions on the sheet.

After data is written to a table, the table contents are removed from the cache described in API usage limits. If the table is accessed immediately after the write, querying the Google Sheets API may not reflect the change yet. In that case the old version of the table is read and cached for the configured amount of time, and it might take some time for the written changes to propagate properly.

Keep in mind that the Google Sheets API has usage limits, that limit the speed of inserting data. If you run into timeouts you can increase timeout times to avoid 503: The service is currently unavailable errors.

The Google Sheets API has usage limits, that may impact the usage of this connector. Increasing the cache duration and/or size may prevent the limit from being reached. Running queries on the information_schema.columns table without a schema and table name filter may lead to hitting the limit, as this requires fetching the sheet data for every table, unless it is already cached.

Because Trino and Google Sheets each support types that the other does not, this connector modifies some types when reading data.

The connector maps Google Sheets types to the corresponding Trino types following this table:

No other types are supported.

In addition to the globally available and read operation statements, this connector supports the following features:

The connector provides specific Table functions to access Google Sheets.

The sheet function allows you to query a Google Sheet directly without specifying it as a named table in the metadata sheet.

For example, for a catalog named ‘example’:

A sheet range or named range can be provided as an optional range argument. The default sheet range is $1:$10000 if one is not provided:

**Examples:**

Example 1 (unknown):
```unknown
connector.name=gsheets
gsheets.credentials-path=/path/to/google-sheets-credentials.json
gsheets.metadata-sheet-id=exampleId
```

Example 2 (unknown):
```unknown
connector.name=gsheets
gsheets.credentials-path=/path/to/google-sheets-credentials.json
gsheets.metadata-sheet-id=exampleId
```

Example 3 (javascript):
```javascript
SELECT *
FROM
  TABLE(example.system.sheet(
      id => 'googleSheetIdHere'));
```

Example 4 (javascript):
```javascript
SELECT *
FROM
  TABLE(example.system.sheet(
      id => 'googleSheetIdHere'));
```

---

## Kafka connector tutorial — Trino 478 Documentation

**URL:** https://trino.io/docs/current/connector/kafka-tutorial.html

**Contents:**
- Kafka connector tutorial#
- Introduction#
- Installation#
  - Step 1: Install Apache Kafka#
  - Step 2: Load data#
  - Step 3: Make the Kafka topics known to Trino#
  - Step 4: Basic data querying#
  - Step 5: Add a topic description file#
  - Step 6: Map all the values from the topic message onto columns#
  - Step 7: Use live data#

The Kafka connector for Trino allows access to live topic data from Apache Kafka using Trino. This tutorial shows how to set up topics, and how to create the topic description files that back Trino tables.

This tutorial assumes familiarity with Trino and a working local Trino installation (see Deploying Trino). It focuses on setting up Apache Kafka and integrating it with Trino.

Download and extract Apache Kafka.

This tutorial was tested with Apache Kafka 0.8.1. It should work with any 0.8.x version of Apache Kafka.

Start ZooKeeper and the Kafka server:

This starts Zookeeper on port 2181 and Kafka on port 9092.

Download the tpch-kafka loader from Maven Central:

Now run the kafka-tpch program to preload a number of topics with tpch data:

Kafka now has a number of topics that are preloaded with data to query.

In your Trino installation, add a catalog properties file etc/catalog/kafka.properties for the Kafka connector. This file lists the Kafka nodes and topics:

Because the Kafka tables all have the tpch. prefix in the configuration, the tables are in the tpch schema. The connector is mounted into the kafka catalog, because the properties file is named kafka.properties.

List the tables to verify that things are working:

Kafka data is unstructured, and it has no metadata to describe the format of the messages. Without further configuration, the Kafka connector can access the data, and map it in raw form. However there are no actual columns besides the built-in ones:

The data from Kafka can be queried using Trino, but it is not yet in actual table shape. The raw data is available through the _message and _key columns, but it is not decoded into columns. As the sample data is in JSON format, the JSON functions and operators built into Trino can be used to slice the data.

The Kafka connector supports topic description files to turn raw data into table format. These files are located in the etc/kafka folder in the Trino installation and must end with .json. It is recommended that the file name matches the table name, but this is not necessary.

Add the following file as etc/kafka/tpch.customer.json and restart Trino:

The customer table now has an additional column: kafka_key.

The topic definition file maps the internal Kafka key, which is a raw long in eight bytes, onto a Trino BIGINT column.

Update the etc/kafka/tpch.customer.json file to add fields for the message, and restart Trino. As the fields in the message are JSON, it uses the JSON data format. This is an example, where different data formats are used for the key and the message.

Now for all the fields in the JSON of the message, columns are defined and the sum query from earlier can operate on the account_balance column directly:

Now all the fields from the customer topic messages are available as Trino table columns.

Trino can query live data in Kafka as it arrives. To simulate a live feed of data, this tutorial sets up a feed of live tweets into Kafka.

Download the twistr tool

Create a developer account at https://dev.twitter.com/ and set up an access and consumer token.

Create a twistr.properties file and put the access and consumer key and secrets into it:

Add the tweets table to the etc/catalog/kafka.properties file:

Add a topic definition file for the Twitter feed as etc/kafka/tweets.json:

As this table does not have an explicit schema name, it is placed into the default schema.

Start the twistr tool:

twistr connects to the Twitter API and feeds the “sample tweet” feed into a Kafka topic called twitter_feed.

Now run queries against live data:

There is now a live feed into Kafka, which can be queried using Trino.

The tweets feed, that was set up in the last step, contains a timestamp in RFC 2822 format as created_at attribute in each tweet.

The topic definition file for the tweets table contains a mapping onto a timestamp using the rfc2822 converter:

This allows the raw data to be mapped onto a Trino TIMESTAMP column:

The Kafka connector contains converters for ISO 8601, RFC 2822 text formats and for number-based timestamps using seconds or milliseconds since the epoch. There is also a generic, text-based formatter, which uses Joda-Time format strings to parse text columns.

**Examples:**

Example 1 (unknown):
```unknown
$ bin/zookeeper-server-start.sh config/zookeeper.properties
[2013-04-22 15:01:37,495] INFO Reading configuration from: config/zookeeper.properties (org.apache.zookeeper.server.quorum.QuorumPeerConfig)
...
```

Example 2 (unknown):
```unknown
$ bin/zookeeper-server-start.sh config/zookeeper.properties
[2013-04-22 15:01:37,495] INFO Reading configuration from: config/zookeeper.properties (org.apache.zookeeper.server.quorum.QuorumPeerConfig)
...
```

Example 3 (unknown):
```unknown
$ bin/kafka-server-start.sh config/server.properties
[2013-04-22 15:01:47,028] INFO Verifying properties (kafka.utils.VerifiableProperties)
[2013-04-22 15:01:47,051] INFO Property socket.send.buffer.bytes is overridden to 1048576 (kafka.utils.VerifiableProperties)
...
```

Example 4 (unknown):
```unknown
$ bin/kafka-server-start.sh config/server.properties
[2013-04-22 15:01:47,028] INFO Verifying properties (kafka.utils.VerifiableProperties)
[2013-04-22 15:01:47,051] INFO Property socket.send.buffer.bytes is overridden to 1048576 (kafka.utils.VerifiableProperties)
...
```

---

## SQL Server connector — Trino 478 Documentation

**URL:** https://trino.io/docs/current/connector/sqlserver.html

**Contents:**
- SQL Server connector#
- Requirements#
- Configuration#
  - Connection security#
  - Data source authentication#
  - Multiple SQL Server databases or servers#
  - General configuration properties#
  - Appending query metadata#
  - Domain compaction threshold#
  - Specific configuration properties#

The SQL Server connector allows querying and creating tables in an external Microsoft SQL Server database. This can be used to join data between different systems like SQL Server and Hive, or between two different SQL Server instances.

To connect to SQL Server, you need:

SQL Server 2019 or higher, or Azure SQL Database.

Network access from the Trino coordinator and workers to SQL Server. Port 1433 is the default port.

The connector can query a single database on a given SQL Server instance. Create a catalog properties file that specifies the SQL server connector by setting the connector.name to sqlserver.

For example, to access a database as example, create the file etc/catalog/example.properties. Replace the connection properties as appropriate for your setup:

The connection-url defines the connection information and parameters to pass to the SQL Server JDBC driver. The supported parameters for the URL are available in the SQL Server JDBC driver documentation.

The connection-user and connection-password are typically required and determine the user credentials for the connection, often a service user. You can use secrets to avoid actual values in the catalog properties files.

The JDBC driver, and therefore the connector, automatically use Transport Layer Security (TLS) encryption and certificate validation. This requires a suitable TLS certificate configured on your SQL Server database host.

If you do not have the necessary configuration established, you can disable encryption in the connection string with the encrypt property:

Further parameters like trustServerCertificate, hostNameInCertificate, trustStore, and trustStorePassword are details in the TLS section of SQL Server JDBC driver documentation.

The connector can provide credentials for the data source connection in multiple ways:

inline, in the connector configuration file

in a separate properties file

as extra credentials set when connecting to Trino

You can use secrets to avoid storing sensitive values in the catalog properties files.

The following table describes configuration properties for connection credentials:

credential-provider.type

Type of the credential provider. Must be one of INLINE, FILE, or KEYSTORE; defaults to INLINE.

Connection user name.

Name of the extra credentials property, whose value to use as the user name. See extraCredentials in Parameter reference.

password-credential-name

Name of the extra credentials property, whose value to use as the password.

connection-credential-file

Location of the properties file where credentials are present. It must contain the connection-user and connection-password properties.

The location of the Java Keystore file, from which to read credentials.

File format of the keystore file, for example JKS or PEM.

Password for the key store.

keystore-user-credential-name

Name of the key store entity to use as the user name.

keystore-user-credential-password

Password for the user name key store entity.

keystore-password-credential-name

Name of the key store entity to use as the password.

keystore-password-credential-password

Password for the password key store entity.

The SQL Server connector can only access a single SQL Server database within a single catalog. Thus, if you have multiple SQL Server databases, or want to connect to multiple SQL Server instances, you must configure multiple instances of the SQL Server connector.

To add another catalog, simply add another properties file to etc/catalog with a different name, making sure it ends in .properties. For example, if you name the property file sales.properties, Trino creates a catalog named sales using the configured connector.

The following table describes general catalog configuration properties for the connector:

case-insensitive-name-matching

Support case insensitive schema and table names. Defaults to false.

case-insensitive-name-matching.cache-ttl

Duration for which case insensitive schema and table names are cached. Defaults to 1m.

case-insensitive-name-matching.config-file

Path to a name mapping configuration file in JSON format that allows Trino to disambiguate between schemas and tables with similar names in different cases. Defaults to null.

case-insensitive-name-matching.config-file.refresh-period

Frequency with which Trino checks the name matching configuration file for changes. The duration value defaults to 0s (refresh disabled).

Duration for which metadata, including table and column statistics, is cached. Defaults to 0s (caching disabled).

metadata.cache-missing

Cache the fact that metadata, including table and column statistics, is not available. Defaults to false.

metadata.schemas.cache-ttl

Duration for which schema metadata is cached. Defaults to the value of metadata.cache-ttl.

metadata.tables.cache-ttl

Duration for which table metadata is cached. Defaults to the value of metadata.cache-ttl.

metadata.statistics.cache-ttl

Duration for which tables statistics are cached. Defaults to the value of metadata.cache-ttl.

metadata.cache-maximum-size

Maximum number of objects stored in the metadata cache. Defaults to 10000.

Maximum number of statements in a batched execution. Do not change this setting from the default. Non-default values may negatively impact performance. Defaults to 1000.

dynamic-filtering.enabled

Push down dynamic filters into JDBC queries. Defaults to true.

dynamic-filtering.wait-timeout

Maximum duration for which Trino waits for dynamic filters to be collected from the build side of joins before starting a JDBC query. Using a large timeout can potentially result in more detailed dynamic filters. However, it can also increase latency for some queries. Defaults to 20s.

The optional parameter query.comment-format allows you to configure a SQL comment that is sent to the datasource with each query. The format of this comment can contain any characters and the following metadata:

$QUERY_ID: The identifier of the query.

$USER: The name of the user who submits the query to Trino.

$SOURCE: The identifier of the client tool used to submit the query, for example trino-cli.

$TRACE_TOKEN: The trace token configured with the client tool.

The comment can provide more context about the query. This additional information is available in the logs of the datasource. To include environment variables from the Trino cluster with the comment , use the ${ENV:VARIABLE-NAME} syntax.

The following example sets a simple comment that identifies each query sent by Trino:

With this configuration, a query such as SELECT * FROM example_table; is sent to the datasource with the comment appended:

The following example improves on the preceding example by using metadata:

If Jane sent the query with the query identifier 20230622_180528_00000_bkizg, the following comment string is sent to the datasource:

Certain JDBC driver settings and logging configurations might cause the comment to be removed.

Pushing down a large list of predicates to the data source can compromise performance. Trino compacts large predicates into a simpler range predicate by default to ensure a balance between performance and predicate pushdown. If necessary, the threshold for this compaction can be increased to improve performance when the data source is capable of taking advantage of large predicates. Increasing this threshold may improve pushdown of large dynamic filters. The domain-compaction-threshold catalog configuration property or the domain_compaction_threshold catalog session property can be used to adjust the default value of 256 for this threshold.

The SQL Server connector supports additional catalog properties to configure the behavior of the connector and the issues queries to the database.

sqlserver.snapshot-isolation.disabled

Control the automatic use of snapshot isolation for transactions issued by Trino in SQL Server. Defaults to false, which means that snapshot isolation is enabled.

When case-insensitive-name-matching is set to true, Trino is able to query non-lowercase schemas and tables by maintaining a mapping of the lowercase name to the actual name in the remote system. However, if two schemas and/or tables have names that differ only in case (such as “customers” and “Customers”) then Trino fails to query them due to ambiguity.

In these cases, use the case-insensitive-name-matching.config-file catalog configuration property to specify a configuration file that maps these remote schemas and tables to their respective Trino schemas and tables. Additionally, the JSON file must include both the schemas and tables properties, even if only as empty arrays.

Queries against one of the tables or schemes defined in the mapping attributes are run against the corresponding remote entity. For example, a query against tables in the case_insensitive_1 schema is forwarded to the CaseSensitiveName schema and a query against case_insensitive_2 is forwarded to the cASEsENSITIVEnAME schema.

At the table mapping level, a query on case_insensitive_1.table_1 as configured above is forwarded to CaseSensitiveName.tablex, and a query on case_insensitive_1.table_2 is forwarded to CaseSensitiveName.TABLEX.

By default, when a change is made to the mapping configuration file, Trino must be restarted to load the changes. Optionally, you can set the case-insensitive-name-matching.config-file.refresh-period to have Trino refresh the properties without requiring a restart:

The connector supports Fault-tolerant execution of query processing. Read and write operations are both supported with any retry policy.

The SQL Server connector provides access to all schemas visible to the specified user in the configured database. For the following examples, assume the SQL Server catalog is example.

You can see the available schemas by running SHOW SCHEMAS:

If you have a schema named web, you can view the tables in this schema by running SHOW TABLES:

You can see a list of the columns in the clicks table in the web database using either of the following:

Finally, you can query the clicks table in the web schema:

If you used a different name for your catalog properties file, use that catalog name instead of example in the above examples.

Because Trino and SQL Server each support types that the other does not, this connector modifies some types when reading or writing data. Data types may not map the same way in both directions between Trino and the data source. Refer to the following sections for type mapping in each direction.

The connector maps SQL Server types to the corresponding Trino types following this table:

SQL Server database type

SQL Server TINYINT is actually unsigned TINYINT

See Numeric type mapping

DECIMAL[(p[, s])], NUMERIC[(p[, s])]

VARCHAR[(n | max)], NVARCHAR[(n | max)]

1 <= n <= 8000, max = 2147483647

1 <= n <= 8000, max = 2147483647

TIMESTAMP(n) WITH TIME ZONE

The connector maps Trino types to the corresponding SQL Server types following this table:

Trino only supports writing values belonging to [0, 127]

NCHAR(n) or NVARCHAR(max)

See Character type mapping

NVARCHAR(n) or NVARCHAR(max)

See Character type mapping

Complete list of SQL Server data types.

For SQL Server FLOAT[(n)]:

If n is not specified maps to Trino Double

If 1 <= n <= 24 maps to Trino REAL

If 24 < n <= 53 maps to Trino DOUBLE

If 1 <= n <= 4000 maps SQL Server NCHAR(n)

If n > 4000 maps SQL Server NVARCHAR(max)

For Trino VARCHAR(n):

If 1 <= n <= 4000 maps SQL Server NVARCHAR(n)

If n > 4000 maps SQL Server NVARCHAR(max)

The following properties can be used to configure how data types from the connected data source are mapped to Trino data types and how the metadata is cached in Trino.

unsupported-type-handling

Configure how unsupported column data types are handled:

IGNORE, column is not accessible.

CONVERT_TO_VARCHAR, column is converted to unbounded VARCHAR.

The respective catalog session property is unsupported_type_handling.

jdbc-types-mapped-to-varchar

Allow forced mapping of comma separated lists of data types to convert to unbounded VARCHAR

The connector provides read access and write access to data and metadata in SQL Server. In addition to the globally available and read operation statements, the connector supports the following features:

INSERT, see also Non-transactional INSERT

UPDATE, see also UPDATE limitation

DELETE, see also DELETE limitation

Schema and table management, see also:

ALTER TABLE RENAME TO limitation

The connector supports adding rows using INSERT statements. By default, data insertion is performed by writing data to a temporary table. You can skip this step to improve performance and write directly to the target table. Set the insert.non-transactional-insert.enabled catalog property or the corresponding non_transactional_insert catalog session property to true.

Note that with this property enabled, data can be corrupted in rare cases where exceptions occur during the insert operation. With transactions disabled, no rollback can be performed.

Only UPDATE statements with constant assignments and predicates are supported. For example, the following statement is supported because the values assigned are constants:

Arithmetic expressions, function calls, and other non-constant UPDATE statements are not supported. For example, the following statement is not supported because arithmetic expressions cannot be used with the SET command:

All column values of a table row cannot be updated simultaneously. For a three column table, the following statement is not supported:

If a WHERE clause is specified, the DELETE operation only works if the predicate in the clause can be fully pushed down to the data source.

The connector does not support renaming tables across multiple schemas. For example, the following statement is supported:

The following statement attempts to rename a table across schemas, and therefore is not supported:

Flush JDBC metadata caches. For example, the following system call flushes the metadata caches for all schemas in the example catalog

The execute procedure allows you to execute a query in the underlying data source directly. The query must use supported syntax of the connected data source. Use the procedure to access features which are not available in Trino or to execute queries that return no result set and therefore can not be used with the query or raw_query pass-through table function. Typical use cases are statements that create or alter objects, and require native feature such as constraints, default values, automatic identifier creation, or indexes. Queries can also invoke statements that insert, update, or delete data, and do not return any data as a result.

The query text is not parsed by Trino, only passed through, and therefore only subject to any security or access control of the underlying data source.

The following example sets the current database to the example_schema of the example catalog. Then it calls the procedure in that schema to drop the default value from your_column on your_table table using the standard SQL syntax in the parameter value assigned for query:

Verify that the specific database supports this syntax, and adapt as necessary based on the documentation for the specific connected database and database version.

The connector provides specific table functions to access SQL Server.

The query function allows you to query the underlying database directly. It requires syntax native to SQL Server, because the full query is pushed down and processed in SQL Server. This can be useful for accessing native features which are not implemented in Trino or for improving query performance in situations where running a query natively may be faster.

The native query passed to the underlying data source is required to return a table as a result set. Only the data source performs validation or security checks for these queries using its own configuration. Trino does not perform these tasks. Only use passthrough queries to read data.

For example, query the example catalog and select the top 10 percent of nations by population:

The procedure function allows you to run stored procedures on the underlying database directly. It requires syntax native to SQL Server, because the full query is pushed down and processed in SQL Server. In order to use this table function set sqlserver.stored-procedure-table-function-enabled to true.

The procedure function does not support running StoredProcedures that return multiple statements, use a non-select statement, use output parameters, or use conditional statements.

This feature is experimental only. The function has security implication and syntax might change and be backward incompatible.

The follow example runs the stored procedure employee_sp in the example catalog and the example_schema schema in the underlying SQL Server database:

If the stored procedure employee_sp requires any input append the parameter value to the procedure statement:

The query engine does not preserve the order of the results of this function. If the passed query contains an ORDER BY clause, the function result may not be ordered as expected.

The connector includes a number of performance improvements, detailed in the following sections.

The SQL Server connector can use table and column statistics for cost based optimizations, to improve query processing performance based on the actual data in the data source.

The statistics are collected by SQL Server and retrieved by the connector.

The connector can use information stored in single-column statistics. SQL Server Database can automatically create column statistics for certain columns. If column statistics are not created automatically for a certain column, you can create them by executing the following statement in SQL Server Database.

SQL Server Database routinely updates the statistics. In some cases, you may want to force statistics update (e.g. after defining new column statistics or after changing data in the table). You can do that by executing the following statement in SQL Server Database.

Refer to SQL Server documentation for information about options, limitations and additional considerations.

The connector supports pushdown for a number of operations:

Aggregate pushdown for the following functions:

The connector performs pushdown where performance may be improved, but in order to preserve correctness an operation may not be pushed down. When pushdown of an operation may result in better performance but risks correctness, the connector prioritizes correctness.

The connector supports cost-based Join pushdown to make intelligent decisions about whether to push down a join operation to the data source.

When cost-based join pushdown is enabled, the connector only pushes down join operations if the available Table statistics suggest that doing so improves performance. Note that if no table statistics are available, join operation pushdown does not occur to avoid a potential decrease in query performance.

The following table describes catalog configuration properties for join pushdown:

join-pushdown.enabled

Enable join pushdown. Equivalent catalog session property is join_pushdown_enabled.

join-pushdown.strategy

Strategy used to evaluate whether join operations are pushed down. Set to AUTOMATIC to enable cost-based join pushdown, or EAGER to push down joins whenever possible. Note that EAGER can push down joins even when table statistics are unavailable, which may result in degraded query performance. Because of this, EAGER is only recommended for testing and troubleshooting purposes.

The connector supports pushdown of predicates on VARCHAR and NVARCHAR columns if the underlying columns in SQL Server use a case-sensitive collation.

The following operators are pushed down:

To ensure correct results, operators are not pushed down for columns using a case-insensitive collation.

You can optionally use the bulk copy API to drastically speed up write operations.

Enable bulk copying and a lock on the destination table to meet minimal logging requirements.

The following table shows the relevant catalog configuration properties and their default values:

sqlserver.bulk-copy-for-write.enabled

Use the SQL Server bulk copy API for writes. The corresponding catalog session property is bulk_copy_for_write.

sqlserver.bulk-copy-for-write.lock-destination-table

Obtain a bulk update lock on the destination table for write operations. The corresponding catalog session property is bulk_copy_for_write_lock_destination_table. Setting is only used when bulk-copy-for-write.enabled=true.

Column names with leading and trailing spaces are not supported.

You can specify the data compression policy for SQL Server tables with the data_compression table property. Valid policies are NONE, ROW or PAGE.

**Examples:**

Example 1 (unknown):
```unknown
connector.name=sqlserver
connection-url=jdbc:sqlserver://<host>:<port>;databaseName=<databaseName>;encrypt=false
connection-user=root
connection-password=secret
```

Example 2 (unknown):
```unknown
connector.name=sqlserver
connection-url=jdbc:sqlserver://<host>:<port>;databaseName=<databaseName>;encrypt=false
connection-user=root
connection-password=secret
```

Example 3 (unknown):
```unknown
connection-url=jdbc:sqlserver://<host>:<port>;databaseName=<databaseName>;encrypt=false
```

Example 4 (unknown):
```unknown
connection-url=jdbc:sqlserver://<host>:<port>;databaseName=<databaseName>;encrypt=false
```

---

## Connectors — Trino 478 Documentation

**URL:** https://trino.io/docs/current/connector.html

**Contents:**
- Connectors#

This section describes the connectors available in Trino to access data from different data sources by configuring catalogs with the connector-specific properties in catalog properties files.

---

## DROP CATALOG — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/drop-catalog.html

**Contents:**
- DROP CATALOG#
- Synopsis#
- Description#
- Examples#
- See also#

Drops an existing catalog. Dropping a catalog does not interrupt any running queries that use it, but makes it unavailable to any new queries.

Some connectors are known not to release all resources when dropping a catalog that uses such connector. This includes all connectors that can read data from HDFS, S3, GCS, or Azure, which are Hive connector, Iceberg connector, Delta Lake connector, and Hudi connector.

This command requires the catalog management type to be set to dynamic.

Drop the catalog example:

Catalog management properties

**Examples:**

Example 1 (unknown):
```unknown
DROP CATALOG catalog_name
```

Example 2 (unknown):
```unknown
DROP CATALOG catalog_name
```

Example 3 (unknown):
```unknown
DROP CATALOG example;
```

Example 4 (unknown):
```unknown
DROP CATALOG example;
```

---

## Hive connector — Trino 478 Documentation

**URL:** https://trino.io/docs/current/connector/hive.html

**Contents:**
- Hive connector#
- Requirements#
- General configuration#
  - Multiple Hive clusters#
  - Hive general configuration properties#
  - File system access configuration#
  - Fault-tolerant execution support#
- Security#
- Authorization#
  - SQL standard based authorization#

The Hive connector allows querying data stored in an Apache Hive data warehouse. Hive is a combination of three components:

Data files in varying formats, that are typically stored in the Hadoop Distributed File System (HDFS) or in object storage systems such as Amazon S3.

Metadata about how the data files are mapped to schemas and tables. This metadata is stored in a database, such as MySQL, and is accessed via the Hive metastore service.

A query language called HiveQL. This query language is executed on a distributed computing framework such as MapReduce or Tez.

Trino only uses the first two components: the data and the metadata. It does not use HiveQL or any part of Hive’s execution environment.

The Hive connector requires a Hive metastore service (HMS), or a compatible implementation of the Hive metastore, such as AWS Glue.

You must select and configure a supported file system in your catalog configuration file.

The coordinator and all workers must have network access to the Hive metastore and the storage system. Hive metastore access with the Thrift protocol defaults to using port 9083.

Data files must be in a supported file format. File formats can be configured using the format table property and other specific properties:

In the case of serializable formats, only specific SerDes are allowed:

RCText - RCFile using ColumnarSerDe

RCBinary - RCFile using LazyBinaryColumnarSerDe

SequenceFile with org.apache.hadoop.io.Text

SequenceFile with org.apache.hadoop.io.BytesWritable containing protocol buffer records using com.twitter.elephantbird.hive.serde.ProtobufDeserializer

CSV - using org.apache.hadoop.hive.serde2.OpenCSVSerde

JSON - using org.apache.hive.hcatalog.data.JsonSerDe

OPENX_JSON - OpenX JSON SerDe from org.openx.data.jsonserde.JsonSerDe. Find more details about the Trino implementation in the source repository.

ESRI - using com.esri.hadoop.hive.serde.EsriJsonSerDe

To configure the Hive connector, create a catalog properties file etc/catalog/example.properties that references the hive connector.

You must configure a metastore for metadata.

You must select and configure one of the supported file systems.

Replace the fs.x.enabled configuration property with the desired file system.

If you are using AWS Glue as your metastore, you must instead set hive.metastore to glue:

Each metastore type has specific configuration properties along with General metastore configuration properties.

You can have as many catalogs as you need, so if you have additional Hive clusters, simply add another properties file to etc/catalog with a different name, making sure it ends in .properties. For example, if you name the property file sales.properties, Trino creates a catalog named sales using the configured connector.

The following table lists general configuration properties for the Hive connector. There are additional sets of configuration properties throughout the Hive connector documentation.

hive.recursive-directories

Enable reading data from subdirectories of table or partition locations. If disabled, subdirectories are ignored. This is equivalent to the hive.mapred.supports.subdirectories property in Hive.

hive.ignore-absent-partitions

Ignore partitions when the file system location does not exist rather than failing the query. This skips data that may be expected to be part of the table.

The default file format used when creating new tables.

hive.orc.use-column-names

Access ORC columns by name. By default, columns in ORC files are accessed by their ordinal position in the Hive table definition. The equivalent catalog session property is orc_use_column_names. See also, ORC format configuration properties

hive.parquet.use-column-names

Access Parquet columns by name by default. Set this property to false to access columns by their ordinal position in the Hive table definition. The equivalent catalog session property is parquet_use_column_names. See also, Parquet format configuration properties

hive.parquet.time-zone

Time zone for Parquet read and write.

hive.compression-codec

The compression codec to use when writing files. Possible values are NONE, SNAPPY, LZ4, ZSTD, or GZIP.

hive.force-local-scheduling

Force splits to be scheduled on the same node as the Hadoop DataNode process serving the split data. This is useful for installations where Trino is collocated with every DataNode.

hive.respect-table-format

Should new partitions be written using the existing table format or the default Trino format?

hive.immutable-partitions

Can new data be inserted into existing partitions? If true then setting hive.insert-existing-partitions-behavior to APPEND is not allowed. This also affects the insert_existing_partitions_behavior session property in the same way.

hive.insert-existing-partitions-behavior

What happens when data is inserted into an existing partition? Possible values are

APPEND - appends data to existing partitions

OVERWRITE - overwrites existing partitions

ERROR - modifying existing partitions is not allowed

The equivalent catalog session property is insert_existing_partitions_behavior.

hive.target-max-file-size

Best effort maximum size of new files.

hive.create-empty-bucket-files

Should empty files be created for buckets that have no data?

hive.validate-bucketing

Enables validation that data is in the correct bucket when reading bucketed tables.

hive.partition-statistics-sample-size

Specifies the number of partitions to analyze when computing table statistics.

hive.max-partitions-per-writers

Maximum number of partitions per writer.

hive.max-partitions-for-eager-load

The maximum number of partitions for a single table scan to load eagerly on the coordinator. Certain optimizations are not possible without eager loading.

hive.max-partitions-per-scan

Maximum number of partitions for a single table scan.

hive.non-managed-table-writes-enabled

Enable writes to non-managed (external) Hive tables.

hive.non-managed-table-creates-enabled

Enable creating non-managed (external) Hive tables.

hive.collect-column-statistics-on-write

Enables automatic column level statistics collection on write. See Table statistics for details.

hive.file-status-cache-tables

Cache directory listing for specific tables. Examples:

fruit.apple,fruit.orange to cache listings only for tables apple and orange in schema fruit

fruit.*,vegetable.* to cache listings for all tables in schemas fruit and vegetable

* to cache listings for all tables in all schemas

hive.file-status-cache.excluded-tables

Whereas hive.file-status-cache-tables is an inclusion list, this is an exclusion list for the cache.

fruit.apple,fruit.orange to NOT cache listings only for tables apple and orange in schema fruit

fruit.*,vegetable.* to NOT cache listings for all tables in schemas fruit and vegetable

hive.file-status-cache.max-retained-size

Maximum retained size of cached file status entries.

hive.file-status-cache-expire-time

How long a cached directory listing is considered valid.

hive.per-transaction-file-status-cache.max-retained-size

Maximum retained size of all entries in per transaction file status cache. Retained size limit is shared across all running queries.

hive.rcfile.time-zone

Adjusts binary encoded timestamp values to a specific time zone. For Hive 3.1+, this must be set to UTC.

hive.timestamp-precision

Specifies the precision to use for Hive columns of type TIMESTAMP. Possible values are MILLISECONDS, MICROSECONDS and NANOSECONDS. Values with higher precision than configured are rounded. The equivalent catalog session property is timestamp_precision for session specific use.

hive.temporary-staging-directory-enabled

Controls whether the temporary staging directory configured at hive.temporary-staging-directory-path is used for write operations. Temporary staging directory is never used for writes to non-sorted tables on S3, encrypted HDFS or external location. Writes to sorted tables will utilize this path for staging temporary files during sorting operation. When disabled, the target storage will be used for staging while writing sorted tables which can be inefficient when writing to object stores like S3.

hive.temporary-staging-directory-path

Controls the location of temporary staging directory that is used for write operations. The ${USER} placeholder can be used to use a different location for each user.

hive.hive-views.enabled

Enable translation for Hive views.

hive.hive-views.legacy-translation

Use the legacy algorithm to translate Hive views. You can use the hive_views_legacy_translation catalog session property for temporary, catalog specific use.

hive.parallel-partitioned-bucketed-writes

Improve parallelism of partitioned and bucketed table writes. When disabled, the number of writing threads is limited to number of buckets.

hive.query-partition-filter-required

Set to true to force a query to use a partition filter. You can use the query_partition_filter_required catalog session property for temporary, catalog specific use.

hive.query-partition-filter-required-schemas

Allow specifying the list of schemas for which Trino will enforce that queries use a filter on partition keys for source tables. The list can be specified using the hive.query-partition-filter-required-schemas, or the query_partition_filter_required_schemas session property. The list is taken into consideration only if the hive.query-partition-filter-required configuration property or the query_partition_filter_required session property is set to true.

hive.table-statistics-enabled

Enables Table statistics. The equivalent catalog session property is statistics_enabled for session specific use. Set to false to disable statistics. Disabling statistics means that Cost-based optimizations can not make smart decisions about the query plan.

Set the default value for the auto_purge table property for managed tables. See the Table properties for more information on auto_purge.

hive.partition-projection-enabled

Enables Athena partition projection support

hive.s3-glacier-filter

Filter S3 objects based on their storage class and restored status if applicable. Possible values are

READ_ALL - read files from all S3 storage classes

READ_NON_GLACIER - read files from non S3 Glacier storage classes

READ_NON_GLACIER_AND_RESTORED - read files from non S3 Glacier storage classes and restored objects from Glacier storage class

hive.max-partition-drops-per-query

Maximum number of partitions to drop in a single query.

hive.metastore.partition-batch-size.max

Maximum number of partitions processed in a single batch.

hive.single-statement-writes

Enables auto-commit for all writes. This can be used to disallow multi-statement write transactions.

hive.metadata.parallelism

Number of threads used for retrieving metadata. Currently, only table loading is parallelized.

hive.protobuf.descriptors.location

Path to a directory where binary Protocol Buffer descriptor files are stored to be used for reading tables stored in the com.twitter.elephantbird.hive.serde.ProtobufDeserializer format.

hive.protobuf.descriptors.cache.max-size

Maximum size of the Protocol Buffer descriptors cache

hive.protobuf.descriptors.cache.refresh-interval

Duration after which loaded Protocol Buffer descriptors should be reloaded from disk.

The connector supports accessing the following file systems:

Azure Storage file system support

Google Cloud Storage file system support

S3 file system support

HDFS file system support

You must enable and configure the specific file system access. Legacy support is not recommended and will be removed.

The connector supports Fault-tolerant execution of query processing. Read and write operations are both supported with any retry policy on non-transactional tables.

Read operations are supported with any retry policy on transactional tables. Write operations and CREATE TABLE ... AS operations are not supported with any retry policy on transactional tables.

The connector supports different means of authentication for the used file system and metastore.

In addition, the following security-related features are supported.

You can enable authorization checks by setting the hive.security property in the catalog properties file. This property must be one of the following values:

allow-all (default value)

No authorization checks are enforced.

Operations that read data or metadata, such as SELECT, are permitted, but none of the operations that write data or metadata, such as CREATE, INSERT or DELETE, are allowed.

Authorization checks are enforced using a catalog-level access control configuration file whose path is specified in the security.config-file catalog configuration property. See Catalog-level access control files for details.

Users are permitted to perform the operations as long as they have the required privileges as per the SQL standard. In this mode, Trino enforces the authorization checks for queries based on the privileges defined in Hive metastore. To alter these privileges, use the GRANT privilege and REVOKE privilege commands.

See the SQL standard based authorization section for details.

When sql-standard security is enabled, Trino enforces the same SQL standard-based authorization as Hive does.

Since Trino’s ROLE syntax support matches the SQL standard, and Hive does not exactly follow the SQL standard, there are the following limitations and differences:

CREATE ROLE role WITH ADMIN is not supported.

The admin role must be enabled to execute CREATE ROLE, DROP ROLE or CREATE SCHEMA.

GRANT role TO user GRANTED BY someone is not supported.

REVOKE role FROM user GRANTED BY someone is not supported.

By default, all a user’s roles, except admin, are enabled in a new user session.

One particular role can be selected by executing SET ROLE role.

SET ROLE ALL enables all of a user’s roles except admin.

The admin role must be enabled explicitly by executing SET ROLE admin.

GRANT privilege ON SCHEMA schema is not supported. Schema ownership can be changed with ALTER SCHEMA schema SET AUTHORIZATION user

The Hive connector supports reading Parquet files encrypted with Parquet Modular Encryption (PME). Decryption keys can be provided via environment variables. Writing encrypted Parquet files is not supported.

pme.environment-key-retriever.enabled

Enable the key retriever that reads decryption keys from environment variables.

AAD prefix used when decoding Parquet files. Must match the prefix used when the files were written, if applicable.

pme.check-footer-integrity

Validate signature for plaintext footer files.

When pme.environment-key-retriever.enabled is set, provide keys with environment variables:

pme.environment-key-retriever.footer-keys

pme.environment-key-retriever.column-keys

Each variable accepts either a single base64-encoded key, or a comma-separated list of id:key pairs (base64-encoded keys) where id must match the key metadata embedded in the Parquet file.

The connector provides read access and write access to data and metadata in the configured object storage system and metadata stores:

Globally available statements; see also Globally available statements

Data management; see also Hive-specific data management

Schema and table management; see also Hive-specific schema and table management

View management; see also Hive-specific view management

User-defined function management

Security operations: see also SQL standard-based authorization for object storage

Refer to the migration guide for practical advice on migrating from Hive to Trino.

The following sections provide Hive-specific information regarding SQL support.

The examples shown here work on Google Cloud Storage by replacing s3:// with gs://.

Create a new Hive table named page_views in the web schema that is stored using the ORC file format, partitioned by date and country, and bucketed by user into 50 buckets. Note that Hive requires the partition columns to be the last columns in the table:

Create a new Hive schema named web that stores tables in an S3 bucket named my-bucket:

Drop a partition from the page_views table:

Query the page_views table:

List the partitions of the page_views table:

Create an external Hive table named request_logs that points at existing data in S3:

Collect statistics for the request_logs table:

Drop the external table request_logs. This only drops the metadata for the table. The referenced data directory is not deleted:

CREATE TABLE AS can be used to create transactional tables in ORC format like this:

Add an empty partition to the page_views table:

Drop stats for a partition of the page_views table:

Tables created in Hive with Twitter Elephantbird are supported to read. The binary protobuf descriptor as mentioned in the serialization.class should be stored in a directory that is configured via hive.protobuf.descriptors.location on every worker.

Use the CALL statement to perform data manipulation or administrative tasks. Procedures must include a qualified catalog name, if your Hive catalog is called web:

The following procedures are available:

system.create_empty_partition(schema_name, table_name, partition_columns, partition_values)

Create an empty partition in the specified table.

system.sync_partition_metadata(schema_name, table_name, mode, case_sensitive)

Check and update partitions list in metastore. There are three modes available:

ADD : add any partitions that exist on the file system, but not in the metastore.

DROP: drop any partitions that exist in the metastore, but not on the file system.

FULL: perform both ADD and DROP.

The case_sensitive argument is optional. The default value is true for compatibility with Hive’s MSCK REPAIR TABLE behavior, which expects the partition column names in file system paths to use lowercase (e.g. col_x=SomeValue). Partitions on the file system not conforming to this convention are ignored, unless the argument is set to false.

system.drop_stats(schema_name, table_name, partition_values)

Drops statistics for a subset of partitions or the entire table. The partitions are specified as an array whose elements are arrays of partition values (similar to the partition_values argument in create_empty_partition). If partition_values argument is omitted, stats are dropped for the entire table.

system.register_partition(schema_name, table_name, partition_columns, partition_values, location)

Registers existing location as a new partition in the metastore for the specified table.

When the location argument is omitted, the partition location is constructed using partition_columns and partition_values.

Due to security reasons, the procedure is enabled only when hive.allow-register-partition-procedure is set to true.

system.unregister_partition(schema_name, table_name, partition_columns, partition_values)

Unregisters given, existing partition in the metastore for the specified table. The partition data is not deleted.

system.flush_metadata_cache()

Flush all Hive metadata caches.

system.flush_metadata_cache(schema_name => ..., table_name => ...)

Flush Hive metadata caches entries connected with selected table. Procedure requires named parameters to be passed

system.flush_metadata_cache(schema_name => ..., table_name => ..., partition_columns => ARRAY[...], partition_values => ARRAY[...])

Flush Hive metadata cache entries connected with selected partition. Procedure requires named parameters to be passed.

The Data management functionality includes support for INSERT, UPDATE, DELETE, and MERGE statements, with the exact support depending on the storage system, file format, and metastore.

When connecting to a Hive metastore version 3.x, the Hive connector supports reading from and writing to insert-only and ACID tables, with full support for partitioning and bucketing.

DELETE applied to non-transactional tables is only supported if the table is partitioned and the WHERE clause matches entire partitions. Transactional Hive tables with ORC format support “row-by-row” deletion, in which the WHERE clause may match arbitrary sets of rows.

UPDATE is only supported for transactional Hive tables with format ORC. UPDATE of partition or bucket columns is not supported.

MERGE is only supported for ACID tables.

ACID tables created with Hive Streaming Ingest are not supported.

The Hive connector supports querying and manipulating Hive tables and schemas (databases). While some uncommon operations must be performed using Hive directly, most operations can be performed using Trino.

Hive table partitions can differ from the current table schema. This occurs when the data types of columns of a table are changed from the data types of columns of preexisting partitions. The Hive connector supports this schema evolution by allowing the same conversions as Hive. The following table lists possible data type conversions.

BOOLEAN, TINYINT, SMALLINT, INTEGER, BIGINT, REAL, DOUBLE, TIMESTAMP, DATE, CHAR as well as narrowing conversions for VARCHAR

VARCHAR, narrowing conversions for CHAR

VARCHAR, SMALLINT, INTEGER, BIGINT, DOUBLE, DECIMAL

VARCHAR, INTEGER, BIGINT, DOUBLE, DECIMAL

VARCHAR, BIGINT, DOUBLE, DECIMAL

VARCHAR, DOUBLE, DECIMAL

DOUBLE, REAL, VARCHAR, TINYINT, SMALLINT, INTEGER, BIGINT, as well as narrowing and widening conversions for DECIMAL

Any conversion failure results in null, which is the same behavior as Hive. For example, converting the string 'foo' to a number, or converting the string '1234' to a TINYINT (which has a maximum value of 127).

Trino supports querying and manipulating Hive tables with the Avro storage format, which has the schema set based on an Avro schema file/literal. Trino is also capable of creating the tables in Trino by inferring the schema from a valid Avro schema file located locally, or remotely in HDFS/Web server.

To specify that the Avro schema should be used for interpreting table data, use the avro_schema_url table property.

The schema can be placed in the local file system or remotely in the following locations:

HDFS (e.g. avro_schema_url = 'hdfs://user/avro/schema/avro_data.avsc')

S3 (e.g. avro_schema_url = 's3n:///schema_bucket/schema/avro_data.avsc')

A web server (e.g. avro_schema_url = 'http://example.org/schema/avro_data.avsc')

The URL, where the schema is located, must be accessible from the Hive metastore and Trino coordinator/worker nodes.

Alternatively, you can use the table property avro_schema_literal to define the Avro schema.

The table created in Trino using the avro_schema_url or avro_schema_literal property behaves the same way as a Hive table with avro.schema.url or avro.schema.literal set.

The columns listed in the DDL (id in the above example) is ignored if avro_schema_url is specified. The table schema matches the schema in the Avro schema file. Before any read operation, the Avro schema is accessed so the query result reflects any changes in schema. Thus Trino takes advantage of Avro’s backward compatibility abilities.

If the schema of the table changes in the Avro schema file, the new schema can still be used to read old data. Newly added/renamed fields must have a default value in the Avro schema file.

The schema evolution behavior is as follows:

Column added in new schema: Data created with an older schema produces a default value when table is using the new schema.

Column removed in new schema: Data created with an older schema no longer outputs the data from the column that was removed.

Column is renamed in the new schema: This is equivalent to removing the column and adding a new one, and data created with an older schema produces a default value when table is using the new schema.

Changing type of column in the new schema: If the type coercion is supported by Avro or the Hive connector, then the conversion happens. An error is thrown for incompatible types.

The following operations are not supported when avro_schema_url is set:

CREATE TABLE AS is not supported.

Bucketing(bucketed_by) columns are not supported in CREATE TABLE.

ALTER TABLE commands modifying columns are not supported.

The connector supports the following commands for use with ALTER TABLE EXECUTE.

The optimize command is used for rewriting the content of the specified table so that it is merged into fewer but larger files. If the table is partitioned, the data compaction acts separately on each partition selected for optimization. This operation improves read performance.

All files with a size below the optional file_size_threshold parameter (default value for the threshold is 100MB) are merged:

The following statement merges files in a table that are under 128 megabytes in size:

You can use a WHERE clause with the columns used to partition the table to filter which partitions are optimized:

You can use a more complex WHERE clause to narrow down the scope of the optimize procedure. The following example casts the timestamp values to dates, and uses a comparison to only optimize partitions with data from the year 2022 or newer:

The optimize command is disabled by default, and can be enabled for a catalog with the <catalog-name>.non_transactional_optimize_enabled session property:

Because Hive tables are non-transactional, take note of the following possible outcomes:

If queries are run against tables that are currently being optimized, duplicate rows may be read.

In rare cases where exceptions occur during the optimize operation, a manual cleanup of the table directory is needed. In this situation, refer to the Trino logs and query failure messages to see which files must be deleted.

Table properties supply or set metadata for the underlying tables. This is key for CREATE TABLE AS statements. Table properties are passed to the connector using a WITH clause:

Indicates to the configured metastore to perform a purge when a table or partition is deleted instead of a soft deletion using the trash.

The URI pointing to Avro schema evolution for the table.

The number of buckets to group data into. Only valid if used with bucketed_by.

The bucketing column for the storage table. Only valid if used with bucket_count.

Specifies which Hive bucketing version to use. Valid values are 1 or 2.

The CSV escape character. Requires CSV format.

The CSV quote character. Requires CSV format.

The CSV separator character. Requires CSV format. You can use other separators such as | or use Unicode to configure invisible separators such tabs with U&'\0009'.

The URI for an external Hive table on S3, Azure Blob Storage, etc. See the Basic usage examples for more information.

The table file format. Valid values include ORC, PARQUET, AVRO, RCBINARY, RCTEXT, SEQUENCEFILE, JSON, OPENX_JSON, TEXTFILE, CSV, and REGEX. The catalog property hive.storage-format sets the default value and can change it to a different default.

The serialization format for NULL value. Requires TextFile, RCText, or SequenceFile format.

orc_bloom_filter_columns

Comma separated list of columns to use for ORC bloom filter. It improves the performance of queries using equality predicates, such as =, IN and small range predicates, when reading ORC files. Requires ORC format.

The ORC bloom filters false positive probability. Requires ORC format.

The partitioning column for the storage table. The columns listed in the partitioned_by clause must be the last columns as defined in the DDL.

parquet_bloom_filter_columns

Comma separated list of columns to use for Parquet bloom filter. It improves the performance of queries using equality predicates, such as =, IN and small range predicates, when reading Parquet files. Requires Parquet format.

skip_footer_line_count

The number of footer lines to ignore when parsing the file for data. Requires TextFile or CSV format tables.

skip_header_line_count

The number of header lines to ignore when parsing the file for data. Requires TextFile or CSV format tables.

The column to sort by to determine bucketing for row. Only valid if bucketed_by and bucket_count are specified as well.

textfile_field_separator

Allows the use of custom field separators, such as ‘|’, for TextFile formatted tables.

textfile_field_separator_escape

Allows the use of a custom escape character for TextFile formatted tables.

Set this property to true to create an ORC ACID transactional table. Requires ORC format. This property may be shown as true for insert-only tables created using older versions of Hive.

partition_projection_enabled

Enables partition projection for selected table. Mapped from AWS Athena table property projection.enabled.

partition_projection_ignore

Ignore any partition projection properties stored in the metastore for the selected table. This is a Trino-only property which allows you to work around compatibility issues on a specific table, and if enabled, Trino ignores all other configuration options related to partition projection.

partition_projection_location_template

Projected partition location template, such as s3a://test/name=${name}/. Mapped from the AWS Athena table property storage.location.template

${table_location}/${partition_name}

Additional properties added to a Hive table. The properties are not used by Trino, and are available in the $properties metadata table. The properties are not included in the output of SHOW CREATE TABLE statements.

The raw Hive table properties are available as a hidden table, containing a separate column per table property, with a single row containing the property values.

The properties table name is composed with the table name and $properties appended. It exposes the parameters of the table in the metastore.

You can inspect the property names and values with a simple query:

The $partitions table provides a list of all partition values of a partitioned table.

The following example query returns all partition values from the page_views table in the web schema of the example catalog:

partition_projection_type

Defines the type of partition projection to use on this column. May be used only on partition columns. Available types: ENUM, INTEGER, DATE, INJECTED. Mapped from the AWS Athena table property projection.${columnName}.type.

partition_projection_values

Used with partition_projection_type set to ENUM. Contains a static list of values used to generate partitions. Mapped from the AWS Athena table property projection.${columnName}.values.

partition_projection_range

Used with partition_projection_type set to INTEGER or DATE to define a range. It is a two-element array, describing the minimum and maximum range values used to generate partitions. Generation starts from the minimum, then increments by the defined partition_projection_interval to the maximum. For example, the format is ['1', '4'] for a partition_projection_type of INTEGER and ['2001-01-01', '2001-01-07'] or ['NOW-3DAYS', 'NOW'] for a partition_projection_type of DATE. Mapped from the AWS Athena table property projection.${columnName}.range.

partition_projection_interval

Used with partition_projection_type set to INTEGER or DATE. It represents the interval used to generate partitions within the given range partition_projection_range. Mapped from the AWS Athena table property projection.${columnName}.interval.

partition_projection_digits

Used with partition_projection_type set to INTEGER. The number of digits to be used with integer column projection. Mapped from the AWS Athena table property projection.${columnName}.digits.

partition_projection_format

Used with partition_projection_type set to DATE. The date column projection format, defined as a string such as yyyy MM or MM-dd-yy HH:mm:ss for use with the Java DateTimeFormatter class. Mapped from the AWS Athena table property projection.${columnName}.format.

partition_projection_interval_unit

Used with partition_projection_type=DATA. The date column projection range interval unit given in partition_projection_interval. Mapped from the AWS Athena table property projection.${columnName}.interval.unit.

In addition to the defined columns, the Hive connector automatically exposes metadata in a number of hidden columns in each table:

$bucket: Bucket number for this row

$path: Full file system path name of the file for this row

$file_modified_time: Date and time of the last modification of the file for this row

$file_size: Size of the file for this row

$partition: Partition name for this row

You can use these columns in your SQL statements like any other column. They can be selected directly, or used in conditional statements. For example, you can inspect the file size, location and partition for each record:

Retrieve all records that belong to files stored in the partition ds=2016-08-09/country=US:

Trino allows reading from Hive materialized views, and can be configured to support reading Hive views.

The Hive connector supports reading from Hive materialized views. In Trino, these views are presented as regular, read-only tables.

Hive views are defined in HiveQL and stored in the Hive Metastore Service. They are analyzed to allow read access to the data.

The Hive connector includes support for reading Hive views with three different modes.

If using Hive views from Trino is required, you must compare results in Hive and Trino for each view definition to ensure identical results. Use the experimental mode whenever possible. Avoid using the legacy mode. Leave Hive views support disabled, if you are not accessing any Hive views from Trino.

You can configure the behavior in your catalog properties file.

By default, Hive views are executed with the RUN AS DEFINER security mode. Set the hive.hive-views.run-as-invoker catalog configuration property to true to use RUN AS INVOKER semantics.

The default behavior is to ignore Hive views. This means that your business logic and data encoded in the views is not available in Trino.

A very simple implementation to execute Hive views, and therefore allow read access to the data in Trino, can be enabled with hive.hive-views.enabled=true and hive.hive-views.legacy-translation=true.

For temporary usage of the legacy behavior for a specific catalog, you can set the hive_views_legacy_translation catalog session property to true.

This legacy behavior interprets any HiveQL query that defines a view as if it is written in SQL. It does not do any translation, but instead relies on the fact that HiveQL is very similar to SQL.

This works for very simple Hive views, but can lead to problems for more complex queries. For example, if a HiveQL function has an identical signature but different behaviors to the SQL version, the returned results may differ. In more extreme cases the queries might fail, or not even be able to be parsed and executed.

The new behavior is better engineered and has the potential to become a lot more powerful than the legacy implementation. It can analyze, process, and rewrite Hive views and contained expressions and statements.

It supports the following Hive view functionality:

UNION [DISTINCT] and UNION ALL against Hive views

Nested GROUP BY clauses

LATERAL VIEW OUTER EXPLODE

LATERAL VIEW [OUTER] EXPLODE on array of struct

LATERAL VIEW json_tuple

You can enable the experimental behavior with hive.hive-views.enabled=true. Remove the hive.hive-views.legacy-translation property or set it to false to make sure legacy is not enabled.

Keep in mind that numerous features are not yet implemented when experimenting with this feature. The following is an incomplete list of missing functionality:

HiveQL current_date, current_timestamp, and others

Hive function calls including translate(), window functions, and others

Common table expressions and simple case expressions

Honor timestamp precision setting

Support all Hive data types and correct mapping to Trino types

Ability to process custom UDFs

The connector includes a number of performance improvements, detailed in the following sections.

The Hive connector supports collecting and managing table statistics to improve query processing performance.

When writing data, the Hive connector always collects basic statistics (numFiles, numRows, rawDataSize, totalSize) and by default will also collect column level statistics:

Collectible statistics

Number of nulls, number of distinct values, min/max values

Number of nulls, number of distinct values, min/max values

Number of nulls, number of distinct values, min/max values

Number of nulls, number of distinct values, min/max values

Number of nulls, number of distinct values, min/max values

Number of nulls, number of distinct values, min/max values

Number of nulls, number of distinct values, min/max values

Number of nulls, number of distinct values, min/max values

Number of nulls, number of distinct values, min/max values

Number of nulls, number of distinct values

Number of nulls, number of distinct values

Number of nulls, number of true/false values

If your queries are complex and include joining large data sets, running ANALYZE on tables/partitions may improve query performance by collecting statistical information about the data.

When analyzing a partitioned table, the partitions to analyze can be specified via the optional partitions property, which is an array containing the values of the partition keys in the order they are declared in the table schema:

This query will collect statistics for two partitions with keys p1_value1, p1_value2 and p2_value1, p2_value2.

On wide tables, collecting statistics for all columns can be expensive and can have a detrimental effect on query planning. It is also typically unnecessary - statistics are only useful on specific columns, like join keys, predicates, grouping keys. One can specify a subset of columns to be analyzed via the optional columns property:

This query collects statistics for columns col_1 and col_2 for the partition with keys p2_value1, p2_value2.

Note that if statistics were previously collected for all columns, they must be dropped before re-analyzing just a subset:

You can also drop statistics for selected partitions only:

The Hive connector supports the dynamic filtering optimization. Dynamic partition pruning is supported for partitioned tables stored in any file format for broadcast as well as partitioned joins. Dynamic bucket pruning is supported for bucketed tables stored in any file format for broadcast joins only.

For tables stored in ORC or Parquet file format, dynamic filters are also pushed into local table scan on worker nodes for broadcast joins. Dynamic filter predicates pushed into the ORC and Parquet readers are used to perform stripe or row-group pruning and save on disk I/O. Sorting the data within ORC or Parquet files by the columns used in join criteria significantly improves the effectiveness of stripe or row-group pruning. This is because grouping similar data within the same stripe or row-group greatly improves the selectivity of the min/max indexes maintained at stripe or row-group level.

It can often be beneficial to wait for the collection of dynamic filters before starting a table scan. This extra wait time can potentially result in significant overall savings in query and CPU time, if dynamic filtering is able to reduce the amount of scanned data.

For the Hive connector, a table scan can be delayed for a configured amount of time until the collection of dynamic filters by using the configuration property hive.dynamic-filtering.wait-timeout in the catalog file or the catalog session property <hive-catalog>.dynamic_filtering_wait_timeout.

Trino offers the possibility to transparently redirect operations on an existing table to the appropriate catalog based on the format of the table and catalog configuration.

In the context of connectors which depend on a metastore service (for example, Hive connector, Iceberg connector and Delta Lake connector), the metastore (Hive metastore service, AWS Glue Data Catalog) can be used to accustom tables with different table formats. Therefore, a metastore database can hold a variety of tables with different table formats.

As a concrete example, let’s use the following simple scenario which makes use of table redirection:

The output of the EXPLAIN statement points out the actual catalog which is handling the SELECT query over the table example_table.

The table redirection functionality works also when using fully qualified names for the tables:

Trino offers table redirection support for the following operations:

Table read operations

Table write operations

Table management operations

Trino does not offer view redirection support.

The connector supports redirection from Hive tables to Iceberg, Delta Lake, and Hudi tables with the following catalog configuration properties:

hive.iceberg-catalog-name: Name of the catalog, configured with the Iceberg connector, to use for reading Iceberg tables.

hive.delta-lake-catalog-name: Name of the catalog, configured with the Delta Lake connector, to use for reading Delta Lake tables.

hive.hudi-catalog-name: Name of the catalog, configured with the Hudi connector, to use for reading Hudi tables.

The connector supports configuring and using file system caching.

The following table describes performance tuning properties for the Hive connector.

Performance tuning configuration properties are considered expert-level features. Altering these properties from their default values is likely to cause instability and performance degradation.

hive.max-outstanding-splits

The target number of buffered splits for each table scan in a query, before the scheduler tries to pause.

hive.max-outstanding-splits-size

The maximum size allowed for buffered splits for each table scan in a query, before the query fails.

hive.max-splits-per-second

The maximum number of splits generated per second per table scan. This can be used to reduce the load on the storage system. By default, there is no limit, which results in Trino maximizing the parallelization of data access.

hive.max-initial-splits

For each table scan, the coordinator first assigns file sections of up to max-initial-split-size. After max-initial-splits have been assigned, max-split-size is used for the remaining splits.

hive.max-initial-split-size

The size of a single file section assigned to a worker until max-initial-splits have been assigned. Smaller splits results in more parallelism, which gives a boost to smaller queries.

The largest size of a single file section assigned to a worker. Smaller splits result in more parallelism and thus can decrease latency, but also have more overhead and increase load on the system.

For security reasons, the sys system catalog is not accessible.

Hive’s timestamp with local zone data type is mapped to timestamp with time zone with UTC timezone. It only supports reading values - writing to tables with columns of this type is not supported.

Due to Hive issues HIVE-21002 and HIVE-22167, Trino does not correctly read TIMESTAMP values from Parquet, RCBinary, or Avro file formats created by Hive 3.1 or later. When reading from these file formats, Trino returns different results than Hive.

Trino does not support gathering table statistics for Hive transactional tables. You must use Hive to gather table statistics with ANALYZE statement after table creation.

**Examples:**

Example 1 (unknown):
```unknown
connector.name=hive
hive.metastore.uri=thrift://example.net:9083
fs.x.enabled=true
```

Example 2 (unknown):
```unknown
connector.name=hive
hive.metastore.uri=thrift://example.net:9083
fs.x.enabled=true
```

Example 3 (unknown):
```unknown
connector.name=hive
hive.metastore=glue
```

Example 4 (unknown):
```unknown
connector.name=hive
hive.metastore=glue
```

---

## Prometheus connector — Trino 478 Documentation

**URL:** https://trino.io/docs/current/connector/prometheus.html

**Contents:**
- Prometheus connector#
- Requirements#
- Configuration#
- Configuration properties#
- Not exhausting your Trino available heap#
- Bearer token authentication#
- Type mapping#
- SQL support#

The Prometheus connector allows reading Prometheus metrics as tables in Trino.

The mechanism for querying Prometheus is to use the Prometheus HTTP API. Specifically, all queries are resolved to Prometheus Instant queries with a form like: http://localhost:9090/api/v1/query?query=up[21d]&time=1568229904.000. In this case the up metric is taken from the Trino query table name, 21d is the duration of the query. The Prometheus time value corresponds to the TIMESTAMP field. Trino queries are translated from their use of the TIMESTAMP field to a duration and time value as needed. Trino splits are generated by dividing the query range into attempted equal chunks.

To query Prometheus, you need:

Network access from the Trino coordinator and workers to the Prometheus server. The default port is 9090.

Prometheus version 2.15.1 or later.

Create etc/catalog/example.properties to mount the Prometheus connector as the example catalog, replacing the properties as appropriate:

The following configuration properties are available:

Where to find Prometheus coordinator host.

http://localhost:9090

prometheus.query.chunk.size.duration

The duration of each query to Prometheus. The equivalent catalog session property is query_chunk_size_duration.

prometheus.max.query.range.duration

Width of overall query to Prometheus, will be divided into prometheus.query.chunk.size.duration queries. The equivalent catalog session property is max_query_range_duration.

How long values from this config file are cached.

prometheus.read-timeout

How much time a query to Prometheus has before timing out.

Username for basic authentication.

prometheus.auth.password

Password for basic authentication.

prometheus.auth.http.header.name

Name of the header to use for authorization.

prometheus.bearer.token.file

File holding bearer token if needed for access to Prometheus.

prometheus.read-timeout

How much time a query to Prometheus has before timing out.

prometheus.case-insensitive-name-matching

Match Prometheus metric names case insensitively.

prometheus.http.additional-headers

Additional headers to send to Prometheus endpoint. These headers must be comma-separated and delimited using :. For example, header1:value1,header2:value2 sends two headers header1 and header2 with the values as value1 and value2. Escape comma (,) or colon(:) characters in a header name or value with a backslash (\).

The prometheus.query.chunk.size.duration and prometheus.max.query.range.duration are values to protect Trino from too much data coming back from Prometheus. The prometheus.max.query.range.duration is the item of particular interest.

On a Prometheus instance that has been running for a while and depending on data retention settings, 21d might be far too much. Perhaps 1h might be a more reasonable setting. In the case of 1h it might be then useful to set prometheus.query.chunk.size.duration to 10m, dividing the query window into 6 queries each of which can be handled in a Trino split.

Primarily query issuers can limit the amount of data returned by Prometheus by taking advantage of WHERE clause limits on TIMESTAMP, setting an upper bound and lower bound that define a relatively small window. For example:

If the query does not include a WHERE clause limit, these config settings are meant to protect against an unlimited query.

Prometheus can be setup to require a Authorization header with every query. The value in prometheus.bearer.token.file allows for a bearer token to be read from the configured file. This file is optional and not required unless your Prometheus setup requires it. prometheus.auth.http.header.name allows you to use a custom header name for bearer token. Default value is Authorization.

Because Trino and Prometheus each support types that the other does not, this connector modifies some types when reading data.

The connector returns fixed columns that have a defined mapping to Trino types according to the following table:

TIMESTAMP(3) WITH TIMEZONE

No other types are supported.

The following example query result shows how the Prometheus up metric is represented in Trino:

The connector provides globally available and read operation statements to access data and metadata in Prometheus.

**Examples:**

Example 1 (unknown):
```unknown
connector.name=prometheus
prometheus.uri=http://localhost:9090
prometheus.query.chunk.size.duration=1d
prometheus.max.query.range.duration=21d
prometheus.cache.ttl=30s
prometheus.bearer.token.file=/path/to/bearer/token/file
prometheus.read-timeout=10s
```

Example 2 (unknown):
```unknown
connector.name=prometheus
prometheus.uri=http://localhost:9090
prometheus.query.chunk.size.duration=1d
prometheus.max.query.range.duration=21d
prometheus.cache.ttl=30s
prometheus.bearer.token.file=/path/to/bearer/token/file
prometheus.read-timeout=10s
```

Example 3 (unknown):
```unknown
SELECT * FROM example.default.up WHERE TIMESTAMP > (NOW() - INTERVAL '10' second);
```

Example 4 (unknown):
```unknown
SELECT * FROM example.default.up WHERE TIMESTAMP > (NOW() - INTERVAL '10' second);
```

---

## MariaDB connector — Trino 478 Documentation

**URL:** https://trino.io/docs/current/connector/mariadb.html

**Contents:**
- MariaDB connector#
- Requirements#
- Configuration#
  - Data source authentication#
  - General configuration properties#
  - Domain compaction threshold#
  - Case insensitive matching#
  - Fault-tolerant execution support#
- Querying MariaDB#
- Type mapping#

The MariaDB connector allows querying and creating tables in an external MariaDB database.

To connect to MariaDB, you need:

MariaDB version 10.10 or higher.

Network access from the Trino coordinator and workers to MariaDB. Port 3306 is the default port.

To configure the MariaDB connector, create a catalog properties file in etc/catalog named, for example, example.properties, to mount the MariaDB connector as the example catalog. Create the file with the following contents, replacing the connection properties as appropriate for your setup:

The connection-user and connection-password are typically required and determine the user credentials for the connection, often a service user. You can use secrets to avoid actual values in the catalog properties files.

The connector can provide credentials for the data source connection in multiple ways:

inline, in the connector configuration file

in a separate properties file

as extra credentials set when connecting to Trino

You can use secrets to avoid storing sensitive values in the catalog properties files.

The following table describes configuration properties for connection credentials:

credential-provider.type

Type of the credential provider. Must be one of INLINE, FILE, or KEYSTORE; defaults to INLINE.

Connection user name.

Name of the extra credentials property, whose value to use as the user name. See extraCredentials in Parameter reference.

password-credential-name

Name of the extra credentials property, whose value to use as the password.

connection-credential-file

Location of the properties file where credentials are present. It must contain the connection-user and connection-password properties.

The location of the Java Keystore file, from which to read credentials.

File format of the keystore file, for example JKS or PEM.

Password for the key store.

keystore-user-credential-name

Name of the key store entity to use as the user name.

keystore-user-credential-password

Password for the user name key store entity.

keystore-password-credential-name

Name of the key store entity to use as the password.

keystore-password-credential-password

Password for the password key store entity.

The following table describes general catalog configuration properties for the connector:

case-insensitive-name-matching

Support case insensitive schema and table names. Defaults to false.

case-insensitive-name-matching.cache-ttl

Duration for which case insensitive schema and table names are cached. Defaults to 1m.

case-insensitive-name-matching.config-file

Path to a name mapping configuration file in JSON format that allows Trino to disambiguate between schemas and tables with similar names in different cases. Defaults to null.

case-insensitive-name-matching.config-file.refresh-period

Frequency with which Trino checks the name matching configuration file for changes. The duration value defaults to 0s (refresh disabled).

Duration for which metadata, including table and column statistics, is cached. Defaults to 0s (caching disabled).

metadata.cache-missing

Cache the fact that metadata, including table and column statistics, is not available. Defaults to false.

metadata.schemas.cache-ttl

Duration for which schema metadata is cached. Defaults to the value of metadata.cache-ttl.

metadata.tables.cache-ttl

Duration for which table metadata is cached. Defaults to the value of metadata.cache-ttl.

metadata.statistics.cache-ttl

Duration for which tables statistics are cached. Defaults to the value of metadata.cache-ttl.

metadata.cache-maximum-size

Maximum number of objects stored in the metadata cache. Defaults to 10000.

Maximum number of statements in a batched execution. Do not change this setting from the default. Non-default values may negatively impact performance. Defaults to 1000.

dynamic-filtering.enabled

Push down dynamic filters into JDBC queries. Defaults to true.

dynamic-filtering.wait-timeout

Maximum duration for which Trino waits for dynamic filters to be collected from the build side of joins before starting a JDBC query. Using a large timeout can potentially result in more detailed dynamic filters. However, it can also increase latency for some queries. Defaults to 20s.

Pushing down a large list of predicates to the data source can compromise performance. Trino compacts large predicates into a simpler range predicate by default to ensure a balance between performance and predicate pushdown. If necessary, the threshold for this compaction can be increased to improve performance when the data source is capable of taking advantage of large predicates. Increasing this threshold may improve pushdown of large dynamic filters. The domain-compaction-threshold catalog configuration property or the domain_compaction_threshold catalog session property can be used to adjust the default value of 256 for this threshold.

When case-insensitive-name-matching is set to true, Trino is able to query non-lowercase schemas and tables by maintaining a mapping of the lowercase name to the actual name in the remote system. However, if two schemas and/or tables have names that differ only in case (such as “customers” and “Customers”) then Trino fails to query them due to ambiguity.

In these cases, use the case-insensitive-name-matching.config-file catalog configuration property to specify a configuration file that maps these remote schemas and tables to their respective Trino schemas and tables. Additionally, the JSON file must include both the schemas and tables properties, even if only as empty arrays.

Queries against one of the tables or schemes defined in the mapping attributes are run against the corresponding remote entity. For example, a query against tables in the case_insensitive_1 schema is forwarded to the CaseSensitiveName schema and a query against case_insensitive_2 is forwarded to the cASEsENSITIVEnAME schema.

At the table mapping level, a query on case_insensitive_1.table_1 as configured above is forwarded to CaseSensitiveName.tablex, and a query on case_insensitive_1.table_2 is forwarded to CaseSensitiveName.TABLEX.

By default, when a change is made to the mapping configuration file, Trino must be restarted to load the changes. Optionally, you can set the case-insensitive-name-matching.config-file.refresh-period to have Trino refresh the properties without requiring a restart:

The connector supports Fault-tolerant execution of query processing. Read and write operations are both supported with any retry policy.

The MariaDB connector provides a schema for every MariaDB database. You can see the available MariaDB databases by running SHOW SCHEMAS:

If you have a MariaDB database named web, you can view the tables in this database by running SHOW TABLES:

You can see a list of the columns in the clicks table in the web database using either of the following:

Finally, you can access the clicks table in the web database:

If you used a different name for your catalog properties file, use that catalog name instead of example in the above examples.

Because Trino and MariaDB each support types that the other does not, this connector modifies some types when reading or writing data. Data types may not map the same way in both directions between Trino and the data source. Refer to the following sections for type mapping in each direction.

The connector maps MariaDB types to the corresponding Trino types according to the following table:

BOOL and BOOLEAN are aliases of TINYINT(1)

MariaDB stores the current timestamp by default. Enable explicit_defaults_for_timestamp to avoid implicit default values and use NULL as the default value.

No other types are supported.

The connector maps Trino types to the corresponding MariaDB types according to the following table:

Maps on VARCHAR of length 255 or less.

Maps on VARCHAR of length between 256 and 65535, inclusive.

Maps on VARCHAR of length between 65536 and 16777215, inclusive.

VARCHAR of length greater than 16777215 and unbounded VARCHAR map to LONGTEXT.

MariaDB stores the current timestamp by default. Enable explicit_defaults_for_timestamp <https://mariadb.com/docs/reference/mdb/system-variables/explicit_defaults_for_timestamp/>_ to avoid implicit default values and use NULL as the default value.

No other types are supported.

Complete list of MariaDB data types.

The following properties can be used to configure how data types from the connected data source are mapped to Trino data types and how the metadata is cached in Trino.

unsupported-type-handling

Configure how unsupported column data types are handled:

IGNORE, column is not accessible.

CONVERT_TO_VARCHAR, column is converted to unbounded VARCHAR.

The respective catalog session property is unsupported_type_handling.

jdbc-types-mapped-to-varchar

Allow forced mapping of comma separated lists of data types to convert to unbounded VARCHAR

The connector provides read access and write access to data and metadata in a MariaDB database. In addition to the globally available and read operation statements, the connector supports the following features:

INSERT, see also Non-transactional INSERT

UPDATE, see also UPDATE limitation

DELETE, see also DELETE limitation

The connector supports adding rows using INSERT statements. By default, data insertion is performed by writing data to a temporary table. You can skip this step to improve performance and write directly to the target table. Set the insert.non-transactional-insert.enabled catalog property or the corresponding non_transactional_insert catalog session property to true.

Note that with this property enabled, data can be corrupted in rare cases where exceptions occur during the insert operation. With transactions disabled, no rollback can be performed.

Only UPDATE statements with constant assignments and predicates are supported. For example, the following statement is supported because the values assigned are constants:

Arithmetic expressions, function calls, and other non-constant UPDATE statements are not supported. For example, the following statement is not supported because arithmetic expressions cannot be used with the SET command:

All column values of a table row cannot be updated simultaneously. For a three column table, the following statement is not supported:

If a WHERE clause is specified, the DELETE operation only works if the predicate in the clause can be fully pushed down to the data source.

Flush JDBC metadata caches. For example, the following system call flushes the metadata caches for all schemas in the example catalog

The execute procedure allows you to execute a query in the underlying data source directly. The query must use supported syntax of the connected data source. Use the procedure to access features which are not available in Trino or to execute queries that return no result set and therefore can not be used with the query or raw_query pass-through table function. Typical use cases are statements that create or alter objects, and require native feature such as constraints, default values, automatic identifier creation, or indexes. Queries can also invoke statements that insert, update, or delete data, and do not return any data as a result.

The query text is not parsed by Trino, only passed through, and therefore only subject to any security or access control of the underlying data source.

The following example sets the current database to the example_schema of the example catalog. Then it calls the procedure in that schema to drop the default value from your_column on your_table table using the standard SQL syntax in the parameter value assigned for query:

Verify that the specific database supports this syntax, and adapt as necessary based on the documentation for the specific connected database and database version.

The connector provides specific table functions to access MariaDB.

The query function allows you to query the underlying database directly. It requires syntax native to MariaDB, because the full query is pushed down and processed in MariaDB. This can be useful for accessing native features which are not available in Trino or for improving query performance in situations where running a query natively may be faster.

The native query passed to the underlying data source is required to return a table as a result set. Only the data source performs validation or security checks for these queries using its own configuration. Trino does not perform these tasks. Only use passthrough queries to read data.

As an example, query the example catalog and select the age of employees by using TIMESTAMPDIFF and CURDATE:

The query engine does not preserve the order of the results of this function. If the passed query contains an ORDER BY clause, the function result may not be ordered as expected.

The connector includes a number of performance improvements, detailed in the following sections.

The MariaDB connector can use table and column statistics for cost based optimizations to improve query processing performance based on the actual data in the data source.

The statistics are collected by MariaDB and retrieved by the connector.

To collect statistics for a table, execute the following statement in MariaDB.

Refer to MariaDB documentation for additional information.

The connector supports pushdown for a number of operations:

Aggregate pushdown for the following functions:

The connector performs pushdown where performance may be improved, but in order to preserve correctness an operation may not be pushed down. When pushdown of an operation may result in better performance but risks correctness, the connector prioritizes correctness.

The connector does not support pushdown of any predicates on columns with textual types like CHAR or VARCHAR. This ensures correctness of results since the data source may compare strings case-insensitively.

In the following example, the predicate is not pushed down for either query since name is a column of type VARCHAR:

**Examples:**

Example 1 (unknown):
```unknown
connector.name=mariadb
connection-url=jdbc:mariadb://example.net:3306
connection-user=root
connection-password=secret
```

Example 2 (unknown):
```unknown
connector.name=mariadb
connection-url=jdbc:mariadb://example.net:3306
connection-user=root
connection-password=secret
```

Example 3 (unknown):
```unknown
{
  "schemas": [
    {
      "remoteSchema": "CaseSensitiveName",
      "mapping": "case_insensitive_1"
    },
    {
      "remoteSchema": "cASEsENSITIVEnAME",
      "mapping": "case_insensitive_2"
    }],
  "tables": [
    {
      "remoteSchema": "CaseSensitiveName",
      "remoteTable": "tablex",
      "mapping": "table_1"
    },
    {
      "remoteSchema": "CaseSensitiveName",
      "remoteTable": "TABLEX",
      "mapping": "table_2"
    }]
}
```

Example 4 (unknown):
```unknown
{
  "schemas": [
    {
      "remoteSchema": "CaseSensitiveName",
      "mapping": "case_insensitive_1"
    },
    {
      "remoteSchema": "cASEsENSITIVEnAME",
      "mapping": "case_insensitive_2"
    }],
  "tables": [
    {
      "remoteSchema": "CaseSensitiveName",
      "remoteTable": "tablex",
      "mapping": "table_1"
    },
    {
      "remoteSchema": "CaseSensitiveName",
      "remoteTable": "TABLEX",
      "mapping": "table_2"
    }]
}
```

---

## DuckDB connector — Trino 478 Documentation

**URL:** https://trino.io/docs/current/connector/duckdb.html

**Contents:**
- DuckDB connector#
- Requirements#
- Configuration#
  - Multiple DuckDB servers#
- Type mapping#
  - DuckDB type to Trino type mapping#
  - Trino type to DuckDB type mapping#
  - Type mapping configuration properties#
- SQL support#
  - Procedures#

The DuckDB connector allows querying and creating tables in an external DuckDB instance. This can be used to join data between different systems like DuckDB and Hive, or between two different DuckDB instances.

All cluster nodes must include libstdc++ as required by the DuckDB JDBC driver.

The path to the persistent DuckDB database must be identical and available on all cluster nodes and point to the same storage location.

The connector can query a DuckDB database. Create a catalog properties file that specifies the DuckDb connector by setting the connector.name to duckdb.

For example, to access a database as the example catalog, create the file etc/catalog/example.properties. Replace the connection properties as appropriate for your setup:

The connection-url defines the connection information and parameters to pass to the DuckDB JDBC driver. The parameters for the URL are available in the DuckDB JDBC driver documentation.

The <path> must point to an existing, persistent DuckDB database file. For example, use jdbc:duckdb:/opt/duckdb/trino.duckdb for a database created with the command duckdb /opt/duckdb/trino.duckdb. The database automatically contains the main schema and the information_schema schema. Use the main schema for your new tables or create a new schema.

When using the connector on a Trino cluster the path must be consistent on all nodes and point to a shared storage to ensure that all nodes operate on the same database.

Using an in-memory DuckDB database jdbc:duckdb: is not supported.

Refer to the DuckDB documentation for tips on securing DuckDB. Note that Trino connects to the database using the JDBC driver and does not use the DuckDB CLI.

The DuckDB connector can only access a single database within a DuckDB instance. Thus, if you have multiple DuckDB servers, or want to connect to multiple DuckDB servers, you must configure multiple instances of the DuckDB connector.

Because Trino and DuckDB each support types that the other does not, this connector modifies some types when reading or writing data. Data types may not map the same way in both directions between Trino and the data source. Refer to the following sections for type mapping in each direction.

List of DuckDB data types.

The connector maps DuckDB types to the corresponding Trino types following this table:

Default precision and scale are (18,3).

No other types are supported.

The connector maps Trino types to the corresponding DuckDB types following this table:

No other types are supported.

The following properties can be used to configure how data types from the connected data source are mapped to Trino data types and how the metadata is cached in Trino.

unsupported-type-handling

Configure how unsupported column data types are handled:

IGNORE, column is not accessible.

CONVERT_TO_VARCHAR, column is converted to unbounded VARCHAR.

The respective catalog session property is unsupported_type_handling.

jdbc-types-mapped-to-varchar

Allow forced mapping of comma separated lists of data types to convert to unbounded VARCHAR

The connector provides read access and write access to data and metadata in a DuckDB database. In addition to the globally available and read operation statements, the connector supports the following features:

Flush JDBC metadata caches. For example, the following system call flushes the metadata caches for all schemas in the example catalog

The execute procedure allows you to execute a query in the underlying data source directly. The query must use supported syntax of the connected data source. Use the procedure to access features which are not available in Trino or to execute queries that return no result set and therefore can not be used with the query or raw_query pass-through table function. Typical use cases are statements that create or alter objects, and require native feature such as constraints, default values, automatic identifier creation, or indexes. Queries can also invoke statements that insert, update, or delete data, and do not return any data as a result.

The query text is not parsed by Trino, only passed through, and therefore only subject to any security or access control of the underlying data source.

The following example sets the current database to the example_schema of the example catalog. Then it calls the procedure in that schema to drop the default value from your_column on your_table table using the standard SQL syntax in the parameter value assigned for query:

Verify that the specific database supports this syntax, and adapt as necessary based on the documentation for the specific connected database and database version.

The connector provides specific table functions to access DuckDB.

The query function allows you to query the underlying database directly. It requires syntax native to DuckDB, because the full query is pushed down and processed in DuckDB. This can be useful for accessing native features which are not available in Trino or for improving query performance in situations where running a query natively may be faster.

Find details about the SQL support of DuckDB that you can use in the query in the DuckDB SQL Command Reference and other statements and functions.

The native query passed to the underlying data source is required to return a table as a result set. Only the data source performs validation or security checks for these queries using its own configuration. Trino does not perform these tasks. Only use passthrough queries to read data.

As a simple example, query the example catalog and select an entire table:

The query engine does not preserve the order of the results of this function. If the passed query contains an ORDER BY clause, the function result may not be ordered as expected.

**Examples:**

Example 1 (unknown):
```unknown
connector.name=duckdb
connection-url=jdbc:duckdb:<path>
```

Example 2 (unknown):
```unknown
connector.name=duckdb
connection-url=jdbc:duckdb:<path>
```

Example 3 (unknown):
```unknown
USE example.example_schema;
CALL system.flush_metadata_cache();
```

Example 4 (unknown):
```unknown
USE example.example_schema;
CALL system.flush_metadata_cache();
```

---

## JMX connector — Trino 478 Documentation

**URL:** https://trino.io/docs/current/connector/jmx.html

**Contents:**
- JMX connector#
- Configuration#
- Querying JMX#
- SQL support#

The JMX connector provides the ability to query Java Management Extensions (JMX) information from all nodes in a Trino cluster. This is very useful for monitoring or debugging. JMX provides information about the Java Virtual Machine and all the software running inside it. Trino itself is heavily instrumented via JMX.

This connector can be configured so that chosen JMX information is periodically dumped and stored in memory for later access.

To configure the JMX connector, create a catalog properties file etc/catalog/example.properties with the following contents:

To enable periodical dumps, define the following properties:

dump-tables is a comma separated list of Managed Beans (MBean). It specifies which MBeans are sampled and stored in memory every dump-period. You can configure the maximum number of history entries with max-entries and it defaults to 86400. The time between dumps can be configured using dump-period and it defaults to 10s.

Commas in MBean names must be escaped using double backslashes (\\) in the following manner:

Double backslashes are required because a single backslash (\) is used to split the value across multiple lines in the following manner:

The JMX connector provides two schemas.

The first one is current that contains every MBean from every node in the Trino cluster. You can see all the available MBeans by running SHOW TABLES:

MBean names map to non-standard table names, and must be quoted with double quotes when referencing them in a query. For example, the following query shows the JVM version of every node:

The following query shows the open and maximum file descriptor counts for each node:

The wildcard character * may be used with table names in the current schema. This allows matching several MBean objects within a single query. The following query returns information from the different Trino memory pools on each node:

The history schema contains the list of tables configured in the connector properties file. The tables have the same columns as those in the current schema, but with an additional timestamp column that stores the time at which the snapshot was taken:

The connector provides globally available and read operation statements to access JMX information on your Trino nodes.

**Examples:**

Example 1 (unknown):
```unknown
connector.name=jmx
```

Example 2 (unknown):
```unknown
connector.name=jmx
```

Example 3 (unknown):
```unknown
connector.name=jmx
jmx.dump-tables=java.lang:type=Runtime,trino.execution.scheduler:name=NodeScheduler
jmx.dump-period=10s
jmx.max-entries=86400
```

Example 4 (unknown):
```unknown
connector.name=jmx
jmx.dump-tables=java.lang:type=Runtime,trino.execution.scheduler:name=NodeScheduler
jmx.dump-period=10s
jmx.max-entries=86400
```

---

## Redshift connector — Trino 478 Documentation

**URL:** https://trino.io/docs/current/connector/redshift.html

**Contents:**
- Redshift connector#
- Requirements#
- Configuration#
  - Connection security#
  - Data source authentication#
  - Multiple Redshift databases or clusters#
  - General configuration properties#
  - Appending query metadata#
  - Domain compaction threshold#
  - Case insensitive matching#

The Redshift connector allows querying and creating tables in an external Amazon Redshift cluster. This can be used to join data between different systems like Redshift and Hive, or between two different Redshift clusters.

To connect to Redshift, you need:

Network access from the Trino coordinator and workers to Redshift. Port 5439 is the default port.

To configure the Redshift connector, create a catalog properties file in etc/catalog named, for example, example.properties, to mount the Redshift connector as the example catalog. Create the file with the following contents, replacing the connection properties as appropriate for your setup:

The connection-user and connection-password are typically required and determine the user credentials for the connection, often a service user. You can use secrets to avoid actual values in the catalog properties files.

If you have TLS configured with a globally-trusted certificate installed on your data source, you can enable TLS between your cluster and the data source by appending a parameter to the JDBC connection string set in the connection-url catalog configuration property.

For example, on version 2.1 of the Redshift JDBC driver, TLS/SSL is enabled by default with the SSL parameter. You can disable or further configure TLS by appending parameters to the connection-url configuration property:

For more information on TLS configuration options, see the Redshift JDBC driver documentation.

The connector can provide credentials for the data source connection in multiple ways:

inline, in the connector configuration file

in a separate properties file

as extra credentials set when connecting to Trino

You can use secrets to avoid storing sensitive values in the catalog properties files.

The following table describes configuration properties for connection credentials:

credential-provider.type

Type of the credential provider. Must be one of INLINE, FILE, or KEYSTORE; defaults to INLINE.

Connection user name.

Name of the extra credentials property, whose value to use as the user name. See extraCredentials in Parameter reference.

password-credential-name

Name of the extra credentials property, whose value to use as the password.

connection-credential-file

Location of the properties file where credentials are present. It must contain the connection-user and connection-password properties.

The location of the Java Keystore file, from which to read credentials.

File format of the keystore file, for example JKS or PEM.

Password for the key store.

keystore-user-credential-name

Name of the key store entity to use as the user name.

keystore-user-credential-password

Password for the user name key store entity.

keystore-password-credential-name

Name of the key store entity to use as the password.

keystore-password-credential-password

Password for the password key store entity.

The Redshift connector can only access a single database within a Redshift cluster. Thus, if you have multiple Redshift databases, or want to connect to multiple Redshift clusters, you must configure multiple instances of the Redshift connector.

To add another catalog, simply add another properties file to etc/catalog with a different name, making sure it ends in .properties. For example, if you name the property file sales.properties, Trino creates a catalog named sales using the configured connector.

The following table describes general catalog configuration properties for the connector:

case-insensitive-name-matching

Support case insensitive schema and table names. Defaults to false.

case-insensitive-name-matching.cache-ttl

Duration for which case insensitive schema and table names are cached. Defaults to 1m.

case-insensitive-name-matching.config-file

Path to a name mapping configuration file in JSON format that allows Trino to disambiguate between schemas and tables with similar names in different cases. Defaults to null.

case-insensitive-name-matching.config-file.refresh-period

Frequency with which Trino checks the name matching configuration file for changes. The duration value defaults to 0s (refresh disabled).

Duration for which metadata, including table and column statistics, is cached. Defaults to 0s (caching disabled).

metadata.cache-missing

Cache the fact that metadata, including table and column statistics, is not available. Defaults to false.

metadata.schemas.cache-ttl

Duration for which schema metadata is cached. Defaults to the value of metadata.cache-ttl.

metadata.tables.cache-ttl

Duration for which table metadata is cached. Defaults to the value of metadata.cache-ttl.

metadata.statistics.cache-ttl

Duration for which tables statistics are cached. Defaults to the value of metadata.cache-ttl.

metadata.cache-maximum-size

Maximum number of objects stored in the metadata cache. Defaults to 10000.

Maximum number of statements in a batched execution. Do not change this setting from the default. Non-default values may negatively impact performance. Defaults to 1000.

dynamic-filtering.enabled

Push down dynamic filters into JDBC queries. Defaults to true.

dynamic-filtering.wait-timeout

Maximum duration for which Trino waits for dynamic filters to be collected from the build side of joins before starting a JDBC query. Using a large timeout can potentially result in more detailed dynamic filters. However, it can also increase latency for some queries. Defaults to 20s.

The optional parameter query.comment-format allows you to configure a SQL comment that is sent to the datasource with each query. The format of this comment can contain any characters and the following metadata:

$QUERY_ID: The identifier of the query.

$USER: The name of the user who submits the query to Trino.

$SOURCE: The identifier of the client tool used to submit the query, for example trino-cli.

$TRACE_TOKEN: The trace token configured with the client tool.

The comment can provide more context about the query. This additional information is available in the logs of the datasource. To include environment variables from the Trino cluster with the comment , use the ${ENV:VARIABLE-NAME} syntax.

The following example sets a simple comment that identifies each query sent by Trino:

With this configuration, a query such as SELECT * FROM example_table; is sent to the datasource with the comment appended:

The following example improves on the preceding example by using metadata:

If Jane sent the query with the query identifier 20230622_180528_00000_bkizg, the following comment string is sent to the datasource:

Certain JDBC driver settings and logging configurations might cause the comment to be removed.

Pushing down a large list of predicates to the data source can compromise performance. Trino compacts large predicates into a simpler range predicate by default to ensure a balance between performance and predicate pushdown. If necessary, the threshold for this compaction can be increased to improve performance when the data source is capable of taking advantage of large predicates. Increasing this threshold may improve pushdown of large dynamic filters. The domain-compaction-threshold catalog configuration property or the domain_compaction_threshold catalog session property can be used to adjust the default value of 256 for this threshold.

When case-insensitive-name-matching is set to true, Trino is able to query non-lowercase schemas and tables by maintaining a mapping of the lowercase name to the actual name in the remote system. However, if two schemas and/or tables have names that differ only in case (such as “customers” and “Customers”) then Trino fails to query them due to ambiguity.

In these cases, use the case-insensitive-name-matching.config-file catalog configuration property to specify a configuration file that maps these remote schemas and tables to their respective Trino schemas and tables. Additionally, the JSON file must include both the schemas and tables properties, even if only as empty arrays.

Queries against one of the tables or schemes defined in the mapping attributes are run against the corresponding remote entity. For example, a query against tables in the case_insensitive_1 schema is forwarded to the CaseSensitiveName schema and a query against case_insensitive_2 is forwarded to the cASEsENSITIVEnAME schema.

At the table mapping level, a query on case_insensitive_1.table_1 as configured above is forwarded to CaseSensitiveName.tablex, and a query on case_insensitive_1.table_2 is forwarded to CaseSensitiveName.TABLEX.

By default, when a change is made to the mapping configuration file, Trino must be restarted to load the changes. Optionally, you can set the case-insensitive-name-matching.config-file.refresh-period to have Trino refresh the properties without requiring a restart:

The connector supports Fault-tolerant execution of query processing. Read and write operations are both supported with any retry policy.

The Redshift connector provides a schema for every Redshift schema. You can see the available Redshift schemas by running SHOW SCHEMAS:

If you have a Redshift schema named web, you can view the tables in this schema by running SHOW TABLES:

You can see a list of the columns in the clicks table in the web database using either of the following:

Finally, you can access the clicks table in the web schema:

If you used a different name for your catalog properties file, use that catalog name instead of example in the above examples.

The following properties can be used to configure how data types from the connected data source are mapped to Trino data types and how the metadata is cached in Trino.

unsupported-type-handling

Configure how unsupported column data types are handled:

IGNORE, column is not accessible.

CONVERT_TO_VARCHAR, column is converted to unbounded VARCHAR.

The respective catalog session property is unsupported_type_handling.

jdbc-types-mapped-to-varchar

Allow forced mapping of comma separated lists of data types to convert to unbounded VARCHAR

The connector provides read access and write access to data and metadata in Redshift. In addition to the globally available and read operation statements, the connector supports the following features:

INSERT, see also Non-transactional INSERT

UPDATE, see also UPDATE limitation

DELETE, see also DELETE limitation

Schema and table management, see also:

ALTER TABLE RENAME TO limitation

ALTER SCHEMA limitation

The connector supports adding rows using INSERT statements. By default, data insertion is performed by writing data to a temporary table. You can skip this step to improve performance and write directly to the target table. Set the insert.non-transactional-insert.enabled catalog property or the corresponding non_transactional_insert catalog session property to true.

Note that with this property enabled, data can be corrupted in rare cases where exceptions occur during the insert operation. With transactions disabled, no rollback can be performed.

Only UPDATE statements with constant assignments and predicates are supported. For example, the following statement is supported because the values assigned are constants:

Arithmetic expressions, function calls, and other non-constant UPDATE statements are not supported. For example, the following statement is not supported because arithmetic expressions cannot be used with the SET command:

All column values of a table row cannot be updated simultaneously. For a three column table, the following statement is not supported:

If a WHERE clause is specified, the DELETE operation only works if the predicate in the clause can be fully pushed down to the data source.

The connector does not support renaming tables across multiple schemas. For example, the following statement is supported:

The following statement attempts to rename a table across schemas, and therefore is not supported:

The connector supports renaming a schema with the ALTER SCHEMA RENAME statement. ALTER SCHEMA SET AUTHORIZATION is not supported.

Flush JDBC metadata caches. For example, the following system call flushes the metadata caches for all schemas in the example catalog

The execute procedure allows you to execute a query in the underlying data source directly. The query must use supported syntax of the connected data source. Use the procedure to access features which are not available in Trino or to execute queries that return no result set and therefore can not be used with the query or raw_query pass-through table function. Typical use cases are statements that create or alter objects, and require native feature such as constraints, default values, automatic identifier creation, or indexes. Queries can also invoke statements that insert, update, or delete data, and do not return any data as a result.

The query text is not parsed by Trino, only passed through, and therefore only subject to any security or access control of the underlying data source.

The following example sets the current database to the example_schema of the example catalog. Then it calls the procedure in that schema to drop the default value from your_column on your_table table using the standard SQL syntax in the parameter value assigned for query:

Verify that the specific database supports this syntax, and adapt as necessary based on the documentation for the specific connected database and database version.

The connector provides specific table functions to access Redshift.

The query function allows you to query the underlying database directly. It requires syntax native to Redshift, because the full query is pushed down and processed in Redshift. This can be useful for accessing native features which are not implemented in Trino or for improving query performance in situations where running a query natively may be faster.

The native query passed to the underlying data source is required to return a table as a result set. Only the data source performs validation or security checks for these queries using its own configuration. Trino does not perform these tasks. Only use passthrough queries to read data.

For example, query the example catalog and select the top 10 nations by population:

The query engine does not preserve the order of the results of this function. If the passed query contains an ORDER BY clause, the function result may not be ordered as expected.

The connector includes a number of performance improvements, detailed in the following sections.

The connector supports the Redshift UNLOAD command to transfer data to Parquet files on S3. This enables parallel read of the data in Trino instead of the default, single-threaded JDBC-based connection to Redshift, used by the connector.

Configure the required S3 location with redshift.unload-location to enable the parallel read. Parquet files are automatically removed with query completion. The Redshift cluster and the configured S3 bucket must use the same AWS region.

redshift.unload-location

A writeable location in Amazon S3 in the same AWS region as the Redshift cluster. Used for temporary storage during query processing using the UNLOAD command from Redshift. To ensure cleanup even for failed automated removal, configure a life cycle policy to auto clean up the bucket regularly.

redshift.unload-iam-role

Optional. Fully specified ARN of the IAM Role attached to the Redshift cluster to use for the UNLOAD command. The role must have read access to the Redshift cluster and write access to the S3 bucket. Defaults to use the default IAM role attached to the Redshift cluster.

Use the unload_enabled catalog session property to deactivate the parallel read during a client session for a specific query, and potentially re-activate it again afterward.

Additionally, define further required S3 configuration such as IAM key, role, or region, except fs.native-s3.enabled,

**Examples:**

Example 1 (unknown):
```unknown
connector.name=redshift
connection-url=jdbc:redshift://example.net:5439/database
connection-user=root
connection-password=secret
```

Example 2 (unknown):
```unknown
connector.name=redshift
connection-url=jdbc:redshift://example.net:5439/database
connection-user=root
connection-password=secret
```

Example 3 (unknown):
```unknown
connection-url=jdbc:redshift://example.net:5439/database;SSL=TRUE;
```

Example 4 (unknown):
```unknown
connection-url=jdbc:redshift://example.net:5439/database;SSL=TRUE;
```

---

## Black Hole connector — Trino 478 Documentation

**URL:** https://trino.io/docs/current/connector/blackhole.html

**Contents:**
- Black Hole connector#
- Configuration#
- Examples#
- SQL support#

Primarily Black Hole connector is designed for high performance testing of other components. It works like the /dev/null device on Unix-like operating systems for data writing and like /dev/null or /dev/zero for data reading. However, it also has some other features that allow testing Trino in a more controlled manner. Metadata for any tables created via this connector is kept in memory on the coordinator and discarded when Trino restarts. Created tables are by default always empty, and any data written to them is ignored and data reads return no rows.

During table creation, a desired rows number can be specified. In such cases, writes behave in the same way, but reads always return the specified number of some constant rows. You shouldn’t rely on the content of such rows.

Create etc/catalog/example.properties to mount the blackhole connector as the example catalog, with the following contents:

Create a table using the blackhole connector:

Insert data into a table in the blackhole connector:

Select from the blackhole connector:

The above query always returns zero.

Create a table with a constant number of rows (500 * 1000 * 2000):

The above query returns 1,000,000,000.

Length of variable length columns can be controlled using the field_length table property (default value is equal to 16):

The consuming and producing rate can be slowed down using the page_processing_delay table property. Setting this property to 5s leads to a 5 second delay before consuming or producing a new page:

The connector provides globally available, read operation, and supports the following additional features:

The connector discards all written data. While read operations are supported, they return rows with all NULL values, with the number of rows controlled via table properties.

**Examples:**

Example 1 (unknown):
```unknown
connector.name=blackhole
```

Example 2 (unknown):
```unknown
connector.name=blackhole
```

Example 3 (unknown):
```unknown
CREATE TABLE example.test.nation AS
SELECT * from tpch.tiny.nation;
```

Example 4 (unknown):
```unknown
CREATE TABLE example.test.nation AS
SELECT * from tpch.tiny.nation;
```

---

## Loki connector — Trino 478 Documentation

**URL:** https://trino.io/docs/current/connector/loki.html

**Contents:**
- Loki connector#
- Requirements#
- Configuration#
- Type mapping#
  - Loki to Trino type mapping#
- SQL support#
  - Table functions#
  - query_range(varchar, timestamp, timestamp) -> table#
- Examples#

The Loki connector allows querying log data stored in Grafana Loki. This document describes how to configure a catalog with the Loki connector to run SQL queries against Loki.

To connect to Loki, you need:

Loki 3.2.0 or higher.

Network access from the Trino coordinator and workers to Loki. Port 3100 is the default port.

The connector can query log data in Loki. Create a catalog properties file that specifies the Loki connector by setting the connector.name to loki.

For example, to access a database as the example catalog, create the file etc/catalog/example.properties.

The following table contains a list of all available configuration properties.

The URI endpoint for the Loki server that Trino cluster nodes use to access the Loki APIs.

Duration that Trino waits for a result from Loki before the specific query request times out. Defaults to 10s. A minimum of 1s is required.

Because Trino and Loki each support types that the other does not, this connector modifies some types when reading data.

Each log line in Loki is split up by the connector into three columns:

These are separately mapped to Trino types:

TIMESTAMP WITH TIME ZONE

values for log queries

values for metrics queries

MAP with label names and values as VARCHAR key value pairs

No other types are supported.

The Loki connector does not provide access to any schema or tables. Instead you must use the query_range table function to return a table representation of the desired log data. Use the data in the returned table like any other table in a SQL query, including use of functions, joins, and other SQL functionality.

The connector provides the following table function to access Loki.

The query_range function allows you to query the log data in Loki with the following parameters:

The first parameter is a varchar string that uses valid LogQL query.

The second parameter is a timestamp formatted data and time representing the start date and time of the log data range to query.

The third parameter is a timestamp formatted data and time representing the end date and time of the log data range to query.

The table function is available in the system schema of the catalog using the Loki connector, and returns a table with the columns timestamp, value, and labels described in the Type mapping section.

The following query invokes the query_range table function in the example catalog. It uses the LogQL query string {origin="CA"} to retrieve all log data with the value CA for the origin label on the log entries. The timestamp parameters set a range of all log entries from the first of January 2025.

The query only returns the timestamp and value for each log entry, and omits the label data in the labels column. The value is a varchar string since the LoqQL query is a log query.

The following examples showcase combinations of LogQL queries passed through the table function with SQL accessing the data in the returned table.

The following query uses a metrics query and therefore returns a count column with double values, limiting the result data to the latest 100 values.

The following query accesses the value of the label named province and returns it as separate column.

**Examples:**

Example 1 (unknown):
```unknown
connector.name=loki
loki.uri=http://loki.example.com:3100
```

Example 2 (unknown):
```unknown
connector.name=loki
loki.uri=http://loki.example.com:3100
```

Example 3 (unknown):
```unknown
SELECT timestamp, value 
FROM
  TABLE(
    example.system.query_range(
      '{origin="CA"}',
      TIMESTAMP '2025-01-01 00:00:00',
      TIMESTAMP '2025-01-02 00:00:00'
    )
  )
;
```

Example 4 (unknown):
```unknown
SELECT timestamp, value 
FROM
  TABLE(
    example.system.query_range(
      '{origin="CA"}',
      TIMESTAMP '2025-01-01 00:00:00',
      TIMESTAMP '2025-01-02 00:00:00'
    )
  )
;
```

---

## Ignite connector — Trino 478 Documentation

**URL:** https://trino.io/docs/current/connector/ignite.html

**Contents:**
- Ignite connector#
- Requirements#
- Configuration#
  - Multiple Ignite servers#
  - General configuration properties#
  - Appending query metadata#
  - Domain compaction threshold#
  - Case insensitive matching#
- Table properties#
  - primary_key#

The Ignite connector allows querying an Apache Ignite database from Trino.

To connect to an Ignite server, you need:

Ignite version 2.9.0 or latter

Network access from the Trino coordinator and workers to the Ignite server. Port 10800 is the default port.

Specify --add-opens=java.base/java.nio=ALL-UNNAMED in the jvm.config when starting the Trino server.

The Ignite connector expose public schema by default.

The connector can query an Ignite instance. Create a catalog properties file that specifies the Ignite connector by setting the connector.name to ignite.

For example, to access an instance as example, create the file etc/catalog/example.properties. Replace the connection properties as appropriate for your setup:

The connection-url defines the connection information and parameters to pass to the Ignite JDBC driver. The parameters for the URL are available in the Ignite JDBC driver documentation. Some parameters can have adverse effects on the connector behavior or not work with the connector.

The connection-user and connection-password are typically required and determine the user credentials for the connection, often a service user. You can use secrets to avoid actual values in the catalog properties files.

If you have multiple Ignite servers you need to configure one catalog for each server. To add another catalog:

Add another properties file to etc/catalog

Save it with a different name that ends in .properties

For example, if you name the property file sales.properties, Trino uses the configured connector to create a catalog named sales.

The following table describes general catalog configuration properties for the connector:

case-insensitive-name-matching

Support case insensitive schema and table names. Defaults to false.

case-insensitive-name-matching.cache-ttl

Duration for which case insensitive schema and table names are cached. Defaults to 1m.

case-insensitive-name-matching.config-file

Path to a name mapping configuration file in JSON format that allows Trino to disambiguate between schemas and tables with similar names in different cases. Defaults to null.

case-insensitive-name-matching.config-file.refresh-period

Frequency with which Trino checks the name matching configuration file for changes. The duration value defaults to 0s (refresh disabled).

Duration for which metadata, including table and column statistics, is cached. Defaults to 0s (caching disabled).

metadata.cache-missing

Cache the fact that metadata, including table and column statistics, is not available. Defaults to false.

metadata.schemas.cache-ttl

Duration for which schema metadata is cached. Defaults to the value of metadata.cache-ttl.

metadata.tables.cache-ttl

Duration for which table metadata is cached. Defaults to the value of metadata.cache-ttl.

metadata.statistics.cache-ttl

Duration for which tables statistics are cached. Defaults to the value of metadata.cache-ttl.

metadata.cache-maximum-size

Maximum number of objects stored in the metadata cache. Defaults to 10000.

Maximum number of statements in a batched execution. Do not change this setting from the default. Non-default values may negatively impact performance. Defaults to 1000.

dynamic-filtering.enabled

Push down dynamic filters into JDBC queries. Defaults to true.

dynamic-filtering.wait-timeout

Maximum duration for which Trino waits for dynamic filters to be collected from the build side of joins before starting a JDBC query. Using a large timeout can potentially result in more detailed dynamic filters. However, it can also increase latency for some queries. Defaults to 20s.

The optional parameter query.comment-format allows you to configure a SQL comment that is sent to the datasource with each query. The format of this comment can contain any characters and the following metadata:

$QUERY_ID: The identifier of the query.

$USER: The name of the user who submits the query to Trino.

$SOURCE: The identifier of the client tool used to submit the query, for example trino-cli.

$TRACE_TOKEN: The trace token configured with the client tool.

The comment can provide more context about the query. This additional information is available in the logs of the datasource. To include environment variables from the Trino cluster with the comment , use the ${ENV:VARIABLE-NAME} syntax.

The following example sets a simple comment that identifies each query sent by Trino:

With this configuration, a query such as SELECT * FROM example_table; is sent to the datasource with the comment appended:

The following example improves on the preceding example by using metadata:

If Jane sent the query with the query identifier 20230622_180528_00000_bkizg, the following comment string is sent to the datasource:

Certain JDBC driver settings and logging configurations might cause the comment to be removed.

Pushing down a large list of predicates to the data source can compromise performance. Trino compacts large predicates into a simpler range predicate by default to ensure a balance between performance and predicate pushdown. If necessary, the threshold for this compaction can be increased to improve performance when the data source is capable of taking advantage of large predicates. Increasing this threshold may improve pushdown of large dynamic filters. The domain-compaction-threshold catalog configuration property or the domain_compaction_threshold catalog session property can be used to adjust the default value of 1000 for this threshold.

When case-insensitive-name-matching is set to true, Trino is able to query non-lowercase schemas and tables by maintaining a mapping of the lowercase name to the actual name in the remote system. However, if two schemas and/or tables have names that differ only in case (such as “customers” and “Customers”) then Trino fails to query them due to ambiguity.

In these cases, use the case-insensitive-name-matching.config-file catalog configuration property to specify a configuration file that maps these remote schemas and tables to their respective Trino schemas and tables. Additionally, the JSON file must include both the schemas and tables properties, even if only as empty arrays.

Queries against one of the tables or schemes defined in the mapping attributes are run against the corresponding remote entity. For example, a query against tables in the case_insensitive_1 schema is forwarded to the CaseSensitiveName schema and a query against case_insensitive_2 is forwarded to the cASEsENSITIVEnAME schema.

At the table mapping level, a query on case_insensitive_1.table_1 as configured above is forwarded to CaseSensitiveName.tablex, and a query on case_insensitive_1.table_2 is forwarded to CaseSensitiveName.TABLEX.

By default, when a change is made to the mapping configuration file, Trino must be restarted to load the changes. Optionally, you can set the case-insensitive-name-matching.config-file.refresh-period to have Trino refresh the properties without requiring a restart:

Table property usage example:

The following are supported Ignite table properties from https://ignite.apache.org/docs/latest/sql-reference/ddl

The primary key of the table, can choose multi columns as the table primary key. Table at least contains one column not in primary key.

This is a list of columns to be used as the table’s primary key. If not specified, a VARCHAR primary key column named DUMMY_ID is generated, the value is derived from the value generated by the UUID function in Ignite.

The following are supported Ignite SQL data types from https://ignite.apache.org/docs/latest/sql-reference/data-types

Ignite SQL data type name

-9223372036854775808, 9223372036854775807, etc.

Data type with fixed precision and scale

-2147483648, 2147483647, etc.

1972-01-01, 2021-07-15, etc.

Represents a byte array.

The connector provides read access and write access to data and metadata in Ignite. In addition to the globally available and read operation statements, the connector supports the following features:

INSERT, see also Non-transactional INSERT

UPDATE, see also UPDATE limitation

MERGE, see also Non-transactional MERGE

ALTER TABLE, see also ALTER TABLE RENAME TO limitation

The connector supports adding rows using INSERT statements. By default, data insertion is performed by writing data to a temporary table. You can skip this step to improve performance and write directly to the target table. Set the insert.non-transactional-insert.enabled catalog property or the corresponding non_transactional_insert catalog session property to true.

Note that with this property enabled, data can be corrupted in rare cases where exceptions occur during the insert operation. With transactions disabled, no rollback can be performed.

Only UPDATE statements with constant assignments and predicates are supported. For example, the following statement is supported because the values assigned are constants:

Arithmetic expressions, function calls, and other non-constant UPDATE statements are not supported. For example, the following statement is not supported because arithmetic expressions cannot be used with the SET command:

All column values of a table row cannot be updated simultaneously. For a three column table, the following statement is not supported:

The connector supports adding, updating, and deleting rows using MERGE statements, if the merge.non-transactional-merge.enabled catalog property or the corresponding non_transactional_merge_enabled catalog session property is set to true. Merge is only supported for directly modifying target tables.

In rare cases, exceptions may occur during the merge operation, potentially resulting in a partial update.

The connector does not support renaming tables across multiple schemas. For example, the following statement is supported:

The following statement attempts to rename a table across schemas, and therefore is not supported:

Flush JDBC metadata caches. For example, the following system call flushes the metadata caches for all schemas in the example catalog

The execute procedure allows you to execute a query in the underlying data source directly. The query must use supported syntax of the connected data source. Use the procedure to access features which are not available in Trino or to execute queries that return no result set and therefore can not be used with the query or raw_query pass-through table function. Typical use cases are statements that create or alter objects, and require native feature such as constraints, default values, automatic identifier creation, or indexes. Queries can also invoke statements that insert, update, or delete data, and do not return any data as a result.

The query text is not parsed by Trino, only passed through, and therefore only subject to any security or access control of the underlying data source.

The following example sets the current database to the example_schema of the example catalog. Then it calls the procedure in that schema to drop the default value from your_column on your_table table using the standard SQL syntax in the parameter value assigned for query:

Verify that the specific database supports this syntax, and adapt as necessary based on the documentation for the specific connected database and database version.

The connector supports pushdown for a number of operations:

Aggregate pushdown for the following functions:

The connector does not support pushdown of any predicates on columns with textual types like CHAR or VARCHAR. This ensures correctness of results since the data source may compare strings case-insensitively.

In the following example, the predicate is not pushed down for either query since name is a column of type VARCHAR:

**Examples:**

Example 1 (unknown):
```unknown
connector.name=ignite
connection-url=jdbc:ignite:thin://host1:10800/
connection-user=exampleuser
connection-password=examplepassword
```

Example 2 (unknown):
```unknown
connector.name=ignite
connection-url=jdbc:ignite:thin://host1:10800/
connection-user=exampleuser
connection-password=examplepassword
```

Example 3 (unknown):
```unknown
query.comment-format=Query sent by Trino.
```

Example 4 (unknown):
```unknown
query.comment-format=Query sent by Trino.
```

---

## SingleStore connector — Trino 478 Documentation

**URL:** https://trino.io/docs/current/connector/singlestore.html

**Contents:**
- SingleStore connector#
- Requirements#
- Configuration#
  - Connection security#
  - Multiple SingleStore servers#
  - General configuration properties#
  - Appending query metadata#
  - Domain compaction threshold#
  - Case insensitive matching#
- Querying SingleStore#

The SingleStore (formerly known as MemSQL) connector allows querying and creating tables in an external SingleStore database.

To connect to SingleStore, you need:

SingleStore version 7.8 or higher.

Network access from the Trino coordinator and workers to SingleStore. Port 3306 is the default port.

To configure the SingleStore connector, create a catalog properties file in etc/catalog named, for example, example.properties, to mount the SingleStore connector as the example catalog. Create the file with the following contents, replacing the connection properties as appropriate for your setup:

The connection-url defines the connection information and parameters to pass to the SingleStore JDBC driver. The supported parameters for the URL are available in the SingleStore JDBC driver documentation.

The connection-user and connection-password are typically required and determine the user credentials for the connection, often a service user. You can use secrets to avoid actual values in the catalog properties files.

If you have TLS configured with a globally-trusted certificate installed on your data source, you can enable TLS between your cluster and the data source by appending a parameter to the JDBC connection string set in the connection-url catalog configuration property.

Enable TLS between your cluster and SingleStore by appending the useSsl=true parameter to the connection-url configuration property:

For more information on TLS configuration options, see the JDBC driver documentation.

You can have as many catalogs as you need, so if you have additional SingleStore servers, simply add another properties file to etc/catalog with a different name (making sure it ends in .properties). For example, if you name the property file sales.properties, Trino will create a catalog named sales using the configured connector.

The following table describes general catalog configuration properties for the connector:

case-insensitive-name-matching

Support case insensitive schema and table names. Defaults to false.

case-insensitive-name-matching.cache-ttl

Duration for which case insensitive schema and table names are cached. Defaults to 1m.

case-insensitive-name-matching.config-file

Path to a name mapping configuration file in JSON format that allows Trino to disambiguate between schemas and tables with similar names in different cases. Defaults to null.

case-insensitive-name-matching.config-file.refresh-period

Frequency with which Trino checks the name matching configuration file for changes. The duration value defaults to 0s (refresh disabled).

Duration for which metadata, including table and column statistics, is cached. Defaults to 0s (caching disabled).

metadata.cache-missing

Cache the fact that metadata, including table and column statistics, is not available. Defaults to false.

metadata.schemas.cache-ttl

Duration for which schema metadata is cached. Defaults to the value of metadata.cache-ttl.

metadata.tables.cache-ttl

Duration for which table metadata is cached. Defaults to the value of metadata.cache-ttl.

metadata.statistics.cache-ttl

Duration for which tables statistics are cached. Defaults to the value of metadata.cache-ttl.

metadata.cache-maximum-size

Maximum number of objects stored in the metadata cache. Defaults to 10000.

Maximum number of statements in a batched execution. Do not change this setting from the default. Non-default values may negatively impact performance. Defaults to 1000.

dynamic-filtering.enabled

Push down dynamic filters into JDBC queries. Defaults to true.

dynamic-filtering.wait-timeout

Maximum duration for which Trino waits for dynamic filters to be collected from the build side of joins before starting a JDBC query. Using a large timeout can potentially result in more detailed dynamic filters. However, it can also increase latency for some queries. Defaults to 20s.

The optional parameter query.comment-format allows you to configure a SQL comment that is sent to the datasource with each query. The format of this comment can contain any characters and the following metadata:

$QUERY_ID: The identifier of the query.

$USER: The name of the user who submits the query to Trino.

$SOURCE: The identifier of the client tool used to submit the query, for example trino-cli.

$TRACE_TOKEN: The trace token configured with the client tool.

The comment can provide more context about the query. This additional information is available in the logs of the datasource. To include environment variables from the Trino cluster with the comment , use the ${ENV:VARIABLE-NAME} syntax.

The following example sets a simple comment that identifies each query sent by Trino:

With this configuration, a query such as SELECT * FROM example_table; is sent to the datasource with the comment appended:

The following example improves on the preceding example by using metadata:

If Jane sent the query with the query identifier 20230622_180528_00000_bkizg, the following comment string is sent to the datasource:

Certain JDBC driver settings and logging configurations might cause the comment to be removed.

Pushing down a large list of predicates to the data source can compromise performance. Trino compacts large predicates into a simpler range predicate by default to ensure a balance between performance and predicate pushdown. If necessary, the threshold for this compaction can be increased to improve performance when the data source is capable of taking advantage of large predicates. Increasing this threshold may improve pushdown of large dynamic filters. The domain-compaction-threshold catalog configuration property or the domain_compaction_threshold catalog session property can be used to adjust the default value of 256 for this threshold.

When case-insensitive-name-matching is set to true, Trino is able to query non-lowercase schemas and tables by maintaining a mapping of the lowercase name to the actual name in the remote system. However, if two schemas and/or tables have names that differ only in case (such as “customers” and “Customers”) then Trino fails to query them due to ambiguity.

In these cases, use the case-insensitive-name-matching.config-file catalog configuration property to specify a configuration file that maps these remote schemas and tables to their respective Trino schemas and tables. Additionally, the JSON file must include both the schemas and tables properties, even if only as empty arrays.

Queries against one of the tables or schemes defined in the mapping attributes are run against the corresponding remote entity. For example, a query against tables in the case_insensitive_1 schema is forwarded to the CaseSensitiveName schema and a query against case_insensitive_2 is forwarded to the cASEsENSITIVEnAME schema.

At the table mapping level, a query on case_insensitive_1.table_1 as configured above is forwarded to CaseSensitiveName.tablex, and a query on case_insensitive_1.table_2 is forwarded to CaseSensitiveName.TABLEX.

By default, when a change is made to the mapping configuration file, Trino must be restarted to load the changes. Optionally, you can set the case-insensitive-name-matching.config-file.refresh-period to have Trino refresh the properties without requiring a restart:

The SingleStore connector provides a schema for every SingleStore database. You can see the available SingleStore databases by running SHOW SCHEMAS:

If you have a SingleStore database named web, you can view the tables in this database by running SHOW TABLES:

You can see a list of the columns in the clicks table in the web database using either of the following:

Finally, you can access the clicks table in the web database:

If you used a different name for your catalog properties file, use that catalog name instead of example in the above examples.

Because Trino and Singlestore each support types that the other does not, this connector modifies some types when reading or writing data. Data types may not map the same way in both directions between Trino and the data source. Refer to the following sections for type mapping in each direction.

The connector maps Singlestore types to the corresponding Trino types following this table:

See Singlestore DECIMAL type handling

No other types are supported.

The connector maps Trino types to the corresponding Singlestore types following this table:

See Singlestore DECIMAL type handling

No other types are supported.

DECIMAL types with unspecified precision or scale are ignored unless the decimal-mapping configuration property or the decimal_mapping session property is set to allow_overflow. Then such types are mapped to a Trino DECIMAL with a default precision of 38 and default scale of 0. To change the scale of the resulting type, use the decimal-default-scale configuration property or the decimal_default_scale session property. The precision is always 38.

By default, values that require rounding or truncation to fit will cause a failure at runtime. This behavior is controlled via the decimal-rounding-mode configuration property or the decimal_rounding_mode session property, which can be set to UNNECESSARY (the default), UP, DOWN, CEILING, FLOOR, HALF_UP, HALF_DOWN, or HALF_EVEN (see RoundingMode).

The following properties can be used to configure how data types from the connected data source are mapped to Trino data types and how the metadata is cached in Trino.

unsupported-type-handling

Configure how unsupported column data types are handled:

IGNORE, column is not accessible.

CONVERT_TO_VARCHAR, column is converted to unbounded VARCHAR.

The respective catalog session property is unsupported_type_handling.

jdbc-types-mapped-to-varchar

Allow forced mapping of comma separated lists of data types to convert to unbounded VARCHAR

The connector provides read access and write access to data and metadata in a SingleStore database. In addition to the globally available and read operation statements, the connector supports the following features:

INSERT, see also Non-transactional INSERT

UPDATE, see also UPDATE limitation

DELETE, see also DELETE limitation

ALTER TABLE, see also ALTER TABLE RENAME TO limitation

The connector supports adding rows using INSERT statements. By default, data insertion is performed by writing data to a temporary table. You can skip this step to improve performance and write directly to the target table. Set the insert.non-transactional-insert.enabled catalog property or the corresponding non_transactional_insert catalog session property to true.

Note that with this property enabled, data can be corrupted in rare cases where exceptions occur during the insert operation. With transactions disabled, no rollback can be performed.

Only UPDATE statements with constant assignments and predicates are supported. For example, the following statement is supported because the values assigned are constants:

Arithmetic expressions, function calls, and other non-constant UPDATE statements are not supported. For example, the following statement is not supported because arithmetic expressions cannot be used with the SET command:

All column values of a table row cannot be updated simultaneously. For a three column table, the following statement is not supported:

If a WHERE clause is specified, the DELETE operation only works if the predicate in the clause can be fully pushed down to the data source.

The connector does not support renaming tables across multiple schemas. For example, the following statement is supported:

The following statement attempts to rename a table across schemas, and therefore is not supported:

Flush JDBC metadata caches. For example, the following system call flushes the metadata caches for all schemas in the example catalog

The execute procedure allows you to execute a query in the underlying data source directly. The query must use supported syntax of the connected data source. Use the procedure to access features which are not available in Trino or to execute queries that return no result set and therefore can not be used with the query or raw_query pass-through table function. Typical use cases are statements that create or alter objects, and require native feature such as constraints, default values, automatic identifier creation, or indexes. Queries can also invoke statements that insert, update, or delete data, and do not return any data as a result.

The query text is not parsed by Trino, only passed through, and therefore only subject to any security or access control of the underlying data source.

The following example sets the current database to the example_schema of the example catalog. Then it calls the procedure in that schema to drop the default value from your_column on your_table table using the standard SQL syntax in the parameter value assigned for query:

Verify that the specific database supports this syntax, and adapt as necessary based on the documentation for the specific connected database and database version.

The connector includes a number of performance improvements, detailed in the following sections.

The connector supports pushdown for a number of operations:

The connector performs pushdown where performance may be improved, but in order to preserve correctness an operation may not be pushed down. When pushdown of an operation may result in better performance but risks correctness, the connector prioritizes correctness.

The join-pushdown.enabled catalog configuration property or join_pushdown_enabled catalog session property control whether the connector pushes down join operations. The property defaults to false, and enabling join pushdowns may negatively impact performance for some queries.

The connector does not support pushdown of any predicates on columns with textual types like CHAR or VARCHAR. This ensures correctness of results since the data source may compare strings case-insensitively.

In the following example, the predicate is not pushed down for either query since name is a column of type VARCHAR:

**Examples:**

Example 1 (unknown):
```unknown
connector.name=singlestore
connection-url=jdbc:singlestore://example.net:3306
connection-user=root
connection-password=secret
```

Example 2 (unknown):
```unknown
connector.name=singlestore
connection-url=jdbc:singlestore://example.net:3306
connection-user=root
connection-password=secret
```

Example 3 (unknown):
```unknown
connection-url=jdbc:singlestore://example.net:3306/?useSsl=true
```

Example 4 (unknown):
```unknown
connection-url=jdbc:singlestore://example.net:3306/?useSsl=true
```

---

## CALL — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/call.html

**Contents:**
- CALL#
- Synopsis#
- Description#
- Examples#

Procedures can be provided by connectors to perform data manipulation or administrative tasks. For example, the System connector defines a procedure for killing a running query.

Some connectors, such as the PostgreSQL connector, are for systems that have their own stored procedures. These stored procedures are separate from the connector-defined procedures discussed here and thus are not directly callable via CALL.

See connector documentation for details on available procedures.

Call a procedure using positional arguments:

Call a procedure using named arguments:

Call a procedure using a fully qualified name:

**Examples:**

Example 1 (javascript):
```javascript
CALL procedure_name ( [ name => ] expression [, ...] )
```

Example 2 (javascript):
```javascript
CALL procedure_name ( [ name => ] expression [, ...] )
```

Example 3 (unknown):
```unknown
CALL test(123, 'apple');
```

Example 4 (unknown):
```unknown
CALL test(123, 'apple');
```

---
