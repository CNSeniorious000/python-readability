async function* readLines() {
  process.stdin.setEncoding("utf-8");
  process.stdin.on("end", process.exit);

  let buffer = "";

  while (true) {
    const chunk = process.stdin.read();

    if (chunk === null) {
      await new Promise((resolve) => {
        process.stdin.once("readable", resolve);
      });
      continue;
    }

    buffer += chunk;

    let lines = buffer.split(/\r?\n/);
    while (lines.length > 1) {
      yield JSON.parse(lines.shift().trim());
    }

    buffer = lines[0];
  }
}

(async () => {
  for await (const chunk of readLines()) {
    let result, error;
    try {
      result = eval(chunk);
    } catch (err) {
      error = err instanceof Error
        ? {
          name: err.name,
          message: err.message,
          stack: err.stack,
        }
        : {
          name: String(typeof err),
          message: String(err),
        };
    }
    process.stdout.write(JSON.stringify({ result, error }) + "\n", "utf-8");
  }
})();
