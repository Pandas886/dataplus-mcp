# Trino - Functions

**Pages:** 31

---

## Aggregate functions — Trino 478 Documentation

**URL:** https://trino.io/docs/current/functions/aggregate.html

**Contents:**
- Aggregate functions#
- Ordering during aggregation#
- Filtering during aggregation#
- General aggregate functions#
- Bitwise aggregate functions#
- Map aggregate functions#
- Approximate aggregate functions#
- Statistical aggregate functions#
- Lambda aggregate functions#

Aggregate functions operate on a set of values to compute a single result.

Except for count(), count_if(), max_by(), min_by() and approx_distinct(), all of these aggregate functions ignore null values and return null for no input rows or when all values are null. For example, sum() returns null rather than zero and avg() does not include null values in the count. The coalesce function can be used to convert null into zero.

Some aggregate functions such as array_agg() produce different results depending on the order of input values. This ordering can be specified by writing an ORDER BY clause within the aggregate function:

The FILTER keyword can be used to remove rows from aggregation processing with a condition expressed using a WHERE clause. This is evaluated for each row before it is used in the aggregation and is supported for all aggregate functions.

A common and very useful example is to use FILTER to remove nulls from consideration when using array_agg:

As another example, imagine you want to add a condition on the count for Iris flowers, modifying the following query:

If you just use a normal WHERE statement you lose information:

Using a filter you retain all information:

Returns an arbitrary non-null value x, if one exists. x can be any valid expression. This allows you to return values from columns that are not directly part of the aggregation, including expressions using these columns, in a query.

For example, the following query returns the customer name from the name column, and returns the sum of all total prices as customer spend. The aggregation however uses the rows grouped by the customer identifier custkey a required, since only that column is guaranteed to be unique:

Returns an arbitrary non-null value of x, if one exists. Identical to any_value().

Returns an array created from the input x elements.

Returns the average (arithmetic mean) of all input values.

Returns the average interval length of all input values.

Returns TRUE if every input value is TRUE, otherwise FALSE.

Returns TRUE if any input value is TRUE, otherwise FALSE.

Returns an order-insensitive checksum of the given values.

Returns the number of input rows.

Returns the number of non-null input values.

Returns the number of TRUE input values. This function is equivalent to count(CASE WHEN x THEN 1 END).

This is an alias for bool_and().

Returns the geometric mean of all input values.

Returns the concatenated input values, separated by the separator string.

The expression value must evaluate to a string data type (varchar). You must explicitly cast non-string datatypes to varchar using CAST(expression AS VARCHAR) before you use them with listagg.

If separator is not specified, the empty string will be used as separator.

In its simplest form the function looks like:

The following example casts the v column to varchar:

The overflow behaviour is by default to throw an error in case that the length of the output of the function exceeds 1048576 bytes:

There exists also the possibility to truncate the output WITH COUNT or WITHOUT COUNT of omitted non-null values in case that the length of the output of the function exceeds 1048576 bytes:

If not specified, the truncation filler string is by default '...'.

This aggregation function can be also used in a scenario involving grouping:

This aggregation function supports filtering during aggregation for scenarios where the aggregation for the data not matching the filter condition still needs to show up in the output:

The current implementation of listagg function does not support window frames.

Returns the maximum value of all input values.

Returns n largest values of all input values of x.

Returns the value of x associated with the maximum value of y over all input values.

Returns n values of x associated with the n largest of all input values of y in descending order of y.

Returns the minimum value of all input values.

Returns n smallest values of all input values of x.

Returns the value of x associated with the minimum value of y over all input values.

Returns n values of x associated with the n smallest of all input values of y in ascending order of y.

Returns the sum of all input values.

Returns the bitwise AND of all input non-NULL values in 2’s complement representation. If all records inside the group are NULL, or if the group is empty, the function returns NULL.

Returns the bitwise OR of all input non-NULL values in 2’s complement representation. If all records inside the group are NULL, or if the group is empty, the function returns NULL.

Returns the bitwise XOR of all input non-NULL values in 2’s complement representation. If all records inside the group are NULL, or if the group is empty, the function returns NULL.

Returns a map containing the count of the number of times each input value occurs.

Returns a map created from the input key / value pairs.

Returns the union of all the input maps. If a key is found in multiple input maps, that key’s value in the resulting map comes from an arbitrary input map.

For example, take the following histogram function that creates multiple maps from the Iris dataset:

You can combine these maps using map_union:

Returns a multimap created from the input key / value pairs. Each key can be associated with multiple values.

Returns the approximate number of distinct input values. This function provides an approximation of count(DISTINCT x). Zero is returned if all input values are null.

This function should produce a standard error of 2.3%, which is the standard deviation of the (approximately normal) error distribution over all possible sets. It does not guarantee an upper bound on the error for any specific input set.

Returns the approximate number of distinct input values. This function provides an approximation of count(DISTINCT x). Zero is returned if all input values are null.

This function should produce a standard error of no more than e, which is the standard deviation of the (approximately normal) error distribution over all possible sets. It does not guarantee an upper bound on the error for any specific input set. The current implementation of this function requires that e be in the range of [0.0040625, 0.26000].

Computes the top frequent values up to buckets elements approximately. Approximate estimation of the function enables us to pick up the frequent values with less memory. Larger capacity improves the accuracy of underlying algorithm with sacrificing the memory capacity. The returned value is a map containing the top elements with corresponding estimated frequency.

The error of the function depends on the permutation of the values and its cardinality. We can set the capacity same as the cardinality of the underlying data to achieve the least error.

buckets and capacity must be bigint. value can be numeric or string type.

The function uses the stream summary data structure proposed in the paper Efficient Computation of Frequent and Top-k Elements in Data Streams by A. Metwalley, D. Agrawl and A. Abbadi.

Returns the approximate percentile for all input values of x at the given percentage. The value of percentage must be between zero and one and must be constant for all input rows.

Returns the approximate percentile for all input values of x at each of the specified percentages. Each element of the percentages array must be between zero and one, and the array must be constant for all input rows.

Returns the approximate weighed percentile for all input values of x using the per-item weight w at the percentage percentage. Weights must be greater or equal to 1. Integer-value weights can be thought of as a replication count for the value x in the percentile set. The value of percentage must be between zero and one and must be constant for all input rows.

Returns the approximate weighed percentile for all input values of x using the per-item weight w at each of the given percentages specified in the array. Weights must be greater or equal to 1. Integer-value weights can be thought of as a replication count for the value x in the percentile set. Each element of the percentages array must be between zero and one, and the array must be constant for all input rows.

See HyperLogLog functions.

See HyperLogLog functions.

See Quantile digest functions.

See T-Digest functions.

Computes an approximate histogram with up to buckets number of buckets for all values. This function is equivalent to the variant of numeric_histogram() that takes a weight, with a per-item weight of 1.

Computes an approximate histogram with up to buckets number of buckets for all values with a per-item weight of weight. The algorithm is based loosely on:

buckets must be a bigint. value and weight must be numeric.

See Quantile digest functions.

See Quantile digest functions.

See Quantile digest functions.

See T-Digest functions.

See T-Digest functions.

Returns correlation coefficient of input values.

Returns the population covariance of input values.

Returns the sample covariance of input values.

Returns the excess kurtosis of all input values. Unbiased estimate using the following expression:

Returns linear regression intercept of input values. y is the dependent value. x is the independent value.

Returns linear regression slope of input values. y is the dependent value. x is the independent value.

Returns the Fisher’s moment coefficient of skewness of all input values.

This is an alias for stddev_samp().

Returns the population standard deviation of all input values.

Returns the sample standard deviation of all input values.

This is an alias for var_samp().

Returns the population variance of all input values.

Returns the sample variance of all input values.

Reduces all input values into a single value. inputFunction will be invoked for each non-null input value. In addition to taking the input value, inputFunction takes the current state, initially initialState, and returns the new state. combineFunction will be invoked to combine two states into a new state. The final state is returned:

The state type must be a boolean, integer, floating-point, char, varchar or date/time/interval.

**Examples:**

Example 1 (unknown):
```unknown
array_agg(x ORDER BY y DESC)
array_agg(x ORDER BY x, y, z)
```

Example 2 (unknown):
```unknown
array_agg(x ORDER BY y DESC)
array_agg(x ORDER BY x, y, z)
```

Example 3 (unknown):
```unknown
aggregate_function(...) FILTER (WHERE <condition>)
```

Example 4 (unknown):
```unknown
aggregate_function(...) FILTER (WHERE <condition>)
```

---

## List of functions and operators — Trino 478 Documentation

**URL:** https://trino.io/docs/current/functions/list.html

**Contents:**
- List of functions and operators#
- ##
- A#
- B#
- C#
- D#
- E#
- F#
- G#
- H#

[] substring operator

|| concatenation operator

< comparison operator

> comparison operator

<= comparison operator

>= comparison operator

= comparison operator

<> comparison operator

!= comparison operator

+ mathematical operator

- mathematical operator

* mathematical operator

/ mathematical operator

% mathematical operator

approx_most_frequent()

bing_tile_coordinates()

bing_tile_zoom_level()

bitwise_right_shift()

bitwise_right_shift_arithmetic()

evaluate_classifier_predictions

from_encoded_polyline()

from_geojson_geometry

from_iso8601_timestamp()

from_iso8601_timestamp_nanos()

from_unixtime_nanos()

geometry_from_hadoop_shape()

geometry_invalid_reason()

geometry_nearest_points()

geometry_to_bing_tiles()

great_circle_distance()

human_readable_seconds()

intersection_cardinality()

json_array_contains()

json_extract_scalar()

learn_libsvm_classifier()

learn_libsvm_regressor()

levenshtein_distance()

line_interpolate_point()

line_interpolate_points()

multimap_from_entries()

random_string(), catalog function of the Faker connector

sequence() (scalar function)

sequence() (table function)

ST_GeometryFromText()

to_encoded_polyline()

to_spherical_geography()

url_extract_fragment()

url_extract_parameter()

url_extract_protocol()

values_at_quantiles()

wilson_interval_lower()

wilson_interval_upper()

---

## Window functions — Trino 478 Documentation

**URL:** https://trino.io/docs/current/functions/window.html

**Contents:**
- Window functions#
- Aggregate functions#
- Ranking functions#
- Value functions#

Window functions perform calculations across rows of the query result. They run after the HAVING clause but before the ORDER BY clause. Invoking a window function requires special syntax using the OVER clause to specify the window. For example, the following query ranks orders for each clerk by price:

The window can be specified in two ways (see WINDOW clause):

By a reference to a named window specification defined in the WINDOW clause,

By an in-line window specification which allows to define window components as well as refer to the window components pre-defined in the WINDOW clause.

All Aggregate functions can be used as window functions by adding the OVER clause. The aggregate function is computed for each row over the rows within the current row’s window frame. Note that ordering during aggregation is not supported.

For example, the following query produces a rolling sum of order prices by day for each clerk:

Returns the cumulative distribution of a value in a group of values. The result is the number of rows preceding or peer with the row in the window ordering of the window partition divided by the total number of rows in the window partition. Thus, any tie values in the ordering will evaluate to the same distribution value. The window frame must not be specified.

Returns the rank of a value in a group of values. This is similar to rank(), except that tie values do not produce gaps in the sequence. The window frame must not be specified.

Divides the rows for each window partition into n buckets ranging from 1 to at most n. Bucket values will differ by at most 1. If the number of rows in the partition does not divide evenly into the number of buckets, then the remainder values are distributed one per bucket, starting with the first bucket.

For example, with 6 rows and 4 buckets, the bucket values would be as follows: 1 1 2 2 3 4

For the ntile() function, the window frame must not be specified.

Returns the percentage ranking of a value in group of values. The result is (r - 1) / (n - 1) where r is the rank() of the row and n is the total number of rows in the window partition. The window frame must not be specified.

Returns the rank of a value in a group of values. The rank is one plus the number of rows preceding the row that are not peer with the row. Thus, tie values in the ordering will produce gaps in the sequence. The ranking is performed for each window partition. The window frame must not be specified.

Returns a unique, sequential number for each row, starting with one, according to the ordering of rows within the window partition. The window frame must not be specified.

By default, null values are respected. If IGNORE NULLS is specified, all rows where x is null are excluded from the calculation. If IGNORE NULLS is specified and x is null for all rows, the default_value is returned, or if it is not specified, null is returned.

Returns the first value of the window.

Returns the last value of the window.

Returns the value at the specified offset from the beginning of the window. Offsets start at 1. The offset can be any scalar expression. If the offset is null or greater than the number of values in the window, null is returned. It is an error for the offset to be zero or negative.

Returns the value at offset rows after the current row in the window partition. Offsets start at 0, which is the current row. The offset can be any scalar expression. The default offset is 1. If the offset is null, an error is raised. If the offset refers to a row that is not within the partition, the default_value is returned, or if it is not specified null is returned. The lead() function requires that the window ordering be specified. Window frame must not be specified.

Returns the value at offset rows before the current row in the window partition. Offsets start at 0, which is the current row. The offset can be any scalar expression. The default offset is 1. If the offset is null, an error is raised. If the offset refers to a row that is not within the partition, the default_value is returned, or if it is not specified null is returned. The lag() function requires that the window ordering be specified. Window frame must not be specified.

