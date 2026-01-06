from scholarly import scholarly
import html

AUTHOR_ID = "_h6KifoAAAAJ"  # your Scholar ID

author = scholarly.search_author_id(AUTHOR_ID)
author = scholarly.fill(author, sections=["publications"])

html_out = "<ul>\n"

for pub in author["publications"]:
    title = html.escape(pub["bib"]["title"])
    year = pub["bib"].get("year", "—")
    venue = pub["bib"].get("venue", "")
    cites = pub.get("num_citations", 0)

    html_out += f"<li><b>{title}</b> ({year})<br>{venue}<br>Citations: {cites}</li>\n"

html_out += "</ul>"

with open("publications_auto.html", "w", encoding="utf-8") as f:
    f.write(html_out)
