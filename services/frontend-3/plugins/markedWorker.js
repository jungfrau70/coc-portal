// markedWorker.js

import { marked } from 'marked';
import { parentPort } from 'worker_threads';

parentPort.on('message', (markdownString) => {
  parentPort.postMessage(marked.parse(markdownString));
});