**Examples:**

Example 1 (unknown):
```unknown
SELECT orderkey, clerk, totalprice,
       rank() OVER (PARTITION BY clerk
                    ORDER BY totalprice DESC) AS rnk
FROM orders
ORDER BY clerk, rnk
```

Example 2 (unknown):
```unknown
SELECT orderkey, clerk, totalprice,
       rank() OVER (PARTITION BY clerk
                    ORDER BY totalprice DESC) AS rnk
FROM orders
ORDER BY clerk, rnk
```

Example 3 (unknown):
```unknown
SELECT clerk, orderdate, orderkey, totalprice,
       sum(totalprice) OVER (PARTITION BY clerk
                             ORDER BY orderdate) AS rolling_sum
FROM orders
ORDER BY clerk, orderdate, orderkey
```

Example 4 (unknown):
```unknown
SELECT clerk, orderdate, orderkey, totalprice,
       sum(totalprice) OVER (PARTITION BY clerk
                             ORDER BY orderdate) AS rolling_sum
FROM orders
ORDER BY clerk, orderdate, orderkey
```

---

## AI functions — Trino 478 Documentation

**URL:** https://trino.io/docs/current/functions/ai.html

**Contents:**
- AI functions#
- Configuration#
  - Providers#
    - Anthropic#
    - OpenAI#
    - Ollama#
  - Model configuration#
- Functions#

The AI functions allow you to invoke a large language model (LLM) to perform various textual tasks. Multiple LLM providers are supported, specifically OpenAI and Anthropic directly, and many others such as Llama, DeepSeek, Phi, Mistral, or Gemma using Ollama.

The LLM must be provided outside Trino as an external service.

Because the AI functions require an external LLM service, they are not available by default. To enable them, you must configure a catalog properties file to register the functions invoking the configured LLM with the specified catalog name.

Create a catalog properties file etc/catalog/llm.properties that references the ai connector:

The AI functions are available with the ai schema name. For the preceding example, the functions use the llm.ai catalog and schema prefix.

To avoid needing to reference the functions with their fully qualified name, configure the sql.path SQL environment property in the config.properties file to include the catalog and schema prefix:

Configure multiple catalogs to use the same functions with different LLM providers. In this case, the functions must be referenced using their fully qualified name, rather than relying on the SQL path.

The AI functions invoke an external LLM. Access to the LLM API must be configured in the catalog. Performance, results, and cost of all AI function invocations are dependent on the LLM provider and the model used. You must specify a model that is suitable for textual analysis.

Required name of the provider. Must be anthropic for using the Anthropic provider or openai for OpenAI or Ollama.

ai.anthropic.endpoint

URL for the Anthropic API endpoint. Defaults to https://api.anthropic.com.

API key value for Anthropic API access. Required with ai.provider set to anthropic.

URL for the OpenAI API or Ollama endpoint. Defaults to https://api.openai.com. Set to the URL endpoint for Ollama when using models via Ollama and add any string for the ai.openai.api-key.

API key value for OpenAI API access. Required with ai.provider set to openai. Required and ignored with Ollama use.

The AI functions connect to the providers over HTTP. Configure the connection using the ai prefix with the HTTP client properties.

The following sections show minimal configurations for Anthropic, OpenAI, and Ollama use.

The Anthropic provider uses the Anthropic API to perform the AI functions:

Use secrets to avoid actual API key values in the catalog properties files.

The OpenAI provider uses the OpenAI API to perform the AI functions:

Use secrets to avoid actual API key values in the catalog properties files.

The OpenAI provider can be used with Ollama to perform the AI functions, as Ollama is compatible with the OpenAI API:

An API key must be specified, but is ignored by Ollama.

Ollama allows you to use Llama, DeepSeek, Phi, Mistral, Gemma and other models on a self-hosted deployment or from a vendor.

All providers support a number of different models. You must configure at least one model to use for the AI function. The model must be suitable for textual analysis. Provider and model choice impacts performance, results, and cost of all AI functions.

Costs vary with AI function used based on the implementation prompt size, the length of the input, and the length of the output from the model, because model providers charge based input and output tokens.

Optionally configure different models from the same provider for each functions as an override:

Required name of the model. Valid names vary by provider. Model must be suitable for textual analysis. The model is used for all functions, unless a specific model is configured for a function as override.

ai.analyze-sentiment.model

Optional override to use a different model for ai_analyze_sentiment().

Optional override to use a different model for ai_classify().

Optional override to use a different model for ai_extract().

Optional override to use a different model for ai_fix_grammar().

Optional override to use a different model for ai_gen().

Optional override to use a different model for ai_mask().

Optional override to use a different model for ai_translate().

The following functions are available in each catalog configured with the ai connector under the ai schema and use the configured LLM provider:

Analyzes the sentiment of the input text.

The sentiment result is positive, negative, neutral, or mixed.

Classifies the input text according to the provided labels.

Extracts values for the provided labels from the input text.

Corrects grammatical errors in the input text.

Generates text based on the input prompt.

Masks the values for the provided labels in the input text by replacing them with the text [MASKED].

Translates the input text to the specified language.

**Examples:**

Example 1 (unknown):
```unknown
connector.name=ai
```

Example 2 (unknown):
```unknown
connector.name=ai
```

Example 3 (unknown):
```unknown
sql.path=llm.ai
```

Example 4 (unknown):
```unknown
sql.path=llm.ai
```

---

## Set Digest functions — Trino 478 Documentation

**URL:** https://trino.io/docs/current/functions/setdigest.html

**Contents:**
- Set Digest functions#
- Data structures#
- Serialization#
- Functions#

Trino offers several functions that deal with the MinHash technique.

MinHash is used to quickly estimate the Jaccard similarity coefficient between two sets.

It is commonly used in data mining to detect near-duplicate web pages at scale. By using this information, the search engines efficiently avoid showing within the search results two pages that are nearly identical.

The following example showcases how the Set Digest functions can be used to naively estimate the similarity between texts. The input texts are split by using the function ngrams() to 4-shingles which are used as input for creating a set digest of each initial text. The set digests are compared to each other to get an approximation of the similarity of their corresponding initial texts:

The above result listing points out, as expected, that the texts with the id 1 and 3 are quite similar.

One may argue that the text with the id 2 is somewhat similar to the texts with the id 1 and 3. Due to the fact in the example above 4-shingles are taken into account for measuring the similarity of the texts, there are no intersections found for the text pairs 1 and 2, respectively 3 and 2 and therefore there the similarity index for these text pairs is 0.

Trino implements Set Digest data sketches by encapsulating the following components:

MinHash with a single hash function

The HyperLogLog structure is used for the approximation of the distinct elements in the original set.

The MinHash structure is used to store a low memory footprint signature of the original set. The similarity of any two sets is estimated by comparing their signatures.

The Trino type for this data structure is called setdigest. Trino offers the ability to merge multiple Set Digest data sketches.

Data sketches can be serialized to and deserialized from varbinary. This allows them to be stored for later use.

Composes all input values of x into a setdigest.

Create a setdigest corresponding to a bigint array:

Create a setdigest corresponding to a varchar array:

Returns the setdigest of the aggregate union of the individual setdigest Set Digest structures.

Returns the cardinality of the set digest from its internal HyperLogLog component.

Returns the estimation for the cardinality of the intersection of the two set digests.

x and y must be of type setdigest

Returns the estimation of Jaccard index for the two set digests.

x and y must be of type setdigest.

Returns a map containing the Murmur3Hash128 hashed values and the count of their occurences within the internal MinHash structure belonging to x.

x must be of type setdigest.

**Examples:**

Example 1 (unknown):
```unknown
WITH text_input(id, text) AS (
         VALUES
             (1, 'The quick brown fox jumps over the lazy dog'),
             (2, 'The quick and the lazy'),
             (3, 'The quick brown fox jumps over the dog')
     ),
     text_ngrams(id, ngrams) AS (
         SELECT id,
                transform(
                  ngrams(
                    split(text, ' '),
                    4
                  ),
                  token -> array_join(token, ' ')
                )
         FROM text_input
     ),
     minhash_digest(id, digest) AS (
         SELECT id,
                (SELECT make_set_digest(v) FROM unnest(ngrams) u(v))
         FROM text_ngrams
     ),
     setdigest_side_by_side(id1, digest1, id2, digest2) AS (
         SELECT m1.id as id1,
                m1.digest as digest1,
                m2.id as id2,
                m2.digest as digest2
         FROM (SELECT id, digest FROM minhash_digest) m1
         JOIN (SELECT id, digest FROM minhash_digest) m2
           ON m1.id != m2.id AND m1.id < m2.id
     )
SELECT id1,
       id2,
       intersection_cardinality(digest1, digest2) AS intersection_cardinality,
       jaccard_index(digest1, digest2)            AS jaccard_index
FROM setdigest_side_by_side
ORDER BY id1, id2;
```

Example 2 (unknown):
```unknown
WITH text_input(id, text) AS (
         VALUES
             (1, 'The quick brown fox jumps over the lazy dog'),
             (2, 'The quick and the lazy'),
             (3, 'The quick brown fox jumps over the dog')
     ),
     text_ngrams(id, ngrams) AS (
         SELECT id,
                transform(
                  ngrams(
                    split(text, ' '),
                    4
                  ),
                  token -> array_join(token, ' ')
                )
         FROM text_input
     ),
     minhash_digest(id, digest) AS (
         SELECT id,
                (SELECT make_set_digest(v) FROM unnest(ngrams) u(v))
         FROM text_ngrams
     ),
     setdigest_side_by_side(id1, digest1, id2, digest2) AS (
         SELECT m1.id as id1,
                m1.digest as digest1,
                m2.id as id2,
                m2.digest as digest2
         FROM (SELECT id, digest FROM minhash_digest) m1
         JOIN (SELECT id, digest FROM minhash_digest) m2
           ON m1.id != m2.id AND m1.id < m2.id
     )
SELECT id1,
       id2,
       intersection_cardinality(digest1, digest2) AS intersection_cardinality,
       jaccard_index(digest1, digest2)            AS jaccard_index
FROM setdigest_side_by_side
ORDER BY id1, id2;
```

Example 3 (unknown):
```unknown
id1 | id2 | intersection_cardinality | jaccard_index
-----+-----+--------------------------+---------------
   1 |   2 |                        0 |           0.0
   1 |   3 |                        4 |           0.6
   2 |   3 |                        0 |           0.0
```

Example 4 (unknown):
```unknown
id1 | id2 | intersection_cardinality | jaccard_index
-----+-----+--------------------------+---------------
   1 |   2 |                        0 |           0.0
   1 |   3 |                        4 |           0.6
   2 |   3 |                        0 |           0.0
```

---

## Conditional expressions — Trino 478 Documentation

**URL:** https://trino.io/docs/current/functions/conditional.html

**Contents:**
- Conditional expressions#
- CASE#
- IF#
- COALESCE#
- NULLIF#
- TRY#
  - Examples#

The standard SQL CASE expression has two forms. The “simple” form searches each value expression from left to right until it finds one that equals expression:

The result for the matching value is returned. If no match is found, the result from the ELSE clause is returned if it exists, otherwise null is returned. Example:

The “searched” form evaluates each boolean condition from left to right until one is true and returns the matching result:

If no conditions are true, the result from the ELSE clause is returned if it exists, otherwise null is returned. Example:

SQL UDFs can use CASE statements that use a slightly different syntax from the CASE expressions. Specifically note the requirements for terminating each clause with a semicolon ; and the usage of END CASE.

The IF expression has two forms, one supplying only a true_value and the other supplying both a true_value and a false_value:

Evaluates and returns true_value if condition is true, otherwise null is returned and true_value is not evaluated.

Evaluates and returns true_value if condition is true, otherwise evaluates and returns false_value.

The following IF and CASE expressions are equivalent:

SQL UDFs can use IF statements that use a slightly different syntax from IF expressions. Specifically note the requirement for terminating each clause with a semicolon ; and the usage of END IF.

Returns the first non-null value in the argument list. Like a CASE expression, arguments are only evaluated if necessary.

Returns null if value1 equals value2, otherwise returns value1.

Evaluate an expression and handle certain types of errors by returning NULL.

In cases where it is preferable that queries produce NULL or default values instead of failing when corrupt or invalid data is encountered, the TRY function may be useful. To specify default values, the TRY function can be used in conjunction with the COALESCE function.

The following errors are handled by TRY:

Invalid cast or function argument

Numeric value out of range

Source table with some invalid data:

Query failure without TRY:

NULL values with TRY:

Query failure without TRY:

Default values with TRY and COALESCE:

**Examples:**

Example 1 (unknown):
```unknown
CASE expression
    WHEN value THEN result
    [ WHEN ... ]
    [ ELSE result ]
END
```

Example 2 (unknown):
```unknown
CASE expression
    WHEN value THEN result
    [ WHEN ... ]
    [ ELSE result ]
END
```

Example 3 (unknown):
```unknown
SELECT a,
       CASE a
           WHEN 1 THEN 'one'
           WHEN 2 THEN 'two'
           ELSE 'many'
       END
```

Example 4 (unknown):
```unknown
SELECT a,
       CASE a
           WHEN 1 THEN 'one'
           WHEN 2 THEN 'two'
           ELSE 'many'
       END
```

