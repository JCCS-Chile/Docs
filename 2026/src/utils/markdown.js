export function normalizeMarkdown(markdown) {
  return markdown.replace(/^---[\s\S]*?---\s*/, "");
}

function renderInline(text) {
  return text
    .replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2">$1</a>')
    .replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>")
    .replace(/`(.+?)`/g, "<code>$1</code>");
}

export function markdownToHtml(markdown) {
  const lines = normalizeMarkdown(markdown).split("\n");
  const html = [];
  let listOpen = false;
  let orderedListOpen = false;
  let quoteOpen = false;
  let tableOpen = false;

  const closeLists = () => {
    if (listOpen) {
      html.push("</ul>");
      listOpen = false;
    }
    if (orderedListOpen) {
      html.push("</ol>");
      orderedListOpen = false;
    }
  };

  const closeQuote = () => {
    if (quoteOpen) {
      html.push("</blockquote>");
      quoteOpen = false;
    }
  };

  const closeTable = () => {
    if (tableOpen) {
      html.push("</tbody></table>");
      tableOpen = false;
    }
  };

  lines.forEach((rawLine) => {
    const line = rawLine.trim();

    if (!line) {
      closeLists();
      closeQuote();
      closeTable();
      return;
    }

    if (line === "---") {
      closeLists();
      closeQuote();
      closeTable();
      html.push("<hr />");
      return;
    }

    if (line.startsWith("<")) {
      closeLists();
      closeQuote();
      closeTable();
      html.push(rawLine);
      return;
    }

    const heading = line.match(/^(#{1,4})\s+(.+)$/);
    if (heading) {
      closeLists();
      closeQuote();
      closeTable();
      html.push(`<h${heading[1].length}>${renderInline(heading[2])}</h${heading[1].length}>`);
      return;
    }

    if (line.startsWith("> ")) {
      closeLists();
      closeTable();
      if (!quoteOpen) {
        html.push("<blockquote>");
        quoteOpen = true;
      }
      html.push(`<p>${renderInline(line.slice(2))}</p>`);
      return;
    }

    if (line.includes("|") && /^\|.+\|$/.test(line) && !/^\|\s*-/.test(line)) {
      closeLists();
      closeQuote();
      const cells = line
        .split("|")
        .slice(1, -1)
        .map((cell) => `<td>${renderInline(cell.trim())}</td>`)
        .join("");
      if (!tableOpen) {
        html.push("<table><tbody>");
        tableOpen = true;
      }
      html.push(`<tr>${cells}</tr>`);
      return;
    }

    if (/^\|\s*-/.test(line)) {
      return;
    }

    const unordered = line.match(/^- (.+)$/);
    if (unordered) {
      closeQuote();
      closeTable();
      if (!listOpen) {
        closeLists();
        html.push("<ul>");
        listOpen = true;
      }
      html.push(`<li>${renderInline(unordered[1])}</li>`);
      return;
    }

    const ordered = line.match(/^\d+\.\s+(.+)$/);
    if (ordered) {
      closeQuote();
      closeTable();
      if (!orderedListOpen) {
        closeLists();
        html.push("<ol>");
        orderedListOpen = true;
      }
      html.push(`<li>${renderInline(ordered[1])}</li>`);
      return;
    }

    closeLists();
    closeQuote();
    closeTable();
    html.push(`<p>${renderInline(line)}</p>`);
  });

  closeLists();
  closeQuote();
  closeTable();

  return html.join("\n");
}
