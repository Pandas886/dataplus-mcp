# Trino - Sql Language

**Pages:** 95

---

## EXPLAIN — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/explain.html

**Contents:**
- EXPLAIN#
- Synopsis#
- Description#
- Examples#
  - EXPLAIN (TYPE LOGICAL)#
  - EXPLAIN (TYPE LOGICAL, FORMAT JSON)#
  - EXPLAIN (TYPE DISTRIBUTED)#
  - EXPLAIN (TYPE DISTRIBUTED, FORMAT JSON)#
  - EXPLAIN (TYPE VALIDATE)#
  - EXPLAIN (TYPE IO)#

where option can be one of:

Show the logical or distributed execution plan of a statement, or validate the statement. The distributed plan is shown by default. Each plan fragment of the distributed plan is executed by a single or multiple Trino nodes. Fragments separation represent the data exchange between Trino nodes. Fragment type specifies how the fragment is executed by Trino nodes and how the data is distributed between fragments:

Fragment is executed on a single node.

Fragment is executed on a fixed number of nodes with the input data distributed using a hash function.

Fragment is executed on a fixed number of nodes with the input data distributed in a round-robin fashion.

Fragment is executed on a fixed number of nodes with the input data broadcasted to all nodes.

Fragment is executed on nodes where input splits are accessed.

Process the supplied query statement and create a logical plan in text format:

The output format is not guaranteed to be backward compatible across Trino versions.

Process the supplied query statement and create a logical plan in JSON format:

Process the supplied query statement and create a distributed plan in text format. The distributed plan splits the logical plan into stages, and therefore explicitly shows the data exchange between workers:

The output format is not guaranteed to be backward compatible across Trino versions.

Process the supplied query statement and create a distributed plan in JSON format. The distributed plan splits the logical plan into stages, and therefore explicitly shows the data exchange between workers:

Validate the supplied query statement for syntactical and semantic correctness. Returns true if the statement is valid:

If the statement is not correct because a syntax error, such as an unknown keyword, is found the error message details the problem:

Similarly if semantic issues are detected, such as an invalid object name nations instead of nation, the error message returns useful information:

Process the supplied query statement and create a plan with input and output details about the accessed objects in JSON format:

**Examples:**

Example 1 (unknown):
```unknown
EXPLAIN [ ( option [, ...] ) ] statement
```

Example 2 (unknown):
```unknown
EXPLAIN [ ( option [, ...] ) ] statement
```

Example 3 (unknown):
```unknown
FORMAT { TEXT | GRAPHVIZ | JSON }
TYPE { LOGICAL | DISTRIBUTED | VALIDATE | IO }
```

Example 4 (unknown):
```unknown
FORMAT { TEXT | GRAPHVIZ | JSON }
TYPE { LOGICAL | DISTRIBUTED | VALIDATE | IO }
```

---

## CREATE MATERIALIZED VIEW — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/create-materialized-view.html

**Contents:**
- CREATE MATERIALIZED VIEW#
- Synopsis#
- Description#
- Examples#
- See also#

Create and validate the definition of a new materialized view view_name of a SELECT query. You need to run the REFRESH MATERIALIZED VIEW statement after the creation to populate the materialized view with data. This materialized view is a physical manifestation of the query results at time of refresh. The data is stored, and can be referenced by future queries.

Queries accessing materialized views are typically faster than retrieving data from a view created with the same query. Any computation, aggregation, and other operation to create the data is performed once during refresh of the materialized views, as compared to each time of accessing the view. Multiple reads of view data over time, or by multiple users, all trigger repeated processing. This is avoided for materialized views.

The optional OR REPLACE clause causes the materialized view to be replaced if it already exists rather than raising an error.

The optional IF NOT EXISTS clause causes the materialized view only to be created if it does not exist yet.

Note that OR REPLACE and IF NOT EXISTS are mutually exclusive clauses.

The optional GRACE PERIOD clause specifies how long the query materialization is used for querying:

Within the grace period since last refresh, data retrieval is highly performant because the query materialization is used. However, the data may not be up to date with the base tables.

After the grace period has elapsed, the data of the materialized view is computed on-the-fly using the query. Retrieval is therefore slower, but the data is up to date with the base tables.

If not specified, the grace period defaults to infinity, and therefore all queries are within the grace period.

Every REFRESH MATERIALIZED VIEW operation resets the start time for the grace period.

The optional COMMENT clause causes a string comment to be stored with the metadata about the materialized view. The comment is displayed with the SHOW CREATE MATERIALIZED VIEW statement and is available in the table system.metadata.materialized_view_properties.

The optional WITH clause is used to define properties for the materialized view creation. Separate multiple property/value pairs by commas. The connector uses the properties as input parameters for the materialized view refresh operation. The supported properties are different for each connector and detailed in the SQL support section of the specific connector’s documentation.

After successful creation, all metadata about the materialized view is available in a system table.

Create a simple materialized view cancelled_orders over the orders table that only includes cancelled orders. Note that orderstatus is a numeric value that is potentially meaningless to a consumer, yet the name of the view clarifies the content:

Create or replace a materialized view order_totals_by_date that summarizes orders across all orders from all customers:

Create a materialized view for a catalog using the Iceberg connector, with a comment and partitioning on two fields in the storage:

Set multiple properties:

Show defined materialized view properties for all catalogs:

Show metadata about the materialized views in all catalogs:

DROP MATERIALIZED VIEW

SHOW CREATE MATERIALIZED VIEW

REFRESH MATERIALIZED VIEW

**Examples:**

Example 1 (unknown):
```unknown
CREATE [ OR REPLACE ] MATERIALIZED VIEW
[ IF NOT EXISTS ] view_name
[ GRACE PERIOD interval ]
[ COMMENT string ]
[ WITH properties ]
AS query
```

Example 2 (unknown):
```unknown
CREATE [ OR REPLACE ] MATERIALIZED VIEW
[ IF NOT EXISTS ] view_name
[ GRACE PERIOD interval ]
[ COMMENT string ]
[ WITH properties ]
AS query
```

Example 3 (unknown):
```unknown
CREATE MATERIALIZED VIEW cancelled_orders
AS
    SELECT orderkey, totalprice
    FROM orders
    WHERE orderstatus = 3;
```

Example 4 (unknown):
```unknown
CREATE MATERIALIZED VIEW cancelled_orders
AS
    SELECT orderkey, totalprice
    FROM orders
    WHERE orderstatus = 3;
```

---

## DROP TABLE — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/drop-table.html

**Contents:**
- DROP TABLE#
- Synopsis#
- Description#
- Examples#
- See also#

Drops an existing table.

The optional IF EXISTS clause causes the error to be suppressed if the table does not exist. The error is not suppressed if a Trino view with the same name exists.

Drop the table orders_by_date:

Drop the table orders_by_date if it exists:

ALTER TABLE, CREATE TABLE

**Examples:**

Example 1 (unknown):
```unknown
DROP TABLE  [ IF EXISTS ] table_name
```

Example 2 (unknown):
```unknown
DROP TABLE  [ IF EXISTS ] table_name
```

Example 3 (unknown):
```unknown
DROP TABLE orders_by_date
```

Example 4 (unknown):
```unknown
DROP TABLE orders_by_date
```

---

## SHOW GRANTS — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/show-grants.html

**Contents:**
- SHOW GRANTS#
- Synopsis#
- Description#
- Examples#
- Limitations#
- See also#

List the grants for the current user on the specified table in the current catalog.

If no table name is specified, the command lists the grants for the current user on all the tables in all schemas of the current catalog.

The command requires the current catalog to be set.

Ensure that authentication has been enabled before running any of the authorization commands.

List the grants for the current user on table orders:

List the grants for the current user on all the tables in all schemas of the current catalog:

Some connectors have no support for SHOW GRANTS. See connector documentation for more details.

GRANT privilege, REVOKE privilege

**Examples:**

Example 1 (unknown):
```unknown
SHOW GRANTS [ ON [ TABLE ] table_name ]
```

Example 2 (unknown):
```unknown
SHOW GRANTS [ ON [ TABLE ] table_name ]
```

Example 3 (unknown):
```unknown
SHOW GRANTS ON TABLE orders;
```

Example 4 (unknown):
```unknown
SHOW GRANTS ON TABLE orders;
```

---

## DESCRIBE INPUT — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/describe-input.html

**Contents:**
- DESCRIBE INPUT#
- Synopsis#
- Description#
- Examples#
- See also#

Lists the input parameters of a prepared statement along with the position and type of each parameter. Parameter types that cannot be determined will appear as unknown.

Prepare and describe a query with three parameters:

Prepare and describe a query with no parameters:

**Examples:**

Example 1 (unknown):
```unknown
DESCRIBE INPUT statement_name
```

Example 2 (unknown):
```unknown
DESCRIBE INPUT statement_name
```

Example 3 (unknown):
```unknown
PREPARE my_select1 FROM
SELECT ? FROM nation WHERE regionkey = ? AND name < ?;
```

Example 4 (unknown):
```unknown
PREPARE my_select1 FROM
SELECT ? FROM nation WHERE regionkey = ? AND name < ?;
```

---

## SHOW SCHEMAS — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/show-schemas.html

**Contents:**
- SHOW SCHEMAS#
- Synopsis#
- Description#

List the schemas in catalog or in the current catalog.

Specify a pattern in the optional LIKE clause to filter the results to the desired subset. For example, the following query allows you to find schemas that have 3 as the third character:

**Examples:**

Example 1 (unknown):
```unknown
SHOW SCHEMAS [ FROM catalog ] [ LIKE pattern ]
```

Example 2 (unknown):
```unknown
SHOW SCHEMAS [ FROM catalog ] [ LIKE pattern ]
```

Example 3 (unknown):
```unknown
SHOW SCHEMAS FROM tpch LIKE '__3%'
```

Example 4 (unknown):
```unknown
SHOW SCHEMAS FROM tpch LIKE '__3%'
```

---

## REFRESH MATERIALIZED VIEW — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/refresh-materialized-view.html

**Contents:**
- REFRESH MATERIALIZED VIEW#
- Synopsis#
- Description#
- See also#

Initially populate or refresh the data stored in the materialized view view_name. The materialized view must be defined with CREATE MATERIALIZED VIEW. Data is retrieved from the underlying tables accessed by the defined query.

The initial population of the materialized view is typically processing intensive since it reads the data from the source tables and performs physical write operations.

The refresh operation can be less intensive, if the underlying data has not changed and the connector has implemented a mechanism to be aware of that. The specific implementation and performance varies by connector used to create the materialized view.

CREATE MATERIALIZED VIEW

DROP MATERIALIZED VIEW

SHOW CREATE MATERIALIZED VIEW

**Examples:**

Example 1 (unknown):
```unknown
REFRESH MATERIALIZED VIEW view_name
```

Example 2 (unknown):
```unknown
REFRESH MATERIALIZED VIEW view_name
```

---

## SET ROLE — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/set-role.html

**Contents:**
- SET ROLE#
- Synopsis#
- Description#
- Limitations#
- See also#

SET ROLE sets the enabled role for the current session.

SET ROLE role enables a single specified role for the current session. For the SET ROLE role statement to succeed, the user executing it should have a grant for the given role.

SET ROLE ALL enables all roles that the current user has been granted for the current session.

SET ROLE NONE disables all the roles granted to the current user for the current session.

The optional IN catalog clause sets the role in a catalog as opposed to a system role.

Some connectors do not support role management. See connector documentation for more details.

CREATE ROLE, DROP ROLE, GRANT role, REVOKE role

**Examples:**

Example 1 (unknown):
```unknown
SET ROLE ( role | ALL | NONE )
[ IN catalog ]
```

Example 2 (unknown):
```unknown
SET ROLE ( role | ALL | NONE )
[ IN catalog ]
```

---

## DROP FUNCTION — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/drop-function.html

**Contents:**
- DROP FUNCTION#
- Synopsis#
- Description#
- Examples#
- See also#

Removes a catalog UDF. The value of udf_name must be fully qualified with catalog and schema location of the UDF, unless the default UDF storage catalog and schema are configured.

The data_types must be included for UDFs that use parameters to ensure the UDF with the correct name and parameter signature is removed.

The optional IF EXISTS clause causes the error to be suppressed if the function does not exist.

The following example removes the meaning_of_life UDF in the default schema of the example catalog:

If the UDF uses an input parameter, the type must be added:

If the default catalog and schema for UDF storage is configured, you can use the following more compact syntax:

User-defined functions

SQL environment properties

**Examples:**

Example 1 (unknown):
```unknown
DROP FUNCTION [ IF EXISTS ] udf_name ( [ [ parameter_name ] data_type [, ...] ] )
```

Example 2 (unknown):
```unknown
DROP FUNCTION [ IF EXISTS ] udf_name ( [ [ parameter_name ] data_type [, ...] ] )
```

Example 3 (unknown):
```unknown
DROP FUNCTION example.default.meaning_of_life();
```

Example 4 (unknown):
```unknown
DROP FUNCTION example.default.meaning_of_life();
```

---

## USE — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/use.html

**Contents:**
- USE#
- Synopsis#
- Description#
- Examples#

Update the session to use the specified catalog and schema. If a catalog is not specified, the schema is resolved relative to the current catalog.

**Examples:**

Example 1 (unknown):
```unknown
USE catalog.schema
USE schema
```

Example 2 (unknown):
```unknown
USE catalog.schema
USE schema
```

Example 3 (unknown):
```unknown
USE hive.finance;
USE information_schema;
```

Example 4 (unknown):
```unknown
USE hive.finance;
USE information_schema;
```

---

## SHOW CREATE FUNCTION — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/show-create-function.html

**Contents:**
- SHOW CREATE FUNCTION#
- Synopsis#
- Description#
- Examples#
- See also#

Show the SQL statement that creates the specified function.

Show the SQL that can be run to create the meaning_of_life function:

User-defined functions

SQL environment properties

**Examples:**

Example 1 (unknown):
```unknown
SHOW CREATE FUNCTION function_name
```

Example 2 (unknown):
```unknown
SHOW CREATE FUNCTION function_name
```

Example 3 (unknown):
```unknown
SHOW CREATE FUNCTION example.default.meaning_of_life;
```

Example 4 (unknown):
```unknown
SHOW CREATE FUNCTION example.default.meaning_of_life;
```

---

## CREATE VIEW — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/create-view.html

**Contents:**
- CREATE VIEW#
- Synopsis#
- Description#
- Security#
- Examples#
- See also#

Create a new view of a SELECT query. The view is a logical table that can be referenced by future queries. Views do not contain any data. Instead, the query stored by the view is executed every time the view is referenced by another query.

The optional OR REPLACE clause causes the view to be replaced if it already exists rather than raising an error.

In the default DEFINER security mode, tables referenced in the view are accessed using the permissions of the view owner (the creator or definer of the view) rather than the user executing the query. This allows providing restricted access to the underlying tables, for which the user may not be allowed to access directly.

In the INVOKER security mode, tables referenced in the view are accessed using the permissions of the user executing the query (the invoker of the view). A view created in this mode is simply a stored query.

Regardless of the security mode, the current_user function will always return the user executing the query and thus may be used within views to filter out rows or otherwise restrict access.

Create a simple view test over the orders table:

Create a view test_with_comment with a view comment:

Create a view orders_by_date that summarizes orders:

Create a view that replaces an existing view:

**Examples:**

Example 1 (unknown):
```unknown
CREATE [ OR REPLACE ] VIEW view_name
[ COMMENT view_comment ]
[ SECURITY { DEFINER | INVOKER } ]
AS query
```

Example 2 (unknown):
```unknown
CREATE [ OR REPLACE ] VIEW view_name
[ COMMENT view_comment ]
[ SECURITY { DEFINER | INVOKER } ]
AS query
```

Example 3 (unknown):
```unknown
CREATE VIEW test AS
SELECT orderkey, orderstatus, totalprice / 2 AS half
FROM orders
```

Example 4 (unknown):
```unknown
CREATE VIEW test AS
SELECT orderkey, orderstatus, totalprice / 2 AS half
FROM orders
```

---

## PREPARE — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/prepare.html

**Contents:**
- PREPARE#
- Synopsis#
- Description#
- Examples#
- See also#

Prepares a statement for execution at a later time. Prepared statements are queries that are saved in a session with a given name. The statement can include parameters in place of literals to be replaced at execution time. Parameters are represented by question marks.

Prepare a select query:

Prepare a select query that includes parameters. The values to compare with regionkey and nationkey will be filled in with the EXECUTE statement:

Prepare an insert query:

EXECUTE, DEALLOCATE PREPARE, EXECUTE IMMEDIATE, DESCRIBE INPUT, DESCRIBE OUTPUT

**Examples:**

Example 1 (unknown):
```unknown
PREPARE statement_name FROM statement
```

Example 2 (unknown):
```unknown
PREPARE statement_name FROM statement
```

Example 3 (unknown):
```unknown
PREPARE my_select1 FROM
SELECT * FROM nation;
```

Example 4 (unknown):
```unknown
PREPARE my_select1 FROM
SELECT * FROM nation;
```

---

## COMMENT — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/comment.html

**Contents:**
- COMMENT#
- Synopsis#
- Description#
- Examples#
- See also#

Set the comment for an object. The comment can be removed by setting the comment to NULL.

Change the comment for the users table to be master table:

Change the comment for the users view to be master view:

Change the comment for the users.name column to be full name:

**Examples:**

Example 1 (unknown):
```unknown
COMMENT ON ( TABLE | VIEW | COLUMN ) name IS 'comments'
```

Example 2 (unknown):
```unknown
COMMENT ON ( TABLE | VIEW | COLUMN ) name IS 'comments'
```

Example 3 (unknown):
```unknown
COMMENT ON TABLE users IS 'master table';
```

Example 4 (unknown):
```unknown
COMMENT ON TABLE users IS 'master table';
```

---

## DESCRIBE — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/describe.html

**Contents:**
- DESCRIBE#
- Synopsis#
- Description#

DESCRIBE is an alias for SHOW COLUMNS.

**Examples:**

Example 1 (unknown):
```unknown
DESCRIBE table_name
```

Example 2 (unknown):
```unknown
DESCRIBE table_name
```

---

## DROP BRANCH — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/drop-branch.html

**Contents:**
- DROP BRANCH#
- Synopsis#
- Description#
- Examples#
- See also#

Drops an existing branch.

The optional IF EXISTS clause causes the error to be suppressed if the branch does not exist.

Drop the branch audit in the table orders:

**Examples:**

Example 1 (unknown):
```unknown
DROP BRANCH [ IF EXISTS ] branch_name
IN TABLE table_name
```

Example 2 (unknown):
```unknown
DROP BRANCH [ IF EXISTS ] branch_name
IN TABLE table_name
```

Example 3 (unknown):
```unknown
DROP BRANCH audit IN TABLE orders
```

Example 4 (unknown):
```unknown
DROP BRANCH audit IN TABLE orders
```

---

## ITERATE — Trino 478 Documentation

**URL:** https://trino.io/docs/current/udf/sql/iterate.html

**Contents:**
- ITERATE#
- Synopsis#
- Description#
- Examples#
- See also#

The ITERATE statement allows processing of blocks in SQL user-defined functions to move processing back to the start of a context block. Contexts are defined by a label. If no label is found, the functions fails with an error message.

Further examples of varying complexity that cover usage of the ITERATE statement in combination with other statements are available in the Example SQL UDFs.

SQL user-defined functions

**Examples:**

Example 1 (unknown):
```unknown
ITERATE label
```

Example 2 (unknown):
```unknown
ITERATE label
```

Example 3 (unknown):
```unknown
FUNCTION count()
RETURNS bigint
BEGIN
  DECLARE a int DEFAULT 0;
  DECLARE b int DEFAULT 0;
  top: REPEAT
    SET a = a + 1;
    IF a <= 3 THEN
        ITERATE top;
    END IF;
    SET b = b + 1;
  RETURN b;
END
```

Example 4 (unknown):
```unknown
FUNCTION count()
RETURNS bigint
BEGIN
  DECLARE a int DEFAULT 0;
  DECLARE b int DEFAULT 0;
  top: REPEAT
    SET a = a + 1;
    IF a <= 3 THEN
        ITERATE top;
    END IF;
    SET b = b + 1;
  RETURN b;
END
```

---

## SET — Trino 478 Documentation

**URL:** https://trino.io/docs/current/udf/sql/set.html

**Contents:**
- SET#
- Synopsis#
- Description#
- Examples#
- See also#

Use the SET statement in SQL user-defined functions to assign a value to a variable, referenced by comma-separated identifiers. The value is determined by evaluating the expression after the = sign.

Before the assignment the variable must be defined with a DECLARE statement. The data type of the variable must be identical to the data type of evaluating the expression.

The following functions returns the value 1 after setting the counter variable multiple times to different values:

Further examples of varying complexity that cover usage of the SET statement in combination with other statements are available in the Example SQL UDFs.

SQL user-defined functions

**Examples:**

Example 1 (unknown):
```unknown
SET identifier = expression
```

Example 2 (unknown):
```unknown
SET identifier = expression
```

Example 3 (unknown):
```unknown
FUNCTION one()
  RETURNS int
  BEGIN
    DECLARE counter int DEFAULT 1;
    SET counter = 0;
    SET counter = counter + 2;
    SET counter = counter / counter;
    RETURN counter;
  END
```

Example 4 (unknown):
```unknown
FUNCTION one()
  RETURNS int
  BEGIN
    DECLARE counter int DEFAULT 1;
    SET counter = 0;
    SET counter = counter + 2;
    SET counter = counter / counter;
    RETURN counter;
  END
```

---

## CASE — Trino 478 Documentation

**URL:** https://trino.io/docs/current/udf/sql/case.html

**Contents:**
- CASE#
- Synopsis#
- Description#
- Examples#
- See also#

The CASE statement is an optional construct to allow conditional processing in SQL user-defined functions.

The WHEN clauses are evaluated sequentially, stopping after the first match, and therefore the order of the statements is significant. The statements of the ELSE clause are executed if none of the WHEN clauses match.

Unlike other languages like C or Java, SQL does not support case fall through, so processing stops at the end of the first matched case.

One or more WHEN clauses can be used.

The following example shows a simple CASE statement usage:

Further examples of varying complexity that cover usage of the CASE statement in combination with other statements are available in the Example SQL UDFs.

SQL user-defined functions

Conditional expressions using CASE

**Examples:**

Example 1 (unknown):
```unknown
CASE
  WHEN condition THEN statements
  [ ... ]
  [ ELSE statements ]
END CASE
```

Example 2 (unknown):
```unknown
CASE
  WHEN condition THEN statements
  [ ... ]
  [ ELSE statements ]
END CASE
```

Example 3 (unknown):
```unknown
CASE expression
  WHEN expression THEN statements
  [ ... ]
  [ ELSE statements ]
END
```

Example 4 (unknown):
```unknown
CASE expression
  WHEN expression THEN statements
  [ ... ]
  [ ELSE statements ]
END
```

---

## Lambda expressions — Trino 478 Documentation

**URL:** https://trino.io/docs/current/functions/lambda.html

**Contents:**
- Lambda expressions#
- Limitations#
- Examples#

Lambda expressions are anonymous functions which are passed as arguments to higher-order SQL functions.

Lambda expressions are written with ->:

Most SQL expressions can be used in a lambda body, with a few exceptions:

Subqueries are not supported: x -> 2 + (SELECT 3)

Aggregations are not supported: x -> max(y)

Obtain the squared elements of an array column with transform():

The function transform() can be also employed to safely cast the elements of an array to strings:

Besides the array column being manipulated, other columns can be captured as well within the lambda expression. The following statement provides a showcase of this feature for calculating the value of the linear function f(x) = ax + b with transform():

Find the array elements containing at least one value greater than 100 with any_match():

Capitalize the first word in a string via regexp_replace():