---

## UUID functions — Trino 478 Documentation

**URL:** https://trino.io/docs/current/functions/uuid.html

**Contents:**
- UUID functions#

Returns a pseudo randomly generated UUID (type 4).

---

## Decimal functions and operators — Trino 478 Documentation

**URL:** https://trino.io/docs/current/functions/decimal.html

**Contents:**
- Decimal functions and operators#
- Decimal literals#
- Binary arithmetic decimal operators#
- Comparison operators#
- Unary decimal operators#

Use the DECIMAL 'xxxxxxx.yyyyyyy' syntax to define a decimal literal.

The precision of a decimal type for a literal will be equal to the number of digits in the literal (including trailing and leading zeros). The scale will be equal to the number of digits in the fractional part (including trailing zeros).

DECIMAL '0000012345.1234500000'

Standard mathematical operators are supported. The table below explains precision and scale calculation rules for result. Assuming x is of type DECIMAL(xp, xs) and y is of type DECIMAL(yp, ys).

Result type precision

If the mathematical result of the operation is not exactly representable with the precision and scale of the result data type, then an exception condition is raised: Value is out of range.

When operating on decimal types with different scale and precision, the values are first coerced to a common super type. For types near the largest representable precision (38), this can result in Value is out of range errors when one of the operands doesn’t fit in the common super type. For example, the common super type of decimal(38, 0) and decimal(38, 1) is decimal(38, 1), but certain values that fit in decimal(38, 0) cannot be represented as a decimal(38, 1).

All standard Comparison functions and operators work for the decimal type.

The - operator performs negation. The type of result is same as type of argument.

**Examples:**

Example 1 (unknown):
```unknown
min(38,
    1 +
    max(xs, ys) +
    max(xp - xs, yp - ys)
)
```

Example 2 (unknown):
```unknown
min(38,
    1 +
    max(xs, ys) +
    max(xp - xs, yp - ys)
)
```

Example 3 (unknown):
```unknown
min(38, xp + yp)
```

Example 4 (unknown):
```unknown
min(38, xp + yp)
```

---

## Color functions — Trino 478 Documentation

**URL:** https://trino.io/docs/current/functions/color.html

**Contents:**
- Color functions#

Renders a single bar in an ANSI bar chart using a default low_color of red and a high_color of green. For example, if x of 25% and width of 40 are passed to this function. A 10-character red bar will be drawn followed by 30 spaces to create a bar of 40 characters.

Renders a single line in an ANSI bar chart of the specified width. The parameter x is a double value between 0 and 1. Values of x that fall outside the range [0, 1] will be truncated to either a 0 or a 1 value. The low_color and high_color capture the color to use for either end of the horizontal bar chart. For example, if x is 0.5, width is 80, low_color is 0xFF0000, and high_color is 0x00FF00 this function will return a 40 character bar that varies from red (0xFF0000) and yellow (0xFFFF00) and the remainder of the 80 character bar will be padded with spaces.

Returns a color capturing a decoded RGB value from a 4-character string of the format “#000”. The input string should be varchar containing a CSS-style short rgb string or one of black, red, green, yellow, blue, magenta, cyan, white.

Returns a color interpolated between low_color and high_color using the double parameters x, low, and high to calculate a fraction which is then passed to the color(fraction, low_color, high_color) function shown below. If x falls outside the range defined by low and high its value is truncated to fit within this range.

Returns a color interpolated between low_color and high_color according to the double argument x between 0 and 1. The parameter x is a double value between 0 and 1. Values of x that fall outside the range [0, 1] will be truncated to either a 0 or a 1 value.

Renders value x using the specific color using ANSI color codes. x can be either a double, bigint, or varchar.

Accepts boolean value b and renders a green true or a red false using ANSI color codes.

Returns a color value capturing the RGB value of three component color values supplied as int parameters ranging from 0 to 255: red, green, blue.

---

## Bitwise functions — Trino 478 Documentation

**URL:** https://trino.io/docs/current/functions/bitwise.html

**Contents:**
- Bitwise functions#

Count the number of bits set in x (treated as bits-bit signed integer) in 2’s complement representation:

Returns the bitwise AND of x and y in 2’s complement representation.

Bitwise AND of 19 (binary: 10011) and 25 (binary: 11001) results in 17 (binary: 10001):

Returns the bitwise NOT of x in 2’s complement representation (NOT x = -x - 1):

Returns the bitwise OR of x and y in 2’s complement representation.

Bitwise OR of 19 (binary: 10011) and 25 (binary: 11001) results in 27 (binary: 11011):

Returns the bitwise XOR of x and y in 2’s complement representation.

Bitwise XOR of 19 (binary: 10011) and 25 (binary: 11001) results in 10 (binary: 01010):

Returns the left shifted value of value.

Shifting 1 (binary: 001) by two bits results in 4 (binary: 00100):

Shifting 5 (binary: 0101) by two bits results in 20 (binary: 010100):

Shifting a value by 0 always results in the original value:

Shifting 0 by a shift always results in 0:

Returns the logical right shifted value of value.

Shifting 8 (binary: 1000) by three bits results in 1 (binary: 001):

Shifting 9 (binary: 1001) by one bit results in 4 (binary: 100):

Shifting a value by 0 always results in the original value:

Shifting a value by 64 or more bits results in 0:

Shifting 0 by a shift always results in 0:

Returns the arithmetic right shifted value of value.

Returns the same values as bitwise_right_shift() when shifting by less than 64 bits. Shifting by 64 or more bits results in 0 for a positive and -1 for a negative value:

See also bitwise_and_agg() and bitwise_or_agg().

**Examples:**

Example 1 (unknown):
```unknown
SELECT bit_count(9, 64); -- 2
SELECT bit_count(9, 8); -- 2
SELECT bit_count(-7, 64); -- 62
SELECT bit_count(-7, 8); -- 6
```

Example 2 (unknown):
```unknown
SELECT bit_count(9, 64); -- 2
SELECT bit_count(9, 8); -- 2
SELECT bit_count(-7, 64); -- 62
SELECT bit_count(-7, 8); -- 6
```

Example 3 (unknown):
```unknown
SELECT bitwise_and(19,25); -- 17
```

Example 4 (unknown):
```unknown
SELECT bitwise_and(19,25); -- 17
```

---

## T-Digest functions — Trino 478 Documentation

**URL:** https://trino.io/docs/current/functions/tdigest.html

**Contents:**
- T-Digest functions#
- Data structures#
- Functions#

A T-digest is a data sketch which stores approximate percentile information. The Trino type for this data structure is called tdigest. T-digests can be merged, and for storage and retrieval they can be cast to and from VARBINARY.

Aggregates all inputs into a single tdigest.

Returns the approximate percentile value from the T-digest, given the number quantile between 0 and 1.

Returns the approximate percentile values as an array, given the input T-digest and an array of values between 0 and 1, which represent the quantiles to return.

Composes all input values of x into a tdigest. x can be of any numeric type.

Composes all input values of x into a tdigest using the per-item weight w. w must be greater or equal than 1. x and w can be of any numeric type.

---

## HyperLogLog functions — Trino 478 Documentation

**URL:** https://trino.io/docs/current/functions/hyperloglog.html

**Contents:**
- HyperLogLog functions#
- Data structures#
- Serialization#
- Functions#

Trino implements the approx_distinct() function using the HyperLogLog data structure.

Trino implements HyperLogLog data sketches as a set of 32-bit buckets which store a maximum hash. They can be stored sparsely (as a map from bucket ID to bucket), or densely (as a contiguous memory block). The HyperLogLog data structure starts as the sparse representation, switching to dense when it is more efficient. The P4HyperLogLog structure is initialized densely and remains dense for its lifetime.

HyperLogLog implicitly casts to P4HyperLogLog, while one can explicitly cast HyperLogLog to P4HyperLogLog:

Data sketches can be serialized to and deserialized from varbinary. This allows them to be stored for later use. Combined with the ability to merge multiple sketches, this allows one to calculate approx_distinct() of the elements of a partition of a query, then for the entirety of a query with very little cost.

For example, calculating the HyperLogLog for daily unique users will allow weekly or monthly unique users to be calculated incrementally by combining the dailies. This is similar to computing weekly revenue by summing daily revenue. Uses of approx_distinct() with GROUPING SETS can be converted to use HyperLogLog. Examples:

Returns the HyperLogLog sketch of the input data set of x. This data sketch underlies approx_distinct() and can be stored and used later by calling cardinality().

This will perform approx_distinct() on the data summarized by the hll HyperLogLog data sketch.

Returns an empty HyperLogLog.

Returns the HyperLogLog of the aggregate union of the individual hll HyperLogLog structures.

**Examples:**

Example 1 (unknown):
```unknown
cast(hll AS P4HyperLogLog)
```

Example 2 (unknown):
```unknown
cast(hll AS P4HyperLogLog)
```

Example 3 (unknown):
```unknown
CREATE TABLE visit_summaries (
  visit_date date,
  hll varbinary
);

INSERT INTO visit_summaries
SELECT visit_date, cast(approx_set(user_id) AS varbinary)
FROM user_visits
GROUP BY visit_date;

SELECT cardinality(merge(cast(hll AS HyperLogLog))) AS weekly_unique_users
FROM visit_summaries
WHERE visit_date >= current_date - interval '7' day;
```

Example 4 (unknown):
```unknown
CREATE TABLE visit_summaries (
  visit_date date,
  hll varbinary
);

INSERT INTO visit_summaries
SELECT visit_date, cast(approx_set(user_id) AS varbinary)
FROM user_visits
GROUP BY visit_date;

SELECT cardinality(merge(cast(hll AS HyperLogLog))) AS weekly_unique_users
FROM visit_summaries
WHERE visit_date >= current_date - interval '7' day;
```

---

## URL functions — Trino 478 Documentation

**URL:** https://trino.io/docs/current/functions/url.html

**Contents:**
- URL functions#
- Extraction functions#
- Encoding functions#

The URL extraction functions extract components from HTTP URLs (or any valid URIs conforming to RFC 2396). The following syntax is supported:

The extracted components do not contain URI syntax separators such as : or ?.

Returns the fragment identifier from url.

Returns the host from url.

Returns the value of the first query string parameter named name from url. Parameter extraction is handled in the typical manner as specified by RFC 1866#section-8.2.1.

Returns the path from url.

Returns the port number from url.

Returns the protocol from url:

Returns the query string from url.

Escapes value by encoding it so that it can be safely included in URL query parameter names and values:

Alphanumeric characters are not encoded.

The characters ., -, * and _ are not encoded.

The ASCII space character is encoded as +.

All other characters are converted to UTF-8 and the bytes are encoded as the string %XX where XX is the uppercase hexadecimal value of the UTF-8 byte.

Unescapes the URL encoded value. This function is the inverse of url_encode().

**Examples:**

Example 1 (unknown):
```unknown
[protocol:][//host[:port]][path][?query][#fragment]
```

Example 2 (unknown):
```unknown
[protocol:][//host[:port]][path][?query][#fragment]
```

Example 3 (unknown):
```unknown
SELECT url_extract_protocol('http://localhost:8080/req_path');
-- http

SELECT url_extract_protocol('https://127.0.0.1:8080/req_path');
-- https

SELECT url_extract_protocol('ftp://path/file');
-- ftp
```

Example 4 (unknown):
```unknown
SELECT url_extract_protocol('http://localhost:8080/req_path');
-- http

SELECT url_extract_protocol('https://127.0.0.1:8080/req_path');
-- https

SELECT url_extract_protocol('ftp://path/file');
-- ftp
```

---

## Quantile digest functions — Trino 478 Documentation

**URL:** https://trino.io/docs/current/functions/qdigest.html

**Contents:**
- Quantile digest functions#
- Data structures#
- Functions#

A quantile digest is a data sketch which stores approximate percentile information. The Trino type for this data structure is called qdigest, and it takes a parameter which must be one of bigint, double or real which represent the set of numbers that may be ingested by the qdigest. They may be merged without losing precision, and for storage and retrieval they may be cast to/from VARBINARY.

Merges all input qdigests into a single qdigest.

Returns the approximate percentile value from the quantile digest given the number quantile between 0 and 1.

Returns the approximate quantile number between 0 and 1 from the quantile digest given an input value. Null is returned if the quantile digest is empty or the input value is outside the range of the quantile digest.

Returns the approximate percentile values as an array given the input quantile digest and array of values between 0 and 1 which represent the quantiles to return.

Returns the qdigest which is composed of all input values of x.

Returns the qdigest which is composed of all input values of x using the per-item weight w.

Returns the qdigest which is composed of all input values of x using the per-item weight w and maximum error of accuracy. accuracy must be a value greater than zero and less than one, and it must be constant for all input rows.

---

## Comparison functions and operators — Trino 478 Documentation

**URL:** https://trino.io/docs/current/functions/comparison.html

**Contents:**
- Comparison functions and operators#
- Comparison operators#
- Range operator: BETWEEN#
- IS NULL and IS NOT NULL#
- IS DISTINCT FROM and IS NOT DISTINCT FROM#
- GREATEST and LEAST#
- Quantified comparison predicates: ALL, ANY and SOME#
- Pattern comparison: LIKE#
- Row comparison: IN#
- Examples#

