# Markdown Syntax Template

## Line Breaks
<!-- End a line with two or more spaces for line break -->
line 1.  
line 2.

## Font type

*Italic*  
**Bold**  
***Bold and Italic***  
`code`  
~~strike trhough~~  
==very important words==  

## Quote

> Quote

> Nested Quote
> > Nested Quote

## List

1. item 1
2. item 2

- bullet 1
- bullet 2

## Image/Links

[link with title](https://duckduckgo.com "The best search engine for privacy")  
<https://www.markdownguide.org>  
<fake@example.com>  
![image](./tux.avif)  
*image caption*

## Code block

```shell
echo "something"
```  

    block2

## Table

| Left | Center | Right |
| :--- | :----: | ---: |
| l1 | c1 | r1 |
| line1 </br> line2 | c2 | r2 |

## Linking header

The IDs are generated from the content of the header according to the following rules:

1. All text is converted to lowercase.
2. All non-word text (e.g., punctuation, HTML) is removed.
3. All spaces are converted to hyphens.
4. Two or more hyphens in a row are converted to one.
5. If a header with the same ID has already been generated, a unique incrementing number is appended, starting at 1.

## Horizontal Rules

***

## Footnotes

Here's a simple footnote,[^1] and here's a longer one.[^bignote]

[^1]: This is the first footnote.
[^bignote]: Here's one with multiple paragraphs and code.  
    Indent paragraphs to include them in the footnote.  
    `{ my code }`  
    Add as many paragraphs as you like

## Checkbox

- [x] Write the press release
- [ ] Update the website
- [ ] Contact the media

## References

1. <https://www.markdownguide.org/basic-syntax/>
2. <https://www.markdownguide.org/extended-syntax/>
3. <https://stackoverflow.com/questions/51221730/markdown-link-to-header>
