from typing import Optional, overload

CMARK_VERSION: str
@overload
def markdown(
    text: str,
    source_pos: Optional[bool] = ...,
    hard_breaks: Optional[bool] = ...,
    no_breaks: Optional[bool] = ...,
    smart: Optional[bool] = ...,
    unsafe: Optional[bool] = ...,
    validate_utf8: Optional[bool] = ...,
) -> str: ...
@overload
def markdown(
    text_file: str,
    source_pos: Optional[bool] = ...,
    hard_breaks: Optional[bool] = ...,
    no_breaks: Optional[bool] = ...,
    smart: Optional[bool] = ...,
    unsafe: Optional[bool] = ...,
    validate_utf8: Optional[bool] = ...,
) -> str: ...
@overload
def markdown(
    text: str,
    output_file: str,
    source_pos: Optional[bool] = ...,
    hard_breaks: Optional[bool] = ...,
    no_breaks: Optional[bool] = ...,
    smart: Optional[bool] = ...,
    unsafe: Optional[bool] = ...,
    validate_utf8: Optional[bool] = ...,
) -> bool: ...
@overload
def markdown(
    text_file: str,
    output_file: str,
    source_pos: Optional[bool] = ...,
    hard_breaks: Optional[bool] = ...,
    no_breaks: Optional[bool] = ...,
    smart: Optional[bool] = ...,
    unsafe: Optional[bool] = ...,
    validate_utf8: Optional[bool] = ...,
) -> bool: ...
