# ADR 005: Decoder and Observer Separation

## Status
Accepted

## Context
In the original design, the `Observer` was responsible for reading physical artifacts (e.g., PDF files, Markdown files) and extracting `ObservationRecord` events. This design tightly coupled physical parsing logic (e.g., PDF byte extraction) with epistemic observation logic (e.g., asserting that "Paragraph 3 exists and contains text X"). If the PDF library changed, the Observer had to change.

## Decision
We decouple the physical ingestion pipeline into two distinct phases: `Decoder` $\rightarrow$ `DocumentModel` $\rightarrow$ `Observer`.
1. **The Decoder**: A purely physical parser (e.g., `PDFDecoder`, `MarkdownDecoder`). It takes raw bytes and outputs a structural `DocumentModel` (a generic tree of paragraphs, headings, tables).
2. **The DocumentModel**: A transient, in-memory structural representation of the artifact.
3. **The Observer**: An epistemic function. It takes the `DocumentModel` and produces deterministic `ObservationRecord` events containing exact byte offsets, lengths, and checksums.

## Consequences
- **Positive**: Observers are now completely insulated from physical file formats. An Observer can run identically on a `DocumentModel` generated from a PDF, a Word Doc, or a Markdown file.
- **Positive**: Decoders can be swapped or upgraded (e.g., moving to a better OCR library) without affecting the epistemic rules of the Observer.
- **Negative**: Introduces an intermediate memory structure (`DocumentModel`), slightly increasing peak memory usage during ingestion.