Less than or equal to

Greater than or equal to

Not equal (non-standard but popular syntax)

The BETWEEN operator tests if a value is within a specified range. It uses the syntax value BETWEEN min AND max:

The preceding statement is equivalent to the following statement:

To test if a value does not fall within the specified range use NOT BETWEEN:

The statement shown above is equivalent to the following statement:

A NULL in a BETWEEN or NOT BETWEEN statement is evaluated using the standard NULL evaluation rules applied to the equivalent expression above:

The BETWEEN and NOT BETWEEN operators can also be used to evaluate any orderable type. For example, a VARCHAR:

Note that the value, min, and max parameters to BETWEEN and NOT BETWEEN must be the same type. For example, Trino produces an error if you ask it if John is between 2.3 and 35.2.

The IS NULL and IS NOT NULL operators test whether a value is null (undefined). Both operators work for all data types.

Using NULL with IS NULL evaluates to true:

But any other constant does not:

In SQL a NULL value signifies an unknown value, so any comparison involving a NULL produces NULL. The IS DISTINCT FROM and IS NOT DISTINCT FROM operators treat NULL as a known value and both operators guarantee either a true or false outcome even in the presence of NULL input:

In the preceding example a NULL value is not considered distinct from NULL. When you are comparing values which may include NULL use these operators to guarantee either a TRUE or FALSE result.

The following truth table demonstrate the handling of NULL in IS DISTINCT FROM and IS NOT DISTINCT FROM:

These functions are not in the SQL standard, but are a common extension. Like most other functions in Trino, they return null if any argument is null. Note that in some other databases, such as PostgreSQL, they only return null if all arguments are null.

The following types are supported:

TIMESTAMP WITH TIME ZONE

Returns the largest of the provided values.

Returns the smallest of the provided values.

The ALL, ANY and SOME quantifiers can be used together with comparison operators in the following way:

Following are the meanings of some quantifier and comparison operator combinations:

Evaluates to true when A is equal to all values.

Evaluates to true when A doesn’t match any value.

Evaluates to true when A is smaller than the smallest value.

Evaluates to true when A is equal to any of the values. This form is equivalent to A IN (...).

Evaluates to true when A doesn’t match one or more values.

Evaluates to true when A is smaller than the biggest value.

ANY and SOME have the same meaning and can be used interchangeably.

The LIKE operator can be used to compare values with a pattern:

Matching characters is case sensitive, and the pattern supports two symbols for matching:

_ matches any single character

% matches zero or more characters

Typically it is often used as a condition in WHERE statements. An example is a query to find all continents starting with E, which returns Europe:

You can negate the result by adding NOT, and get all other continents, all not starting with E:

If you only have one specific character to match, you can use the _ symbol for each character. The following query uses two underscores and produces only Asia as result:

The wildcard characters _ and % must be escaped to allow you to match them as literals. This can be achieved by specifying the ESCAPE character to use:

The above query returns true since the escaped underscore symbol matches. If you need to match the used escape character as well, you can escape it.

If you want to match for the chosen escape character, you simply escape itself. For example, you can use \\ to match for \.

The IN operator can be used in a WHERE clause to compare column values with a list of values. The list of values can be supplied by a subquery or directly as static values in an array:

Use the optional NOT keyword to negate the condition.

The following example shows a simple usage with a static array:

The values in the clause are used for multiple comparisons that are combined as a logical OR. The preceding query is equivalent to the following query:

You can negate the comparisons by adding NOT, and get all other regions except the values in list:

When using a subquery to determine the values to use in the comparison, the subquery must return a single column and one or more rows. For example, the following query returns nation name of countries in regions starting with the letter A, specifically Africa, America, and Asia:

The following example queries showcase aspects of using comparison functions and operators related to implied ordering of values, implicit casting, and different types.

The following queries show a subtle difference between char and varchar types. The length parameter for varchar is an optional maximum length parameter and comparison is based on the data only, ignoring the length:

The length parameter for char defines a fixed length character array. Comparison with different length automatically includes a cast to the same larger length. The cast is performed as automatic padding with spaces, and therefore both queries in the following return true:

The following queries show how date types are ordered, and how date is implicitly cast to timestamp with zero time values:

**Examples:**

Example 1 (unknown):
```unknown
SELECT 3 BETWEEN 2 AND 6;
```

Example 2 (unknown):
```unknown
SELECT 3 BETWEEN 2 AND 6;
```

Example 3 (unknown):
```unknown
SELECT 3 >= 2 AND 3 <= 6;
```

Example 4 (unknown):
```unknown
SELECT 3 >= 2 AND 3 <= 6;
```

---

## FUNCTION — Trino 478 Documentation

**URL:** https://trino.io/docs/current/udf/function.html

**Contents:**
- FUNCTION#
- Synopsis#
- Description#
- Examples#
- See also#

Declare a user-defined function.

The name of the UDF. Inline user-defined functions can use a simple string. Catalog user-defined functions must qualify the name of the catalog and schema, delimited by ., to store the UDF or rely on the default catalog and schema for UDF storage.

The list of parameters is a comma-separated list of names parameter_name and data types data_type, see data type. An empty list, specified as () is also valid.

The type value after the RETURNS keyword identifies the data type of the UDF output.

The optional LANGUAGE characteristic identifies the language used for the UDF definition with language. The SQL and PYTHON languages are supported by default. Additional languages may be supported via a language engine plugin. If not specified, the default language is SQL.

The optional DETERMINISTIC or NOT DETERMINISTIC characteristic declares that the UDF is deterministic. This means that repeated UDF calls with identical input parameters yield the same result. A UDF is non-deterministic if it calls any non-deterministic UDFs and functions. By default, UDFs are assumed to have a deterministic behavior.

The optional RETURNS NULL ON NULL INPUT characteristic declares that the UDF returns a NULL value when any of the input parameters are NULL. The UDF is not invoked with a NULL input value.

The CALLED ON NULL INPUT characteristic declares that the UDF is invoked with NULL input parameter values.

The RETURNS NULL ON NULL INPUT and CALLED ON NULL INPUT characteristics are mutually exclusive, with CALLED ON NULL INPUT as the default.

The security declaration of SECURITY INVOKER or SECURITY DEFINER is only valid for catalog UDFs. It sets the mode for processing the UDF with the permissions of the user who calls the UDF (INVOKER) or the user who created the UDF (DEFINER).

The COMMENT characteristic can be used to provide information about the function to other users as description. The information is accessible with SHOW FUNCTIONS.

The optional WITH clause can be used to specify properties for the function. The available properties vary based on the function language. For Python user-defined functions, the handler property specifies the name of the Python function to invoke.

For SQL UDFs the body of the UDF can either be a simple single RETURN statement with an expression, or compound list of statements in a BEGIN block. UDF must contain a RETURN statement at the end of the top-level block, even if it’s unreachable.

For UDFs in other languages, the definition is enclosed in a $$-quoted string.

A simple catalog function:

Equivalent usage with an inline function:

Further examples of varying complexity that cover usage of the FUNCTION statement in combination with other statements are available in the SQL UDF documentation and the Python UDF documentation.

User-defined functions

SQL user-defined functions

Python user-defined functions

**Examples:**

Example 1 (unknown):
```unknown
FUNCTION name ( [ parameter_name data_type [, ...] ] )
  RETURNS type
  [ LANGUAGE language]
  [ NOT? DETERMINISTIC ]
  [ RETURNS NULL ON NULL INPUT ]
  [ CALLED ON NULL INPUT ]
  [ SECURITY { DEFINER | INVOKER } ]
  [ COMMENT description]
  [ WITH ( property_name = expression [, ...] ) ]
  { statements | AS definition }
```

Example 2 (unknown):
```unknown
FUNCTION name ( [ parameter_name data_type [, ...] ] )
  RETURNS type
  [ LANGUAGE language]
  [ NOT? DETERMINISTIC ]
  [ RETURNS NULL ON NULL INPUT ]
  [ CALLED ON NULL INPUT ]
  [ SECURITY { DEFINER | INVOKER } ]
  [ COMMENT description]
  [ WITH ( property_name = expression [, ...] ) ]
  { statements | AS definition }
```

Example 3 (unknown):
```unknown
CREATE FUNCTION example.default.meaning_of_life()
  RETURNS BIGINT
  RETURN 42;
```

Example 4 (unknown):
```unknown
CREATE FUNCTION example.default.meaning_of_life()
  RETURNS BIGINT
  RETURN 42;
```

---

## Machine learning functions — Trino 478 Documentation

**URL:** https://trino.io/docs/current/functions/ml.html

**Contents:**
- Machine learning functions#
- Feature vector#
- Classification#
- Regression#
- Machine learning functions#

The machine learning plugin provides machine learning functionality as an aggregation function. It enables you to train Support Vector Machine (SVM) based classifiers and regressors for the supervised learning problems.

The machine learning functions are not optimized for distributed processing. The capability to train large data sets is limited by this execution of the final training on a single instance.

To solve a problem with the machine learning technique, especially as a supervised learning problem, it is necessary to represent the data set with the sequence of pairs of labels and feature vector. A label is a target value you want to predict from the unseen feature and a feature is a N-dimensional vector whose elements are numerical values. In Trino, a feature vector is represented as a map-type value, whose key is an index of each feature, so that it can express a sparse vector. Since classifiers and regressors can recognize the map-type feature vector, there is a function to construct the feature from the existing numerical values, features():

The output from features() can be directly passed to ML functions.

Classification is a type of supervised learning problem to predict the distinct label from the given feature vector. The interface looks similar to the construction of the SVM model from the sequence of pairs of labels and features implemented in Teradata Aster or BigQuery ML. The function to train a classification model looks like as follows:

It returns the trained model in a serialized format.

classify() returns the predicted label by using the trained model. The trained model can not be saved natively, and needs to be passed in the format of a nested query:

As a result you need to run the training process at the same time when predicting values. Internally, the model is trained by libsvm. You can use learn_libsvm_classifier() to control the internal parameters of the model.

Regression is another type of supervised learning problem, predicting continuous value, unlike the classification problem. The target must be numerical values that can be described as double.

The following code shows the creation of the model predicting sepal_length from the other 3 features:

The way to use the model is similar to the classification case:

Internally, the model is trained by libsvm. learn_libsvm_regressor() provides you a way to control the training process.

Returns the map representing the feature vector.

Returns an SVM-based classifier model, trained with the given label and feature data sets.

Returns an SVM-based classifier model, trained with the given label and feature data sets. You can control the training process by libsvm parameters.

Returns a label predicted by the given classifier SVM model.

Returns an SVM-based regressor model, trained with the given target and feature data sets.

Returns an SVM-based regressor model, trained with the given target and feature data sets. You can control the training process by libsvm parameters.

Returns a predicted target value by the given regressor SVM model.

**Examples:**

Example 1 (unknown):
```unknown
SELECT features(1.0, 2.0, 3.0) AS features;
```

Example 2 (unknown):
```unknown
SELECT features(1.0, 2.0, 3.0) AS features;
```

Example 3 (unknown):
```unknown
features
-----------------------
 {0=1.0, 1=2.0, 2=3.0}
```

Example 4 (unknown):
```unknown
features
-----------------------
 {0=1.0, 1=2.0, 2=3.0}
```

---

## System information — Trino 478 Documentation

**URL:** https://trino.io/docs/current/functions/system.html

**Contents:**
- System information#

Functions providing information about the Trino cluster system environment. More information is available by querying the various schemas and tables exposed by the System connector.

Returns the Trino version used on the cluster. Equivalent to the value of the node_version column in the system.runtime.nodes table.

---

## Date and time functions and operators — Trino 478 Documentation

**URL:** https://trino.io/docs/current/functions/datetime.html

**Contents:**
- Date and time functions and operators#
- Date and time operators#
- Time zone conversion#
- Date and time functions#
- Truncation function#
- Interval functions#
- Duration function#
- MySQL date functions#
- Java date functions#
- Extraction function#

These functions and operators operate on date and time data types.

date '2012-08-08' + interval '2' day

time '01:00' + interval '3' hour

timestamp '2012-08-08 01:00' + interval '29' hour

2012-08-09 06:00:00.000

timestamp '2012-10-31 01:00' + interval '1' month

2012-11-30 01:00:00.000

interval '2' day + interval '3' hour

interval '3' year + interval '5' month

date '2012-08-08' - interval '2' day

time '01:00' - interval '3' hour

timestamp '2012-08-08 01:00' - interval '29' hour

2012-08-06 20:00:00.000

timestamp '2012-10-31 01:00' - interval '1' month

2012-09-30 01:00:00.000

interval '2' day - interval '3' hour

interval '3' year - interval '5' month

The AT TIME ZONE operator sets the time zone of a timestamp:

Returns the current date as of the start of the query.

Returns the current time with time zone as of the start of the query.

Returns the current timestamp with time zone as of the start of the query, with 3 digits of subsecond precision,

Returns the current timestamp with time zone as of the start of the query, with p digits of subsecond precision:

Returns the current time zone in the format defined by IANA (e.g., America/Los_Angeles) or as fixed offset from UTC (e.g., +08:35)

This is an alias for CAST(x AS date).

Returns the last day of the month.

Parses the ISO 8601 formatted date string, optionally with time and time zone, into a timestamp(3) with time zone. The time defaults to 00:00:00.000, and the time zone defaults to the session time zone:

Parses the ISO 8601 formatted date and time string. The time zone defaults to the session time zone:

Parses the ISO 8601 formatted date string into a date. The date can be a calendar date, a week date using ISO week numbering, or year and day of year combined:

Converts a timestamp(p) with time zone to a time zone specified in zone.

In the following example, the input timezone is GMT, which is seven hours ahead of America/Los_Angeles in November 2022:

Returns the timestamp specified in timestamp with the time zone specified in zone with precision p:

Returns the UNIX timestamp unixtime as a timestamp with time zone. unixtime is the number of seconds since 1970-01-01 00:00:00 UTC.

Returns the UNIX timestamp unixtime as a timestamp with time zone using zone for the time zone. unixtime is the number of seconds since 1970-01-01 00:00:00 UTC.

Returns the UNIX timestamp unixtime as a timestamp with time zone using hours and minutes for the time zone offset. unixtime is the number of seconds since 1970-01-01 00:00:00 in double data type.

Returns the UNIX timestamp unixtime as a timestamp with time zone. unixtime is the number of nanoseconds since 1970-01-01 00:00:00.000000000 UTC:

Returns the current time as of the start of the query.

Returns the current timestamp as of the start of the query, with 3 digits of subsecond precision.

Returns the current timestamp as of the start of the query, with p digits of subsecond precision:

This is an alias for current_timestamp.

Formats x as an ISO 8601 string. x can be date, timestamp, or timestamp with time zone.

Returns the day-to-second interval as milliseconds.

Returns timestamp as a UNIX timestamp.

The following SQL-standard functions do not use parenthesis:

The date_trunc function supports the following units:

Example Truncated Value

2001-08-22 03:04:05.321

2001-08-22 03:04:05.000

2001-08-22 03:04:00.000

2001-08-22 03:00:00.000

2001-08-22 00:00:00.000

2001-08-20 00:00:00.000

2001-08-01 00:00:00.000

2001-07-01 00:00:00.000

2001-01-01 00:00:00.000

The above examples use the timestamp 2001-08-22 03:04:05.321 as the input.

Returns x truncated to unit:

The functions in this section support the following interval units:

Adds an interval value of type unit to timestamp. Subtraction can be performed by using a negative value:

Returns timestamp2 - timestamp1 expressed in terms of unit:

The parse_duration function supports the following units:

Parses string of format value unit into an interval, where value is fractional number of unit values:

Formats the double value of seconds into a human-readable string containing weeks, days, hours, minutes, and seconds:

The functions in this section use a format string that is compatible with the MySQL date_parse and str_to_date functions. The following table, based on the MySQL manual, describes the format specifiers:

Abbreviated weekday name (Sun .. Sat)

Abbreviated month name (Jan .. Dec)

Month, numeric (1 .. 12), this specifier does not support 0 as a month.

Day of the month with English suffix (0th, 1st, 2nd, 3rd, …)

Day of the month, numeric (01 .. 31), this specifier does not support 0 as a month or day.

Day of the month, numeric (1 .. 31), this specifier does not support 0 as a day.

Fraction of second (6 digits for printing: 000000 .. 999000; 1 - 9 digits for parsing: 0 .. 999999999), timestamp is truncated to milliseconds.

Minutes, numeric (00 .. 59)

Day of year (001 .. 366)

Month name (January .. December)

Month, numeric (01 .. 12), this specifier does not support 0 as a month.

Time of day, 12-hour (equivalent to %h:%i:%s %p)

Time of day, 24-hour (equivalent to %H:%i:%s)

Week (00 .. 53), where Sunday is the first day of the week

Week (00 .. 53), where Monday is the first day of the week

Week (01 .. 53), where Sunday is the first day of the week; used with %X

Week (01 .. 53), where Monday is the first day of the week; used with %x

Weekday name (Sunday .. Saturday)

Day of the week (0 .. 6), where Sunday is the first day of the week, this specifier is not supported,consider using day_of_week() (it uses 1-7 instead of 0-6).

Year for the week where Sunday is the first day of the week, numeric, four digits; used with %V

Year for the week, where Monday is the first day of the week, numeric, four digits; used with %v

Year, numeric, four digits

Year, numeric (two digits), when parsing, two-digit year format assumes range 1970 .. 2069, so “70” will result in year 1970 but “69” will produce 2069.

A literal % character

x, for any x not listed above

The following specifiers are not currently supported: %D %U %u %V %w %X

Formats timestamp as a string using format:

Parses string into a timestamp using format:

The functions in this section use a format string that is compatible with JodaTime’s DateTimeFormat pattern format.

Formats timestamp as a string using format.

Parses string into a timestamp with time zone using format.

The extract function supports the following fields:

The types supported by the extract function vary depending on the field to be extracted. Most fields support all date and time types.

Returns field from x:

This SQL-standard function uses special syntax for specifying the arguments.

Returns the day of the month from x.

This is an alias for day().

Returns the ISO day of the week from x. The value ranges from 1 (Monday) to 7 (Sunday).

Returns the day of the year from x. The value ranges from 1 to 366.

This is an alias for day_of_week().

This is an alias for day_of_year().

Returns the hour of the day from x. The value ranges from 0 to 23.

Returns the millisecond of the second from x.

Returns the minute of the hour from x.

Returns the month of the year from x.

Returns the quarter of the year from x. The value ranges from 1 to 4.

Returns the second of the minute from x.

Returns the hour of the time zone offset from timestamp.

Returns the minute of the time zone offset from timestamp.

Returns the ISO week of the year from x. The value ranges from 1 to 53.

This is an alias for week().

Returns the year from x.

Returns the year of the ISO week from x.

This is an alias for year_of_week().

Returns the timezone identifier from timestamp(p) with time zone. The format of the returned identifier is identical to the format used in the input timestamp:

Returns the timezone identifier from a time(p) with time zone. The format of the returned identifier is identical to the format used in the input time:

**Examples:**

Example 1 (unknown):
```unknown
SELECT timestamp '2012-10-31 01:00 UTC';
-- 2012-10-31 01:00:00.000 UTC

SELECT timestamp '2012-10-31 01:00 UTC' AT TIME ZONE 'America/Los_Angeles';
-- 2012-10-30 18:00:00.000 America/Los_Angeles
```

Example 2 (unknown):
```unknown
SELECT timestamp '2012-10-31 01:00 UTC';
-- 2012-10-31 01:00:00.000 UTC

SELECT timestamp '2012-10-31 01:00 UTC' AT TIME ZONE 'America/Los_Angeles';
-- 2012-10-30 18:00:00.000 America/Los_Angeles
```

Example 3 (unknown):
```unknown
SELECT current_timestamp(6);
-- 2020-06-24 08:25:31.759993 America/Los_Angeles
```

Example 4 (unknown):
```unknown
SELECT current_timestamp(6);
-- 2020-06-24 08:25:31.759993 America/Los_Angeles
```

---

## Mathematical functions and operators — Trino 478 Documentation

**URL:** https://trino.io/docs/current/functions/math.html

**Contents:**
- Mathematical functions and operators#
- Mathematical operators#
- Mathematical functions#
- Random functions#
- Trigonometric functions#
- Geometric functions#
- Floating point functions#
- Base conversion functions#
- Statistical functions#
- Cumulative distribution functions#

Division (integer division performs truncation)

Returns the absolute value of x.

Returns the cube root of x.

This is an alias for ceiling().

Returns x rounded up to the nearest integer.

Converts angle x in radians to degrees.

Returns the constant Euler’s number.

Returns Euler’s number raised to the power of x.

Returns x rounded down to the nearest integer.

Returns the natural logarithm of x.

Returns the base b logarithm of x.

Returns the base 2 logarithm of x.

Returns the base 10 logarithm of x.

Returns the modulus (remainder) of n divided by m.

Returns the constant Pi.

This is an alias for power().

Returns x raised to the power of p.

Converts angle x in degrees to radians.

Returns x rounded to the nearest integer.

Returns x rounded to d decimal places.

Returns the signum function of x, that is:

0 if the argument is 0,

1 if the argument is greater than 0,

-1 if the argument is less than 0.

For floating point arguments, the function additionally returns:

-0 if the argument is -0,

NaN if the argument is NaN,

1 if the argument is +Infinity,

-1 if the argument is -Infinity.

Returns the square root of x.

Returns x rounded to integer by dropping digits after decimal point.

Returns the bin number of x in an equi-width histogram with the specified bound1 and bound2 bounds and n number of buckets.

Returns the bin number of x according to the bins specified by the array bins. The bins parameter must be an array of doubles and is assumed to be in sorted ascending order.

This is an alias for random().

Returns a pseudo-random value in the range 0.0 <= x < 1.0.

Returns a pseudo-random number between 0 and n (exclusive).

Returns a pseudo-random number between m and n (exclusive).

All trigonometric function arguments are expressed in radians. See unit conversion functions degrees() and radians().

Returns the arc cosine of x.

Returns the arc sine of x.

Returns the arc tangent of x.

Returns the arc tangent of y / x.

Returns the cosine of x.

Returns the hyperbolic cosine of x.

Returns the sine of x.

Returns the hyperbolic sine of x.

Returns the tangent of x.

Returns the hyperbolic tangent of x.

Calculates the cosine distance between two dense vectors:

Calculates the cosine distance between two sparse vectors:

Calculates the cosine similarity of two dense vectors:

Calculates the cosine similarity of two sparse vectors:

Returns the constant representing positive infinity.

Determine if x is finite.

Determine if x is infinite.

Determine if x is not-a-number.

Returns the constant representing not-a-number.

Returns the value of string interpreted as a base-radix number.

Returns the base-radix representation of x.

Computes the Student’s t-distribution probability density function for given x and degrees of freedom (df). The x must be a real value and degrees of freedom must be an integer and positive value.

Returns the lower bound of the Wilson score interval of a Bernoulli trial process at a confidence specified by the z-score z.

Returns the upper bound of the Wilson score interval of a Bernoulli trial process at a confidence specified by the z-score z.

Compute the Beta cdf with given a, b parameters: P(N < v; a, b). The a, b parameters must be positive real numbers and value v must be a real value. The value v must lie on the interval [0, 1].

Compute the inverse of the Beta cdf with given a, b parameters for the cumulative probability (p): P(N < n). The a, b parameters must be positive real values. The probability p must lie on the interval [0, 1].

Compute the inverse of the Normal cdf with given mean and standard deviation (sd) for the cumulative probability (p): P(N < n). The mean must be a real value and the standard deviation must be a real and positive value. The probability p must lie on the interval (0, 1).

Compute the Normal cdf with given mean and standard deviation (sd): P(N < v; mean, sd). The mean and value v must be real values and the standard deviation must be a real and positive value.

Compute the Student’s t-distribution cumulative density function for given x and degrees of freedom (df). The x must be a real value and degrees of freedom must be an integer and positive value.

**Examples:**

Example 1 (unknown):
```unknown
SELECT cosine_distance(ARRAY[1.0, 2.0], ARRAY[3.0, 4.0]);
-- 0.01613008990009257
```

Example 2 (unknown):
```unknown
SELECT cosine_distance(ARRAY[1.0, 2.0], ARRAY[3.0, 4.0]);
-- 0.01613008990009257
```

Example 3 (unknown):
```unknown
SELECT cosine_distance(MAP(ARRAY['a'], ARRAY[1.0]), MAP(ARRAY['a'], ARRAY[2.0]));
-- 0.0
```

Example 4 (unknown):
```unknown
SELECT cosine_distance(MAP(ARRAY['a'], ARRAY[1.0]), MAP(ARRAY['a'], ARRAY[2.0]));
-- 0.0
```

---

## Binary functions and operators — Trino 478 Documentation

**URL:** https://trino.io/docs/current/functions/binary.html

**Contents:**
- Binary functions and operators#
- Binary operators#
- Binary functions#
- Base64 encoding functions#
- Hex encoding functions#
- Integer encoding functions#
- Floating-point encoding functions#
- Hashing functions#
- HMAC functions#

The || operator performs concatenation.

Returns the concatenation of binary1, binary2, ..., binaryN. This function provides the same functionality as the SQL-standard concatenation operator (||).

Returns the length of binary in bytes.

Left pads binary to size bytes with padbinary. If size is less than the length of binary, the result is truncated to size characters. size must not be negative and padbinary must be non-empty.

Right pads binary to size bytes with padbinary. If size is less than the length of binary, the result is truncated to size characters. size must not be negative and padbinary must be non-empty.

Returns the rest of binary from the starting position start, measured in bytes. Positions start with 1. A negative starting position is interpreted as being relative to the end of the string.

Returns a substring from binary of length length from the starting position start, measured in bytes. Positions start with 1. A negative starting position is interpreted as being relative to the end of the string.

Returns binary with the bytes in reverse order.

The Base64 functions implement the encoding specified in RFC 4648.

Decodes binary data from the base64 encoded string.

Encodes binary into a base64 string representation.

Decodes binary data from the base64 encoded string using the URL safe alphabet.

Encodes binary into a base64 string representation using the URL safe alphabet.

Decodes binary data from the base32 encoded string.

Encodes binary into a base32 string representation.

Decodes binary data from the hex encoded string.