Lambda expressions can be also applied in aggregation functions. Following statement is a sample the overly complex calculation of the sum of all elements of a column by making use of reduce_agg():

**Examples:**

Example 1 (unknown):
```unknown
x -> x + 1
(x, y) -> x + y
x -> regexp_like(x, 'a+')
x -> x[1] / x[2]
x -> IF(x > 0, x, -x)
x -> COALESCE(x, 0)
x -> CAST(x AS JSON)
x -> x + TRY(1 / 0)
```

Example 2 (unknown):
```unknown
x -> x + 1
(x, y) -> x + y
x -> regexp_like(x, 'a+')
x -> x[1] / x[2]
x -> IF(x > 0, x, -x)
x -> COALESCE(x, 0)
x -> CAST(x AS JSON)
x -> x + TRY(1 / 0)
```

Example 3 (unknown):
```unknown
SELECT numbers,
       transform(numbers, n -> n * n) as squared_numbers
FROM (
    VALUES
        (ARRAY[1, 2]),
        (ARRAY[3, 4]),
        (ARRAY[5, 6, 7])
) AS t(numbers);
```

Example 4 (unknown):
```unknown
SELECT numbers,
       transform(numbers, n -> n * n) as squared_numbers
FROM (
    VALUES
        (ARRAY[1, 2]),
        (ARRAY[3, 4]),
        (ARRAY[5, 6, 7])
) AS t(numbers);
```

---

## START TRANSACTION — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/start-transaction.html

**Contents:**
- START TRANSACTION#
- Synopsis#
- Description#
- Examples#
- See also#

Start a new transaction for the current session.

**Examples:**

Example 1 (unknown):
```unknown
START TRANSACTION [ mode [, ...] ]
```

Example 2 (unknown):
```unknown
START TRANSACTION [ mode [, ...] ]
```

Example 3 (unknown):
```unknown
ISOLATION LEVEL { READ UNCOMMITTED | READ COMMITTED | REPEATABLE READ | SERIALIZABLE }
READ { ONLY | WRITE }
```

Example 4 (unknown):
```unknown
ISOLATION LEVEL { READ UNCOMMITTED | READ COMMITTED | REPEATABLE READ | SERIALIZABLE }
READ { ONLY | WRITE }
```

---

## SHOW FUNCTIONS — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/show-functions.html

**Contents:**
- SHOW FUNCTIONS#
- Synopsis#
- Description#
- Examples#
- See also#

List functions in schema or all functions in the current session path. This can include built-in functions, functions from a custom plugin, and User-defined functions.

For each function returned, the following information is displayed:

Use the optional FROM keyword to only list functions in a specific catalog and schema. The location in schema must be specified as cataglog_name.schema_name.

Specify a pattern in the optional LIKE clause to filter the results to the desired subset.

List all UDFs and plugin functions in the default schema of the example catalog:

List all functions with a name beginning with array:

List all functions with a name beginning with cf:

Functions and operators

User-defined functions

**Examples:**

Example 1 (unknown):
```unknown
SHOW FUNCTIONS [ FROM schema ] [ LIKE pattern ]
```

Example 2 (unknown):
```unknown
SHOW FUNCTIONS [ FROM schema ] [ LIKE pattern ]
```

Example 3 (unknown):
```unknown
SHOW FUNCTIONS FROM example.default;
```

Example 4 (unknown):
```unknown
SHOW FUNCTIONS FROM example.default;
```

---

## DENY — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/deny.html

**Contents:**
- DENY#
- Synopsis#
- Description#
- Examples#
- Limitations#
- See also#

Denies the specified privileges to the specified grantee.

Deny on a table rejects the specified privilege on all current and future columns of the table.

Deny on a schema rejects the specified privilege on all current and future columns of all current and future tables of the schema.

Deny INSERT and SELECT privileges on the table orders to user alice:

Deny DELETE privilege on the schema finance to user bob:

Deny SELECT privilege on the table orders to everyone:

Deny INSERT privilege on the audit branch of the orders table to user alice:

The system access controls as well as the connectors provided by default in Trino have no support for DENY.

GRANT privilege, REVOKE privilege, SHOW GRANTS

**Examples:**

Example 1 (unknown):
```unknown
DENY ( privilege [, ...] | ( ALL PRIVILEGES ) )
ON [ BRANCH branch_name IN ] ( table_name | TABLE table_name | SCHEMA schema_name)
TO ( user | USER user | ROLE role )
```

Example 2 (unknown):
```unknown
DENY ( privilege [, ...] | ( ALL PRIVILEGES ) )
ON [ BRANCH branch_name IN ] ( table_name | TABLE table_name | SCHEMA schema_name)
TO ( user | USER user | ROLE role )
```

Example 3 (unknown):
```unknown
DENY INSERT, SELECT ON orders TO alice;
```

Example 4 (unknown):
```unknown
DENY INSERT, SELECT ON orders TO alice;
```

---

## TRUNCATE — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/truncate.html

**Contents:**
- TRUNCATE#
- Synopsis#
- Description#
- Examples#

Delete all rows from a table.

Truncate the table orders:

**Examples:**

Example 1 (unknown):
```unknown
TRUNCATE TABLE table_name
```

Example 2 (unknown):
```unknown
TRUNCATE TABLE table_name
```

Example 3 (unknown):
```unknown
TRUNCATE TABLE orders;
```

Example 4 (unknown):
```unknown
TRUNCATE TABLE orders;
```

---

## UPDATE — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/update.html

**Contents:**
- UPDATE#
- Synopsis#
- Description#
- Examples#
- Limitations#

Update selected columns values in existing rows in a table.

The columns named in the column = expression assignments will be updated for all rows that match the WHERE condition. The values of all column update expressions for a matching row are evaluated before any column value is changed. When the type of the expression and the type of the column differ, the usual implicit CASTs, such as widening numeric fields, are applied to the UPDATE expression values.

Update the status of all purchases that haven’t been assigned a ship date:

Update the account manager and account assign date for all customers:

Update the manager to be the name of the employee who matches the manager ID:

Update the status of all purchases that haven’t been assigned a ship date in the audit branch:

Some connectors have limited or no support for UPDATE. See connector documentation for more details.

**Examples:**

Example 1 (unknown):
```unknown
UPDATE table_name [ @ branch_name ]
SET [ ( column = expression [, ... ] ) ] [ WHERE condition ]
```

Example 2 (unknown):
```unknown
UPDATE table_name [ @ branch_name ]
SET [ ( column = expression [, ... ] ) ] [ WHERE condition ]
```

Example 3 (unknown):
```unknown
UPDATE
  purchases
SET
  status = 'OVERDUE'
WHERE
  ship_date IS NULL;
```

Example 4 (unknown):
```unknown
UPDATE
  purchases
SET
  status = 'OVERDUE'
WHERE
  ship_date IS NULL;
```

---

## EXECUTE IMMEDIATE — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/execute-immediate.html

**Contents:**
- EXECUTE IMMEDIATE#
- Synopsis#
- Description#
- Examples#
- See also#

Executes a statement without the need to prepare or deallocate the statement. Parameter values are defined in the USING clause.

Execute a query with no parameters:

Execute a query with two parameters:

This is equivalent to:

EXECUTE, PREPARE, DEALLOCATE PREPARE

**Examples:**

Example 1 (unknown):
```unknown
EXECUTE IMMEDIATE `statement` [ USING parameter1 [ , parameter2, ... ] ]
```

Example 2 (unknown):
```unknown
EXECUTE IMMEDIATE `statement` [ USING parameter1 [ , parameter2, ... ] ]
```

Example 3 (unknown):
```unknown
EXECUTE IMMEDIATE
'SELECT name FROM nation';
```

Example 4 (unknown):
```unknown
EXECUTE IMMEDIATE
'SELECT name FROM nation';
```

---

## Teradata functions — Trino 478 Documentation

**URL:** https://trino.io/docs/current/functions/teradata.html

**Contents:**
- Teradata functions#
- String functions#
- Date functions#

These functions provide compatibility with Teradata SQL.

Returns the hexadecimal representation of the UTF-16BE encoding of the string.

Alias for strpos() function.

The functions in this section use a format string that is compatible with the Teradata datetime functions. The following table, based on the Teradata reference manual, describes the supported format specifiers:

Punctuation characters are ignored

Hour of the day (0-23)

Case insensitivity is not currently supported. All specifiers must be lowercase.

Formats timestamp as a string using format.

Parses string into a TIMESTAMP using format.

Parses string into a DATE using format.

---

## SHOW CREATE TABLE — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/show-create-table.html

**Contents:**
- SHOW CREATE TABLE#
- Synopsis#
- Description#
- Examples#
- See also#

Show the SQL statement that creates the specified table.

Show the SQL that can be run to create the orders table:

**Examples:**

Example 1 (unknown):
```unknown
SHOW CREATE TABLE table_name
```

Example 2 (unknown):
```unknown
SHOW CREATE TABLE table_name
```

Example 3 (unknown):
```unknown
SHOW CREATE TABLE sf1.orders;
```

Example 4 (unknown):
```unknown
SHOW CREATE TABLE sf1.orders;
```

---

## SQL environment properties — Trino 478 Documentation

**URL:** https://trino.io/docs/current/admin/properties-sql-environment.html

**Contents:**
- SQL environment properties#
- sql.forced-session-time-zone#
- sql.default-catalog#
- sql.default-schema#
- sql.default-function-catalog#
- sql.default-function-schema#
- sql.path#

SQL environment properties allow you to globally configure parameters relevant to all SQL queries and the context they are processed in.

Force the time zone for any query processing to the configured value, and therefore override the time zone of the client. The time zone must be specified as a string such as UTC or other valid values.

Set the default catalog for all clients. Any default catalog configuration provided by a client overrides this default.

Set the default schema for all clients. Must be set to a schema name that is valid for the default catalog. Any default schema configuration provided by a client overrides this default.

Set the default catalog for User-defined functions storage for all clients. The connector used in the catalog must support User-defined function management. Any usage of a fully qualified name for a UDF overrides this default.

The default catalog and schema for UDF storage must be configured together, and the resulting entry must be set as part of the path. For example, the following section for Config properties uses the functions schema in the brain catalog for UDF storage, and adds it as the only entry on the path:

Set the default schema for UDF storage for all clients. Must be set to a schema name that is valid for the default function catalog. Any usage of a fully qualified name for a UDF overrides this default.

Define the default collection of paths to functions or table functions in specific catalogs and schemas. Paths are specified as catalog_name.schema_name. Multiple paths must be separated by commas. Find more details about the path in SET PATH.

**Examples:**

Example 1 (unknown):
```unknown
sql.default-function-catalog=brain
sql.default-function-schema=default
sql.path=brain.default
```

Example 2 (unknown):
```unknown
sql.default-function-catalog=brain
sql.default-function-schema=default
sql.path=brain.default
```

---

## DROP VIEW — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/drop-view.html

**Contents:**
- DROP VIEW#
- Synopsis#
- Description#
- Examples#
- See also#

Drop an existing view.

The optional IF EXISTS clause causes the error to be suppressed if the view does not exist.

Drop the view orders_by_date:

Drop the view orders_by_date if it exists:

**Examples:**

Example 1 (unknown):
```unknown
DROP VIEW [ IF EXISTS ] view_name
```

Example 2 (unknown):
```unknown
DROP VIEW [ IF EXISTS ] view_name
```

Example 3 (unknown):
```unknown
DROP VIEW orders_by_date
```

Example 4 (unknown):
```unknown
DROP VIEW orders_by_date
```

---

## REPEAT — Trino 478 Documentation

**URL:** https://trino.io/docs/current/udf/sql/repeat.html

**Contents:**
- REPEAT#
- Synopsis#
- Description#
- Examples#
- See also#

The REPEAT UNTIL statement is an optional construct in SQL user-defined functions to allow processing of a block of statements as long as a condition is met. The condition is validated as a last step of each iteration.

The block of statements is processed at least once. After the first, and every subsequent processing the expression condidtion is validated. If the result is true, processing moves to END REPEAT and continues with the next statement in the function. If the result is false, the statements are processed again.

The optional label before the REPEAT keyword can be used to name the block.

Note that a WHILE statement is very similar, with the difference that for REPEAT the statements are processed at least once, and for WHILE blocks the statements might not be processed at all.

The following SQL UDF shows a UDF with a REPEAT statement that runs until the value of a is greater or equal to 10.

Since a is also the input value and it is increased before the check the UDF always returns 10 for input values of 9 or less, and the input value

1 for all higher values.

Following are a couple of example invocations with result and explanation:

Further examples of varying complexity that cover usage of the REPEAT statement in combination with other statements are available in the Example SQL UDFs.

SQL user-defined functions

**Examples:**

Example 1 (unknown):
```unknown
[label :] REPEAT
    statements
UNTIL condition
END REPEAT
```

Example 2 (unknown):
```unknown
[label :] REPEAT
    statements
UNTIL condition
END REPEAT
```

Example 3 (unknown):
```unknown
FUNCTION test_repeat(a bigint)
  RETURNS bigint
  BEGIN
    REPEAT
      SET a = a + 1;
    UNTIL a >= 10
    END REPEAT;
    RETURN a;
  END
```

Example 4 (unknown):
```unknown
FUNCTION test_repeat(a bigint)
  RETURNS bigint
  BEGIN
    REPEAT
      SET a = a + 1;
    UNTIL a >= 10
    END REPEAT;
    RETURN a;
  END
```

---

## DROP MATERIALIZED VIEW — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/drop-materialized-view.html

**Contents:**
- DROP MATERIALIZED VIEW#
- Synopsis#
- Description#
- Examples#
- See also#

Drop an existing materialized view view_name.

The optional IF EXISTS clause causes the error to be suppressed if the materialized view does not exist.

Drop the materialized view orders_by_date:

Drop the materialized view orders_by_date if it exists:

CREATE MATERIALIZED VIEW

SHOW CREATE MATERIALIZED VIEW

REFRESH MATERIALIZED VIEW

**Examples:**

Example 1 (unknown):
```unknown
DROP MATERIALIZED VIEW [ IF EXISTS ] view_name
```

Example 2 (unknown):
```unknown
DROP MATERIALIZED VIEW [ IF EXISTS ] view_name
```

Example 3 (unknown):
```unknown
DROP MATERIALIZED VIEW orders_by_date;
```

Example 4 (unknown):
```unknown
DROP MATERIALIZED VIEW orders_by_date;
```

---

## WHILE — Trino 478 Documentation

**URL:** https://trino.io/docs/current/udf/sql/while.html

**Contents:**
- WHILE#
- Synopsis#
- Description#
- Examples#
- See also#

The WHILE statement is an optional construct in SQL user-defined functions to allow processing of a block of statements as long as a condition is met. The condition is validated as a first step of each iteration.

The expression that defines the condition is evaluated at least once. If the result is true, processing moves to DO, through following statements and back to WHILE and the condition. If the result is false, processing moves to END WHILE and continues with the next statement in the function.

The optional label before the WHILE keyword can be used to name the block.

Note that a WHILE statement is very similar, with the difference that for REPEAT the statements are processed at least once, and for WHILE blocks the statements might not be processed at all.

Further examples of varying complexity that cover usage of the WHILE statement in combination with other statements are available in the Example SQL UDFs.

SQL user-defined functions

**Examples:**

Example 1 (unknown):
```unknown
[label :] WHILE condition DO
  statements
END WHILE
```

Example 2 (unknown):
```unknown
[label :] WHILE condition DO
  statements
END WHILE
```

Example 3 (unknown):
```unknown
WHILE p > 1 DO
  SET r = r * n;
  SET p = p - 1;
END WHILE;
```

Example 4 (unknown):
```unknown
WHILE p > 1 DO
  SET r = r * n;
  SET p = p - 1;
END WHILE;
```

---

## MATCH_RECOGNIZE — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/match-recognize.html

**Contents:**
- MATCH_RECOGNIZE#
- Synopsis#
- Description#
- Example#
- Partitioning and ordering#
- Row pattern measures#
- Rows per match#
- After match skip#
- Row pattern syntax#
  - concatenation#

The MATCH_RECOGNIZE clause is an optional subclause of the FROM clause. It is used to detect patterns in a set of rows. Patterns of interest are specified using row pattern syntax based on regular expressions. The input to pattern matching is a table, a view or a subquery. For each detected match, one or more rows are returned. They contain requested information about the match.

Row pattern matching is a powerful tool when analyzing complex sequences of events. The following examples show some of the typical use cases:

in trade applications, tracking trends or identifying customers with specific behavioral patterns

in shipping applications, tracking packages through all possible valid paths,

in financial applications, detecting unusual incidents, which might signal fraud

In the following example, the pattern describes a V-shape over the totalprice column. A match is found whenever orders made by a customer first decrease in price, and then increase past the starting point:

In the following sections, all subclauses of the MATCH_RECOGNIZE clause are explained with this example query.

The PARTITION BY clause allows you to break up the input table into separate sections, that are independently processed for pattern matching. Without a partition declaration, the whole input table is used. This behavior is analogous to the semantics of PARTITION BY clause in window specification. In the example, the orders table is partitioned by the custkey value, so that pattern matching is performed for all orders of a specific customer independently from orders of other customers.

The optional ORDER BY clause is generally useful to allow matching on an ordered data set. For example, sorting the input by orderdate allows for matching on a trend of changes over time.

The MEASURES clause allows to specify what information is retrieved from a matched sequence of rows.

A measure expression is a scalar expression whose value is computed based on a match. In the example, three row pattern measures are specified:

A.totalprice AS starting_price returns the price in the first row of the match, which is the only row associated with A according to the pattern.

LAST(B.totalprice) AS bottom_price returns the lowest price (corresponding to the bottom of the “V” in the pattern). It is the price in the last row associated with B, which is the last row of the descending section.

LAST(U.totalprice) AS top_price returns the highest price in the match. It is the price in the last row associated with C or D, which is also the final row of the match.

Measure expressions can refer to the columns of the input table. They also allow special syntax to combine the input information with the details of the match (see Row pattern recognition expressions).

Each measure defines an output column of the pattern recognition. The column can be referenced with the measure_name.

The MEASURES clause is optional. When no measures are specified, certain input columns (depending on ROWS PER MATCH clause) are the output of the pattern recognition.

This clause can be used to specify the quantity of output rows. There are two main options:

ONE ROW PER MATCH is the default option. For every match, a single row of output is produced. Output consists of PARTITION BY columns and measures. The output is also produced for empty matches, based on their starting rows. Rows that are unmatched (that is, neither included in some non-empty match, nor being the starting row of an empty match), are not included in the output.

For ALL ROWS PER MATCH, every row of a match produces an output row, unless it is excluded from the output by the exclusion syntax. Output consists of PARTITION BY columns, ORDER BY columns, measures and remaining columns from the input table. By default, empty matches are shown and unmatched rows are skipped, similarly as with the ONE ROW PER MATCH option. However, this behavior can be changed by modifiers:

shows empty matches and skips unmatched rows, like the default.

excludes empty matches from the output.

shows empty matches and produces additional output row for each unmatched row.

There are special rules for computing row pattern measures for empty matches and unmatched rows. They are explained in Evaluating expressions in empty matches and unmatched rows.

Unmatched rows can only occur when the pattern does not allow an empty match. Otherwise, they are considered as starting rows of empty matches. The option ALL ROWS PER MATCH WITH UNMATCHED ROWS is recommended when pattern recognition is expected to pass all input rows, and it is not certain whether the pattern allows an empty match.

The AFTER MATCH SKIP clause specifies where pattern matching resumes after a non-empty match is found.

The default option is:

With this option, pattern matching starts from the row after the last row of the match. Overlapping matches are not detected.

With the following option, pattern matching starts from the second row of the match:

In the example, if a V-shape is detected, further overlapping matches are found, starting from consecutive rows on the descending slope of the “V”. Skipping to the next row is the default behavior after detecting an empty match or unmatched row.

The following AFTER MATCH SKIP options allow to resume pattern matching based on the components of the pattern. Pattern matching starts from the last (default) or first row matched to a certain row pattern variable. It can be either a primary pattern variable (they are explained in Row pattern syntax) or a union variable:

It is forbidden to skip to the first row of the current match, because it results in an infinite loop. For example specifying AFTER MATCH SKIP TO A fails, because A is the first element of the pattern, and jumping back to it creates an infinite loop. Similarly, skipping to a pattern variable which is not present in the match causes failure.

All other options than the default AFTER MATCH SKIP PAST LAST ROW allow detection of overlapping matches. The combination of ALL ROWS PER MATCH WITH UNMATCHED ROWS with AFTER MATCH SKIP PAST LAST ROW is the only configuration that guarantees exactly one output row for each input row.

Row pattern is a form of a regular expression with some syntactical extensions specific to row pattern recognition. It is specified in the PATTERN clause:

The basic element of row pattern is a primary pattern variable. Like pattern matching in character strings searches for characters, pattern matching in row sequences searches for rows which can be “labeled” with certain primary pattern variables. A primary pattern variable has a form of an identifier and is defined by a boolean condition. This condition determines whether a particular input row can be mapped to this variable and take part in the match.

In the example PATTERN (A B+ C+ D+), there are four primary pattern variables: A, B, C, and D.

Row pattern syntax includes the following usage:

It is a sequence of components without operators between them. All components are matched in the same order as they are specified.

It is a sequence of components separated by |. Exactly one of the components is matched. In case when multiple components can be matched, the leftmost matching component is chosen.

It is equivalent to alternation of all permutations of its components. All components are matched in some order. If multiple matches are possible for different orderings of the components, the match is chosen based on the lexicographical order established by the order of components in the PERMUTE list. In the above example, the most preferred option is A B C, and the least preferred option is C B A.

Exclusion syntax is used to specify portions of the match to exclude from the output. It is useful in combination with the ALL ROWS PER MATCH option, when only certain sections of the match are interesting.

If you change the example to use ALL ROWS PER MATCH, and the pattern is modified to PATTERN (A {- B+ C+ -} D+), the result consists of the initial matched row and the trailing section of rows.

Specifying pattern exclusions does not affect the computation of expressions in MEASURES and DEFINE clauses. Exclusions also do not affect pattern matching. They have the same semantics as regular grouping with parentheses.

It is forbidden to specify pattern exclusions with the option ALL ROWS PER MATCH WITH UNMATCHED ROWS.

Pattern quantifiers allow to specify the desired number of repetitions of a sub-pattern in a match. They are appended after the relevant pattern component:

There are following row pattern quantifiers:

zero or more repetitions:

one or more repetitions:

zero or one repetition:

exact number of repetitions, specified by a non-negative integer number:

number of repetitions ranging between bounds, specified by non-negative integer numbers:

Specifying bounds is optional. If the left bound is omitted, it defaults to 0. So, {, 5} can be described as “between zero and five repetitions”. If the right bound is omitted, the number of accepted repetitions is unbounded. So, {5, } can be described as “at least five repetitions”. Also, {,} is equivalent to *.

Quantifiers are greedy by default. It means that higher number of repetitions is preferred over lower number. This behavior can be changed to reluctant by appending ? immediately after the quantifier. With {3, 5}, 3 repetitions is the least desired option and 5 repetitions – the most desired. With {3, 5}?, 3 repetitions are most desired. Similarly, ? prefers 1 repetition, while ?? prefers 0 repetitions.

As explained in Row pattern syntax, primary pattern variables are the basic elements of row pattern. In addition to primary pattern variables, you can define union variables. They are introduced in the SUBSET clause:

In the preceding example, union variable U is defined as union of primary variables C and D. Union variables are useful in MEASURES, DEFINE and AFTER MATCH SKIP clauses. They allow you to refer to set of rows matched to either primary variable from a subset.

