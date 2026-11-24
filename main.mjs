import { mkdirSync, writeFileSync } from 'node:fs';

const LINE = 'Your export failed because one cell in your spreadsheet says NULL, and the database took it literally.';

// The bounty gate: a single line of 1-200 UTF-8 characters, no trailing
// newline, so the entry is exactly 102 bytes every run.
if (LINE.length > 200 || LINE.includes('\n')) {
  throw new Error('entry line violates the 1-200 character single-line gate');
}

mkdirSync('/output', { recursive: true });
writeFileSync('/output/entry.txt', LINE, 'utf8');
