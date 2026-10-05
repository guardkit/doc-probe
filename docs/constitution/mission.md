Status: accepted — 5 October 2026, Rich (throwaway factory test project)

# doc-probe: mission

## Who it is for
Developers who want small, predictable statistics about a piece of plain text.

## The problem
Counting words, lines and characters is easy to get subtly wrong (blank lines, punctuation, Unicode).
doc-probe gives one obvious, well-tested answer.

## How success is measured
- Every public function has a test and the test command passes.
- The same input always gives the same output.

## What it will not do
- No natural-language processing, no file formats other than plain text, no network access.

## Rules the product must keep
- **Words are separated by whitespace only.** Punctuation stays part of the word it touches.
- **Empty or whitespace-only text has zero words and zero lines.**
- Functions never modify their input and never raise on ordinary text.

## End-to-end example
`word_count("Hello,  world!\n")` returns `2`.