With the pattern: PATTERN((A | B){5} C+) it cannot be determined upfront if the match contains any A or any B. A union variable can be used to access the last row matched to either A or B. Define SUBSET U = (A, B), and the expression LAST(U.totalprice) returns the value of the totalprice column from the last row mapped to either A or B. Also, AFTER MATCH SKIP TO LAST A or AFTER MATCH SKIP TO LAST B can result in failure if A or B is not present in the match. AFTER MATCH SKIP TO LAST U does not fail.

The DEFINE clause is where row pattern primary variables are defined. Each variable is associated with a boolean condition:

During pattern matching, when a certain variable is considered for the next step of the match, the boolean condition is evaluated in context of the current match. If the result is true, then the current row, “labeled” with the variable, becomes part of the match.

In the preceding example, assume that the pattern allows to match B at some point. There are some rows already matched to some pattern variables. Now, variable B is being considered for the current row. Before the match is made, the defining condition for B is evaluated. In this example, it is only true if the value of the totalprice column in the current row is lower than totalprice in the preceding row.

The mechanism of matching variables to rows shows the difference between pattern matching in row sequences and regular expression matching in text. In text, characters remain constantly in their positions. In row pattern matching, a row can be mapped to different variables in different matches, depending on the preceding part of the match, and even on the match number.

It is not required that every primary variable has a definition in the DEFINE clause. Variables not mentioned in the DEFINE clause are implicitly associated with true condition, which means that they can be matched to every row.

Boolean expressions in the DEFINE clause allow the same special syntax as expressions in the MEASURES clause. Details are explained in Row pattern recognition expressions.

Expressions in MEASURES and DEFINE clauses are scalar expressions evaluated over rows of the input table. They support special syntax, specific to pattern recognition context. They can combine input information with the information about the current match. Special syntax allows to access pattern variables assigned to rows, browse rows based on how they are matched, and refer to the sequential number of the match.

A column name prefixed with a pattern variable refers to values of this column in all rows matched to this variable, or to any variable from the subset in case of union variable. If a column name is not prefixed, it is considered as prefixed with the universal pattern variable, defined as union of all primary pattern variables. In other words, a non-prefixed column name refers to all rows of the current match.

It is forbidden to prefix a column name with a table name in the pattern recognition context.

The classifier function returns the primary pattern variable associated with the row. The return type is varchar. The optional argument is a pattern variable. It limits the rows of interest, the same way as with prefixed column references. The classifier function is particularly useful with a union variable as the argument. It allows you to determine which variable from the subset actually matched.

The match_number function returns the sequential number of the match within partition, starting from 1. Empty matches are assigned sequential numbers as well as non-empty matches. The return type is bigint.

In the above example, the first function navigates to the first row matched to pattern variable A, and then searches forward until it finds two more occurrences of variable A within the match. The result is the value of the totalprice column in that row.

In the above example, the last function navigates to the last row matched to pattern variable A, and then searches backwards until it finds two more occurrences of variable A within the match. The result is the value of the totalprice column in that row.

With the first and last functions the result is null, if the searched row is not found in the mach.

The second argument is optional. The default value is 0, which means that by default these functions navigate to the first or last row of interest. If specified, the second argument must be a non-negative integer number.

In the above example, the prev function navigates to the last row matched to pattern variable A, and then searches two rows backward. The result is the value of the totalprice column in that row.

In the above example, the next function navigates to the last row matched to pattern variable A, and then searches two rows forward. The result is the value of the totalprice column in that row.

With the prev and next functions, it is possible to navigate and retrieve values outside the match. If the navigation goes beyond partition bounds, the result is null.

The second argument is optional. The default value is 1, which means that by default these functions navigate to previous or next row. If specified, the second argument must be a non-negative integer number.

It is possible to nest logical navigation functions within physical navigation functions:

In case of nesting, first the logical navigation is performed. It establishes the starting row for the physical navigation. When both navigation operations succeed, the value is retrieved from the designated row.

Pattern navigation functions require at least one column reference or classifier function inside of their first argument. The following examples are correct:

It is also required that all column references and all classifier calls inside a pattern navigation function are consistent in referred pattern variables. They must all refer either to the same primary variable, the same union variable, or to the implicit universal pattern variable. The following examples are correct:

It is allowed to use aggregate functions in a row pattern recognition context. Aggregate functions are evaluated over all rows of the current match or over a subset of rows based on the matched pattern variables. The running and final semantics are supported, with running as the default.

The following expression returns the average value of the totalprice column for all rows matched to pattern variable A:

The following expression returns the average value of the totalprice column for all rows matched to pattern variables from subset U:

The following expression returns the average value of the totalprice column for all rows of the match:

In case when the aggregate function has multiple arguments, it is required that all arguments refer consistently to the same set of rows:

If an aggregate argument does not contain any column reference or classifier function, it does not refer to any pattern variable. In such a case other aggregate arguments determine the set of rows to aggregate over. If none of the arguments contains a pattern variable reference, the universal row pattern variable is implicit. This means that the aggregate function applies to all rows of the match:

Aggregate function arguments must not contain pattern navigation functions. Similarly, aggregate functions cannot be nested in pattern navigation functions.

It is allowed to use the classifier and match_number functions in aggregate function arguments. The following expression returns an array containing all matched pattern variables:

This is particularly useful in combination with the option ONE ROW PER MATCH. It allows to get all the components of the match while keeping the output size reduced.

Like other aggregate functions in a row pattern recognition context, the count function can be applied to all rows of the match, or to rows associated with certain row pattern variables:

The count function in a row pattern recognition context allows special syntax to support the count(*) behavior over a limited set of rows:

During pattern matching in a sequence of rows, one row after another is examined to determine if it fits the pattern. At any step, a partial match is known, but it is not yet known what rows will be added in the future or what pattern variables they will be mapped to. So, when evaluating a boolean condition in the DEFINE clause for the current row, only the preceding part of the match (plus the current row) is “visible”. This is the running semantics.

When evaluating expressions in the MEASURES clause, the match is complete. It is then possible to apply the final semantics. In the final semantics, the whole match is “visible” as from the position of the final row.

In the MEASURES clause, the running semantics can also be applied. When outputting information row by row (as in ALL ROWS PER MATCH), the running semantics evaluate expressions from the positions of consecutive rows.

The running and final semantics are denoted by the keywords: RUNNING and FINAL, preceding a logical navigation function first or last, or an aggregate function:

The running semantics is default in MEASURES and DEFINE clauses. FINAL can only be specified in the MEASURES clause.

With the option ONE ROW PER MATCH, row pattern measures are evaluated from the position of the final row in the match. Therefore, running and final semantics are the same.

An empty match occurs when the row pattern is successfully matched, but no pattern variables are assigned. The following pattern produces an empty match for every row:

When evaluating row pattern measures for an empty match:

all column references return null

all navigation operations return null

classifier function returns null

match_number function returns the sequential number of the match

all aggregate functions are evaluated over an empty set of rows

Like every match, an empty match has its starting row. All input values which are to be output along with the measures (as explained in Rows per match), are the values from the starting row.

An unmatched row is a row that is neither part of any non-empty match nor the starting row of an empty match. With the option ALL ROWS PER MATCH WITH UNMATCHED ROWS, a single output row is produced. In that row, all row pattern measures are null. All input values which are to be output along with the measures (as explained in Rows per match), are the values from the unmatched row. Using the match_number function as a measure can help differentiate between an empty match and unmatched row.

**Examples:**

Example 1 (unknown):
```unknown
MATCH_RECOGNIZE (
  [ PARTITION BY column [, ...] ]
  [ ORDER BY column [, ...] ]
  [ MEASURES measure_definition [, ...] ]
  [ rows_per_match ]
  [ AFTER MATCH skip_to ]
  PATTERN ( row_pattern )
  [ SUBSET subset_definition [, ...] ]
  DEFINE variable_definition [, ...]
  )
```

Example 2 (unknown):
```unknown
MATCH_RECOGNIZE (
  [ PARTITION BY column [, ...] ]
  [ ORDER BY column [, ...] ]
  [ MEASURES measure_definition [, ...] ]
  [ rows_per_match ]
  [ AFTER MATCH skip_to ]
  PATTERN ( row_pattern )
  [ SUBSET subset_definition [, ...] ]
  DEFINE variable_definition [, ...]
  )
```

Example 3 (unknown):
```unknown
SELECT * FROM orders MATCH_RECOGNIZE(
     PARTITION BY custkey
     ORDER BY orderdate
     MEASURES
              A.totalprice AS starting_price,
              LAST(B.totalprice) AS bottom_price,
              LAST(U.totalprice) AS top_price
     ONE ROW PER MATCH
     AFTER MATCH SKIP PAST LAST ROW
     PATTERN (A B+ C+ D+)
     SUBSET U = (C, D)
     DEFINE
              B AS totalprice < PREV(totalprice),
              C AS totalprice > PREV(totalprice) AND totalprice <= A.totalprice,
              D AS totalprice > PREV(totalprice)
     )
```

Example 4 (unknown):
```unknown
SELECT * FROM orders MATCH_RECOGNIZE(
     PARTITION BY custkey
     ORDER BY orderdate
     MEASURES
              A.totalprice AS starting_price,
              LAST(B.totalprice) AS bottom_price,
              LAST(U.totalprice) AS top_price
     ONE ROW PER MATCH
     AFTER MATCH SKIP PAST LAST ROW
     PATTERN (A B+ C+ D+)
     SUBSET U = (C, D)
     DEFINE
              B AS totalprice < PREV(totalprice),
              C AS totalprice > PREV(totalprice) AND totalprice <= A.totalprice,
              D AS totalprice > PREV(totalprice)
     )
```

---

## CREATE TABLE AS — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/create-table-as.html

**Contents:**
- CREATE TABLE AS#
- Synopsis#
- Description#
- Examples#
- See also#

Create a new table containing the result of a SELECT query. Use CREATE TABLE to create an empty table.

The optional OR REPLACE clause causes an existing table with the specified name to be replaced with the new table definition. Support for table replacement varies across connectors. Refer to the connector documentation for details.

The optional IF NOT EXISTS clause causes the error to be suppressed if the table already exists.

OR REPLACE and IF NOT EXISTS cannot be used together.

The optional WITH clause can be used to set properties on the newly created table. To list all available table properties, run the following query:

Create a new table orders_column_aliased with the results of a query and the given column names:

Create a new table orders_by_date that summarizes orders:

Create the table orders_by_date if it does not already exist:

Create a new empty_nation table with the same schema as nation and no data:

**Examples:**

Example 1 (unknown):
```unknown
CREATE [ OR REPLACE ] TABLE [ IF NOT EXISTS ] table_name [ ( column_alias, ... ) ]
[ COMMENT table_comment ]
[ WITH ( property_name = expression [, ...] ) ]
AS query
[ WITH [ NO ] DATA ]
```

Example 2 (unknown):
```unknown
CREATE [ OR REPLACE ] TABLE [ IF NOT EXISTS ] table_name [ ( column_alias, ... ) ]
[ COMMENT table_comment ]
[ WITH ( property_name = expression [, ...] ) ]
AS query
[ WITH [ NO ] DATA ]
```

Example 3 (unknown):
```unknown
SELECT * FROM system.metadata.table_properties
```

Example 4 (unknown):
```unknown
SELECT * FROM system.metadata.table_properties
```

---

## SQL statement support — Trino 478 Documentation

**URL:** https://trino.io/docs/current/language/sql-support.html

**Contents:**
- SQL statement support#
- Globally available statements#
  - Catalog management#
- Read operations#
- Write operations#
  - Data management#
  - Schema and table management#
  - View management#
  - Materialized view management#
  - User-defined function management#

The SQL statement support in Trino can be categorized into several topics. Many statements are part of the core engine and therefore available in all use cases. For example, you can always set session properties or inspect an explain plan and perform other actions with the globally available statements.

However, the details and architecture of the connected data sources can limit some SQL functionality. For example, if the data source does not support any write operations, then a DELETE statement cannot be executed against the data source.

Similarly, if the underlying system does not have any security concepts, SQL statements like CREATE ROLE cannot be supported by Trino and the connector.

The categories of these different topics are related to read operations, write operations, security operations and transactions.

Details of the support for specific statements is available with the documentation for each connector.

The following statements are implemented in the core engine and available with any connector:

The following statements are used to manage dynamic catalogs:

The following statements provide read access to data and metadata exposed by a connector accessing a data source. They are supported by all connectors:

SELECT including MATCH_RECOGNIZE

SHOW CREATE MATERIALIZED VIEW

The following statements provide write access to data and metadata exposed by a connector accessing a data source. Availability varies widely from connector to connector:

CREATE MATERIALIZED VIEW

ALTER MATERIALIZED VIEW

DROP MATERIALIZED VIEW

REFRESH MATERIALIZED VIEW

The following statements are used to manage Catalog user-defined functions:

The following statements provide security-related operations to security configuration, data, and metadata exposed by a connector accessing a data source. Most connectors do not support these operations:

The following statements manage transactions. Most connectors do not support transactions:

---

## SHOW CREATE VIEW — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/show-create-view.html

**Contents:**
- SHOW CREATE VIEW#
- Synopsis#
- Description#
- See also#

Show the SQL statement that creates the specified view.

**Examples:**

Example 1 (unknown):
```unknown
SHOW CREATE VIEW view_name
```

Example 2 (unknown):
```unknown
SHOW CREATE VIEW view_name
```

---

## JSON functions and operators — Trino 478 Documentation

**URL:** https://trino.io/docs/current/functions/json.html

**Contents:**
- JSON functions and operators#
- JSON path language#
  - JSON path syntax and semantics#
    - literals#
    - variables#
    - arithmetic binary expressions#
    - arithmetic unary expressions#
    - member accessor#
    - wildcard member accessor#
    - descendant member accessor#

The SQL standard describes functions and operators to process JSON data. They allow you to access JSON data according to its structure, generate JSON data, and store it persistently in SQL tables.

Importantly, the SQL standard imposes that there is no dedicated data type to represent JSON data in SQL. Instead, JSON data is represented as character or binary strings. Although Trino supports JSON type, it is not used or produced by the following functions.

Trino supports three functions for querying JSON data: json_exists, json_query, and json_value. Each of them is based on the same mechanism of exploring and processing JSON input using JSON path.

Trino also supports two functions for generating JSON data – json_array, and json_object.

The JSON path language is a special language, used exclusively by certain SQL operators to specify the query to perform on the JSON input. Although JSON path expressions are embedded in SQL queries, their syntax significantly differs from SQL. The semantics of predicates, operators, etc. in JSON path expressions generally follow the semantics of SQL. The JSON path language is case-sensitive for keywords and identifiers.

JSON path expressions are recursive structures. Although the name “path” suggests a linear sequence of operations going step by step deeper into the JSON structure, a JSON path expression is in fact a tree. It can access the input JSON item multiple times, in multiple ways, and combine the results. Moreover, the result of a JSON path expression is not a single item, but an ordered sequence of items. Each of the sub-expressions takes one or more input sequences, and returns a sequence as the result.

In the lax mode, most path operations first unnest all JSON arrays in the input sequence. Any divergence from this rule is mentioned in the following listing. Path modes are explained in JSON path modes.

The JSON path language features are divided into: literals, variables, arithmetic binary expressions, arithmetic unary expressions, and a group of operators collectively known as accessors.

They include exact and approximate numbers, and are interpreted as if they were SQL values.

They are enclosed in double quotes.

It has the semantics of the JSON null, not of SQL null. See Comparison rules.

It refers to the currently processed input of the JSON function.

It refers to a named parameter by its name.

current item variable

It is used inside the filter expression to refer to the currently processed item from the input sequence.

last subscript variable

It refers to the last index of the innermost enclosing array. Array indexes in JSON path expressions are zero-based.

The JSON path language supports five arithmetic binary operators:

Both operands, <path1> and <path2>, are evaluated to sequences of items. For arithmetic binary operators, each input sequence must contain a single numeric item. The arithmetic operation is performed according to SQL semantics, and it returns a sequence containing a single element with the result.

The operators follow the same precedence rules as in SQL arithmetic operations, and parentheses can be used for grouping.

The operand <path> is evaluated to a sequence of items. Every item must be a numeric value. The unary plus or minus is applied to every item in the sequence, following SQL semantics, and the results form the returned sequence.

The member accessor returns the value of the member with the specified key for each JSON object in the input sequence.

The condition when a JSON object does not have such a member is called a structural error. In the lax mode, it is suppressed, and the faulty object is excluded from the result.

Let <path> return a sequence of three JSON objects:

the expression <path>.customer succeeds in the first and the third object, but the second object lacks the required member. In strict mode, path evaluation fails. In lax mode, the second object is silently skipped, and the resulting sequence is 100, 300.

All items in the input sequence must be JSON objects.

Trino does not support JSON objects with duplicate keys.

Returns values from all key-value pairs for each JSON object in the input sequence. All the partial results are concatenated into the returned sequence.

Let <path> return a sequence of three JSON objects:

All items in the input sequence must be JSON objects.

The order of values returned from a single JSON object is arbitrary. The sub-sequences from all JSON objects are concatenated in the same order in which the JSON objects appear in the input sequence.

Returns the values associated with the specified key in all JSON objects on all levels of nesting in the input sequence.

The order of returned values is that of preorder depth first search. First, the enclosing object is visited, and then all child nodes are visited.

This method does not perform array unwrapping in the lax mode. The results are the same in the lax and strict modes. The method traverses into JSON arrays and JSON objects. Non-structural JSON items are skipped.

Let <path> be a sequence containing a JSON object:

Returns the elements at the specified indexes for each JSON array in the input sequence. Indexes are zero-based.

The <subscripts> list contains one or more subscripts. Each subscript specifies a single index or a range (ends inclusive):

In lax mode, any non-array items resulting from the evaluation of the input sequence are wrapped into single-element arrays. Note that this is an exception to the rule of automatic array wrapping.

Each array in the input sequence is processed in the following way:

The variable last is set to the last index of the array.

All subscript indexes are computed in order of declaration. For a singleton subscript <path1>, the result must be a singleton numeric item. For a range subscript <path2> to <path3>, two numeric items are expected.

The specified array elements are added in order to the output sequence.

Let <path> return a sequence of three JSON arrays:

The following expression returns a sequence containing the last element from every array:

The following expression returns the third and fourth element from every array:

Note that the first array does not have the fourth element, and the last array does not have the third or fourth element. Accessing non-existent elements is a structural error. In strict mode, it causes the path expression to fail. In lax mode, such errors are suppressed, and only the existing elements are returned.

Another example of a structural error is an improper range specification such as 5 to 3.

Note that the subscripts may overlap, and they do not need to follow the element order. The order in the returned sequence follows the subscripts:

Returns all elements of each JSON array in the input sequence.

In lax mode, any non-array items resulting from the evaluation of the input sequence are wrapped into single-element arrays. Note that this is an exception to the rule of automatic array wrapping.

The output order follows the order of the original JSON arrays. Also, the order of elements within the arrays is preserved.

Let <path> return a sequence of three JSON arrays:

Retrieves the items from the input sequence which satisfy the predicate.

JSON path predicates are syntactically similar to boolean expressions in SQL. However, the semantics are different in many aspects:

They operate on sequences of items.

They have their own error handling (they never fail).

They behave different depending on the lax or strict mode.

The predicate evaluates to true, false, or unknown. Note that some predicate expressions involve nested JSON path expression. When evaluating the nested path, the variable @ refers to the currently examined item from the input sequence.

The following predicate expressions are supported:

Returns true if the nested path evaluates to a non-empty sequence, and false when the nested path evaluates to an empty sequence. If the path evaluation throws an error, returns unknown.

starts with predicate

The nested <path> must evaluate to a sequence of textual items, and the other operand must evaluate to a single textual item. If evaluating of either operand throws an error, the result is unknown. All items from the sequence are checked for starting with the right operand. The result is true if a match is found, otherwise false. However, if any of the comparisons throws an error, the result in the strict mode is unknown. The result in the lax mode depends on whether the match or the error was found first.

Returns true if the nested predicate evaluates to unknown, and false otherwise.

Both operands of a comparison evaluate to sequences of items. If either evaluation throws an error, the result is unknown. Items from the left and right sequence are then compared pairwise. Similarly to the starts with predicate, the result is true if any of the comparisons returns true, otherwise false. However, if any of the comparisons throws an error, for example because the compared types are not compatible, the result in the strict mode is unknown. The result in the lax mode depends on whether the true comparison or the error was found first.

Null values in the context of comparison behave different than SQL null:

null != null, null < null, … –> false

null compared to a scalar value –> false

null compared to a JSON array or a JSON object –> false

When comparing two scalar values, true or false is returned if the comparison is successfully performed. The semantics of the comparison is the same as in SQL. In case of an error, e.g. comparing text and number, unknown is returned.

Comparing a scalar value with a JSON array or a JSON object, and comparing JSON arrays/objects is an error, so unknown is returned.

Let <path> return a sequence of three JSON objects:

The following accessors are collectively referred to as item methods.

Converts numeric or text values into double values.

Let <path> return a sequence -1, 23e4, "5.6":

Gets the ceiling, the floor or the absolute value for every numeric item in the sequence. The semantics of the operations is the same as in SQL.

Let <path> return a sequence -1.5, -1, 1.3:

Returns a collection of JSON objects including one object per every member of the original object for every JSON object in the sequence.

The returned objects have three members:

“name”, which is the original key,

“value”, which is the original bound value,

“id”, which is the unique number, specific to an input object.

Let <path> be a sequence of three JSON objects:

It is required that all items in the input sequence are JSON objects.

The order of the returned values follows the order of the original JSON objects. However, within objects, the order of returned entries is arbitrary.

Returns a textual value containing the type name for every item in the sequence.

This method does not perform array unwrapping in the lax mode.

The returned values are:

"null" for JSON null,

"number" for a numeric item,

"string" for a textual item,

"boolean" for a boolean item,

"date" for an item of type date,

"time without time zone" for an item of type time,

"time with time zone" for an item of type time with time zone,

"timestamp without time zone" for an item of type timestamp,

"timestamp with time zone" for an item of type timestamp with time zone,

"array" for JSON array,

"object" for JSON object,

Returns a numeric value containing the size for every JSON array in the sequence.

This method does not perform array unwrapping in the lax mode. Instead, all non-array items are wrapped in singleton JSON arrays, so their size is 1.

It is required that all items in the input sequence are JSON arrays.

Let <path> return a sequence of three JSON arrays:

The SQL standard describes the datetime() JSON path item method and the like_regex() JSON path predicate. Trino does not support them.

The JSON path expression can be evaluated in two modes: strict and lax. In the strict mode, it is required that the input JSON data strictly fits the schema required by the path expression. In the lax mode, the input JSON data can diverge from the expected schema.

The following table shows the differences between the two modes.

Performing an operation which requires a non-array on an array, e.g.:

$.key requires a JSON object

$.floor() requires a numeric value

The array is automatically unnested, and the operation is performed on each array element.

Performing an operation which requires an array on a non-array, e.g.:

The non-array item is automatically wrapped in a singleton array, and the operation is performed on the array.

A structural error: accessing a non-existent element of an array or a non-existent member of a JSON object, e.g.:

$[-1] (array index out of bounds)

$.key, where the input JSON object does not have a member key

The error is suppressed, and the operation results in an empty sequence.

Let <path> return a sequence of three items, a JSON array, a JSON object, and a scalar numeric value:

The following example shows the wildcard array accessor in the lax mode. The JSON array returns all its elements, while the JSON object and the number are wrapped in singleton arrays and then unnested, so effectively they appear unchanged in the output sequence:

When calling the size() method, the JSON object and the number are also wrapped in singleton arrays:

In some cases, the lax mode cannot prevent failure. In the following example, even though the JSON array is unwrapped prior to calling the floor() method, the item "a" causes type mismatch.

The json_exists function determines whether a JSON value satisfies a JSON path specification.

