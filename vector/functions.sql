CREATE OR REPLACE FUNCTION pixel_area (z integer)
  RETURNS float
  AS 'SELECT (24505721471.3958/(2^(2*z)));'
  LANGUAGE SQL
  IMMUTABLE
  STRICT;