Encodes binary into a hex string representation.

Decodes the 32-bit two’s complement big-endian binary. The input must be exactly 4 bytes.

Encodes integer into a 32-bit two’s complement big-endian format.

Decodes the 64-bit two’s complement big-endian binary. The input must be exactly 8 bytes.

Encodes bigint into a 64-bit two’s complement big-endian format.

Decodes the 32-bit big-endian binary in IEEE 754 single-precision floating-point format. The input must be exactly 4 bytes.

Encodes real into a 32-bit big-endian binary according to IEEE 754 single-precision floating-point format.

Decodes the 64-bit big-endian binary in IEEE 754 double-precision floating-point format. The input must be exactly 8 bytes.

Encodes double into a 64-bit big-endian binary according to IEEE 754 double-precision floating-point format.

Computes the CRC-32 of binary. For general purpose hashing, use xxhash64(), as it is much faster and produces a better quality hash.

Computes the MD5 hash of binary.

Computes the SHA1 hash of binary.

Computes the SHA256 hash of binary.

Computes the SHA512 hash of binary.

Computes the 32-bit SpookyHashV2 hash of binary.

Computes the 64-bit SpookyHashV2 hash of binary.

Computes the xxHash64 hash of binary.

Computes the 128-bit MurmurHash3 hash of binary.

Computes HMAC with MD5 of binary with the given key.

Computes HMAC with SHA1 of binary with the given key.

Computes HMAC with SHA256 of binary with the given key.

Computes HMAC with SHA512 of binary with the given key.

**Examples:**

Example 1 (unknown):
```unknown
SELECT murmur3(from_base64('aaaaaa'));
-- ba 58 55 63 55 69 b4 2f 49 20 37 2c a0 e3 96 ef
```

Example 2 (unknown):
```unknown
SELECT murmur3(from_base64('aaaaaa'));
-- ba 58 55 63 55 69 b4 2f 49 20 37 2c a0 e3 96 ef
```

---

## Logical operators — Trino 478 Documentation

**URL:** https://trino.io/docs/current/functions/logical.html

**Contents:**
- Logical operators#
- Logical operators#
- Effect of NULL on logical operators#

True if both values are true

True if either value is true

True if the value is false

The result of an AND comparison may be NULL if one or both sides of the expression are NULL. If at least one side of an AND operator is FALSE the expression evaluates to FALSE:

The result of an OR comparison may be NULL if one or both sides of the expression are NULL. If at least one side of an OR operator is TRUE the expression evaluates to TRUE:

The following truth table demonstrates the handling of NULL in AND and OR:

The logical complement of NULL is NULL as shown in the following example:

The following truth table demonstrates the handling of NULL in NOT:

**Examples:**

Example 1 (unknown):
```unknown
SELECT CAST(null AS boolean) AND true; -- null

SELECT CAST(null AS boolean) AND false; -- false

SELECT CAST(null AS boolean) AND CAST(null AS boolean); -- null
```

Example 2 (unknown):
```unknown
SELECT CAST(null AS boolean) AND true; -- null

SELECT CAST(null AS boolean) AND false; -- false

SELECT CAST(null AS boolean) AND CAST(null AS boolean); -- null
```

Example 3 (unknown):
```unknown
SELECT CAST(null AS boolean) OR CAST(null AS boolean); -- null

SELECT CAST(null AS boolean) OR false; -- null

SELECT CAST(null AS boolean) OR true; -- true
```

Example 4 (unknown):
```unknown
SELECT CAST(null AS boolean) OR CAST(null AS boolean); -- null

SELECT CAST(null AS boolean) OR false; -- null

SELECT CAST(null AS boolean) OR true; -- true
```

---

## List of functions by topic — Trino 478 Documentation

**URL:** https://trino.io/docs/current/functions/list-by-topic.html

**Contents:**
- List of functions by topic#
- Aggregate#
- Array#
- Binary#
- Bitwise#
- Color#
- Comparison#
- Conditional#
- Conversion#
- Date and time#

For more details, see Aggregate functions

approx_most_frequent()

For more details, see Array functions and operators

For more details, see Binary functions and operators

For more details, see Bitwise functions

bitwise_right_shift()

bitwise_right_shift_arithmetic()

For more details, see Color functions

For more details, see Comparison functions and operators

For more details, see Conditional expressions

For more details, see Conversion functions

For more details, see Date and time functions and operators

from_iso8601_timestamp()

from_unixtime_nanos()

human_readable_seconds()

For more details, see Geospatial functions

bing_tile_coordinates()

bing_tile_zoom_level()

from_encoded_polyline()

from_geojson_geometry()

geometry_from_hadoop_shape()

geometry_invalid_reason()

geometry_nearest_points()

geometry_to_bing_tiles()

great_circle_distance()

line_interpolate_point()

ST_GeometryFromText()

to_encoded_polyline()

to_geojson_geometry()

to_spherical_geography()

For more details, see HyperLogLog functions

For more details, see JSON functions and operators

json_array_contains()

json_extract_scalar()

For more details, see Lambda expressions

For more details, see Machine learning functions

learn_libsvm_classifier()

learn_libsvm_regressor()

For more details, see Map functions and operators

multimap_from_entries()

For more details, see Mathematical functions and operators

wilson_interval_lower()

wilson_interval_upper()

For more details, see Quantile digest functions

values_at_quantiles()

For more details, see Regular expression functions

For more details, see Session information

For more details, see Set Digest functions

intersection_cardinality()

For more details, see String functions and operators

levenshtein_distance()

randmom_string(), catalog function of the Faker connector

For more details, see System information

For more details, see Table functions

For more details, see T-Digest functions

For more details, see Teradata functions

For more details, see URL functions

url_extract_fragment()

url_extract_parameter()

url_extract_protocol()

For more details, see UUID functions

For more details, see Window functions

---

## Map functions and operators — Trino 478 Documentation

**URL:** https://trino.io/docs/current/functions/map.html

**Contents:**
- Map functions and operators#
- Subscript operator: []#
- Map functions#

Map functions and operators use the MAP type. Create a map with the data type constructor using an array of keys and another array of values in the same order. Keys must be character-based and can not be null.

Create an array with integer values

Create an array of character values:

Values must use the same type or it must be possible to coerce values to a common type. The following example uses integer and decimal values and the resulting array contains decimals:

Null values are allowed:

The [] operator is used to retrieve the value corresponding to a given key from a map. This operator throws an error if the key is not contained in the map. See also element_at function that returns NULL in such case.

The following example constructs a map and then accesses the element with the key key2:

Returns the cardinality (size) of the map x.

Returns value for given key, or NULL if the key is not contained in the map.

Returns an empty map.

Returns a map created using the given key/value arrays.

See also map_agg() and multimap_agg() for creating a map as an aggregation.

Returns a map created from the given array of entries.

Returns a multimap created from the given array of entries. Each key can be associated with multiple values.

Returns an array of all entries in the given map.

Returns the union of all the given maps. If a key is found in multiple given maps, that key’s value in the resulting map comes from the last one of those maps.

Constructs a map from those entries of map for which function returns true:

Returns all the keys in the map x.

Returns all the values in the map x.

Merges the two given maps into a single map by applying function to the pair of values with the same key. For keys only presented in one map, NULL will be passed as the value for the missing key.

Returns a map that applies function to each entry of map and transforms the keys:

Returns a map that applies function to each entry of map and transforms the values:

**Examples:**

Example 1 (unknown):
```unknown
SELECT MAP(ARRAY['key1', 'key2', 'key3' ], ARRAY[2373, 3463, 45837]);
-- {key1=2373, key2=3463, key3=45837}
```

Example 2 (unknown):
```unknown
SELECT MAP(ARRAY['key1', 'key2', 'key3' ], ARRAY[2373, 3463, 45837]);
-- {key1=2373, key2=3463, key3=45837}
```

Example 3 (unknown):
```unknown
SELECT MAP(ARRAY['key1', 'key2', 'key3' ], ARRAY['v1', 'v2', 'v3']);
-- {key1=v1, key2=v2, key3=v3}
```

Example 4 (unknown):
```unknown
SELECT MAP(ARRAY['key1', 'key2', 'key3' ], ARRAY['v1', 'v2', 'v3']);
-- {key1=v1, key2=v2, key3=v3}
```

---

## Geospatial functions — Trino 478 Documentation

**URL:** https://trino.io/docs/current/functions/geospatial.html

**Contents:**
- Geospatial functions#
- Constructors#
- Relationship tests#
- Operations#
- Accessors#
- Aggregations#
- Bing tiles#
- Encoded polylines#

Trino Geospatial functions that begin with the ST_ prefix support the SQL/MM specification and are compliant with the Open Geospatial Consortium’s (OGC) OpenGIS Specifications. As such, many Trino Geospatial functions require, or more accurately, assume that geometries that are operated on are both simple and valid. For example, it does not make sense to calculate the area of a polygon that has a hole defined outside the polygon, or to construct a polygon from a non-simple boundary line.

Trino Geospatial functions support the Well-Known Text (WKT) and Well-Known Binary (WKB) form of spatial objects:

LINESTRING (0 0, 1 1, 1 2)

POLYGON ((0 0, 4 0, 4 4, 0 4, 0 0), (1 1, 2 1, 2 2, 1 2, 1 1))

MULTIPOINT (0 0, 1 2)

MULTILINESTRING ((0 0, 1 1, 1 2), (2 3, 3 2, 5 4))

MULTIPOLYGON (((0 0, 4 0, 4 4, 0 4, 0 0), (1 1, 2 1, 2 2, 1 2, 1 1)), ((-1 -1, -1 -2, -2 -2, -2 -1, -1 -1)))

GEOMETRYCOLLECTION (POINT(2 3), LINESTRING (2 3, 3 4))

Use ST_GeometryFromText() and ST_GeomFromBinary() functions to create geometry objects from WKT or WKB.

The SphericalGeography type provides native support for spatial features represented on geographic coordinates (sometimes called geodetic coordinates, or lat/lon, or lon/lat). Geographic coordinates are spherical coordinates expressed in angular units (degrees).

The basis for the Geometry type is a plane. The shortest path between two points on the plane is a straight line. That means calculations on geometries (areas, distances, lengths, intersections, etc.) can be calculated using cartesian mathematics and straight line vectors.

The basis for the SphericalGeography type is a sphere. The shortest path between two points on the sphere is a great circle arc. That means that calculations on geographies (areas, distances, lengths, intersections, etc.) must be calculated on the sphere, using more complicated mathematics. More accurate measurements that take the actual spheroidal shape of the world into account are not supported.

Values returned by the measurement functions ST_Distance() and ST_Length() are in the unit of meters; values returned by ST_Area() are in square meters.

Use to_spherical_geography() function to convert a geometry object to geography object.

For example, ST_Distance(ST_Point(-71.0882, 42.3607), ST_Point(-74.1197, 40.6976)) returns 3.4577 in the unit of the passed-in values on the Euclidean plane, while ST_Distance(to_spherical_geography(ST_Point(-71.0882, 42.3607)), to_spherical_geography(ST_Point(-74.1197, 40.6976))) returns 312822.179 in meters.

Returns the WKB representation of the geometry.

Returns the WKT representation of the geometry. For empty geometries, ST_AsText(ST_LineFromText('LINESTRING EMPTY')) will produce 'MULTILINESTRING EMPTY' and ST_AsText(ST_Polygon('POLYGON EMPTY')) will produce 'MULTIPOLYGON EMPTY'.

Returns a geometry type object from WKT representation.

Returns a geometry type object from WKB or EWKB representation.

Returns a geometry type object from KML representation.

Returns a geometry type object from Spatial Framework for Hadoop representation.

Returns a geometry type linestring object from WKT representation.

Returns a LineString formed from an array of points. If there are fewer than two non-empty points in the input array, an empty LineString will be returned. Array elements must not be NULL or the same as the previous element. The returned geometry may not be simple, e.g. may self-intersect or may contain duplicate vertexes depending on the input.

Returns a MultiPoint geometry object formed from the specified points. Returns NULL if input array is empty. Array elements must not be NULL or empty. The returned geometry may not be simple and may contain duplicate points if input array has duplicates.

Returns a geometry type point object with the given coordinate values.

Returns a geometry type polygon object from WKT representation.

Converts a Geometry object to a SphericalGeography object on the sphere of the Earth’s radius. This function is only applicable to POINT, MULTIPOINT, LINESTRING, MULTILINESTRING, POLYGON, MULTIPOLYGON geometries defined in 2D space, or GEOMETRYCOLLECTION of such geometries. For each point of the input geometry, it verifies that point.x is within [-180.0, 180.0] and point.y is within [-90.0, 90.0], and uses them as (longitude, latitude) degrees to construct the shape of the SphericalGeography result.

Converts a SphericalGeography object to a Geometry object.

Returns true if and only if no points of the second geometry lie in the exterior of the first geometry, and at least one point of the interior of the first geometry lies in the interior of the second geometry.

Returns true if the supplied geometries have some, but not all, interior points in common.

Returns true if the give geometries do not spatially intersect – if they do not share any space together.

Returns true if the given geometries represent the same geometry.

Returns true if the given geometries spatially intersect in two dimensions (share any portion of space) and false if they do not (they are disjoint).