The json_path is evaluated using the json_input as the context variable ($), and the passed arguments as the named variables ($variable_name). The returned value is true if the path returns a non-empty sequence, and false if the path returns an empty sequence. If an error occurs, the returned value depends on the ON ERROR clause. The default value returned ON ERROR is FALSE. The ON ERROR clause is applied for the following kinds of errors:

Input conversion errors, such as malformed JSON

JSON path evaluation errors, e.g. division by zero

json_input is a character string or a binary string. It should contain a single JSON item. For a binary string, you can specify encoding.

json_path is a string literal, containing the path mode specification, and the path expression, following the syntax rules described in JSON path syntax and semantics.

In the PASSING clause you can pass arbitrary expressions to be used by the path expression.

The passed parameters can be referenced in the path expression by named variables, prefixed with $.

Additionally to SQL values, you can pass JSON values, specifying the format and optional encoding:

Note that the JSON path language is case-sensitive, while the unquoted SQL identifiers are upper-cased. Therefore, it is recommended to use quoted identifiers in the PASSING clause:

Let customers be a table containing two columns: id:bigint, description:varchar.

‘{“comment” : “nice”, “children” : [10, 13, 16]}’

‘{“comment” : “problematic”, “children” : [8, 11]}’

‘{“comment” : “knows best”, “children” : [2]}’

The following query checks which customers have children above the age of 10:

In the following query, the path mode is strict. We check the third child for each customer. This should cause a structural error for the customers who do not have three or more children. This error is handled according to the ON ERROR clause.

The json_query function extracts a JSON value from a JSON value.

The constant string json_path is evaluated using the json_input as the context variable ($), and the passed arguments as the named variables ($variable_name).

The returned value is a JSON item returned by the path. By default, it is represented as a character string (varchar). In the RETURNING clause, you can specify other character string type or varbinary. With varbinary, you can also specify the desired encoding.

json_input is a character string or a binary string. It should contain a single JSON item. For a binary string, you can specify encoding.

json_path is a string literal, containing the path mode specification, and the path expression, following the syntax rules described in JSON path syntax and semantics.

In the PASSING clause you can pass arbitrary expressions to be used by the path expression.

The passed parameters can be referenced in the path expression by named variables, prefixed with $.

Additionally to SQL values, you can pass JSON values, specifying the format and optional encoding:

Note that the JSON path language is case-sensitive, while the unquoted SQL identifiers are upper-cased. Therefore, it is recommended to use quoted identifiers in the PASSING clause:

The ARRAY WRAPPER clause lets you modify the output by wrapping the results in a JSON array. WITHOUT ARRAY WRAPPER is the default option. WITH CONDITIONAL ARRAY WRAPPER wraps every result which is not a singleton JSON array or JSON object. WITH UNCONDITIONAL ARRAY WRAPPER wraps every result.

The QUOTES clause lets you modify the result for a scalar string by removing the double quotes being part of the JSON string representation.

Let customers be a table containing two columns: id:bigint, description:varchar.

‘{“comment” : “nice”, “children” : [10, 13, 16]}’

‘{“comment” : “problematic”, “children” : [8, 11]}’

‘{“comment” : “knows best”, “children” : [2]}’

The following query gets the children array for each customer:

The following query gets the collection of children for each customer. Note that the json_query function can only output a single JSON item. If you don’t use array wrapper, you get an error for every customer with multiple children. The error is handled according to the ON ERROR clause.

The following query gets the last child for each customer, wrapped in a JSON array:

The following query gets all children above the age of 12 for each customer, wrapped in a JSON array. The second and the third customer don’t have children of this age. Such case is handled according to the ON EMPTY clause. The default value returned ON EMPTY is NULL. In the following example, EMPTY ARRAY ON EMPTY is specified.

The following query shows the result of the QUOTES clause. Note that KEEP QUOTES is the default.

If an error occurs, the returned value depends on the ON ERROR clause. The default value returned ON ERROR is NULL. One example of error is multiple items returned by the path. Other errors caught and handled according to the ON ERROR clause are:

Input conversion errors, such as malformed JSON

JSON path evaluation errors, e.g. division by zero

Output conversion errors

The json_value function extracts a scalar SQL value from a JSON value.

The json_path is evaluated using the json_input as the context variable ($), and the passed arguments as the named variables ($variable_name).

The returned value is the SQL scalar returned by the path. By default, it is converted to string (varchar). In the RETURNING clause, you can specify other desired type: a character string type, numeric, boolean or datetime type.

json_input is a character string or a binary string. It should contain a single JSON item. For a binary string, you can specify encoding.

json_path is a string literal, containing the path mode specification, and the path expression, following the syntax rules described in JSON path syntax and semantics.

In the PASSING clause you can pass arbitrary expressions to be used by the path expression.

The passed parameters can be referenced in the path expression by named variables, prefixed with $.

Additionally to SQL values, you can pass JSON values, specifying the format and optional encoding:

Note that the JSON path language is case-sensitive, while the unquoted SQL identifiers are upper-cased. Therefore, it is recommended to use quoted identifiers in the PASSING clause:

If the path returns an empty sequence, the ON EMPTY clause is applied. The default value returned ON EMPTY is NULL. You can also specify the default value:

If an error occurs, the returned value depends on the ON ERROR clause. The default value returned ON ERROR is NULL. One example of error is multiple items returned by the path. Other errors caught and handled according to the ON ERROR clause are:

Input conversion errors, such as malformed JSON

JSON path evaluation errors, e.g. division by zero

Returned scalar not convertible to the desired type

Let customers be a table containing two columns: id:bigint, description:varchar.

‘{“comment” : “nice”, “children” : [10, 13, 16]}’

‘{“comment” : “problematic”, “children” : [8, 11]}’

‘{“comment” : “knows best”, “children” : [2]}’

The following query gets the comment for each customer as char(12):

The following query gets the first child’s age for each customer as tinyint:

The following query gets the third child’s age for each customer. In the strict mode, this should cause a structural error for the customers who do not have the third child. This error is handled according to the ON ERROR clause.

After changing the mode to lax, the structural error is suppressed, and the customers without a third child produce empty sequence. This case is handled according to the ON EMPTY clause.

The json_table clause extracts a table from a JSON value. Use this clause to transform JSON data into a relational format, making it easier to query and analyze. Use json_table in the FROM clause of a SELECT statement to create a table from JSON data.

The COLUMNS clause supports the following column_definition arguments:

json_input is a character string or a binary string. It must contain a single JSON item.

json_path is a string literal containing the path mode specification and the path expression. It follows the syntax rules described in JSON path syntax and semantics.

In the PASSING clause, pass values as named parameters that the json_path expression can reference.

Use named parameters to reference the values in the path expression. Prefix named parameters with $.

You can also pass JSON values in the PASSING clause. Use FORMAT JSON to specify the format and ENCODING to specify the encoding:

The json_path value is case-sensitive. The SQL identifiers are uppercase. Use quoted identifiers in the PASSING clause:

The PLAN clause specifies how to join columns from different paths. Use OUTER or INNER to define how to join parent paths with their child paths. Use CROSS or UNION to join siblings.

COLUMNS defines the schema of your table. Each column_definition specifies how to extract and format your json_input value into a relational column.

PLAN is an optional clause to control how to process and join nested JSON data.

ON ERROR specifies how to handle processing errors. ERROR ON ERROR throws an error. EMPTY ON ERROR returns an empty result set.

column_name specifies a column name.

FOR ORDINALITY adds a row number column to the output table, starting at 1. Specify the column name in the column definition:

NESTED PATH extracts data from nested levels of a json_input value. Each NESTED PATH clause can contain column_definition values.

The json_table function returns a result set that you can use like any other table in your queries. You can join the result set with other tables or combine multiple arrays from your JSON data.

You can also process nested JSON objects without parsing the data multiple times.

Use json_table as a lateral join to process JSON data from another table.

The following query uses json_table to extract values from a JSON array and return them as rows in a table with three columns:

The following query uses json_table to extract values from an array of nested JSON objects. It flattens the nested JSON data into a single table. The example query processes an array of continent names, where each continent contains an array of countries and their populations.

The NESTED PATH 'lax $[*]' clause iterates through the continent objects, while the NESTED PATH 'lax $.countries[*]' iterates through each country within each continent. This creates a flat table structure with four rows combining each continent with each of its countries. Continent values repeat for each of their countries.

The following query uses PLAN to specify an OUTER join between a parent path and a child path:

The following query uses PLAN to specify an INNER join between a parent path and a child path:

The json_array function creates a JSON array containing given elements.

The array elements can be arbitrary expressions. Each passed value is converted into a JSON item according to its type, and optional FORMAT and ENCODING specification.

You can pass SQL values of types boolean, numeric, and character string. They are converted to corresponding JSON literals:

Additionally to SQL values, you can pass JSON values. They are character or binary strings with a specified format and optional encoding:

You can also nest other JSON-returning functions. In that case, the FORMAT option is implicit:

Other passed values are cast to varchar, and they become JSON text literals:

You can omit the arguments altogether to get an empty array:

If a value passed for an array element is null, it is treated according to the specified null treatment option. If ABSENT ON NULL is specified, the null element is omitted in the result. If NULL ON NULL is specified, JSON null is added to the result. ABSENT ON NULL is the default configuration:

The SQL standard imposes that there is no dedicated data type to represent JSON data in SQL. Instead, JSON data is represented as character or binary strings. By default, the json_array function returns varchar containing the textual representation of the JSON array. With the RETURNING clause, you can specify other character string type:

You can also specify to use varbinary and the required encoding as return type. The default encoding is UTF8:

The json_object function creates a JSON object containing given key-value pairs.

There are two conventions for passing keys and values:

In the second convention, you can omit the KEY keyword:

The keys can be arbitrary expressions. They must be of character string type. Each key is converted into a JSON text item, and it becomes a key in the created JSON object. Keys must not be null.

The values can be arbitrary expressions. Each passed value is converted into a JSON item according to its type, and optional FORMAT and ENCODING specification.

You can pass SQL values of types boolean, numeric, and character string. They are converted to corresponding JSON literals:

Additionally to SQL values, you can pass JSON values. They are character or binary strings with a specified format and optional encoding:

You can also nest other JSON-returning functions. In that case, the FORMAT option is implicit:

Other passed values are cast to varchar, and they become JSON text literals:

You can omit the arguments altogether to get an empty object:

The values passed for JSON object keys must not be null. It is allowed to pass null for JSON object values. A null value is treated according to the specified null treatment option. If NULL ON NULL is specified, a JSON object entry with null value is added to the result. If ABSENT ON NULL is specified, the entry is omitted in the result. NULL ON NULL is the default configuration.:

If a duplicate key is encountered, it is handled according to the specified key uniqueness constraint.

If WITH UNIQUE KEYS is specified, a duplicate key results in a query failure:

Note that this option is not supported if any of the arguments has a FORMAT specification.

If WITHOUT UNIQUE KEYS is specified, duplicate keys are not supported due to implementation limitation. WITHOUT UNIQUE KEYS is the default configuration.

The SQL standard imposes that there is no dedicated data type to represent JSON data in SQL. Instead, JSON data is represented as character or binary strings. By default, the json_object function returns varchar containing the textual representation of the JSON object. With the RETURNING clause, you can specify other character string type:

You can also specify to use varbinary and the required encoding as return type. The default encoding is UTF8:

The following functions and operators are not compliant with the SQL standard, and should be considered deprecated. According to the SQL standard, there shall be no JSON data type. Instead, JSON values should be represented as string values. The remaining functionality of the following functions is covered by the functions described previously.

The following types can be cast to JSON:

Additionally, ARRAY, MAP, and ROW types can be cast to JSON when the following requirements are met:

ARRAY types can be cast when the element type of the array is one of the supported types.

MAP types can be cast when the key type of the map is VARCHAR and the value type of the map is a supported type,

ROW types can be cast when every field type of the row is a supported type.

Cast operations with supported character string types treat the input as a string, not validated as JSON. This means that a cast operation with a string-type input of invalid JSON results in a successful cast to invalid JSON.

Instead, consider using the json_parse() function to create validated JSON from a string.

The following examples show the behavior of casting to JSON with these types:

Casting from NULL to JSON is not straightforward. Casting from a standalone NULL will produce SQL NULL instead of JSON 'null'. However, when casting from arrays or map containing NULLs, the produced JSON will have nulls in it.

Casting to BOOLEAN, TINYINT, SMALLINT, INTEGER, BIGINT, REAL, DOUBLE or VARCHAR is supported. Casting to ARRAY and MAP is supported when the element type of the array is one of the supported types, or when the key type of the map is VARCHAR and value type of the map is one of the supported types. Behaviors of the casts are shown with the examples below:

JSON arrays can have mixed element types and JSON maps can have mixed value types. This makes it impossible to cast them to SQL arrays and maps in some cases. To address this, Trino supports partial casting of arrays and maps:

When casting from JSON to ROW, both JSON array and JSON object are supported.

In addition to the functions explained in more details in the preceding sections, the following functions are available:

Determine if json is a scalar (i.e. a JSON number, a JSON string, true, false or null):

Determine if value exists in json (a string containing a JSON array):

The semantics of this function are broken. If the extracted element is a string, it will be converted into an invalid JSON value that is not properly quoted (the value will not be surrounded by quotes and any interior quotes will not be escaped).

We recommend against using this function. It cannot be fixed without impacting existing usages and may be removed in a future release.

Returns the element at the specified index into the json_array. The index is zero-based:

This function also supports negative indexes for fetching element indexed from the end of an array:

If the element at the specified index doesn’t exist, the function returns null:

Returns the array length of json (a string containing a JSON array):

Evaluates the JSONPath-like expression json_path on json (a string containing JSON) and returns the result as a JSON string:

The json_query function provides a more powerful and feature-rich alternative to parse and extract JSON data.

Like json_extract(), but returns the result value as a string (as opposed to being encoded as JSON). The value referenced by json_path must be a scalar (boolean, number or string).

Returns the JSON text serialized from the input JSON value. This is inverse function to json_parse().

json_format() and CAST(json AS VARCHAR) have completely different semantics.

json_format() serializes the input JSON value to JSON text conforming to RFC 7159. The JSON value can be a JSON object, a JSON array, a JSON string, a JSON number, true, false or null.

CAST(json AS VARCHAR) casts the JSON value to the corresponding SQL VARCHAR value. For JSON string, JSON number, true, false or null, the cast behavior is same as the corresponding SQL type. JSON object and JSON array cannot be cast to VARCHAR.

Returns the JSON value deserialized from the input JSON text. This is inverse function to json_format():

json_parse() and CAST(string AS JSON) have completely different semantics.

json_parse() expects a JSON text conforming to RFC 7159, and returns the JSON value deserialized from the JSON text. The JSON value can be a JSON object, a JSON array, a JSON string, a JSON number, true, false or null.

CAST(string AS JSON) takes any VARCHAR value as input, and returns a JSON string with its value set to input string.

Like json_extract(), but returns the size of the value. For objects or arrays, the size is the number of members, and the size of a scalar value is zero.

**Examples:**

Example 1 (unknown):
```unknown
-1, 1.2e3, NaN
```

Example 2 (unknown):
```unknown
-1, 1.2e3, NaN
```

Example 3 (unknown):
```unknown
"Some text"
```

Example 4 (unknown):
```unknown
"Some text"
```

---

## SHOW ROLES — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/show-roles.html

**Contents:**
- SHOW ROLES#
- Synopsis#
- Description#

SHOW ROLES lists all the system roles or all the roles in catalog.

SHOW CURRENT ROLES lists the enabled system roles or roles in catalog.

**Examples:**

Example 1 (unknown):
```unknown
SHOW [CURRENT] ROLES [ FROM catalog ]
```

Example 2 (unknown):
```unknown
SHOW [CURRENT] ROLES [ FROM catalog ]
```

---

## SET TIME ZONE — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/set-time-zone.html

**Contents:**
- SET TIME ZONE#
- Synopsis#
- Description#
- Examples#
- Limitations#
- See also#

Sets the default time zone for the current session.

If the LOCAL option is specified, the time zone for the current session is set to the initial time zone of the session.

If the expression option is specified:

if the type of the expression is a string, the time zone for the current session is set to the corresponding region-based time zone ID or the corresponding zone offset.

if the type of the expression is an interval, the time zone for the current session is set to the corresponding zone offset relative to UTC. It must be in the range of [-14,14] hours.

Use the default time zone for the current session:

Use a zone offset for specifying the time zone:

Use an interval literal for specifying the time zone:

Use a region-based time zone identifier for specifying the time zone:

The time zone identifier to be used can be passed as the output of a function call:

Setting the default time zone for the session has no effect if the sql.forced-session-time-zone configuration property is already set.

**Examples:**

Example 1 (unknown):
```unknown
SET TIME ZONE LOCAL
SET TIME ZONE expression
```

Example 2 (unknown):
```unknown
SET TIME ZONE LOCAL
SET TIME ZONE expression
```

Example 3 (unknown):
```unknown
SET TIME ZONE LOCAL;
```

Example 4 (unknown):
```unknown
SET TIME ZONE LOCAL;
```

---

## BEGIN — Trino 478 Documentation

**URL:** https://trino.io/docs/current/udf/sql/begin.html

**Contents:**
- BEGIN#
- Synopsis#
- Description#
- Examples#
- See also#

Marks the start and end of a block in a SQL user-defined functions. BEGIN can be used wherever a statement can be used to group multiple statements together and to declare variables local to the block. A typical use case is as first statement within a FUNCTION. Blocks can also be nested.

After the BEGIN keyword, you can add variable declarations using DECLARE statements, followed by one or more statements that define the main body of the SQL UDF, separated by ;. The following statements can be used:

The following example computes the value 42:

Further examples of varying complexity that cover usage of the BEGIN statement in combination with other statements are available in the Example SQL UDFs.

User-defined functions

SQL user-defined functions

**Examples:**

Example 1 (unknown):
```unknown
BEGIN
  [ DECLARE ... ]
  statements
END
```

Example 2 (unknown):
```unknown
BEGIN
  [ DECLARE ... ]
  statements
END
```

Example 3 (unknown):
```unknown
FUNCTION meaning_of_life()
  RETURNS integer
  BEGIN
    DECLARE a integer DEFAULT 6;
    DECLARE b integer DEFAULT 7;
    RETURN a * b;
  END
```

Example 4 (unknown):
```unknown
FUNCTION meaning_of_life()
  RETURNS integer
  BEGIN
    DECLARE a integer DEFAULT 6;
    DECLARE b integer DEFAULT 7;
    RETURN a * b;
  END
```

---

## COMMIT — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/commit.html

**Contents:**
- COMMIT#
- Synopsis#
- Description#
- Examples#
- See also#

Commit the current transaction.

ROLLBACK, START TRANSACTION

**Examples:**

Example 1 (unknown):
```unknown
COMMIT [ WORK ]
```

Example 2 (unknown):
```unknown
COMMIT [ WORK ]
```

Example 3 (unknown):
```unknown
COMMIT;
COMMIT WORK;
```

Example 4 (unknown):
```unknown
COMMIT;
COMMIT WORK;
```

---

## SHOW CATALOGS — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/show-catalogs.html

**Contents:**
- SHOW CATALOGS#
- Synopsis#
- Description#

List the available catalogs.

Specify a pattern in the optional LIKE clause to filter the results to the desired subset. For example, the following query allows you to find catalogs that begin with t:

**Examples:**

Example 1 (unknown):
```unknown
SHOW CATALOGS [ LIKE pattern ]
```

Example 2 (unknown):
```unknown
SHOW CATALOGS [ LIKE pattern ]
```

Example 3 (unknown):
```unknown
SHOW CATALOGS LIKE 't%'
```

Example 4 (unknown):
```unknown
SHOW CATALOGS LIKE 't%'
```

---

## CREATE BRANCH — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/create-branch.html

**Contents:**
- CREATE BRANCH#
- Synopsis#
- Description#
- Examples#
- See also#

The optional OR REPLACE clause causes an existing branch with the specified name to be replaced with the new branch definition. Support for branch replacement varies across connectors. Refer to the connector documentation for details.

The optional IF NOT EXISTS clause causes the error to be suppressed if the branch already exists.

The optional WITH clause can be used to set properties on the newly created branch.

The optional FROM clause can be used to set the source branch from which the new branch is created.

Create a new branch audit in the table orders:

Create a new branch audit in the table orders from the branch dev:

**Examples:**

Example 1 (unknown):
```unknown
CREATE [ OR REPLACE ] BRANCH [ IF NOT EXISTS ] branch_name
[ WITH ( property_name = expression [, ...] ) ]
IN TABLE table_name
[ FROM source_branch ]
```

Example 2 (unknown):
```unknown
CREATE [ OR REPLACE ] BRANCH [ IF NOT EXISTS ] branch_name
[ WITH ( property_name = expression [, ...] ) ]
IN TABLE table_name
[ FROM source_branch ]
```

Example 3 (unknown):
```unknown
CREATE BRANCH audit IN TABLE orders
```

Example 4 (unknown):
```unknown
CREATE BRANCH audit IN TABLE orders
```

---

## Table functions — Trino 478 Documentation

**URL:** https://trino.io/docs/current/functions/table.html

**Contents:**
- Table functions#
- Built-in table functions#
  - exclude_columns table function#
  - sequence table function#
- Table function invocation#
  - Function resolution#
  - Arguments#
  - Argument passing conventions#

A table function is a function returning a table. It can be invoked inside the FROM clause of a query:

The row type of the returned table can depend on the arguments passed with invocation of the function. If different row types can be returned, the function is a polymorphic table function.

Polymorphic table functions allow you to dynamically invoke custom logic from within the SQL query. They can be used for working with external systems as well as for enhancing Trino with capabilities going beyond the SQL standard.

For the list of built-in table functions available in Trino, see built-in table functions.

Trino supports adding custom table functions. They are declared by connectors through implementing dedicated interfaces. For guidance on adding new table functions, see the developer guide.

Connectors offer support for different functions on a per-connector basis. For more information about supported table functions, refer to the connector documentation.

Use the exclude_columns table function to return a new table based on an input table table, with the exclusion of all columns specified in descriptor:

The argument input is a table or a query. The argument columns is a descriptor without types.

Example query using the orders table from the TPC-H dataset, provided by the TPC-H connector:

The table function is useful for queries where you want to return nearly all columns from tables with many columns. You can avoid enumerating all columns, and only need to specify the columns to exclude.

Use the sequence table function to return a table with a single column sequential_number containing a sequence of bigint:

start is the first element in the sequence. The default value is 0.

stop is the end of the range, inclusive. The last element in the sequence is equal to stop, or it is the last value within range, reachable by steps.

step is the difference between subsequent values. The default value is 1.

The result of the sequence table function might not be ordered. If required, enforce ordering in the enclosing query:

You invoke a table function in the FROM clause of a query. Table function invocation syntax is similar to a scalar function call.

Every table function is provided by a catalog, and it belongs to a schema in the catalog. You can qualify the function name with a schema name, or with catalog and schema names:

Otherwise, the standard Trino name resolution is applied. The connection between the function and the catalog must be identified, because the function is executed by the corresponding connector. If the function is not registered by the specified catalog, the query fails.

The table function name is resolved case-insensitive, analogically to scalar function and table resolution in Trino.

There are three types of arguments.

They must be constant expressions, and they can be of any SQL type, which is compatible with the declared argument type:

Descriptors consist of fields with names and optional data types:

To pass null for a descriptor, use:

You can pass a table name, or a query. Use the keyword TABLE:

