"""Constants specific to Confluence and CQL."""

# Based on https://developer.atlassian.com/cloud/confluence/cql-functions/#reserved-words
# List might need refinement based on actual parser behavior
# Using lowercase for case-insensitive matching
RESERVED_CQL_WORDS = {
    "after",
    "and",
    "as",
    "avg",
    "before",
    "begin",
    "by",
    "commit",
    "contains",
    "count",
    "distinct",
    "else",
    "empty",
    "end",
    "explain",
    "from",
    "having",
    "if",
    "in",
    "inner",
    "insert",
    "into",
    "is",
    "isnull",
    "left",
    "like",
    "limit",
    "max",
    "min",
    "not",
    "null",
    "or",
    "order",
    "outer",
    "right",
    "select",
    "sum",
    "then",
    "was",
    "where",
    "update",
}

# Add other Confluence-specific constants here if needed in the future.