Returns true if the given geometries share space, are of the same dimension, but are not completely contained by each other.

Returns true if first geometry is spatially related to second geometry.

Returns true if the given geometries have at least one point in common, but their interiors do not intersect.

Returns true if first geometry is completely inside second geometry.

Returns the points on each geometry nearest the other. If either geometry is empty, return NULL. Otherwise, return a row of two Points that have the minimum distance of any two points on the geometries. The first Point will be from the first Geometry argument, the second from the second Geometry argument. If there are multiple pairs with the minimum distance, one pair is chosen arbitrarily.

Returns a geometry that represents the point set union of the input geometries. Performance of this function, in conjunction with array_agg() to first aggregate the input geometries, may be better than geometry_union_agg(), at the expense of higher memory utilization.

Returns the closure of the combinatorial boundary of this geometry.

Returns the geometry that represents all points whose distance from the specified geometry is less than or equal to the specified distance. If the points of the geometry are extremely close together (delta < 1e-8), this might return an empty geometry.

Returns the geometry value that represents the point set difference of the given geometries.

Returns the bounding rectangular polygon of a geometry.

Returns an array of two points: the lower left and upper right corners of the bounding rectangular polygon of a geometry. Returns NULL if input geometry is empty.

Returns a line string representing the exterior ring of the input polygon.

Returns the geometry value that represents the point set intersection of two geometries.

Returns the geometry value that represents the point set symmetric difference of two geometries.

Returns a geometry that represents the point set union of the input geometries.

See also: geometry_union(), geometry_union_agg()

Returns the 2D Euclidean area of a geometry.

For Point and LineString types, returns 0.0. For GeometryCollection types, returns the sum of the areas of the individual geometries.

Returns the area of a polygon or multi-polygon in square meters using a spherical model for Earth.

Returns the point value that is the mathematical centroid of a geometry.

Returns the minimum convex geometry that encloses all input geometries.

Returns the coordinate dimension of the geometry.

Returns the inherent dimension of this geometry object, which must be less than or equal to the coordinate dimension.

Returns the 2-dimensional cartesian minimum distance (based on spatial ref) between two geometries in projected units.

Returns the great-circle distance in meters between two SphericalGeography points.

Returns the geometry element at a given index (indices start at 1). If the geometry is a collection of geometries (e.g., GEOMETRYCOLLECTION or MULTI*), returns the geometry at a given index. If the given index is less than 1 or greater than the total number of elements in the collection, returns NULL. Use ST_NumGeometries() to find out the total number of elements. Singular geometries (e.g., POINT, LINESTRING, POLYGON), are treated as collections of one element. Empty geometries are treated as empty collections.

Returns the interior ring element at the specified index (indices start at 1). If the given index is less than 1 or greater than the total number of interior rings in the input geometry, returns NULL. The input geometry must be a polygon. Use ST_NumInteriorRing() to find out the total number of elements.

Returns the type of the geometry.

Returns true if the linestring’s start and end points are coincident.

Returns true if this Geometry is an empty geometrycollection, polygon, point etc.

Returns true if this Geometry has no anomalous geometric points, such as self intersection or self tangency.

Returns true if and only if the line is closed and simple.

Returns true if and only if the input geometry is well-formed. Use geometry_invalid_reason() to determine why the geometry is not well-formed.

Returns the length of a linestring or multi-linestring using Euclidean measurement on a two-dimensional plane (based on spatial ref) in projected units.

Returns the length of a linestring or multi-linestring on a spherical model of the Earth. This is equivalent to the sum of great-circle distances between adjacent points on the linestring.

Returns the vertex of a linestring at a given index (indices start at 1). If the given index is less than 1 or greater than the total number of elements in the collection, returns NULL. Use ST_NumPoints() to find out the total number of elements.

Returns an array of points in a linestring.

Returns X maxima of a bounding box of a geometry.

Returns Y maxima of a bounding box of a geometry.

Returns X minima of a bounding box of a geometry.

Returns Y minima of a bounding box of a geometry.

Returns the first point of a LineString geometry as a Point. This is a shortcut for ST_PointN(geometry, 1).

Returns a “simplified” version of the input geometry using the Douglas-Peucker algorithm. Will avoid creating derived geometries (polygons in particular) that are invalid.

Returns the last point of a LineString geometry as a Point. This is a shortcut for ST_PointN(geometry, ST_NumPoints(geometry)).

Returns the X coordinate of the point.

Returns the Y coordinate of the point.

Returns an array of all interior rings found in the input geometry, or an empty array if the polygon has no interior rings. Returns NULL if the input geometry is empty. The input geometry must be a polygon.

Returns the number of geometries in the collection. If the geometry is a collection of geometries (e.g., GEOMETRYCOLLECTION or MULTI*), returns the number of geometries, for single geometries returns 1, for empty geometries returns 0.

Returns an array of geometries in the specified collection. Returns a one-element array if the input geometry is not a multi-geometry. Returns NULL if input geometry is empty.

Returns the number of points in a geometry. This is an extension to the SQL/MM ST_NumPoints function which only applies to point and linestring.

Returns the cardinality of the collection of interior rings of a polygon.

Returns a Point interpolated along a LineString at the fraction given. The fraction must be between 0 and 1, inclusive.

Returns an array of Points interpolated along a LineString. The fraction must be between 0 and 1, inclusive.

Returns a float between 0 and 1 representing the location of the closest point on the LineString to the given Point, as a fraction of total 2d line length.

Returns NULL if a LineString or a Point is empty or NULL.

Returns the reason for why the input geometry is not valid. Returns NULL if the input is valid.

Returns the great-circle distance between two points on Earth’s surface in kilometers.

Returns the GeoJSON encoded defined by the input spherical geography.

Returns the spherical geography type object from the GeoJSON representation stripping non geometry key/values. Feature and FeatureCollection are not supported.

Returns the minimum convex geometry that encloses all input geometries.

Returns a geometry that represents the point set union of all input geometries.

These functions convert between geometries and Bing tiles.

Creates a Bing tile object from XY coordinates and a zoom level. Zoom levels from 1 to 23 are supported.

Creates a Bing tile object from a quadkey.

Returns a Bing tile at a given zoom level containing a point at a given latitude and longitude. Latitude must be within [-85.05112878, 85.05112878] range. Longitude must be within [-180, 180] range. Zoom levels from 1 to 23 are supported.

Returns a collection of Bing tiles that surround the point specified by the latitude and longitude arguments at a given zoom level.

Returns a minimum set of Bing tiles at specified zoom level that cover a circle of specified radius in km around a specified (latitude, longitude) point.

Returns the XY coordinates of a given Bing tile.

Returns the polygon representation of a given Bing tile.

Returns the quadkey of a given Bing tile.

Returns the zoom level of a given Bing tile.

Returns the minimum set of Bing tiles that fully covers a given geometry at a given zoom level. Zoom levels from 1 to 23 are supported.

These functions convert between geometries and encoded polylines.

Encodes a linestring or multipoint to a polyline.

Decodes a polyline to a linestring.

---

## Regular expression function properties — Trino 478 Documentation

**URL:** https://trino.io/docs/current/admin/properties-regexp-function.html

**Contents:**
- Regular expression function properties#
- regex-library#
- re2j.dfa-states-limit#
- re2j.dfa-retries#

These properties allow tuning the Regular expression functions.

Allowed values: JONI, RE2J

Which library to use for regular expression functions. JONI is generally faster for common usage, but can require exponential time for certain expression patterns. RE2J uses a different algorithm, which guarantees linear time, but is often slower.

Default value: 2147483647

The maximum number of states to use when RE2J builds the fast, but potentially memory intensive, deterministic finite automaton (DFA) for regular expression matching. If the limit is reached, RE2J falls back to the algorithm that uses the slower, but less memory intensive non-deterministic finite automaton (NFA). Decreasing this value decreases the maximum memory footprint of a regular expression search at the cost of speed.

The number of times that RE2J retries the DFA algorithm, when it reaches a states limit before using the slower, but less memory intensive NFA algorithm, for all future inputs for that search. If hitting the limit for a given input row is likely to be an outlier, you want to be able to process subsequent rows using the faster DFA algorithm. If you are likely to hit the limit on matches for subsequent rows as well, you want to use the correct algorithm from the beginning so as not to waste time and resources. The more rows you are processing, the larger this value should be.

---

## IP Address Functions — Trino 478 Documentation

**URL:** https://trino.io/docs/current/functions/ipaddress.html

**Contents:**
- IP Address Functions#

Returns true if the address exists in the CIDR network:

**Examples:**

Example 1 (unknown):
```unknown
SELECT contains('10.0.0.0/8', IPADDRESS '10.255.255.255'); -- true
SELECT contains('10.0.0.0/8', IPADDRESS '11.255.255.255'); -- false

SELECT contains('2001:0db8:0:0:0:ff00:0042:8329/128', IPADDRESS '2001:0db8:0:0:0:ff00:0042:8329'); -- true
SELECT contains('2001:0db8:0:0:0:ff00:0042:8329/128', IPADDRESS '2001:0db8:0:0:0:ff00:0042:8328'); -- false
```

Example 2 (unknown):
```unknown
SELECT contains('10.0.0.0/8', IPADDRESS '10.255.255.255'); -- true
SELECT contains('10.0.0.0/8', IPADDRESS '11.255.255.255'); -- false

SELECT contains('2001:0db8:0:0:0:ff00:0042:8329/128', IPADDRESS '2001:0db8:0:0:0:ff00:0042:8329'); -- true
SELECT contains('2001:0db8:0:0:0:ff00:0042:8329/128', IPADDRESS '2001:0db8:0:0:0:ff00:0042:8328'); -- false
```

---

## Regular expression functions — Trino 478 Documentation

**URL:** https://trino.io/docs/current/functions/regexp.html

**Contents:**
- Regular expression functions#

All the regular expression functions use the Java pattern syntax, with a few notable exceptions:

When using multi-line mode (enabled via the (?m) flag), only \n is recognized as a line terminator. Additionally, the (?d) flag is not supported and must not be used.

Case-insensitive matching (enabled via the (?i) flag) is always performed in a Unicode-aware manner. However, context-sensitive and local-sensitive matching is not supported. Additionally, the (?u) flag is not supported and must not be used.

Surrogate pairs are not supported. For example, \uD800\uDC00 is not treated as U+10000 and must be specified as \x{10000}.

Boundaries (\b) are incorrectly handled for a non-spacing mark without a base character.

\Q and \E are not supported in character classes (such as [A-Z123]) and are instead treated as literals.

Unicode character classes (\p{prop}) are supported with the following differences:

All underscores in names must be removed. For example, use OldItalic instead of Old_Italic.

Scripts must be specified directly, without the Is, script= or sc= prefixes. Example: \p{Hiragana}

Blocks must be specified with the In prefix. The block= and blk= prefixes are not supported. Example: \p{Mongolian}

Categories must be specified directly, without the Is, general_category= or gc= prefixes. Example: \p{L}

Binary properties must be specified directly, without the Is. Example: \p{NoncharacterCodePoint}

Returns the number of occurrence of pattern in string:

Returns the substring(s) matched by the regular expression pattern in string:

Finds all occurrences of the regular expression pattern in string and returns the capturing group number group:

Returns the first substring matched by the regular expression pattern in string:

Finds the first occurrence of the regular expression pattern in string and returns the capturing group number group:

Evaluates the regular expression pattern and determines if it is contained within string.

The pattern only needs to be contained within string, rather than needing to match all of string. In other words, this performs a contains operation rather than a match operation. You can match the entire string by anchoring the pattern using ^ and $:

Returns the index of the first occurrence (counting from 1) of pattern in string. Returns -1 if not found:

Returns the index of the first occurrence of pattern in string, starting from start (include start). Returns -1 if not found:

Returns the index of the nth occurrence of pattern in string, starting from start (include start). Returns -1 if not found:

Removes every instance of the substring matched by the regular expression pattern from string:

Replaces every instance of the substring matched by the regular expression pattern in string with replacement. Capturing groups can be referenced in replacement using $g for a numbered group or ${name} for a named group. A dollar sign ($) may be included in the replacement by escaping it with a backslash (\$):

Replaces every instance of the substring matched by the regular expression pattern in string using function. The lambda expression function is invoked for each match with the capturing groups passed as an array. Capturing group numbers start at one; there is no group for the entire match (if you need this, surround the entire expression with parenthesis).

Splits string using the regular expression pattern and returns an array. Trailing empty strings are preserved:

**Examples:**

Example 1 (unknown):
```unknown
SELECT regexp_count('1a 2b 14m', '\s*[a-z]+\s*'); -- 3
```

Example 2 (unknown):
```unknown
SELECT regexp_count('1a 2b 14m', '\s*[a-z]+\s*'); -- 3
```

Example 3 (unknown):
```unknown
SELECT regexp_extract_all('1a 2b 14m', '\d+'); -- [1, 2, 14]
```

Example 4 (unknown):
```unknown
SELECT regexp_extract_all('1a 2b 14m', '\d+'); -- [1, 2, 14]
```

---

## String functions and operators — Trino 478 Documentation

**URL:** https://trino.io/docs/current/functions/string.html

**Contents:**
- String functions and operators#
- String operators#
- String functions#
- Unicode functions#

The || operator performs concatenation.

