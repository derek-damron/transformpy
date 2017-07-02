def trim(x=None, method="value", lo=None, hi=None):
    # Check x
    if x is None:
        raise TypeError("Please provide an list x to trim")
    if not all(isinstance(i, (int, long, float)) for i in x):
        raise TypeError("x must consist of only numeric types")
        
    # Check method
    if method not in ["value"]:
        raise ValueError("method must be 'value'")

    # Check that at least one lo/hi value provided
    if lo is None and hi is None:
        raise ValueError("Please provide at least one lo or hi value")
        
    # Check lo
    if lo is not None:
        if not isinstance(lo, (int, long, float)):
            raise ValueError("lo must be a single numeric value if specified")
        
    # Check hi
    if hi is not None:
        if not isinstance(hi, (int, long, float)):
            raise ValueError("hi must be a single numeric value if specified")

    # Check lo <= hi
    if lo is not None and hi is not None and hi < lo:
        raise ValueError("lo must be less than or equal to the hi")
        
    # Trim
    if lo is not None:
        x = [lo if i < lo
             else i
             for i in x]
    if hi is not None:
        x = [hi if i > hi
             else i
             for i in x]
        
    return(x)

