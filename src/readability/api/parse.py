from dataclasses import dataclass
from typing import Optional, overload

from ..impl import parse as _parse
from ..utils.cases import to_camel_cases, to_snake_cases


@dataclass(slots=True, kw_only=True)
class Article:
    """The object that `parse` returns.

    It contains some metadata, and if the `extraction` option is set to `true` (default),
    it also contains the extracted content.
    """

    title: Optional[str]
    """`title` (string): the title of the article."""

    byline: Optional[str]
    """`byline` (string): the author of the article."""

    dir: Optional[str]
    """`dir` (string): the direction of the text in the article."""

    lang: Optional[str]
    """`lang` (string): the language of the article."""

    content: Optional[str]
    """`content` (string): the article content."""

    text_content: Optional[str]
    """`textContent` (string): the article content, stripped of all HTML tags."""

    length: Optional[int]
    """`length` (number): the number of characters in the article content."""

    excerpt: Optional[str]
    """`excerpt` (string): a short excerpt of the article content."""

    site_name: Optional[str]
    """`siteName` (string): the name of the site where the article was published."""

    published_time: Optional[str]
    """`publishedTime` (string): the time the article was published."""


@overload
def parse(html: str) -> Article: ...
@overload
def parse(
    html: str,
    *,
    base_uri: str | None = None,
    debug: bool = False,
    max_elems_to_parse: int = 0,
    nb_top_candidates: int = 5,
    char_threshold: int = 500,
    classes_to_preserve: list[str] = [],
    keep_classes: bool = False,
    disable_json_ld: bool = False,
    link_density_modifier: int = 0,
    extraction: bool = True,
) -> Article: ...


def parse(html, **kwargs):
    """
    Runs readability.

    Parameters:
        html (str): The HTML content to parse.
        base_uri (str, optional): The base URI for the document. Used to resolve the `href` and `src` props.
        debug (bool, optional): Whether to enable logging. Defaults to False.
        max_elems_to_parse (int, optional): The maximum number of elements to parse. Defaults to 0.
        nb_top_candidates (int, optional): The number of top candidates to consider when analyzing how tight the competition is among candidates. Defaults to 5.
        char_threshold (int, optional): The number of characters an article must have in order to return a result. Defaults to 500.
        classes_to_preserve (list[str], optional): A set of classes to preserve on HTML elements when the `keep_classes` option is set to False. Defaults to an empty list.
        keep_classes (bool, optional): Whether to preserve all classes on HTML elements. When set to False, only classes specified in the `classes_to_preserve` array are kept. Defaults to False.
        disable_json_ld (bool, optional): When extracting page metadata, cheer-reader gives precedence to Schema.org fields specified in the JSON-LD format. Set this option to True to skip JSON-LD parsing. Defaults to False.
        link_density_modifier (int, optional): A number that is added to the base link density threshold during the shadiness checks. This can be used to penalize nodes with a high link density or vice versa. Defaults to 0.
        extraction (bool, optional): Some libraries are only interested in the metadata and don't want to pay the price of a full extraction. When you enable this option, the `content`, `textContent`, `length`, and `excerpt` will be `null`. Defaults to True.

    Returns:
        ReadabilityResult: An object containing the parsing result.
    """

    result = _parse(html, to_camel_cases(kwargs))

    return Article(**to_snake_cases(result))
