import { type Options, Readability } from "@paoramen/cheer-reader";
import { load } from "cheerio";
import { parseDocument } from "htmlparser2";

export function parse(htmlContent: string, { baseURI, ...options }: Partial<Options> = {}) {
  const reader = new Readability(load(parseDocument(htmlContent), { baseURI }), options);
  return reader.parse();
}
