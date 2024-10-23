import { type Options, Readability } from "@paoramen/cheer-reader";
import { load } from "cheerio";
import { parseDocument } from "htmlparser2";

export function parse(htmlContent: string, options: Partial<Options> = {}) {
  const reader = new Readability(load(parseDocument(htmlContent)), options);
  return reader.parse();
}