The LIKE statement can be used for pattern matching and is documented in Pattern comparison: LIKE.

These functions assume that the input strings contain valid UTF-8 encoded Unicode code points. There are no explicit checks for valid UTF-8 and the functions may return incorrect results on invalid UTF-8. Invalid UTF-8 data can be corrected with from_utf8().

Additionally, the functions operate on Unicode code points and not user visible characters (or grapheme clusters). Some languages combine multiple code points into a single user-perceived character, the basic unit of a writing system for a language, but the functions will treat each code point as a separate unit.

The lower() and upper() functions do not perform locale-sensitive, context-sensitive, or one-to-many mappings required for some languages. Specifically, this will return incorrect results for Lithuanian, Turkish and Azeri.

Returns the Unicode code point n as a single character string.

Returns the Unicode code point of the only character of string.

Returns the concatenation of string1, string2, ..., stringN. This function provides the same functionality as the SQL-standard concatenation operator (||).

Returns the concatenation of string1, string2, ..., stringN using string0 as a separator. If string0 is null, then the return value is null. Any null values provided in the arguments after the separator are skipped.

Returns the concatenation of elements in the array using string0 as a separator. If string0 is null, then the return value is null. Any null values in the array are skipped.

Returns the Hamming distance of string1 and string2, i.e. the number of positions at which the corresponding characters are different. Note that the two strings must have the same length.

Returns the length of string in characters.

Returns the Levenshtein edit distance of string1 and string2, i.e. the minimum number of single-character edits (insertions, deletions or substitutions) needed to change string1 into string2.

Converts string to lowercase.

Left pads string to size characters with padstring. If size is less than the length of string, the result is truncated to size characters. size must not be negative and padstring must be non-empty.

Removes leading whitespace from string.

Tests whether a string of digits is valid according to the Luhn algorithm.

This checksum function, also known as modulo 10 or mod 10, is widely applied on credit card numbers and government identification numbers to distinguish valid numbers from mistyped, incorrect numbers.

Valid identification number:

Invalid identification number:

Returns the starting position of the first instance of substring in string. Positions start with 1. If not found, 0 is returned.

This SQL-standard function has special syntax and uses the IN keyword for the arguments. See also strpos().

Removes all instances of search from string.

Replaces all instances of search with replace in string.

Returns string with the characters in reverse order.

Right pads string to size characters with padstring. If size is less than the length of string, the result is truncated to size characters. size must not be negative and padstring must be non-empty.

Removes trailing whitespace from string.

It is typically used to evaluate the similarity of two expressions phonetically, that is how the string sounds when spoken:

Splits string on delimiter and returns an array.

Splits string on delimiter and returns an array of size at most limit. The last element in the array always contain everything left in the string. limit must be a positive number.

Splits string on delimiter and returns the field index. Field indexes start with 1. If the index is larger than the number of fields, then null is returned.

Splits string by entryDelimiter and keyValueDelimiter and returns a map. entryDelimiter splits string into key-value pairs. keyValueDelimiter splits each pair into key and value.

Splits string by entryDelimiter and keyValueDelimiter and returns a map containing an array of values for each unique key. entryDelimiter splits string into key-value pairs. keyValueDelimiter splits each pair into key and value. The values for each key will be in the same order as they appeared in string.

Returns the starting position of the first instance of substring in string. Positions start with 1. If not found, 0 is returned.

Returns the position of the N-th instance of substring in string. When instance is a negative number the search will start from the end of string. Positions start with 1. If not found, 0 is returned.

Tests whether substring is a prefix of string.

This is an alias for substring().

Returns the rest of string from the starting position start. Positions start with 1. A negative starting position is interpreted as being relative to the end of the string.

This is an alias for substring().

Returns a substring from string of length length from the starting position start. Positions start with 1. A negative starting position is interpreted as being relative to the end of the string.

Returns the source string translated by replacing characters found in the from string with the corresponding characters in the to string. If the from string contains duplicates, only the first is used. If the source character does not exist in the from string, the source character will be copied without translation. If the index of the matching character in the from string is beyond the length of the to string, the source character will be omitted from the resulting string.

Here are some examples illustrating the translate function:

Removes leading and trailing whitespace from string.

Removes any leading and/or trailing characters as specified up to and including string from source:

Converts string to uppercase.

Returns the stem of word in the English language.

Returns the stem of word in the lang language.

Transforms string with NFC normalization form.

Transforms string with the specified normalization form. form must be one of the following keywords:

Canonical Decomposition

Canonical Decomposition, followed by Canonical Composition

Compatibility Decomposition

Compatibility Decomposition, followed by Canonical Composition

This SQL-standard function has special syntax and requires specifying form as a keyword, not as a string.

Encodes string into a UTF-8 varbinary representation.

Decodes a UTF-8 encoded string from binary. Invalid UTF-8 sequences are replaced with the Unicode replacement character U+FFFD.

Decodes a UTF-8 encoded string from binary. Invalid UTF-8 sequences are replaced with replace. The replacement string replace must either be a single character or empty (in which case invalid characters are removed).

**Examples:**

Example 1 (unknown):
```unknown
select luhn_check('79927398713');
-- true
```

Example 2 (unknown):
```unknown
select luhn_check('79927398713');
-- true
```

Example 3 (unknown):
```unknown
select luhn_check('79927398714');
-- false
```

Example 4 (unknown):
```unknown
select luhn_check('79927398714');
-- false
```

---

## Array functions and operators — Trino 478 Documentation

**URL:** https://trino.io/docs/current/functions/array.html

**Contents:**
- Array functions and operators#
- Subscript operator: []#
- Concatenation operator: ||#
- Array functions#

Array functions and operators use the ARRAY type. Create an array with the data type constructor.

Create an array of integer numbers:

Create an array of character values:

Array elements must use the same type or it must be possible to coerce values to a common type. The following example uses integer and decimal values and the resulting array contains decimals:

Null values are allowed:

The [] operator is used to access an element of an array and is indexed starting from one:

The following example constructs an array and then accesses the second element:

The || operator is used to concatenate an array with an array or an element of the same type:

Returns whether all elements of an array match the given predicate. Returns true if all the elements match the predicate (a special case is when the array is empty); false if one or more elements don’t match; NULL if the predicate function returns NULL for one or more elements and true for all other elements.

Returns whether any elements of an array match the given predicate. Returns true if one or more elements match the predicate; false if none of the elements matches (a special case is when the array is empty); NULL if the predicate function returns NULL for one or more elements and false for all other elements.

Remove duplicate values from the array x.

Returns an array of the elements in the intersection of x and y, without duplicates.

Returns an array of the elements in the union of x and y, without duplicates.

Returns an array of elements in x but not in y, without duplicates.

Returns a map where the keys are the unique elements in the input array x and the values are the number of times that each element appears in x. Null values are ignored.

Returns an empty map if the input array has no non-null elements.

Concatenates the elements of the given array using the delimiter. Null elements are omitted in the result.

Concatenates the elements of the given array using the delimiter and an optional string to replace nulls.

Returns the maximum value of input array.

Returns the minimum value of input array.

Returns the position of the first occurrence of the element in array x (or 0 if not found).

Remove all elements that equal element from array x.

Sorts and returns the array x. The elements of x must be orderable. Null elements will be placed at the end of the returned array.

Sorts and returns the array based on the given comparator function. The comparator will take two nullable arguments representing two nullable elements of the array. It returns -1, 0, or 1 as the first nullable element is less than, equal to, or greater than the second nullable element. If the comparator function returns other values (including NULL), the query will fail and raise an error.

Tests if arrays x and y have any non-null elements in common. Returns null if there are no non-null elements in common but either array contains null.

Returns the cardinality (size) of the array x.

Concatenates the arrays array1, array2, ..., arrayN. This function provides the same functionality as the SQL-standard concatenation operator (||).

Returns n-element sub-groups of input array. If the input array has no duplicates, combinations returns n-element subsets.

Order of sub-groups is deterministic but unspecified. Order of elements within a sub-group deterministic but unspecified. n must be not be greater than 5, and the total size of sub-groups generated must be smaller than 100,000.

Returns true if the array x contains the element.

Return true if array x contains all of array seq as a subsequence (all values in the same consecutive order).

Returns element of array at given index. If index > 0, this function provides the same functionality as the SQL-standard subscript operator ([]), except that the function returns NULL when accessing an index larger than array length, whereas the subscript operator would fail in such a case. If index < 0, element_at accesses elements from the last to the first.

Constructs an array from those elements of array for which function returns true:

Flattens an array(array(T)) to an array(T) by concatenating the contained arrays.

Returns n-grams (sub-sequences of adjacent n elements) for the array. The order of the n-grams in the result is unspecified.

Returns whether no elements of an array match the given predicate. Returns true if none of the elements matches the predicate (a special case is when the array is empty); false if one or more elements match; NULL if the predicate function returns NULL for one or more elements and false for all other elements.

Returns a single value reduced from array. inputFunction will be invoked for each element in array in order. In addition to taking the element, inputFunction takes the current state, initially initialState, and returns the new state. outputFunction will be invoked to turn the final state into the result value. It may be the identity function (i -> i).

Repeat element for count times.

Returns an array which has the reversed order of array x.

Generate a sequence of integers from start to stop, incrementing by 1 if start is less than or equal to stop, otherwise -1.

Generate a sequence of integers from start to stop, incrementing by step.

Generate a sequence of dates from start date to stop date, incrementing by 1 day if start date is less than or equal to stop date, otherwise -1 day.

Generate a sequence of dates from start to stop, incrementing by step. The type of step can be either INTERVAL DAY TO SECOND or INTERVAL YEAR TO MONTH.

Generate a sequence of timestamps from start to stop, incrementing by step. The type of step can be either INTERVAL DAY TO SECOND or INTERVAL YEAR TO MONTH.

Generate a random permutation of the given array x.

Subsets array x starting from index start (or starting from the end if start is negative) with a length of length.

Remove n elements from the end of array:

Returns an array that is the result of applying function to each element of array:

Calculates the euclidean distance:

Calculates the dot product:

Merges the given arrays, element-wise, into a single array of rows. The M-th element of the N-th argument will be the N-th field of the M-th output element. If the arguments have an uneven length, missing values are filled with NULL.

Merges the two given arrays, element-wise, into a single array using function. If one array is shorter, nulls are appended at the end to match the length of the longer array, before applying function.

**Examples:**

Example 1 (unknown):
```unknown
SELECT ARRAY[1, 2, 4];
-- [1, 2, 4]
```

Example 2 (unknown):
```unknown
SELECT ARRAY[1, 2, 4];
-- [1, 2, 4]
```

Example 3 (unknown):
```unknown
SELECT ARRAY['foo', 'bar', 'bazz'];
-- [foo, bar, bazz]
```

Example 4 (unknown):
```unknown
SELECT ARRAY['foo', 'bar', 'bazz'];
-- [foo, bar, bazz]
```

---

## Conversion functions — Trino 478 Documentation

**URL:** https://trino.io/docs/current/functions/conversion.html

**Contents:**
- Conversion functions#
- Conversion functions#
- Formatting#
- Data size#
- Miscellaneous#

Trino will implicitly convert numeric and character values to the correct type if such a conversion is possible. Trino will not convert between character and numeric types. For example, a query that expects a varchar will not automatically convert a bigint value to an equivalent varchar.

When necessary, values can be explicitly cast to a particular type.

Explicitly cast a value as a type. This can be used to cast a varchar to a numeric value type and vice versa.

Like cast(), but returns null if the cast fails.

Returns a formatted string using the specified format string and arguments:

Returns a formatted string using a unit symbol:

The parse_data_size function supports the following units:

Parses string of format value unit into a number, where value is the fractional number of unit values:

Returns the name of the type of the provided expression:

**Examples:**

Example 1 (unknown):
```unknown
SELECT format('%s%%', 123);
-- '123%'

SELECT format('%.5f', pi());
-- '3.14159'

SELECT format('%03d', 8);
-- '008'

SELECT format('%,.2f', 1234567.89);
-- '1,234,567.89'

SELECT format('%-7s,%7s', 'hello', 'world');
-- 'hello  ,  world'

SELECT format('%2$s %3$s %1$s', 'a', 'b', 'c');
-- 'b c a'

SELECT format('%1$tA, %1$tB %1$te, %1$tY', date '2006-07-04');
-- 'Tuesday, July 4, 2006'
```

Example 2 (unknown):
```unknown
SELECT format('%s%%', 123);
-- '123%'

SELECT format('%.5f', pi());
-- '3.14159'

SELECT format('%03d', 8);
-- '008'

SELECT format('%,.2f', 1234567.89);
-- '1,234,567.89'

SELECT format('%-7s,%7s', 'hello', 'world');
-- 'hello  ,  world'

SELECT format('%2$s %3$s %1$s', 'a', 'b', 'c');
-- 'b c a'

SELECT format('%1$tA, %1$tB %1$te, %1$tY', date '2006-07-04');
-- 'Tuesday, July 4, 2006'
```

Example 3 (unknown):
```unknown
SELECT format_number(123456); -- '123K'
SELECT format_number(1000000); -- '1M'
```

Example 4 (unknown):
```unknown
SELECT format_number(123456); -- '123K'
SELECT format_number(1000000); -- '1M'
```

---