If the table argument is declared as set semantics, you can specify partitioning and ordering. Each partition is processed independently by the table function. If you do not specify partitioning, the argument is processed as a single partition. You can also specify PRUNE WHEN EMPTY or KEEP WHEN EMPTY. With PRUNE WHEN EMPTY you declare that you are not interested in the function result if the argument is empty. This information is used by the Trino engine to optimize the query. The KEEP WHEN EMPTY option indicates that the function should be executed even if the table argument is empty. By specifying KEEP WHEN EMPTY or PRUNE WHEN EMPTY, you override the property set for the argument by the function author.

The following example shows how the table argument properties should be ordered:

There are two conventions of passing arguments to a table function:

Arguments passed by name:

In this convention, you can pass the arguments in arbitrary order. Arguments declared with default values can be skipped. Argument names are resolved case-sensitive, and with automatic uppercasing of unquoted names.

Arguments passed positionally:

In this convention, you must follow the order in which the arguments are declared. You can skip a suffix of the argument list, provided that all the skipped arguments are declared with default values.

You cannot mix the argument conventions in one invocation.

You can also use parameters in arguments:

**Examples:**

Example 1 (unknown):
```unknown
SELECT * FROM TABLE(my_function(1, 100))
```

Example 2 (unknown):
```unknown
SELECT * FROM TABLE(my_function(1, 100))
```

Example 3 (javascript):
```javascript
SELECT *
FROM TABLE(exclude_columns(
                        input => TABLE(orders),
                        columns => DESCRIPTOR(clerk, comment)));
```

Example 4 (javascript):
```javascript
SELECT *
FROM TABLE(exclude_columns(
                        input => TABLE(orders),
                        columns => DESCRIPTOR(clerk, comment)));
```

---

## CREATE CATALOG — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/create-catalog.html

**Contents:**
- CREATE CATALOG#
- Synopsis#
- Description#
- Examples#
- See also#

Create a new catalog using the specified connector.

The optional WITH clause is used to set properties on the newly created catalog. Property names can be double-quoted, which is required if they contain special characters, like -. Refer to the connectors documentation to learn about all available properties. All property values must be varchars (single quoted), including numbers and boolean values.

The query fails in the following circumstances:

A required property is missing.

An invalid property is set, for example there is a typo in the property name, or a property name from a different connector was used.

The value of the property is invalid, for example a numeric value is out of range, or a string value doesn’t match the required pattern.

The value references an environmental variable that is not set on the coordinator node.

The complete CREATE CATALOG query is logged, and visible in the Web UI. This includes any sensitive properties, like passwords and other credentials. See Secrets.

This command requires the catalog management type to be set to dynamic.

Create a new catalog called tpch using the TPC-H connector:

Create a new catalog called brain using the Memory connector:

Notice that the connector property contains dashes (-) and needs to quoted using a double quote ("). The value 128MB is quoted using single quotes, because it is a string literal.

Create a new catalog called example using the PostgreSQL connector:

This example assumes that the POSTGRES_USER and POSTGRES_PASSWORD environmental variables are set as secrets on all nodes of the cluster.

Catalog management properties

**Examples:**

Example 1 (unknown):
```unknown
CREATE CATALOG
catalog_name
USING connector_name
[ WITH ( property_name = expression [, ...] ) ]
```

Example 2 (unknown):
```unknown
CREATE CATALOG
catalog_name
USING connector_name
[ WITH ( property_name = expression [, ...] ) ]
```

Example 3 (unknown):
```unknown
CREATE CATALOG tpch USING tpch;
```

Example 4 (unknown):
```unknown
CREATE CATALOG tpch USING tpch;
```

---

## VALUES — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/values.html

**Contents:**
- VALUES#
- Synopsis#
- Description#
- Examples#
- See also#

where row is a single expression or

Defines a literal inline table.

VALUES can be used anywhere a query can be used (e.g., the FROM clause of a SELECT, an INSERT, or even at the top level). VALUES creates an anonymous table without column names, but the table and columns can be named using an AS clause with column aliases.

Return a table with one column and three rows:

Return a table with two columns and three rows:

Return table with column id and name:

Create a new table with column id and name:

**Examples:**

Example 1 (unknown):
```unknown
VALUES row [, ...]
```

Example 2 (unknown):
```unknown
VALUES row [, ...]
```

Example 3 (unknown):
```unknown
( column_expression [, ...] )
```

Example 4 (unknown):
```unknown
( column_expression [, ...] )
```

---

## GRANT role — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/grant-roles.html

**Contents:**
- GRANT role#
- Synopsis#
- Description#
- Examples#
- Limitations#
- See also#

Grants the specified role(s) to the specified principal(s).

If the WITH ADMIN OPTION clause is specified, the role(s) are granted to the users with GRANT option.

For the GRANT statement for roles to succeed, the user executing it either should be the role admin or should possess the GRANT option for the given role.

The optional GRANTED BY clause causes the role(s) to be granted with the specified principal as a grantor. If the GRANTED BY clause is not specified, the roles are granted with the current user as a grantor.

The optional IN catalog clause grants the roles in a catalog as opposed to a system roles.

Grant role bar to user foo

Grant roles bar and foo to user baz and role qux with admin option

Some connectors do not support role management. See connector documentation for more details.

CREATE ROLE, DROP ROLE, SET ROLE, REVOKE role

**Examples:**

Example 1 (unknown):
```unknown
GRANT role_name [, ...]
TO ( user | USER user_name | ROLE role_name) [, ...]
[ GRANTED BY ( user | USER user | ROLE role | CURRENT_USER | CURRENT_ROLE ) ]
[ WITH ADMIN OPTION ]
[ IN catalog ]
```

Example 2 (unknown):
```unknown
GRANT role_name [, ...]
TO ( user | USER user_name | ROLE role_name) [, ...]
[ GRANTED BY ( user | USER user | ROLE role | CURRENT_USER | CURRENT_ROLE ) ]
[ WITH ADMIN OPTION ]
[ IN catalog ]
```

Example 3 (unknown):
```unknown
GRANT bar TO USER foo;
```

Example 4 (unknown):
```unknown
GRANT bar TO USER foo;
```

---

## SHOW TABLES — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/show-tables.html

**Contents:**
- SHOW TABLES#
- Synopsis#
- Description#
- Examples#
- See also#

List the tables and views in the current schema, for example set with USE or by a client connection.

Use a fully qualified path to a schema in the form of catalog_name.schema_name to specify any schema in any catalog in the FROM clause.

Specify a pattern in the optional LIKE clause to filter the results to the desired subset.

The following query lists tables and views that begin with p in the tiny schema of the tpch catalog:

Schema and table management

**Examples:**

Example 1 (unknown):
```unknown
SHOW TABLES [ FROM schema ] [ LIKE pattern ]
```

Example 2 (unknown):
```unknown
SHOW TABLES [ FROM schema ] [ LIKE pattern ]
```

Example 3 (unknown):
```unknown
SHOW TABLES FROM tpch.tiny LIKE 'p%';
```

Example 4 (unknown):
```unknown
SHOW TABLES FROM tpch.tiny LIKE 'p%';
```

---

## ROLLBACK — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/rollback.html

**Contents:**
- ROLLBACK#
- Synopsis#
- Description#
- Examples#
- See also#

Rollback the current transaction.

COMMIT, START TRANSACTION

**Examples:**

Example 1 (unknown):
```unknown
ROLLBACK [ WORK ]
```

Example 2 (unknown):
```unknown
ROLLBACK [ WORK ]
```

Example 3 (unknown):
```unknown
ROLLBACK;
ROLLBACK WORK;
```

Example 4 (unknown):
```unknown
ROLLBACK;
ROLLBACK WORK;
```

---

## SHOW CREATE SCHEMA — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/show-create-schema.html

**Contents:**
- SHOW CREATE SCHEMA#
- Synopsis#
- Description#
- See also#

Show the SQL statement that creates the specified schema.

**Examples:**

Example 1 (unknown):
```unknown
SHOW CREATE SCHEMA schema_name
```

Example 2 (unknown):
```unknown
SHOW CREATE SCHEMA schema_name
```

---

## DELETE — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/delete.html

**Contents:**
- DELETE#
- Synopsis#
- Description#
- Examples#
- Limitations#

Delete rows from a table. If the WHERE clause is specified, only the matching rows are deleted. Otherwise, all rows from the table are deleted.

Delete all line items shipped by air:

Delete all line items for low priority orders:

Delete all orders in the audit branch:

Some connectors have limited or no support for DELETE. See connector documentation for more details.

**Examples:**

Example 1 (unknown):
```unknown
DELETE FROM table_name [ @ branch_name ] [ WHERE condition ]
```

Example 2 (unknown):
```unknown
DELETE FROM table_name [ @ branch_name ] [ WHERE condition ]
```

Example 3 (unknown):
```unknown
DELETE FROM lineitem WHERE shipmode = 'AIR';
```

Example 4 (unknown):
```unknown
DELETE FROM lineitem WHERE shipmode = 'AIR';
```

---

## Functions and operators — Trino 478 Documentation

**URL:** https://trino.io/docs/current/functions.html

**Contents:**
- Functions and operators#
- Functions by name#
- Functions per topic#

This section describes the built-in SQL functions and operators supported by Trino. They allow you to implement complex capabilities and behavior of the queries executed by Trino operating on the underlying data sources.

Refer to the following sections for further details:

SQL data types and other general aspects

SQL statement and syntax reference

In addition, Trino supports implementation of custom functions or custom table functions provided by a plugin, and creation of User-defined functions.

If you are looking for a specific function or operator by name use SHOW FUNCTIONS, or refer to the following resources:

---

## SHOW SESSION — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/show-session.html

**Contents:**
- SHOW SESSION#
- Synopsis#
- Description#
- See also#

List the current session properties.

Specify a pattern in the optional LIKE clause to filter the results to the desired subset. For example, the following query allows you to find session properties that begin with query:

RESET SESSION, SET SESSION

**Examples:**

Example 1 (unknown):
```unknown
SHOW SESSION [ LIKE pattern ]
```

Example 2 (unknown):
```unknown
SHOW SESSION [ LIKE pattern ]
```

Example 3 (unknown):
```unknown
SHOW SESSION LIKE 'query%'
```

Example 4 (unknown):
```unknown
SHOW SESSION LIKE 'query%'
```

---

## Example SQL UDFs — Trino 478 Documentation

**URL:** https://trino.io/docs/current/udf/sql/examples.html

**Contents:**
- Example SQL UDFs#
- Inline and catalog UDFs#
- Declaration examples#
- Conditional flows#
- Fibonacci example#
- Labels and loops#
- SQL UDFs and built-in functions#
- Optional parameter example#
- Date string parsing example#
- Human-readable days#

After learning about SQL user-defined functions, the following sections show numerous examples of valid SQL UDFs. The UDFs are suitable as Inline user-defined functions or Catalog user-defined functions, after adjusting the name and the example invocations.

The examples combine numerous supported statements. Refer to the specific statement documentation for further details:

FUNCTION for general UDF declaration

BEGIN and DECLARE for SQL UDF blocks

SET for assigning values to variables

RETURN for returning results

CASE and IF for conditional flows

LOOP, REPEAT, and WHILE for looping constructs

ITERATE and LEAVE for flow control

The following section shows the differences in usage with inline and catalog UDFs with a simple SQL UDF example. The same pattern applies to all other following sections.

A very simple SQL UDF that returns a static value without requiring any input:

A full example of this UDF as inline UDF and usage in a string concatenation with a cast:

Provided the catalog example supports UDF storage in the default schema, you can use the following:

With the UDF stored in the catalog, you can run the UDF multiple times without repeated definition:

Alternatively, you can configure the SQL PATH in the Config properties to a catalog and schema that support UDF storage:

Now you can manage UDFs without the full path:

UDF invocation works without the full path:

The result of calling the UDF answer() is always identical, so you can declare it as deterministic, and add some other information:

The comment and other information about the UDF is visible in the output of SHOW FUNCTIONS.

A simple UDF that returns a greeting back to the input string fullname concatenating two strings and the input value:

Following is an example invocation:

A first example UDF, that uses multiple statements in a BEGIN block. It calculates the result of a multiplication of the input integer with 99. The bigint data type is used for all variables and values. The value of integer 99 is cast to bigint in the default value assignment for the variable x:

Following is an example invocation:

A first example of conditional flow control in a SQL UDF using the CASE statement. The simple bigint input value is compared to a number of values:

Following are a couple of example invocations with result and explanation:

A second example of a SQL UDF with a CASE statement, this time with two parameters, showcasing the importance of the order of the conditions:

Following are a couple of example invocations with result and explanation:

This SQL UDF calculates the n-th value in the Fibonacci series, in which each number is the sum of the two preceding ones. The two initial values are set to 1 as the defaults for a and b. The UDF uses an IF statement condition to return 1 for all input values of 2 or less. The WHILE block then starts to calculate each number in the series, starting with a=1 and b=1 and iterates until it reaches the n-th position. In each iteration it sets a and b for the preceding to values, so it can calculate the sum, and finally return it. Note that processing the UDF takes longer and longer with higher n values, and the result is deterministic:

Following are a couple of example invocations with result and explanation:

This SQL UDF uses the top label to name the WHILE block, and then controls the flow with conditional statements, ITERATE, and LEAVE. For the values of a=1 and a=2 in the first two iterations of the loop the ITERATE call moves the flow up to top before b is ever increased. Then b is increased for the values a=3, a=4, a=5, a=6, and a=7, resulting in b=5. The LEAVE call then causes the exit of the block before a is increased further to 10 and therefore the result of the UDF is 5:

This SQL UDF implements calculating the n to the power of p by repeated multiplication and keeping track of the number of multiplications performed. Note that this SQL UDF does not return the correct 0 for p=0 since the top block is merely escaped and the value of n is returned. The same incorrect behavior happens for negative values of p:

Following are a couple of example invocations with result and explanation:

This SQL UDF returns 7 as a result of the increase of b in the loop from a=3 to a=10:

This SQL UDF returns 2 and shows that labels can be repeated and label usage within a block refers to the label of that block:

This SQL UDF shows that multiple data types and built-in functions like length() and cardinality() can be used in a UDF. The two nested BEGIN blocks also show how variable names are local within these blocks x, but the global r from the top-level block can be accessed in the nested blocks:

UDFs can invoke other UDFs and other functions. The full signature of a UDF is composed of the UDF name and parameters, and determines the exact UDF to use. You can declare multiple UDFs with the same name, but with a different number of arguments or different argument types. One example use case is to implement an optional parameter.

The following SQL UDF truncates a string to the specified length including three dots at the end of the output:

Following are example invocations and output:

If you want to provide a UDF with the same name, but without the parameter for length, you can create another UDF that invokes the preceding UDF:

You can now use both UDFs. When the length parameter is omitted, the default value from the second declaration is used.

This example SQL UDF parses a date string of type VARCHAR into TIMESTAMP WITH TIME ZONE. Date strings are commonly represented by ISO 8601 standard, such as 2023-12-01, 2023-12-01T23. Date strings are also often represented in the YYYYmmdd and YYYYmmddHH format, such as 20230101 and 2023010123. Hive tables can use this format to represent day and hourly partitions, for example /day=20230101, /hour=2023010123.

This UDF parses date strings in a best-effort fashion and can be used as a replacement for date string manipulation functions such as date, date_parse, from_iso8601_date, and from_iso8601_timestamp.

Note that the UDF defaults the time value to 00:00:00.000 and the time zone to the session time zone:

Following are a couple of example invocations with result and explanation:

Trino includes a built-in function called human_readable_seconds() that formats a number of seconds into a string:

The example SQL UDF hrd formats a number of days into a human-readable text that provides the approximate number of years and months:

The following examples show the output for a range of values under one month, under one year, and various larger values:

Improvements of the SQL UDF could include the following modifications:

Take into account that one month equals 30.4375 days.

Take into account that one year equals 365.25 days.

Add weeks to the output.

Expand to cover decades, centuries, and millennia.

This example SQL UDF strtrunc truncates strings longer than 60 characters, leaving the first 30 and the last 25 characters, and cutting out extra characters in the middle:

The preceding declaration is very compact and consists of only one complex statement with a CASE expression and multiple function calls. It can therefore define the complete logic in the RETURN clause.

The following statement shows the same capability within the SQL UDF itself. Note the duplicate RETURN inside and outside the CASE statement and the required END CASE;. The second RETURN statement is required, because a SQL UDF must end with a RETURN statement. As a result the ELSE clause can be omitted:

The next example changes over from a CASE to an IF statement, and avoids the duplicate RETURN:

All the preceding examples create the same output. Following is an example query which generates long strings to truncate:

The preceding query produces the following output with all variants of the SQL UDF:

A possible improvement is to introduce parameters for the total length.

Trino includes a built-in format_number() function. However, it is using units that do not work well with bytes. The following format_data_size SQL UDF can format large values of bytes into a human-readable string:

Below is a query that shows how it formats a wide range of values:

The preceding query produces the following output:

Trino already has a built-in bar() color function, but it is using ANSI escape codes to output colors, and thus is only usable for displaying results in a terminal. The following example shows a similar SQL UDF that only uses ASCII characters:

It can be used to visualize a value:

The preceding query produces the following output:

It is also possible to draw more compacted charts. Following is a SQL UDF drawing vertical bars:

It can be used to draw a distribution of values, in a single column:

The preceding query produces the following output:

Trino already has a built-in aggregate function called approx_most_frequent() that can calculate the most frequently occurring values. It returns a map with values as keys and number of occurrences as values. Maps are not ordered, so when displayed, the entries can change places on subsequent runs of the same query, and readers must still compare all frequencies to find the one most frequent value. The following is a SQL UDF that returns ordered results as a string:

Following is an example query to count generated strings:

The preceding query produces the following result:

**Examples:**

Example 1 (unknown):
```unknown
FUNCTION answer()
RETURNS BIGINT
RETURN 42
```

Example 2 (unknown):
```unknown
FUNCTION answer()
RETURNS BIGINT
RETURN 42
```

Example 3 (unknown):
```unknown
WITH
  FUNCTION answer()
  RETURNS BIGINT
  RETURN 42
SELECT 'The answer is ' || CAST(answer() as varchar);
-- The answer is 42
```

Example 4 (unknown):
```unknown
WITH
  FUNCTION answer()
  RETURNS BIGINT
  RETURN 42
SELECT 'The answer is ' || CAST(answer() as varchar);
-- The answer is 42
```

---

## ALTER VIEW — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/alter-view.html

**Contents:**
- ALTER VIEW#
- Synopsis#
- Description#
- Examples#
- See also#

Change the definition of an existing view.

Rename view people to users:

Change owner of VIEW people to user alice:

**Examples:**

Example 1 (unknown):
```unknown
ALTER VIEW name RENAME TO new_name
ALTER VIEW name REFRESH
ALTER VIEW name SET AUTHORIZATION ( user | USER user | ROLE role )
```

Example 2 (unknown):
```unknown
ALTER VIEW name RENAME TO new_name
ALTER VIEW name REFRESH
ALTER VIEW name SET AUTHORIZATION ( user | USER user | ROLE role )
```

Example 3 (unknown):
```unknown
ALTER VIEW people RENAME TO users
```

Example 4 (unknown):
```unknown
ALTER VIEW people RENAME TO users
```

---

## DECLARE — Trino 478 Documentation

**URL:** https://trino.io/docs/current/udf/sql/declare.html

**Contents:**
- DECLARE#
- Synopsis#
- Description#
- Examples#
- See also#

Use the DECLARE statement directly after the BEGIN keyword in SQL user-defined functions to define one or more variables with an identifier as name. Each statement must specify the data type of the variable with type. It can optionally include a default, initial value defined by an expression. The default value is NULL if not specified.

A simple declaration of the variable x with the tinyint data type and the implicit default value of null:

A declaration of multiple string variables with length restricted to 25 characters:

A declaration of an exact decimal number with a default value:

A declaration with a default value from an expression:

Further examples of varying complexity that cover usage of the DECLARE statement in combination with other statements are available in the Example SQL UDFs.

SQL user-defined functions

**Examples:**

Example 1 (unknown):
```unknown
DECLARE identifier [, ...] type [ DEFAULT expression ]
```

Example 2 (unknown):
```unknown
DECLARE identifier [, ...] type [ DEFAULT expression ]
```

Example 3 (unknown):
```unknown
DECLARE x tinyint;
```

Example 4 (unknown):
```unknown
DECLARE x tinyint;
```

---

## ALTER TABLE — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/alter-table.html

**Contents:**
- ALTER TABLE#
- Synopsis#
- Description#
  - SET PROPERTIES#
  - EXECUTE#
- Examples#
- See also#

Change the definition of an existing table.

The optional IF EXISTS clause, when used before the table name, causes the error to be suppressed if the table does not exist.

The optional IF EXISTS clause, when used before the column name, causes the error to be suppressed if the column does not exist.

The optional IF NOT EXISTS clause causes the error to be suppressed if the column already exists.

The ALTER TABLE SET PROPERTIES statement followed by a number of property_name and expression pairs applies the specified properties and values to a table. Omitting an already-set property from this statement leaves that property unchanged in the table.

A property in a SET PROPERTIES statement can be set to DEFAULT, which reverts its value back to the default in that table.

Support for ALTER TABLE SET PROPERTIES varies between connectors, as not all connectors support modifying table properties.

The ALTER TABLE EXECUTE statement followed by a command and parameters modifies the table according to the specified command and parameters. ALTER TABLE EXECUTE supports different commands on a per-connector basis.

You can use the => operator for passing named parameter values. The left side is the name of the parameter, the right side is the value being passed.

Executable commands are contributed by connectors, such as the optimize command provided by the Hive, Delta Lake, and Iceberg connectors. For example, a user observing many small files in the storage of a table called test_table in the test schema of the example catalog, can use the optimize command to merge all files below the file_size_threshold value. The result is fewer, but larger files, which typically results in higher query performance on the data in the files:

Rename table users to people:

Rename table users to people if table users exists:

Add column zip to the users table:

Add column zip to the users table if table users exists and column zip not already exists:

Add column id as the first column to the users table:

Add column zip after column country to the users table:

Drop column zip from the users table:

Drop column zip from the users table if table users and column zip exists:

Rename column id to user_id in the users table:

Rename column id to user_id in the users table if table users and column id exists:

Change type of column id to bigint in the users table:

Drop a not null constraint on id column in the users table:

Change owner of table people to user alice:

Allow everyone with role public to drop and alter table people:

Set table properties (x = y) in table people:

Set multiple table properties (foo = 123 and foo bar = 456) in table people:

Set table property x to its default value in table``people``:

**Examples:**

Example 1 (javascript):
```javascript
ALTER TABLE [ IF EXISTS ] name RENAME TO new_name
ALTER TABLE [ IF EXISTS ] name ADD COLUMN [ IF NOT EXISTS ] column_name data_type
  [ DEFAULT default ] [ NOT NULL ] [ COMMENT comment ]
  [ WITH ( property_name = expression [, ...] ) ]
  [ FIRST | LAST | AFTER after_column_name ]
ALTER TABLE [ IF EXISTS ] name DROP COLUMN [ IF EXISTS ] column_name
ALTER TABLE [ IF EXISTS ] name RENAME COLUMN [ IF EXISTS ] old_name TO new_name
ALTER TABLE [ IF EXISTS ] name ALTER COLUMN column_name SET DATA TYPE new_type
ALTER TABLE [ IF EXISTS ] name ALTER COLUMN column_name DROP NOT NULL
ALTER TABLE name SET AUTHORIZATION ( user | USER user | ROLE role )
ALTER TABLE name SET PROPERTIES property_name = expression [, ...]
ALTER TABLE name EXECUTE command [ ( parameter => expression [, ... ] ) ]
    [ WHERE expression ]
```

Example 2 (javascript):
```javascript
ALTER TABLE [ IF EXISTS ] name RENAME TO new_name
ALTER TABLE [ IF EXISTS ] name ADD COLUMN [ IF NOT EXISTS ] column_name data_type
  [ DEFAULT default ] [ NOT NULL ] [ COMMENT comment ]
  [ WITH ( property_name = expression [, ...] ) ]
  [ FIRST | LAST | AFTER after_column_name ]
ALTER TABLE [ IF EXISTS ] name DROP COLUMN [ IF EXISTS ] column_name
ALTER TABLE [ IF EXISTS ] name RENAME COLUMN [ IF EXISTS ] old_name TO new_name
ALTER TABLE [ IF EXISTS ] name ALTER COLUMN column_name SET DATA TYPE new_type
ALTER TABLE [ IF EXISTS ] name ALTER COLUMN column_name DROP NOT NULL
ALTER TABLE name SET AUTHORIZATION ( user | USER user | ROLE role )
ALTER TABLE name SET PROPERTIES property_name = expression [, ...]
ALTER TABLE name EXECUTE command [ ( parameter => expression [, ... ] ) ]
    [ WHERE expression ]
```

Example 3 (javascript):
```javascript
ALTER TABLE example.test.test_table EXECUTE optimize(file_size_threshold => '16MB')
```

Example 4 (javascript):
```javascript
ALTER TABLE example.test.test_table EXECUTE optimize(file_size_threshold => '16MB')
```

---

## DESCRIBE OUTPUT — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/describe-output.html

**Contents:**
- DESCRIBE OUTPUT#
- Synopsis#
- Description#
- Examples#
- See also#

List the output columns of a prepared statement, including the column name (or alias), catalog, schema, table, type, type size in bytes, and a boolean indicating if the column is aliased.

Prepare and describe a query with four output columns:

Prepare and describe a query whose output columns are expressions:

Prepare and describe a row count query:

**Examples:**

Example 1 (unknown):
```unknown
DESCRIBE OUTPUT statement_name
```

Example 2 (unknown):
```unknown
DESCRIBE OUTPUT statement_name
```

Example 3 (unknown):
```unknown
PREPARE my_select1 FROM
SELECT * FROM nation;
```

Example 4 (unknown):
```unknown
PREPARE my_select1 FROM
SELECT * FROM nation;
```

---

## CREATE FUNCTION — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/create-function.html

**Contents:**
- CREATE FUNCTION#
- Synopsis#
- Description#
- Examples#
- See also#

Create or replace a Catalog user-defined functions. The udf_definition is composed of the usage of FUNCTION and nested statements. The name of the UDF must be fully qualified with catalog and schema location, unless the default UDF storage catalog and schema are configured. The connector used in the catalog must support UDF storage.

The optional OR REPLACE clause causes the UDF to be replaced if it already exists rather than raising an error.

The following example creates the meaning_of_life UDF in the default schema of the example catalog:

If the default catalog and schema for UDF storage is configured, you can use the following more compact syntax:

Further examples of varying complexity that cover usage of the FUNCTION statement in combination with other statements are available in the SQL UDF examples documentation.

User-defined functions

SQL environment properties

**Examples:**

Example 1 (unknown):
```unknown
CREATE [OR REPLACE] FUNCTION
  udf_definition
```

Example 2 (unknown):
```unknown
CREATE [OR REPLACE] FUNCTION
  udf_definition
```

Example 3 (unknown):
```unknown
CREATE FUNCTION example.default.meaning_of_life()
  RETURNS bigint
  BEGIN
    RETURN 42;
  END;
```

Example 4 (unknown):
```unknown
CREATE FUNCTION example.default.meaning_of_life()
  RETURNS bigint
  BEGIN
    RETURN 42;
  END;
```

---

## DEALLOCATE PREPARE — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/deallocate-prepare.html

**Contents:**
- DEALLOCATE PREPARE#
- Synopsis#
- Description#
- Examples#
- See also#

Removes a statement with the name statement_name from the list of prepared statements in a session.

Deallocate a statement with the name my_query:

PREPARE, EXECUTE, EXECUTE IMMEDIATE

**Examples:**

Example 1 (unknown):
```unknown
DEALLOCATE PREPARE statement_name
```

Example 2 (unknown):
```unknown
DEALLOCATE PREPARE statement_name
```

Example 3 (unknown):
```unknown
DEALLOCATE PREPARE my_query;
```

Example 4 (unknown):
```unknown
DEALLOCATE PREPARE my_query;
```

---

## ALTER MATERIALIZED VIEW — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/alter-materialized-view.html

**Contents:**
- ALTER MATERIALIZED VIEW#
- Synopsis#
- Description#
  - SET PROPERTIES#
- Examples#
- See also#

Change the name of an existing materialized view.

The optional IF EXISTS clause causes the error to be suppressed if the materialized view does not exist. The error is not suppressed if the materialized view does not exist, but a table or view with the given name exists.

The ALTER MATERIALIZED VIEW SET PROPERTIES statement followed by some number of property_name and expression pairs applies the specified properties and values to a materialized view. Omitting an already-set property from this statement leaves that property unchanged in the materialized view.

A property in a SET PROPERTIES statement can be set to DEFAULT, which reverts its value back to the default in that materialized view.

Support for ALTER MATERIALIZED VIEW SET PROPERTIES varies between connectors. Refer to the connector documentation for more details.

Rename materialized view people to users in the current schema:

Rename materialized view people to users, if materialized view people exists in the current catalog and schema:

Set view properties (x = y) in materialized view people:

Set multiple view properties (foo = 123 and foo bar = 456) in materialized view people:

Set view property x to its default value in materialized view people:

Change owner of materialized view people to user alice:

CREATE MATERIALIZED VIEW

REFRESH MATERIALIZED VIEW

DROP MATERIALIZED VIEW

**Examples:**

Example 1 (unknown):
```unknown
ALTER MATERIALIZED VIEW [ IF EXISTS ] name RENAME TO new_name
ALTER MATERIALIZED VIEW name SET PROPERTIES property_name = expression [, ...]
ALTER MATERIALIZED VIEW name SET AUTHORIZATION ( user | USER user | ROLE role )
```

Example 2 (unknown):
```unknown
ALTER MATERIALIZED VIEW [ IF EXISTS ] name RENAME TO new_name
ALTER MATERIALIZED VIEW name SET PROPERTIES property_name = expression [, ...]
ALTER MATERIALIZED VIEW name SET AUTHORIZATION ( user | USER user | ROLE role )
```

Example 3 (unknown):
```unknown
ALTER MATERIALIZED VIEW people RENAME TO users;
```

Example 4 (unknown):
```unknown
ALTER MATERIALIZED VIEW people RENAME TO users;
```

---

## SHOW COLUMNS — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/show-columns.html

**Contents:**
- SHOW COLUMNS#
- Synopsis#
- Description#

List the columns in a table along with their data type and other attributes:

Specify a pattern in the optional LIKE clause to filter the results to the desired subset. For example, the following query allows you to find columns ending in key:

**Examples:**

Example 1 (unknown):
```unknown
SHOW COLUMNS FROM table [ LIKE pattern ]
```

Example 2 (unknown):
```unknown
SHOW COLUMNS FROM table [ LIKE pattern ]
```

Example 3 (unknown):
```unknown
SHOW COLUMNS FROM nation;
```

Example 4 (unknown):
```unknown
SHOW COLUMNS FROM nation;
```

---

## RESET SESSION AUTHORIZATION — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/reset-session-authorization.html

**Contents:**
- RESET SESSION AUTHORIZATION#
- Synopsis#
- Description#
- See also#

Resets the current authorization user back to the original user. The original user is usually the authenticated user (principal), or it can be the session user when the session user is provided by the client.

SET SESSION AUTHORIZATION

**Examples:**

Example 1 (unknown):
```unknown
RESET SESSION AUTHORIZATION
```

Example 2 (unknown):
```unknown
RESET SESSION AUTHORIZATION
```

---

## Session information — Trino 478 Documentation

**URL:** https://trino.io/docs/current/functions/session.html

**Contents:**
- Session information#

Functions providing information about the query execution environment.

Returns the current user running the query.

Returns the list of groups for the current user running the query.

Returns a character string that represents the current catalog name.

Returns a character string that represents the current unqualified schema name.

This is part of the SQL standard and does not use parenthesis.

---

## REVOKE role — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/revoke-roles.html

**Contents:**
- REVOKE role#
- Synopsis#
- Description#
- Examples#
- Limitations#
- See also#

Revokes the specified role(s) from the specified principal(s).

If the ADMIN OPTION FOR clause is specified, the GRANT permission is revoked instead of the role.

For the REVOKE statement for roles to succeed, the user executing it either should be the role admin or should possess the GRANT option for the given role.

The optional GRANTED BY clause causes the role(s) to be revoked with the specified principal as a revoker. If the GRANTED BY clause is not specified, the roles are revoked by the current user as a revoker.

The optional IN catalog clause revokes the roles in a catalog as opposed to a system roles.

Revoke role bar from user foo

Revoke admin option for roles bar and foo from user baz and role qux

Some connectors do not support role management. See connector documentation for more details.

CREATE ROLE, DROP ROLE, SET ROLE, GRANT role

**Examples:**

Example 1 (unknown):
```unknown
REVOKE
[ ADMIN OPTION FOR ]
role_name [, ...]
FROM ( user | USER user | ROLE role) [, ...]
[ GRANTED BY ( user | USER user | ROLE role | CURRENT_USER | CURRENT_ROLE ) ]
[ IN catalog ]
```

Example 2 (unknown):
```unknown
REVOKE
[ ADMIN OPTION FOR ]
role_name [, ...]
FROM ( user | USER user | ROLE role) [, ...]
[ GRANTED BY ( user | USER user | ROLE role | CURRENT_USER | CURRENT_ROLE ) ]
[ IN catalog ]
```

Example 3 (unknown):
```unknown
REVOKE bar FROM USER foo;
```

Example 4 (unknown):
```unknown
REVOKE bar FROM USER foo;
```

---

## LEAVE — Trino 478 Documentation

**URL:** https://trino.io/docs/current/udf/sql/leave.html

**Contents:**
- LEAVE#
- Synopsis#
- Description#
- Examples#
- See also#

The LEAVE statement allows processing of blocks in SQL user-defined functions to move out of a specified context. Contexts are defined by a label. If no label is found, the functions fails with an error message.

The following function includes a LOOP labelled top. The conditional IF statement inside the loop can cause the exit from processing the loop when the value for the parameter p is 1 or less. This can be the case if the value is passed in as 1 or less or after a number of iterations through the loop.

Further examples of varying complexity that cover usage of the LEAVE statement in combination with other statements are available in the Example SQL UDFs.

SQL user-defined functions

**Examples:**

Example 1 (unknown):
```unknown
LEAVE label
```

Example 2 (unknown):
```unknown
LEAVE label
```

Example 3 (unknown):
```unknown
FUNCTION my_pow(n int, p int)
RETURNS int
BEGIN
  DECLARE r int DEFAULT n;
  top: LOOP
    IF p <= 1 THEN
      LEAVE top;
    END IF;
    SET r = r * n;
    SET p = p - 1;
  END LOOP;
  RETURN r;
END
```

Example 4 (unknown):
```unknown
FUNCTION my_pow(n int, p int)
RETURNS int
BEGIN
  DECLARE r int DEFAULT n;
  top: LOOP
    IF p <= 1 THEN
      LEAVE top;
    END IF;
    SET r = r * n;
    SET p = p - 1;
  END LOOP;
  RETURN r;
END
```

---

## SET PATH — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/set-path.html

**Contents:**
- SET PATH#
- Synopsis#
- Description#
- Examples#
- See also#

Define a collection of paths to functions or table functions in specific catalogs and schemas for the current session.

Each path-element uses a period-separated syntax to specify the catalog name and schema location <catalog>.<schema> of the function, or only the schema location <schema> in the current catalog. The current catalog is set with USE, or as part of a client tool connection. Catalog and schema must exist.

The following example sets a path to access functions in the system schema of the example catalog:

The catalog uses the PostgreSQL connector, and you can therefore use the query table function directly, without the full catalog and schema qualifiers:

SQL environment properties

**Examples:**

Example 1 (unknown):
```unknown
SET PATH path-element[, ...]
```

Example 2 (unknown):
```unknown
SET PATH path-element[, ...]
```

Example 3 (unknown):
```unknown
SET PATH example.system;
```

Example 4 (unknown):
```unknown
SET PATH example.system;
```

---

## DROP ROLE — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/drop-role.html

**Contents:**
- DROP ROLE#
- Synopsis#
- Description#
- Examples#
- Limitations#
- See also#

DROP ROLE drops the specified role.

For DROP ROLE statement to succeed, the user executing it should possess admin privileges for the given role.

The optional IF EXISTS prevents the statement from failing if the role isn’t found.

The optional IN catalog clause drops the role in a catalog as opposed to a system role.

Some connectors do not support role management. See connector documentation for more details.

CREATE ROLE, SET ROLE, GRANT role, REVOKE role

**Examples:**

Example 1 (unknown):
```unknown
DROP ROLE [ IF EXISTS ] role_name
[ IN catalog ]
```

Example 2 (unknown):
```unknown
DROP ROLE [ IF EXISTS ] role_name
[ IN catalog ]
```

Example 3 (unknown):
```unknown
DROP ROLE admin;
```

Example 4 (unknown):
```unknown
DROP ROLE admin;
```

---

## MERGE — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/merge.html

**Contents:**
- MERGE#
- Synopsis#
- Description#
- Examples#
- Limitations#

where when_clause is one of

Conditionally update and/or delete rows of a table and/or insert new rows into a table.

MERGE changes data in the target_table based on the contents of the source_table. The search_condition defines a condition, such as a relation from identical columns, to associate the source and target data.

MERGE supports an arbitrary number of WHEN clauses. MATCHED conditions can execute DELETE or UPDATE operations on the target data, while NOT MATCHED conditions can add data from the source to the target table with INSERT. Additional conditions can narrow down the affected rows.

For each source row, the WHEN clauses are processed in order. Only the first matching WHEN clause is executed and subsequent clauses are ignored. The query fails if a single target table row matches more than one source row.

In WHEN clauses with UPDATE operations, the column value expressions can depend on any field of the target or the source. In the NOT MATCHED case, the INSERT expressions can depend on any field of the source.

Typical usage of MERGE involves two tables with similar structure, containing different data. For example, the source table is part of a transactional usage in a production system, while the target table is located in a data warehouse used for analytics. Periodically, MERGE operations are run to combine recent production data with long-term data in the analytics warehouse. As long as you can define a search condition between the two tables, you can also use very different tables.

Delete all customers mentioned in the source table:

For matching customer rows, increment the purchases, and if there is no match, insert the row from the source table:

MERGE into the target table from the source table, deleting any matching target row for which the source address is Centreville. For all other matching rows, add the source purchases and set the address to the source address. If there is no match in the target table, insert the source table row:

Delete all customers mentioned in audit branch of the source table:

Any connector can be used as a source table for a MERGE statement. Only connectors which support the MERGE statement can be the target of a merge operation. See the connector documentation for more information.

**Examples:**

Example 1 (unknown):
```unknown
MERGE INTO target_table [ @ branch_name ] [ [ AS ]  target_alias ]
USING { source_table | query } [ [ AS ] source_alias ]
ON search_condition
when_clause [...]
```

Example 2 (unknown):
```unknown
MERGE INTO target_table [ @ branch_name ] [ [ AS ]  target_alias ]
USING { source_table | query } [ [ AS ] source_alias ]
ON search_condition
when_clause [...]
```

Example 3 (unknown):
```unknown
WHEN MATCHED [ AND condition ]
    THEN DELETE
```

Example 4 (unknown):
```unknown
WHEN MATCHED [ AND condition ]
    THEN DELETE
```

---

## REVOKE privilege — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/revoke.html

**Contents:**
- REVOKE privilege#
- Synopsis#
- Description#
- Examples#
- Limitations#
- See also#

Revokes the specified privileges from the specified grantee.

Specifying ALL PRIVILEGES revokes DELETE, INSERT and SELECT privileges.

Specifying ROLE PUBLIC revokes privileges from the PUBLIC role. Users will retain privileges assigned to them directly or via other roles.

If the optional GRANT OPTION FOR clause is specified, only the GRANT OPTION is removed. Otherwise, both the GRANT and GRANT OPTION are revoked.

For REVOKE statement to succeed, the user executing it should possess the specified privileges as well as the GRANT OPTION for those privileges.

Revoke on a table revokes the specified privilege on all columns of the table.

Revoke on a schema revokes the specified privilege on all columns of all tables of the schema.

Revoke INSERT and SELECT privileges on the table orders from user alice:

Revoke DELETE privilege on the schema finance from user bob:

Revoke SELECT privilege on the table nation from everyone, additionally revoking the privilege to grant SELECT privilege:

Revoke all privileges on the table test from user alice:

Revoke INSERT privilege on the audit branch of the orders table from user alice:

Some connectors have no support for REVOKE. See connector documentation for more details.

DENY, GRANT privilege, SHOW GRANTS

**Examples:**

Example 1 (unknown):
```unknown
REVOKE [ GRANT OPTION FOR ]
( privilege [, ...] | ALL PRIVILEGES )
ON [ BRANCH branch_name IN ] ( table_name | TABLE table_name | SCHEMA schema_name )
FROM ( user | USER user | ROLE role )
```

Example 2 (unknown):
```unknown
REVOKE [ GRANT OPTION FOR ]
( privilege [, ...] | ALL PRIVILEGES )
ON [ BRANCH branch_name IN ] ( table_name | TABLE table_name | SCHEMA schema_name )
FROM ( user | USER user | ROLE role )
```

Example 3 (unknown):
```unknown
REVOKE INSERT, SELECT ON orders FROM alice;
```

Example 4 (unknown):
```unknown
REVOKE INSERT, SELECT ON orders FROM alice;
```

---

## SHOW ROLE GRANTS — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/show-role-grants.html

**Contents:**
- SHOW ROLE GRANTS#
- Synopsis#
- Description#

List non-recursively the system roles or roles in catalog that have been granted to the session user.

**Examples:**

Example 1 (unknown):
```unknown
SHOW ROLE GRANTS [ FROM catalog ]
```

Example 2 (unknown):
```unknown
SHOW ROLE GRANTS [ FROM catalog ]
```

---

## RETURN — Trino 478 Documentation

**URL:** https://trino.io/docs/current/udf/sql/return.html

**Contents:**
- RETURN#
- Synopsis#
- Description#
- Examples#
- See also#

Provide the value from a SQL user-defined functions to the caller. The value is the result of evaluating the expression. It can be a static value, a declared variable or a more complex expression.

The following examples return a static value, the result of an expression, and the value of the variable x:

Further examples of varying complexity that cover usage of the RETURN statement in combination with other statements are available in the Example SQL UDFs.

All SQL UDFs must contain a RETURN statement at the end of the top-level block in the FUNCTION declaration, even if it’s unreachable.

SQL user-defined functions

**Examples:**

Example 1 (unknown):
```unknown
RETURN expression
```

Example 2 (unknown):
```unknown
RETURN expression
```

Example 3 (unknown):
```unknown
RETURN 42;
RETURN 6 * 7;
RETURN x;
```

Example 4 (unknown):
```unknown
RETURN 42;
RETURN 6 * 7;
RETURN x;
```

---

## ALTER SCHEMA — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/alter-schema.html

**Contents:**
- ALTER SCHEMA#
- Synopsis#
- Description#
- Examples#
- See Also#

Change the definition of an existing schema.

Rename schema web to traffic:

Change owner of schema web to user alice:

Allow everyone to drop schema and create tables in schema web:

**Examples:**

Example 1 (unknown):
```unknown
ALTER SCHEMA name RENAME TO new_name
ALTER SCHEMA name SET AUTHORIZATION ( user | USER user | ROLE role )
```

Example 2 (unknown):
```unknown
ALTER SCHEMA name RENAME TO new_name
ALTER SCHEMA name SET AUTHORIZATION ( user | USER user | ROLE role )
```

Example 3 (unknown):
```unknown
ALTER SCHEMA web RENAME TO traffic
```

Example 4 (unknown):
```unknown
ALTER SCHEMA web RENAME TO traffic
```

---

## SET SESSION AUTHORIZATION — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/set-session-authorization.html

**Contents:**
- SET SESSION AUTHORIZATION#
- Synopsis#
- Description#
- Examples#
- See also#

Changes the current user of the session. For the SET SESSION AUTHORIZATION username statement to succeed, the original user (that the client connected with) must be able to impersonate the specified user. User impersonation can be enabled in the system access control.

In the following example, the original user when the connection to Trino is made is Kevin. The following sets the session authorization user to John:

Queries will now execute as John instead of Kevin.

All supported syntax to change the session authorization users are shown below.

Changing the session authorization with single quotes:

Changing the session authorization with double quotes:

Changing the session authorization without quotes:

RESET SESSION AUTHORIZATION

**Examples:**

Example 1 (unknown):
```unknown
SET SESSION AUTHORIZATION username
```

Example 2 (unknown):
```unknown
SET SESSION AUTHORIZATION username
```

Example 3 (unknown):
```unknown
SET SESSION AUTHORIZATION 'John';
```

Example 4 (unknown):
```unknown
SET SESSION AUTHORIZATION 'John';
```

---

## GRANT privilege — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/grant.html

**Contents:**
- GRANT privilege#
- Synopsis#
- Description#
- Examples#
- Limitations#
- See also#

Grants the specified privileges to the specified grantee.

Specifying ALL PRIVILEGES grants DELETE, INSERT, UPDATE and SELECT privileges.

Specifying ROLE PUBLIC grants privileges to the PUBLIC role and hence to all users.

The optional WITH GRANT OPTION clause allows the grantee to grant these same privileges to others.

For GRANT statement to succeed, the user executing it should possess the specified privileges as well as the GRANT OPTION for those privileges.

Grant on a table grants the specified privilege on all current and future columns of the table.

Grant on a schema grants the specified privilege on all current and future columns of all current and future tables of the schema.

Grant INSERT and SELECT privileges on the table orders to user alice:

Grant DELETE privilege on the schema finance to user bob:

Grant SELECT privilege on the table nation to user alice, additionally allowing alice to grant SELECT privilege to others:

Grant SELECT privilege on the table orders to everyone:

Grant INSERT privilege on the audit branch of the orders table to user alice:

Some connectors have no support for GRANT. See connector documentation for more details.

DENY, REVOKE privilege, SHOW GRANTS

**Examples:**

Example 1 (unknown):
```unknown
GRANT ( privilege [, ...] | ( ALL PRIVILEGES ) )
ON [ BRANCH branch_name IN ] ( table_name | TABLE table_name | SCHEMA schema_name)
TO ( user | USER user | ROLE role )
[ WITH GRANT OPTION ]
```

Example 2 (unknown):
```unknown
GRANT ( privilege [, ...] | ( ALL PRIVILEGES ) )
ON [ BRANCH branch_name IN ] ( table_name | TABLE table_name | SCHEMA schema_name)
TO ( user | USER user | ROLE role )
[ WITH GRANT OPTION ]
```

Example 3 (unknown):
```unknown
GRANT INSERT, SELECT ON orders TO alice;
```

Example 4 (unknown):
```unknown
GRANT INSERT, SELECT ON orders TO alice;
```

---

## IF — Trino 478 Documentation

**URL:** https://trino.io/docs/current/udf/sql/if.html

**Contents:**
- IF#
- Synopsis#
- Description#
- Examples#
- See also#

The IF THEN statement is an optional construct to allow conditional processing in SQL user-defined functions. Each condition following an IF or ELSEIF must evaluate to a boolean. The result of processing the expression must result in a boolean true value to process the statements in the THEN block. A result of false results in skipping the THEN block and moving to evaluate the next ELSEIF and ELSE blocks in order.

The ELSEIF and ELSE segments are optional.

Further examples of varying complexity that cover usage of the IF statement in combination with other statements are available in the Example SQL UDFs.

SQL user-defined functions

Conditional expressions using IF

**Examples:**

Example 1 (unknown):
```unknown
IF condition
  THEN statements
  [ ELSEIF condition THEN statements ]
  [ ... ]
  [ ELSE statements ]
END IF
```

Example 2 (unknown):
```unknown
IF condition
  THEN statements
  [ ELSEIF condition THEN statements ]
  [ ... ]
  [ ELSE statements ]
END IF
```

Example 3 (unknown):
```unknown
FUNCTION simple_if(a bigint)
  RETURNS varchar
  BEGIN
    IF a = 0 THEN
      RETURN 'zero';
    ELSEIF a = 1 THEN
      RETURN 'one';
    ELSE
      RETURN 'more than one or negative';
    END IF;
  END
```

Example 4 (unknown):
```unknown
FUNCTION simple_if(a bigint)
  RETURNS varchar
  BEGIN
    IF a = 0 THEN
      RETURN 'zero';
    ELSEIF a = 1 THEN
      RETURN 'one';
    ELSE
      RETURN 'more than one or negative';
    END IF;
  END
```

---

## SHOW STATS — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/show-stats.html

**Contents:**
- SHOW STATS#
- Synopsis#
- Description#

Returns approximated statistics for the named table or for the results of a query. Returns NULL for any statistics that are not populated or unavailable on the data source.

Statistics are returned as a row for each column, plus a summary row for the table (identifiable by a NULL value for column_name). The following table lists the returned columns and what statistics they represent. Any additional statistics collected on the data source, other than those listed here, are not included.

The name of the column

NULL in the table summary row

The total size in bytes of all the values in the column

NULL in the table summary row. Available for columns of string data types with variable widths.

distinct_values_count

The estimated number of distinct values in the column

NULL in the table summary row

The portion of the values in the column that are NULL

NULL in the table summary row.

The estimated number of rows in the table

NULL in column statistic rows

The lowest value found in this column

NULL in the table summary row. Available for columns of DATE, integer, floating-point, and exact numeric data types.

The highest value found in this column

NULL in the table summary row. Available for columns of DATE, integer, floating-point, and exact numeric data types.

**Examples:**

Example 1 (unknown):
```unknown
SHOW STATS FOR table
SHOW STATS FOR ( query )
```

Example 2 (unknown):
```unknown
SHOW STATS FOR table
SHOW STATS FOR ( query )
```

---

## EXECUTE — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/execute.html

**Contents:**
- EXECUTE#
- Synopsis#
- Description#
- Examples#
- See also#

Executes a prepared statement with the name statement_name. Parameter values are defined in the USING clause.

Prepare and execute a query with no parameters:

Prepare and execute a query with two parameters:

This is equivalent to:

PREPARE, DEALLOCATE PREPARE, EXECUTE IMMEDIATE

**Examples:**

Example 1 (unknown):
```unknown
EXECUTE statement_name [ USING parameter1 [ , parameter2, ... ] ]
```

Example 2 (unknown):
```unknown
EXECUTE statement_name [ USING parameter1 [ , parameter2, ... ] ]
```

Example 3 (unknown):
```unknown
PREPARE my_select1 FROM
SELECT name FROM nation;
```

Example 4 (unknown):
```unknown
PREPARE my_select1 FROM
SELECT name FROM nation;
```

---

## SET SESSION — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/set-session.html

**Contents:**
- SET SESSION#
- Synopsis#
- Description#
- Session properties#
- Examples#
- See also#

Set a session property value or a catalog session property.

A session property is a configuration property that can be temporarily modified by a user for the duration of the current connection session to the Trino cluster. Many configuration properties have a corresponding session property that accepts the same values as the config property.

There are two types of session properties:

System session properties apply to the whole cluster. Most session properties are system session properties unless specified otherwise.

Catalog session properties are connector-defined session properties that can be set on a per-catalog basis. These properties must be set separately for each catalog by including the catalog name as a prefix, such as catalogname.property_name.

Session properties are tied to the current session, so a user can have multiple connections to a cluster that each have different values for the same session properties. Once a session ends, either by disconnecting or creating a new session, any changes made to session properties during the previous session are lost.

The following example sets a system session property change maximum query run time:

The following example sets the incremental_refresh_enabled catalog session property for a catalog using the Iceberg connector named example:

The related catalog configuration property iceberg.incremental-refresh-enabled defaults to true, and the session property allows you to override this setting in for specific catalog and the current session. The example.incremental_refresh_enabled catalog session property does not apply to any other catalog, even if another catalog also uses the Iceberg connector.

RESET SESSION, SHOW SESSION

**Examples:**

Example 1 (unknown):
```unknown
SET SESSION name = expression
SET SESSION catalog.name = expression
```

Example 2 (unknown):
```unknown
SET SESSION name = expression
SET SESSION catalog.name = expression
```

Example 3 (unknown):
```unknown
SET SESSION query_max_run_time = '10m';
```

Example 4 (unknown):
```unknown
SET SESSION query_max_run_time = '10m';
```

---

## CREATE ROLE — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/create-role.html

**Contents:**
- CREATE ROLE#
- Synopsis#
- Description#
- Examples#
- Limitations#
- See also#

CREATE ROLE creates the specified role.

The optional WITH ADMIN clause causes the role to be created with the specified user as a role admin. A role admin has permission to drop or grant a role. If the optional WITH ADMIN clause is not specified, the role is created with current user as admin.

The optional IN catalog clause creates the role in a catalog as opposed to a system role.

Create role moderator with admin bob:

Some connectors do not support role management. See connector documentation for more details.

DROP ROLE, SET ROLE, GRANT role, REVOKE role

**Examples:**

Example 1 (unknown):
```unknown
CREATE ROLE role_name
[ WITH ADMIN ( user | USER user | ROLE role | CURRENT_USER | CURRENT_ROLE ) ]
[ IN catalog ]
```

Example 2 (unknown):
```unknown
CREATE ROLE role_name
[ WITH ADMIN ( user | USER user | ROLE role | CURRENT_USER | CURRENT_ROLE ) ]
[ IN catalog ]
```

Example 3 (unknown):
```unknown
CREATE ROLE admin;
```

Example 4 (unknown):
```unknown
CREATE ROLE admin;
```

---

## SELECT — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/select.html

**Contents:**
- SELECT#
- Synopsis#
- Description#
- WITH SESSION clause#
- WITH FUNCTION clause#
- WITH clause#
- WITH RECURSIVE clause#
- SELECT clause#
  - Select expressions#
- GROUP BY clause#

where from_item is one of

For detailed description of MATCH_RECOGNIZE clause, see pattern recognition in FROM clause.

For description of table functions usage, see table functions.

and join_type is one of

and grouping_element is one of

Retrieve rows from zero or more tables.

The WITH SESSION clause allows you to set session and catalog session property values applicable for the processing of the current SELECT statement only. The defined values override any other configuration and session property settings. Multiple properties are separated by commas.

The following example overrides the global configuration property query.max-execution-time with the session property query_max_execution_time to reduce the time to 2h. It also overrides the catalog property iceberg.query-partition-filter-required from the example catalog using Iceberg connector setting the catalog session property query_partition_filter_required to true:

The WITH FUNCTION clause allows you to define a list of Inline user-defined functions that are available for use in the rest of the query.

The following example declares and uses two inline UDFs:

Find further information about UDFs in general, inline UDFs, all supported statements, and examples in User-defined functions.

The WITH clause defines named relations for use within a query. It allows flattening nested queries or simplifying subqueries. For example, the following queries are equivalent:

This also works with multiple subqueries:

Additionally, the relations within a WITH clause can chain:

Currently, the SQL for the WITH clause will be inlined anywhere the named relation is used. This means that if the relation is used more than once and the query is non-deterministic, the results may be different each time.

The WITH RECURSIVE clause is a variant of the WITH clause. It defines a list of queries to process, including recursive processing of suitable queries.

This feature is experimental only. Proceed to use it only if you understand potential query failures and the impact of the recursion processing on your workload.

A recursive WITH-query must be shaped as a UNION of two relations. The first relation is called the recursion base, and the second relation is called the recursion step. Trino supports recursive WITH-queries with a single recursive reference to a WITH-query from within the query. The name T of the query T can be mentioned once in the FROM clause of the recursion step relation.

The following listing shows a simple example, that displays a commonly used form of a single query in the list:

In the preceding query the simple assignment VALUES (1) defines the recursion base relation. SELECT n + 1 FROM t WHERE n < 4 defines the recursion step relation. The recursion processing performs these steps:

recursive base yields 1

first recursion yields 1 + 1 = 2

second recursion uses the result from the first and adds one: 2 + 1 = 3

third recursion uses the result from the second and adds one again: 3 + 1 = 4

fourth recursion aborts since n = 4

this results in t having values 1, 2, 3 and 4

the final statement performs the sum operation of these elements with the final result value 10

The types of the returned columns are those of the base relation. Therefore it is required that types in the step relation can be coerced to base relation types.

The RECURSIVE clause applies to all queries in the WITH list, but not all of them must be recursive. If a WITH-query is not shaped according to the rules mentioned above or it does not contain a recursive reference, it is processed like a regular WITH-query. Column aliases are mandatory for all the queries in the recursive WITH list.

The following limitations apply as a result of following the SQL standard and due to implementation choices, in addition to WITH clause limitations:

only single-element recursive cycles are supported. Like in regular WITH-queries, references to previous queries in the WITH list are allowed. References to following queries are forbidden.

usage of outer joins, set operations, limit clause, and others is not always allowed in the step relation

recursion depth is fixed, defaults to 10, and doesn’t depend on the actual query results

You can adjust the recursion depth with the session property max_recursion_depth. When changing the value consider that the size of the query plan growth is quadratic with the recursion depth.

The SELECT clause specifies the output of the query. Each select_expression defines a column or columns to be included in the result.

The ALL and DISTINCT quantifiers determine whether duplicate rows are included in the result set. If the argument ALL is specified, all rows are included. If the argument DISTINCT is specified, only unique rows are included in the result set. In this case, each output column must be of a type that allows comparison. If neither argument is specified, the behavior defaults to ALL.

Each select_expression must be in one of the following forms:

In the case of expression [ [ AS ] column_alias ], a single output column is defined.

In the case of row_expression.* [ AS ( column_alias [, ...] ) ], the row_expression is an arbitrary expression of type ROW. All fields of the row define output columns to be included in the result set.

In the case of relation.*, all columns of relation are included in the result set. In this case column aliases are not allowed.

In the case of *, all columns of the relation defined by the query are included in the result set.

In the result set, the order of columns is the same as the order of their specification by the select expressions. If a select expression returns multiple columns, they are ordered the same way they were ordered in the source relation or row type expression.

If column aliases are specified, they override any preexisting column or row field names:

Otherwise, the existing names are used:

and in their absence, anonymous columns are produced:

The GROUP BY clause divides the output of a SELECT statement into groups of rows containing matching values. A simple GROUP BY clause may contain any expression composed of input columns or it may be an ordinal number selecting an output column by position (starting at one).

The following queries are equivalent. They both group the output by the nationkey input column with the first query using the ordinal position of the output column and the second query using the input column name:

GROUP BY clauses can group output by input column names not appearing in the output of a select statement. For example, the following query generates row counts for the customer table using the input column mktsegment:

When a GROUP BY clause is used in a SELECT statement all output expressions must be either aggregate functions or columns present in the GROUP BY clause.

Trino also supports complex aggregations using the GROUPING SETS, CUBE and ROLLUP syntax. This syntax allows users to perform analysis that requires aggregation on multiple sets of columns in a single query. Complex grouping operations do not support grouping on expressions composed of input columns. Only column names are allowed.

Complex grouping operations are often equivalent to a UNION ALL of simple GROUP BY expressions, as shown in the following examples. This equivalence does not apply, however, when the source of data for the aggregation is non-deterministic.

When AUTO is specified, the Trino engine automatically determines the grouping columns instead of requiring them to be listed explicitly. In this mode, any column in the SELECT list that is not part of an aggregate function is implicitly treated as a grouping column.

This example query calculates the total account balance per market segment. The AUTO clause derives mktsegment as the grouping key, since it is not used in any aggregate function (i.e., sum).

Grouping sets allow users to specify multiple lists of columns to group on. The columns not part of a given sublist of grouping columns are set to NULL.

GROUPING SETS semantics are demonstrated by this example query:

The preceding query may be considered logically equivalent to a UNION ALL of multiple GROUP BY queries:

However, the query with the complex grouping syntax (GROUPING SETS, CUBE or ROLLUP) will only read from the underlying data source once, while the query with the UNION ALL reads the underlying data three times. This is why queries with a UNION ALL may produce inconsistent results when the data source is not deterministic.

The CUBE operator generates all possible grouping sets (i.e. a power set) for a given set of columns. For example, the query:

The ROLLUP operator generates all possible subtotals for a given set of columns. For example, the query:

Multiple grouping expressions in the same query are interpreted as having cross-product semantics. For example, the following query:

which can be rewritten as:

is logically equivalent to:

The ALL and DISTINCT quantifiers determine whether duplicate grouping sets each produce distinct output rows. This is particularly useful when multiple complex grouping sets are combined in the same query. For example, the following query:

However, if the query uses the DISTINCT quantifier for the GROUP BY:

only unique grouping sets are generated:

The default set quantifier is ALL.

grouping(col1, ..., colN) -> bigint

The grouping operation returns a bit set converted to decimal, indicating which columns are present in a grouping. It must be used in conjunction with GROUPING SETS, ROLLUP, CUBE or GROUP BY and its arguments must match exactly the columns referenced in the corresponding GROUPING SETS, ROLLUP, CUBE or GROUP BY clause.

To compute the resulting bit set for a particular row, bits are assigned to the argument columns with the rightmost column being the least significant bit. For a given grouping, a bit is set to 0 if the corresponding column is included in the grouping and to 1 otherwise. For example, consider the query below:

The first grouping in the above result only includes the origin_state column and excludes the origin_zip and destination_state columns. The bit set constructed for that grouping is 011 where the most significant bit represents origin_state.

The HAVING clause is used in conjunction with aggregate functions and the GROUP BY clause to control which groups are selected. A HAVING clause eliminates groups that do not satisfy the given conditions. HAVING filters groups after groups and aggregates are computed.

The following example queries the customer table and selects groups with an account balance greater than the specified value:

The WINDOW clause is used to define named window specifications. The defined named window specifications can be referred to in the SELECT and ORDER BY clauses of the enclosing query:

The window definition list of WINDOW clause can contain one or multiple named window specifications of the form

A window specification has the following components:

The existing window name, which refers to a named window specification in the WINDOW clause. The window specification associated with the referenced name is the basis of the current specification.

The partition specification, which separates the input rows into different partitions. This is analogous to how the GROUP BY clause separates rows into different groups for aggregate functions.

The ordering specification, which determines the order in which input rows will be processed by the window function.

The window frame, which specifies a sliding window of rows to be processed by the function for a given row. If the frame is not specified, it defaults to RANGE UNBOUNDED PRECEDING, which is the same as RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW. This frame contains all rows from the start of the partition up to the last peer of the current row. In the absence of ORDER BY, all rows are considered peers, so RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW is equivalent to BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING. The window frame syntax supports additional clauses for row pattern recognition. If the row pattern recognition clauses are specified, the window frame for a particular row consists of the rows matched by a pattern starting from that row. Additionally, if the frame specifies row pattern measures, they can be called over the window, similarly to window functions. For more details, see Row pattern recognition in window structures .

Each window component is optional. If a window specification does not specify window partitioning, ordering or frame, those components are obtained from the window specification referenced by the existing window name, or from another window specification in the reference chain. In case when there is no existing window name specified, or none of the referenced window specifications contains the component, the default value is used.

UNION INTERSECT and EXCEPT are all set operations. These clauses are used to combine the results of more than one select statement into a single result set:

The argument ALL or DISTINCT controls which rows are included in the final result set. If the argument ALL is specified all rows are included even if the rows are identical. If the argument DISTINCT is specified only unique rows are included in the combined result set. If neither is specified, the behavior defaults to DISTINCT.

Multiple set operations are processed left to right, unless the order is explicitly specified via parentheses. Additionally, INTERSECT binds more tightly than EXCEPT and UNION. That means A UNION B INTERSECT C EXCEPT D is the same as A UNION (B INTERSECT C) EXCEPT D.

UNION combines all the rows that are in the result set from the first query with those that are in the result set for the second query. The following is an example of one of the simplest possible UNION clauses. It selects the value 13 and combines this result set with a second query that selects the value 42:

The following query demonstrates the difference between UNION and UNION ALL. It selects the value 13 and combines this result set with a second query that selects the values 42 and 13:

CORRESPONDING matches columns by name instead of by position:

INTERSECT returns only the rows that are in the result sets of both the first and the second queries. The following is an example of one of the simplest possible INTERSECT clauses. It selects the values 13 and 42 and combines this result set with a second query that selects the value 13. Since 42 is only in the result set of the first query, it is not included in the final results.:

CORRESPONDING matches columns by name instead of by position:

EXCEPT returns the rows that are in the result set of the first query, but not the second. The following is an example of one of the simplest possible EXCEPT clauses. It selects the values 13 and 42 and combines this result set with a second query that selects the value 13. Since 13 is also in the result set of the second query, it is not included in the final result.:

CORRESPONDING matches columns by name instead of by position:

The ORDER BY clause is used to sort a result set by one or more output expressions:

Each expression may be composed of output columns, or it may be an ordinal number selecting an output column by position, starting at one. The ORDER BY clause is evaluated after any GROUP BY or HAVING clause, and before any OFFSET, LIMIT or FETCH FIRST clause. The default null ordering is NULLS LAST, regardless of the ordering direction.

Note that, following the SQL specification, an ORDER BY clause only affects the order of rows for queries that immediately contain the clause. Trino follows that specification, and drops redundant usage of the clause to avoid negative performance impacts.

In the following example, the clause only applies to the select statement.

Since tables in SQL are inherently unordered, and the ORDER BY clause in this case does not result in any difference, but negatively impacts performance of running the overall insert statement, Trino skips the sort operation.

Another example where the ORDER BY clause is redundant, and does not affect the outcome of the overall statement, is a nested query:

More background information and details can be found in a blog post about this optimization.

The OFFSET clause is used to discard a number of leading rows from the result set:

If the ORDER BY clause is present, the OFFSET clause is evaluated over a sorted result set, and the set remains sorted after the leading rows are discarded:

Otherwise, it is arbitrary which rows are discarded. If the count specified in the OFFSET clause equals or exceeds the size of the result set, the final result is empty.

The LIMIT or FETCH FIRST clause restricts the number of rows in the result set.

The following example queries a large table, but the LIMIT clause restricts the output to only have five rows (because the query lacks an ORDER BY, exactly which rows are returned is arbitrary):

LIMIT ALL is the same as omitting the LIMIT clause.

The FETCH FIRST clause supports either the FIRST or NEXT keywords and the ROW or ROWS keywords. These keywords are equivalent and the choice of keyword has no effect on query execution.

If the count is not specified in the FETCH FIRST clause, it defaults to 1:

If the OFFSET clause is present, the LIMIT or FETCH FIRST clause is evaluated after the OFFSET clause:

For the FETCH FIRST clause, the argument ONLY or WITH TIES controls which rows are included in the result set.

If the argument ONLY is specified, the result set is limited to the exact number of leading rows determined by the count.

If the argument WITH TIES is specified, it is required that the ORDER BY clause be present. The result set consists of the same set of leading rows and all of the rows in the same peer group as the last of them (‘ties’) as established by the ordering in the ORDER BY clause. The result set is sorted:

There are multiple sample methods:

Each row is selected to be in the table sample with a probability of the sample percentage. When a table is sampled using the Bernoulli method, all physical blocks of the table are scanned and certain rows are skipped (based on a comparison between the sample percentage and a random value calculated at runtime).

The probability of a row being included in the result is independent from any other row. This does not reduce the time required to read the sampled table from disk. It may have an impact on the total query time if the sampled output is processed further.

This sampling method divides the table into logical segments of data and samples the table at this granularity. This sampling method either selects all the rows from a particular segment of data or skips it (based on a comparison between the sample percentage and a random value calculated at runtime).

The rows selected in a system sampling will be dependent on which connector is used. For example, when used with Hive, it is dependent on how the data is laid out on HDFS. This method does not guarantee independent sampling probabilities.

Neither of the two methods allow deterministic bounds on the number of rows returned.

Using sampling with joins:

UNNEST can be used to expand an ARRAY or MAP into a relation. Arrays are expanded into a single column:

Maps are expanded into two columns (key, value):

UNNEST can be used in combination with an ARRAY of ROW structures for expanding each field of the ROW into a corresponding column:

UNNEST can optionally have a WITH ORDINALITY clause, in which case an additional ordinality column is added to the end:

UNNEST returns zero entries when the array/map is empty:

UNNEST returns zero entries when the array/map is null:

UNNEST is normally used with a JOIN, and can reference columns from relations on the left side of the join:

UNNEST can also be used with multiple arguments, in which case they are expanded into multiple columns, with as many rows as the highest cardinality argument (the other columns are padded with nulls):

LEFT JOIN is preferable in order to avoid losing the row containing the array/map field in question when referenced columns from relations on the left side of the join can be empty or have NULL values:

Note that in case of using LEFT JOIN the only condition supported by the current implementation is ON TRUE.

JSON_TABLE transforms JSON data into a relational table format. Like UNNEST and LATERAL, use JSON_TABLE in the FROM clause of a SELECT statement. For more information, see JSON_TABLE.

Joins allow you to combine data from multiple relations.

A cross join returns the Cartesian product (all combinations) of two relations. Cross joins can either be specified using the explit CROSS JOIN syntax or by specifying multiple relations in the FROM clause.

Both of the following queries are equivalent:

The nation table contains 25 rows and the region table contains 5 rows, so a cross join between the two tables produces 125 rows:

Subqueries appearing in the FROM clause can be preceded by the keyword LATERAL. This allows them to reference columns provided by preceding FROM items.

A LATERAL join can appear at the top level in the FROM list, or anywhere within a parenthesized join tree. In the latter case, it can also refer to any items that are on the left-hand side of a JOIN for which it is on the right-hand side.

When a FROM item contains LATERAL cross-references, evaluation proceeds as follows: for each row of the FROM item providing the cross-referenced columns, the LATERAL item is evaluated using that row set’s values of the columns. The resulting rows are joined as usual with the rows they were computed from. This is repeated for set of rows from the column source tables.

LATERAL is primarily useful when the cross-referenced column is necessary for computing the rows to be joined:

When two relations in a join have columns with the same name, the column references must be qualified using the relation alias (if the relation has an alias), or with the relation name:

The following query will fail with the error Column 'name' is ambiguous:

A subquery is an expression which is composed of a query. The subquery is correlated when it refers to columns outside of the subquery. Logically, the subquery will be evaluated for each row in the surrounding query. The referenced columns will thus be constant during any single evaluation of the subquery.

Support for correlated subqueries is limited. Not every standard form is supported.

The EXISTS predicate determines if a subquery returns any rows:

The IN predicate determines if any values produced by the subquery are equal to the provided expression. The result of IN follows the standard rules for nulls. The subquery must produce exactly one column:

A scalar subquery is a non-correlated subquery that returns zero or one row. It is an error for the subquery to produce more than one row. The returned value is NULL if the subquery produces no rows:

Currently only single column can be returned from the scalar subquery.

**Examples:**

Example 1 (unknown):
```unknown
[ WITH SESSION [ name = expression [, ...] ]
[ WITH [ FUNCTION udf ] [, ...] ]
[ WITH [ RECURSIVE ] with_query [, ...] ]
SELECT [ ALL | DISTINCT ] select_expression [, ...]
[ FROM from_item [, ...] ]
[ WHERE condition ]
[ GROUP BY [ ALL | DISTINCT ] grouping_element [, ...] ]
[ HAVING condition]
[ WINDOW window_definition_list]
[ { UNION | INTERSECT | EXCEPT } [ ALL | DISTINCT ] select ]
[ ORDER BY expression [ ASC | DESC ] [, ...] ]
[ OFFSET count [ ROW | ROWS ] ]
[ LIMIT { count | ALL } ]
[ FETCH { FIRST | NEXT } [ count ] { ROW | ROWS } { ONLY | WITH TIES } ]
```

Example 2 (unknown):
```unknown
[ WITH SESSION [ name = expression [, ...] ]
[ WITH [ FUNCTION udf ] [, ...] ]
[ WITH [ RECURSIVE ] with_query [, ...] ]
SELECT [ ALL | DISTINCT ] select_expression [, ...]
[ FROM from_item [, ...] ]
[ WHERE condition ]
[ GROUP BY [ ALL | DISTINCT ] grouping_element [, ...] ]
[ HAVING condition]
[ WINDOW window_definition_list]
[ { UNION | INTERSECT | EXCEPT } [ ALL | DISTINCT ] select ]
[ ORDER BY expression [ ASC | DESC ] [, ...] ]
[ OFFSET count [ ROW | ROWS ] ]
[ LIMIT { count | ALL } ]
[ FETCH { FIRST | NEXT } [ count ] { ROW | ROWS } { ONLY | WITH TIES } ]
```

Example 3 (unknown):
```unknown
table_name [ [ AS ] alias [ ( column_alias [, ...] ) ] ]
```

Example 4 (unknown):
```unknown
table_name [ [ AS ] alias [ ( column_alias [, ...] ) ] ]
```

---

## Row pattern recognition in window structures — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/pattern-recognition-in-window.html

**Contents:**
- Row pattern recognition in window structures#
- Window with row pattern recognition#
- Description of the pattern recognition clauses#
- Processing input with row pattern recognition#
- Empty matches and unmatched rows#

A window structure can be defined in the WINDOW clause or in the OVER clause of a window operation. In both cases, the window specification can include row pattern recognition clauses. They are part of the window frame. The syntax and semantics of row pattern recognition in window are similar to those of the MATCH_RECOGNIZE clause.

This section explains the details of row pattern recognition in window structures, and highlights the similarities and the differences between both pattern recognition mechanisms.

Window specification:

Generally, a window frame specifies the frame_extent, which defines the “sliding window” of rows to be processed by a window function. It can be defined in terms of ROWS, RANGE or GROUPS.

A window frame with row pattern recognition involves many other syntactical components, mandatory or optional, and enforces certain limitations on the frame_extent.

Window frame with row pattern recognition:

The frame_extent with row pattern recognition must be defined in terms of ROWS. The frame start must be at the CURRENT ROW, which limits the allowed frame extent values to the following:

For every input row processed by the window, the portion of rows enclosed by the frame_extent limits the search area for row pattern recognition. Unlike in MATCH_RECOGNIZE, where the pattern search can explore all rows until the partition end, and all rows of the partition are available for computations, in window structures the pattern matching can neither match rows nor retrieve input values outside the frame.

Besides the frame_extent, pattern matching requires the PATTERN and DEFINE clauses.

The PATTERN clause specifies a row pattern, which is a form of a regular expression with some syntactical extensions. The row pattern syntax is similar to the row pattern syntax in MATCH_RECOGNIZE. However, the anchor patterns ^ and $ are not allowed in a window specification.

The DEFINE clause defines the row pattern primary variables in terms of boolean conditions that must be satisfied. It is similar to the DEFINE clause of MATCH_RECOGNIZE. The only difference is that the window syntax does not support the MATCH_NUMBER function.

The MEASURES clause is syntactically similar to the MEASURES clause of MATCH_RECOGNIZE. The only limitation is that the MATCH_NUMBER function is not allowed. However, the semantics of this clause differs between MATCH_RECOGNIZE and window. While in MATCH_RECOGNIZE every measure produces an output column, the measures in window should be considered as definitions associated with the window structure. They can be called over the window, in the same manner as regular window functions:

Measures defined in a window can be referenced in the SELECT clause and in the ORDER BY clause of the enclosing query.

The RUNNING and FINAL keywords are allowed in the MEASURES clause. They can precede a logical navigation function FIRST or LAST, or an aggregate function. However, they have no effect. Every computation is performed from the position of the final row of the match, so the semantics is effectively FINAL.

The AFTER MATCH SKIP clause has the same syntax as the AFTER MATCH SKIP clause of MATCH_RECOGNIZE.

The INITIAL or SEEK modifier is specific to row pattern recognition in window. With INITIAL, which is the default, the pattern match for an input row can only be found starting from that row. With SEEK, if there is no match starting from the current row, the engine tries to find a match starting from subsequent rows within the frame. As a result, it is possible to associate an input row with a match which is detached from that row.

The SUBSET clause is used to define union variables as sets of primary pattern variables. You can use union variables to refer to a set of rows matched to any primary pattern variable from the subset:

The following expression returns the total_price value from the last row matched to either A or B:

If you want to refer to all rows of the match, there is no need to define a SUBSET containing all pattern variables. There is an implicit universal pattern variable applied to any non prefixed column name and any CLASSIFIER call without an argument. The following expression returns the total_price value from the last matched row:

The following call returns the primary pattern variable of the first matched row:

In window, unlike in MATCH_RECOGNIZE, you cannot specify ONE ROW PER MATCH or ALL ROWS PER MATCH. This is because all calls over window, whether they are regular window functions or measures, must comply with the window semantics. A call over window is supposed to produce exactly one output row for every input row. And so, the output mode of pattern recognition in window is a combination of ONE ROW PER MATCH and WITH UNMATCHED ROWS.

Pattern recognition in window processes input rows in two different cases:

upon a row pattern measure call over the window:

upon a window function call over the window:

The output row produced for each input row, consists of:

all values from the input row

the value of the called measure or window function, computed with respect to the pattern match associated with the row

Processing the input can be described as the following sequence of steps:

Partition the input data accordingly to PARTITION BY

Order each partition by the ORDER BY expressions

For a measure, produce a one-row output as for an unmatched row

For a window function, evaluate the function over an empty frame and produce a one-row output

Determine the frame extent

Try match the row pattern starting from the current row within the frame extent

If no match is found, and SEEK is specified, try to find a match starting from subsequent rows within the frame extent

For a measure, produce a one-row output for an unmatched row

For a window function, evaluate the function over an empty frame and produce a one-row output

For a measure, produce a one-row output for the match

For a window function, evaluate the function over a frame limited to the matched rows sequence and produce a one-row output

Evaluate the AFTER MATCH SKIP clause, and mark the ‘skipped’ rows

If no match can be associated with a particular input row, the row is unmatched. This happens when no match can be found for the row. This also happens when no match is attempted for the row, because it is skipped by the AFTER MATCH SKIP clause of some preceding row. For an unmatched row, every row pattern measure is null. Every window function is evaluated over an empty frame.

An empty match is a successful match which does not involve any pattern variables. In other words, an empty match does not contain any rows. If an empty match is associated with an input row, every row pattern measure for that row is evaluated over an empty sequence of rows. All navigation operations and the CLASSIFIER function return null. Every window function is evaluated over an empty frame.

In most cases, the results for empty matches and unmatched rows are the same. A constant measure can be helpful to distinguish between them:

The following call returns 'matched' for every matched row, including empty matches, and null for every unmatched row:

**Examples:**

Example 1 (unknown):
```unknown
(
[ existing_window_name ]
[ PARTITION BY column [, ...] ]
[ ORDER BY column [, ...] ]
[ window_frame ]
)
```

Example 2 (unknown):
```unknown
(
[ existing_window_name ]
[ PARTITION BY column [, ...] ]
[ ORDER BY column [, ...] ]
[ window_frame ]
)
```

Example 3 (unknown):
```unknown
[ MEASURES measure_definition [, ...] ]
frame_extent
[ AFTER MATCH skip_to ]
[ INITIAL | SEEK ]
[ PATTERN ( row_pattern ) ]
[ SUBSET subset_definition [, ...] ]
[ DEFINE variable_definition [, ...] ]
```

Example 4 (unknown):
```unknown
[ MEASURES measure_definition [, ...] ]
frame_extent
[ AFTER MATCH skip_to ]
[ INITIAL | SEEK ]
[ PATTERN ( row_pattern ) ]
[ SUBSET subset_definition [, ...] ]
[ DEFINE variable_definition [, ...] ]
```

---

## ALTER BRANCH — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/alter-branch.html

**Contents:**
- ALTER BRANCH#
- Synopsis#
- Description#
- Examples#
- See also#

Fast-forward the current snapshot of one branch to the latest snapshot of another.

Fast-forward the main branch to the head of audit branch in the orders table:

**Examples:**

Example 1 (unknown):
```unknown
ALTER BRANCH source_branch IN TABLE table_name FAST FORWARD TO target_branch
```

Example 2 (unknown):
```unknown
ALTER BRANCH source_branch IN TABLE table_name FAST FORWARD TO target_branch
```

Example 3 (unknown):
```unknown
ALTER BRANCH main IN TABLE orders FAST FORWARD TO audit
```

Example 4 (unknown):
```unknown
ALTER BRANCH main IN TABLE orders FAST FORWARD TO audit
```

---

## SHOW BRANCHES — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/show-branches.html

**Contents:**
- SHOW BRANCHES#
- Synopsis#
- Description#
- Examples#

List the available branches.

List the branches in the table orders:

**Examples:**

Example 1 (unknown):
```unknown
SHOW BRANCHES ( FROM | IN ) TABLE table_name
```

Example 2 (unknown):
```unknown
SHOW BRANCHES ( FROM | IN ) TABLE table_name
```

Example 3 (unknown):
```unknown
SHOW BRANCHES IN TABLE orders
```

Example 4 (unknown):
```unknown
SHOW BRANCHES IN TABLE orders
```

---

## CREATE SCHEMA — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/create-schema.html

**Contents:**
- CREATE SCHEMA#
- Synopsis#
- Description#
- Examples#
- See also#

Create a new, empty schema. A schema is a container that holds tables, views and other database objects.

The optional IF NOT EXISTS clause causes the error to be suppressed if the schema already exists.

The optional AUTHORIZATION clause can be used to set the owner of the newly created schema to a user or role.

The optional WITH clause can be used to set properties on the newly created schema. To list all available schema properties, run the following query:

Create a new schema web in the current catalog:

Create a new schema sales in the hive catalog:

Create the schema traffic if it does not already exist:

Create a new schema web and set the owner to user alice:

Create a new schema web, set the LOCATION property to /hive/data/web and set the owner to user alice:

Create a new schema web and allow everyone to drop schema and create tables in schema web:

Create a new schema web, set the LOCATION property to /hive/data/web and allow everyone to drop schema and create tables in schema web:

ALTER SCHEMA, DROP SCHEMA

**Examples:**

Example 1 (unknown):
```unknown
CREATE SCHEMA [ IF NOT EXISTS ] schema_name
[ AUTHORIZATION ( user | USER user | ROLE role ) ]
[ WITH ( property_name = expression [, ...] ) ]
```

Example 2 (unknown):
```unknown
CREATE SCHEMA [ IF NOT EXISTS ] schema_name
[ AUTHORIZATION ( user | USER user | ROLE role ) ]
[ WITH ( property_name = expression [, ...] ) ]
```

Example 3 (unknown):
```unknown
SELECT * FROM system.metadata.schema_properties
```

Example 4 (unknown):
```unknown
SELECT * FROM system.metadata.schema_properties
```

---

## SHOW CREATE MATERIALIZED VIEW — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/show-create-materialized-view.html

**Contents:**
- SHOW CREATE MATERIALIZED VIEW#
- Synopsis#
- Description#
- See also#

Show the SQL statement that creates the specified materialized view view_name.

CREATE MATERIALIZED VIEW

DROP MATERIALIZED VIEW

REFRESH MATERIALIZED VIEW

**Examples:**

Example 1 (unknown):
```unknown
SHOW CREATE MATERIALIZED VIEW view_name
```

Example 2 (unknown):
```unknown
SHOW CREATE MATERIALIZED VIEW view_name
```

---

## RESET SESSION — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/reset-session.html

**Contents:**
- RESET SESSION#
- Synopsis#
- Description#
- Examples#
- See also#

Reset a session property value to the default value.

SET SESSION, SHOW SESSION

**Examples:**

Example 1 (unknown):
```unknown
RESET SESSION name
RESET SESSION catalog.name
```

Example 2 (unknown):
```unknown
RESET SESSION name
RESET SESSION catalog.name
```

Example 3 (unknown):
```unknown
RESET SESSION query_max_run_time;
RESET SESSION hive.optimized_reader_enabled;
```

Example 4 (unknown):
```unknown
RESET SESSION query_max_run_time;
RESET SESSION hive.optimized_reader_enabled;
```

---

## EXPLAIN ANALYZE — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/explain-analyze.html

**Contents:**
- EXPLAIN ANALYZE#
- Synopsis#
- Description#
- Examples#
- See also#

Execute the statement and show the distributed execution plan of the statement along with the cost of each operation.

The VERBOSE option will give more detailed information and low-level statistics; understanding these may require knowledge of Trino internals and implementation details.

The stats may not be entirely accurate, especially for queries that complete quickly.

In the example below, you can see the CPU time spent in each stage, as well as the relative cost of each plan node in the stage. Note that the relative cost of the plan nodes is based on wall time, which may or may not be correlated to CPU time. For each plan node you can see some additional statistics (e.g: average input per node instance). Such statistics are useful when one wants to detect data anomalies for a query (e.g: skewness).

When the VERBOSE option is used, some operators may report additional information. For example, the window function operator will output the following:

**Examples:**

Example 1 (unknown):
```unknown
EXPLAIN ANALYZE [VERBOSE] statement
```

Example 2 (unknown):
```unknown
EXPLAIN ANALYZE [VERBOSE] statement
```

Example 3 (unknown):
```unknown
EXPLAIN ANALYZE SELECT count(*), clerk FROM orders
WHERE orderdate > date '1995-01-01' GROUP BY clerk;
```

Example 4 (unknown):
```unknown
EXPLAIN ANALYZE SELECT count(*), clerk FROM orders
WHERE orderdate > date '1995-01-01' GROUP BY clerk;
```

---

## DROP SCHEMA — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/drop-schema.html

**Contents:**
- DROP SCHEMA#
- Synopsis#
- Description#
- Examples#
- See also#

Drop an existing schema. The schema must be empty.

The optional IF EXISTS clause causes the error to be suppressed if the schema does not exist.

Drop the schema sales if it exists:

Drop the schema archive, along with everything it contains:

Drop the schema archive, only if there are no objects contained in the schema:

ALTER SCHEMA, CREATE SCHEMA

**Examples:**

Example 1 (unknown):
```unknown
DROP SCHEMA [ IF EXISTS ] schema_name [ CASCADE | RESTRICT ]
```

Example 2 (unknown):
```unknown
DROP SCHEMA [ IF EXISTS ] schema_name [ CASCADE | RESTRICT ]
```

Example 3 (unknown):
```unknown
DROP SCHEMA web
```

Example 4 (unknown):
```unknown
DROP SCHEMA web
```

---

## CREATE TABLE — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/create-table.html

**Contents:**
- CREATE TABLE#
- Synopsis#
- Description#
- Examples#
- See also#

Create a new, empty table with the specified columns. Use CREATE TABLE AS to create a table with data.

The optional OR REPLACE clause causes an existing table with the specified name to be replaced with the new table definition. Support for table replacement varies across connectors. Refer to the connector documentation for details.

The optional IF NOT EXISTS clause causes the error to be suppressed if the table already exists.

OR REPLACE and IF NOT EXISTS cannot be used together.

The optional WITH clause can be used to set properties on the newly created table or on single columns. To list all available table properties, run the following query:

To list all available column properties, run the following query:

The LIKE clause can be used to include all the column definitions from an existing table in the new table. Multiple LIKE clauses may be specified, which allows copying the columns from multiple tables.

If INCLUDING PROPERTIES is specified, all the table properties are copied to the new table. If the WITH clause specifies the same property name as one of the copied properties, the value from the WITH clause will be used. The default behavior is EXCLUDING PROPERTIES. The INCLUDING PROPERTIES option maybe specified for at most one table.

Create a new table orders:

Create the table orders if it does not already exist, adding a table comment and a column comment:

Create the table bigger_orders using the columns from orders plus additional columns at the start and end:

ALTER TABLE, DROP TABLE, CREATE TABLE AS, SHOW CREATE TABLE

**Examples:**

Example 1 (unknown):
```unknown
CREATE [ OR REPLACE ] TABLE [ IF NOT EXISTS ]
table_name (
  { column_name data_type [ DEFAULT default ] [ NOT NULL ]
      [ COMMENT comment ]
      [ WITH ( property_name = expression [, ...] ) ]
  | LIKE existing_table_name
      [ { INCLUDING | EXCLUDING } PROPERTIES ]
  }
  [, ...]
)
[ COMMENT table_comment ]
[ WITH ( property_name = expression [, ...] ) ]
```

Example 2 (unknown):
```unknown
CREATE [ OR REPLACE ] TABLE [ IF NOT EXISTS ]
table_name (
  { column_name data_type [ DEFAULT default ] [ NOT NULL ]
      [ COMMENT comment ]
      [ WITH ( property_name = expression [, ...] ) ]
  | LIKE existing_table_name
      [ { INCLUDING | EXCLUDING } PROPERTIES ]
  }
  [, ...]
)
[ COMMENT table_comment ]
[ WITH ( property_name = expression [, ...] ) ]
```

Example 3 (unknown):
```unknown
SELECT * FROM system.metadata.table_properties
```

Example 4 (unknown):
```unknown
SELECT * FROM system.metadata.table_properties
```

---

## INSERT — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql/insert.html

**Contents:**
- INSERT#
- Synopsis#
- Description#
- Examples#
- See also#

Insert new rows into a table.

If the list of column names is specified, they must exactly match the list of columns produced by the query. Each column in the table not present in the column list will be filled with a null value. Otherwise, if the list of columns is not specified, the columns produced by the query must exactly match the columns in the table being inserted into.

Load additional rows into the orders table from the new_orders table:

Insert a single row into the cities table:

Insert multiple rows into the cities table:

Insert a single row into the nation table with the specified column list:

Insert a row without specifying the comment column. That column will be null:

Insert a single row into audit branch of the cities table:

**Examples:**

Example 1 (unknown):
```unknown
INSERT INTO table_name [ @ branch_name ] [ ( column [, ... ] ) ] query
```

Example 2 (unknown):
```unknown
INSERT INTO table_name [ @ branch_name ] [ ( column [, ... ] ) ] query
```

Example 3 (unknown):
```unknown
INSERT INTO orders
SELECT * FROM new_orders;
```

Example 4 (unknown):
```unknown
INSERT INTO orders
SELECT * FROM new_orders;
```

---

## SQL user-defined functions — Trino 478 Documentation

**URL:** https://trino.io/docs/current/udf/sql.html

**Contents:**
- SQL user-defined functions#
- SQL UDF declaration#
- Labels#
- Limitations#

A SQL user-defined function, also known as SQL routine, is a user-defined function that uses the SQL routine language and statements for the definition of the function.

Declare a SQL UDF using the FUNCTION keyword and the following statements can be used in addition to built-in functions and operators and other UDFs:

A minimal example declares the UDF doubleup that returns the input integer value x multiplied by two. The example shows declaration as Inline user-defined functions and invocation with the value 21 to yield the result 42:

The same UDF can also be declared as Catalog user-defined functions.

Find simple examples in each statement documentation, and refer to the Example SQL UDFs for more complex use cases that combine multiple statements.

SQL UDFs can contain labels as markers for a specific block in the declaration before the following keywords:

The label is used to name the block to continue processing with the ITERATE statement or exit the block with the LEAVE statement. This flow control is supported for nested blocks, allowing to continue or exit an outer block, not just the innermost block. For example, the following snippet uses the label top to name the complete block from REPEAT to END REPEAT:

Labels can be used with the ITERATE and LEAVE statements to continue processing the block or leave the block. This flow control is also supported for nested blocks and labels.

The following limitations apply to SQL UDFs.

UDFs must be declared before they are referenced.

Recursion cannot be declared or processed.

Mutual recursion can not be declared or processed.

Queries cannot be processed in a UDF.

Specifically this means that UDFs can not use SELECT queries to retrieve data or any other queries to process data within the UDF. Instead queries can use UDFs to process data. UDFs only work on data provided as input values and only provide output data from the RETURN statement.

**Examples:**

Example 1 (unknown):
```unknown
WITH
  FUNCTION doubleup(x integer)
    RETURNS integer
    RETURN x * 2
SELECT doubleup(21);
-- 42
```

Example 2 (unknown):
```unknown
WITH
  FUNCTION doubleup(x integer)
    RETURNS integer
    RETURN x * 2
SELECT doubleup(21);
-- 42
```

Example 3 (unknown):
```unknown
top: REPEAT
  SET a = a + 1;
  IF a <= 3 THEN
    ITERATE top;
  END IF;
  SET b = b + 1;
  UNTIL a >= 10
END REPEAT;
```

Example 4 (unknown):
```unknown
top: REPEAT
  SET a = a + 1;
  IF a <= 3 THEN
    ITERATE top;
  END IF;
  SET b = b + 1;
  UNTIL a >= 10
END REPEAT;
```

---

## SQL statement syntax — Trino 478 Documentation

**URL:** https://trino.io/docs/current/sql.html

**Contents:**
- SQL statement syntax#

This section describes the syntax for SQL statements that can be executed in Trino.

Refer to the following sections for further details:

SQL data types and other general aspects

SQL functions and operators

---

## LOOP — Trino 478 Documentation

**URL:** https://trino.io/docs/current/udf/sql/loop.html

**Contents:**
- LOOP#
- Synopsis#
- Description#
- Examples#
- See also#

The LOOP statement is an optional construct in SQL user-defined functions to allow processing of a block of statements repeatedly.

The block of statements is processed until an explicit use of LEAVE causes processing to exit the loop. If processing reaches END LOOP, another iteration of processing from the beginning starts. LEAVE statements are typically wrapped in an IF statement that declares a condition to stop the loop.

The optional label before the LOOP keyword can be used to name the block.

The following function counts up to 100 with a step size step in a loop starting from the start value start_value, and returns the number of incremental steps in the loop to get to a value of 100 or higher:

Further examples of varying complexity that cover usage of the LOOP statement in combination with other statements are available in the SQL UDF examples documentation.

SQL user-defined functions

**Examples:**

Example 1 (unknown):
```unknown
[label :] LOOP
    statements
END LOOP
```

Example 2 (unknown):
```unknown
[label :] LOOP
    statements
END LOOP
```

Example 3 (unknown):
```unknown
FUNCTION to_one_hundred(start_value int, step int)
  RETURNS int
  BEGIN
    DECLARE count int DEFAULT 0;
    DECLARE current int DEFAULT 0;
    SET current = start_value;
    abc: LOOP
      IF current >= 100 THEN
        LEAVE abc;
      END IF;
      SET count = count + 1;
      SET current = current + step;
    END LOOP;
    RETURN count;
  END
```

Example 4 (unknown):
```unknown
FUNCTION to_one_hundred(start_value int, step int)
  RETURNS int
  BEGIN
    DECLARE count int DEFAULT 0;
    DECLARE current int DEFAULT 0;
    SET current = start_value;
    abc: LOOP
      IF current >= 100 THEN
        LEAVE abc;
      END IF;
      SET count = count + 1;
      SET current = current + step;
    END LOOP;
    RETURN count;
  END
```

---
