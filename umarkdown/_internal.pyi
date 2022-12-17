from typing import Optional

CMARK_VERSION: str

def markdown(
    text: str,
    source_pos: Optional[bool] = ...,
    hard_breaks: Optional[bool] = ...,
    no_breaks: Optional[bool] = ...,
    smart: Optional[bool] = ...,
    unsafe: Optional[bool] = ...,
    validate_utf8: Optional[bool] = ...,
) -> str: ...
